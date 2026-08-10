#!/usr/bin/env python3
"""Audit current public bibliography/source-registry external links.

This script is deliberately non-destructive. It reads only current bibliography
chunks and canonical source-registry routes, checks unique HTTP(S) URLs, and writes
a machine-readable JSON plus a Markdown summary. It never rewrites source rows.

Exit status is always zero unless the audit itself cannot run. Dead/blocked/timeout
results are evidence for review, not CI failures.
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
USER_AGENT = "MicroscopeSlidesInMotion-LinkAudit/1.0 (+https://github.com/zhhos98-cell/slides_history_microscopy)"
SOFT_REACHABLE = {401, 403, 405, 406, 409, 418, 423, 425, 429, 451}
DEAD_CODES = {404, 410}


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
    superseded = set((manifest.get("superseded_ids") or {}).keys())
    by_url: dict[str, list[dict[str, str]]] = defaultdict(list)
    canonical_count = 0
    for chunk in manifest["chunks"]:
        payload = load_json(f"sources/{chunk}")
        for row in payload.get("records", []):
            if row["id"] in superseded:
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
    expected = manifest.get("canonical_record_count")
    if expected is not None and canonical_count != expected:
        raise RuntimeError(f"source-registry canonical count {canonical_count} != manifest {expected}")
    return by_url


def classify_http(code: int) -> str:
    if 200 <= code < 400:
        return "ok"
    if code in SOFT_REACHABLE:
        return "reachable_but_restricted"
    if code in DEAD_CODES:
        return "dead"
    if 400 <= code < 500:
        return "client_error_review"
    if 500 <= code < 600:
        return "server_error_review"
    return "review"


def check_url(url: str, timeout: float) -> dict[str, Any]:
    started = time.monotonic()
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/json,text/plain,*/*;q=0.5",
            "Range": "bytes=0-2047",
        },
        method="GET",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            code = int(response.getcode() or 0)
            final_url = response.geturl()
            response.read(2048)
            return {
                "status": classify_http(code),
                "http_status": code,
                "final_url": final_url,
                "redirected": final_url.rstrip("/") != url.rstrip("/"),
                "elapsed_ms": round((time.monotonic() - started) * 1000),
                "error": None,
            }
    except urllib.error.HTTPError as exc:
        return {
            "status": classify_http(exc.code),
            "http_status": int(exc.code),
            "final_url": exc.geturl() or url,
            "redirected": (exc.geturl() or url).rstrip("/") != url.rstrip("/"),
            "elapsed_ms": round((time.monotonic() - started) * 1000),
            "error": f"HTTPError: {exc.reason}",
        }
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
        return {
            "status": status,
            "http_status": None,
            "final_url": url,
            "redirected": False,
            "elapsed_ms": round((time.monotonic() - started) * 1000),
            "error": f"URLError: {reason}",
        }
    except Exception as exc:  # diagnostic fallback
        return {
            "status": "network_error_review",
            "http_status": None,
            "final_url": url,
            "redirected": False,
            "elapsed_ms": round((time.monotonic() - started) * 1000),
            "error": f"{type(exc).__name__}: {exc}",
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

    rows = []
    for url in urls:
        result = {"url": url, **results[url], "references": refs[url]}
        rows.append(result)

    counts = Counter(r["status"] for r in rows)
    dead = [r for r in rows if r["status"] == "dead"]
    review = [r for r in rows if r["status"].endswith("_review")]
    restricted = [r for r in rows if r["status"] == "reachable_but_restricted"]
    redirects = [r for r in rows if r["redirected"]]

    timestamp = datetime.now(timezone.utc).isoformat()
    payload = {
        "schema_version": "1.0.0-external-link-audit",
        "generated_utc": timestamp,
        "scope": "Current 206-row bibliography + canonical source-registry routes only; historical snapshots excluded.",
        "method": {
            "request": "HTTP GET with small Range request, redirects followed",
            "timeout_seconds": args.timeout,
            "workers": args.workers,
            "classification": {
                "ok": "2xx/3xx",
                "reachable_but_restricted": sorted(SOFT_REACHABLE),
                "dead": sorted(DEAD_CODES),
                "*_review": "other 4xx/5xx/network/TLS/DNS/timeout states; manual verification required",
            },
        },
        "counts": {
            "unique_urls": len(rows),
            "bibliography_unique_urls": len(bib),
            "source_registry_unique_urls": len(src),
            "by_status": dict(sorted(counts.items())),
            "redirected": len(redirects),
            "dead": len(dead),
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
    lines.extend(["", "## Dead (404/410)", ""])
    if dead:
        for row in dead:
            lines.append(f"- `{row['http_status']}` {row['url']} — {fmt_refs(row)}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Manual review", ""])
    if review:
        for row in review:
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
        "A 404/410 is a strong dead-pointer signal. 401/403/429 and similar results are retained as reachable-but-restricted because institutional anti-bot controls can block automated clients while the page remains live. Timeouts, TLS/DNS failures and 5xx responses require manual follow-up before any source row is rewritten.",
        "",
    ])
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps(payload["counts"], indent=2))
    print(f"JSON={json_path.relative_to(ROOT)}")
    print(f"MD={md_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
