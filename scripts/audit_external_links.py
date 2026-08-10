#!/usr/bin/env python3
"""Audit current public bibliography/source-registry external links.

This script is deliberately non-destructive. It reads only current bibliography
chunks and canonical source-registry routes, checks unique HTTP(S) URLs, and writes
a machine-readable JSON plus a Markdown summary. It never rewrites source rows.

Exit status is always zero unless the audit itself cannot run. HTTP failures are
review signals rather than automatic deletion rules. In particular, 404/410 and
416 responses are retried without a Range header before classification.
"""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import csv
import json
import socket
import ssl
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
AUDIT_SCHEMA = "1.1.0-external-link-audit"
AUDIT_UA = "MicroscopeSlidesInMotion-LinkAudit/1.1 (+https://github.com/zhhos98-cell/slides_history_microscopy)"
BROWSER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126 Safari/537.36"
SOFT_REACHABLE = {401, 403, 405, 406, 409, 418, 423, 425, 429, 451}
DEAD_CODES = {404, 410}
RETRY_WITHOUT_RANGE = DEAD_CODES | {416}


def load_json(rel: str) -> Any:
    return json.loads((ROOT / rel).read_text(encoding="utf-8-sig"))


def parse_bibliography_urls() -> dict[str, list[dict[str, str]]]:
    manifest = load_json("bibliography/bibliography-manifest.json")
    by_url: dict[str, list[dict[str, str]]] = defaultdict(list)
    for chunk in manifest["chunks"]:
        with (ROOT / "bibliography" / chunk).open(newline="", encoding="utf-8-sig") as handle:
            for row in csv.DictReader(handle):
                links = row.get("links") or ""
                for part in links.split(";"):
                    part = part.strip()
                    if "http://" not in part and "https://" not in part:
                        continue
                    idx = min(i for i in [part.find("http://"), part.find("https://")] if i >= 0)
                    label = part[:idx].strip().rstrip(":").strip()
                    url = part[idx:].strip().rstrip(".,)")
                    by_url[url].append({
                        "layer": "bibliography",
                        "id": row["id"],
                        "title": row["title"],
                        "label": label,
                    })
    return by_url


def parse_source_registry_urls() -> dict[str, list[dict[str, str]]]:
    manifest = load_json("sources/source-registry-manifest.json")
    suppressed = set((manifest.get("superseded_ids") or {}).keys()) | set((manifest.get("excluded_ids") or {}).keys())
    by_url: dict[str, list[dict[str, str]]] = defaultdict(list)
    canonical_count = 0
    for chunk in manifest["chunks"]:
        payload = load_json(f"sources/{chunk}")
        for row in payload.get("records", []):
            if row["id"] in suppressed:
                continue
            canonical_count += 1
            for field in ["url", "secondary_url"]:
                url = (row.get(field) or "").strip()
                if not url:
                    continue
                by_url[url].append({
                    "layer": "source_registry",
                    "id": row["id"],
                    "title": row["collection"],
                    "label": field,
                })
    expected = (manifest.get("counts") or {}).get("canonical_records")
    if expected is not None and canonical_count != expected:
        raise RuntimeError(f"source-registry canonical count {canonical_count} != manifest {expected}")
    return by_url


def classify_http(code: int) -> str:
    if 200 <= code < 400:
        return "ok"
    if code in SOFT_REACHABLE:
        return "reachable_but_restricted"
    if code in DEAD_CODES:
        return "dead_candidate"
    if code == 416:
        return "range_error_review"
    if 400 <= code < 500:
        return "client_error_review"
    if 500 <= code < 600:
        return "server_error_review"
    return "review"


def request_once(url: str, timeout: float, *, use_range: bool, browser_ua: bool) -> dict[str, Any]:
    headers = {
        "User-Agent": BROWSER_UA if browser_ua else AUDIT_UA,
        "Accept": "text/html,application/xhtml+xml,application/json,text/plain,*/*;q=0.5",
    }
    if use_range:
        headers["Range"] = "bytes=0-2047"
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            code = int(response.getcode() or 0)
            response.read(2048)
            return {"http_status": code, "final_url": response.geturl(), "error": None}
    except urllib.error.HTTPError as exc:
        return {"http_status": int(exc.code), "final_url": exc.geturl() or url, "error": f"HTTPError: {exc.reason}"}
    except urllib.error.URLError as exc:
        reason = exc.reason
        if isinstance(reason, socket.timeout):
            status = "timeout_review"
        elif isinstance(reason, ssl.SSLError):
            status = "tls_review"
        elif isinstance(reason, socket.gaierror):
            status = "dns_review"
        else:
            text = str(reason).lower()
            status = "timeout_review" if "timed out" in text else "network_error_review"
        return {"http_status": None, "final_url": url, "error": f"URLError: {reason}", "network_status": status}
    except Exception as exc:
        return {"http_status": None, "final_url": url, "error": f"{type(exc).__name__}: {exc}", "network_status": "network_error_review"}


def check_url(url: str, timeout: float) -> dict[str, Any]:
    started = time.monotonic()
    attempts: list[dict[str, Any]] = []

    first = request_once(url, timeout, use_range=True, browser_ua=False)
    attempts.append({"mode": "range_audit_ua", **first})
    code = first.get("http_status")

    final = first
    if code in RETRY_WITHOUT_RANGE:
        second = request_once(url, timeout, use_range=False, browser_ua=True)
        attempts.append({"mode": "full_browser_ua", **second})
        final = second

    final_code = final.get("http_status")
    if final_code is None:
        status = final.get("network_status", "network_error_review")
    else:
        status = classify_http(int(final_code))

    final_url = final.get("final_url") or url
    return {
        "status": status,
        "http_status": final_code,
        "final_url": final_url,
        "redirected": final_url.rstrip("/") != url.rstrip("/"),
        "elapsed_ms": round((time.monotonic() - started) * 1000),
        "error": final.get("error"),
        "attempts": attempts,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=float, default=12.0)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--output-dir", default="outputs/link_audit")
    args = parser.parse_args()

    bib = parse_bibliography_urls()
    src = parse_source_registry_urls()
    refs: dict[str, list[dict[str, str]]] = defaultdict(list)
    for mapping in [bib, src]:
        for url, items in mapping.items():
            refs[url].extend(items)

    urls = sorted(refs)
    results: dict[str, dict[str, Any]] = {}
    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        pending = {pool.submit(check_url, url, args.timeout): url for url in urls}
        for done in futures.as_completed(pending):
            url = pending[done]
            results[url] = done.result()

    rows = [{"url": url, **results[url], "references": refs[url]} for url in urls]
    counts = Counter(r["status"] for r in rows)
    dead_candidates = [r for r in rows if r["status"] == "dead_candidate"]
    review = [r for r in rows if r["status"].endswith("_review") or r["status"] == "dead_candidate"]
    restricted = [r for r in rows if r["status"] == "reachable_but_restricted"]
    redirects = [r for r in rows if r["redirected"]]

    timestamp = datetime.now(timezone.utc).isoformat()
    payload = {
        "schema_version": AUDIT_SCHEMA,
        "generated_utc": timestamp,
        "scope": "Current 206-row bibliography + canonical source-registry routes only; superseded, excluded and historical snapshot rows omitted.",
        "method": {
            "request": "HTTP GET with small Range request; 404/410/416 retried without Range using a browser-style user agent; redirects followed",
            "timeout_seconds": args.timeout,
            "workers": args.workers,
            "classification": {
                "ok": "2xx/3xx",
                "reachable_but_restricted": sorted(SOFT_REACHABLE),
                "dead_candidate": "404/410 after no-Range retry; manual verification still required",
                "*_review": "other 4xx/5xx/network/TLS/DNS/timeout states; manual verification required",
            },
        },
        "counts": {
            "unique_urls": len(rows),
            "bibliography_unique_urls": len(bib),
            "source_registry_unique_urls": len(src),
            "by_status": dict(sorted(counts.items())),
            "redirected": len(redirects),
            "dead_candidates": len(dead_candidates),
            "review": len(review),
            "restricted": len(restricted),
        },
        "results": rows,
    }

    outdir = ROOT / args.output_dir
    outdir.mkdir(parents=True, exist_ok=True)
    json_path = outdir / "external_link_audit.json"
    md_path = outdir / "external_link_audit.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    def fmt_refs(row: dict[str, Any]) -> str:
        return "; ".join(f"{r['layer']}:{r['id']}" for r in row["references"])

    lines = [
        "# External link audit",
        "",
        f"Generated UTC: `{timestamp}`",
        "",
        f"Unique URLs checked: **{len(rows)}** (bibliography {len(bib)}; source registry {len(src)}).",
        "",
        "## Status counts",
        "",
    ]
    for key, value in sorted(counts.items()):
        lines.append(f"- `{key}`: **{value}**")
    lines.extend(["", "## Dead candidates (404/410 after retry)", ""])
    if dead_candidates:
        for row in dead_candidates:
            lines.append(f"- `{row['http_status']}` {row['url']} — {fmt_refs(row)}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Manual review", ""])
    other_review = [r for r in review if r["status"] != "dead_candidate"]
    if other_review:
        for row in other_review:
            lines.append(f"- `{row['status']}` / `{row['http_status']}` {row['url']} — {fmt_refs(row)} — {row['error'] or ''}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Restricted but reachable", ""])
    if restricted:
        for row in restricted:
            lines.append(f"- `{row['http_status']}` {row['url']} — {fmt_refs(row)}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Redirects", ""])
    if redirects:
        for row in redirects:
            lines.append(f"- {row['url']} → {row['final_url']}")
    else:
        lines.append("- None.")
    lines.extend([
        "",
        "## Interpretation rule",
        "",
        "No automated result deletes a source row. 404/410 becomes a dead candidate only after a second request without Range; it still requires manual confirmation. 401/403/429 and similar results are retained as reachable-but-restricted because institutional anti-bot controls can block automated clients while the page remains live. Timeouts, TLS/DNS failures and 5xx responses require manual follow-up before any source row is rewritten.",
        "",
    ])
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(payload["counts"], indent=2))
    print(f"JSON={json_path.relative_to(ROOT)}")
    print(f"MD={md_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
