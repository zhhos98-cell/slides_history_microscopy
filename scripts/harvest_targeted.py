#!/usr/bin/env python3
"""Third-wave targeted metadata harvester for the frozen microscope-slide survey.

This script is deliberately narrower than harvest_institution.py. It is used only
for catalogues that proved high-yield in the first two reconnaissance runs. Each
adapter has a bounded recipe: fixed seed pages, catalogue-specific link patterns,
or a small set of public search-form POST requests. It never bulk-downloads
images, never follows login/access-control paths, and discards PDFs over 5 MB.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
from typing import Any

from harvest_institution import (
    USER_AGENT,
    html_to_text,
    identifier_candidates,
    quantity_candidates,
    skip_binary,
)

SURVEY = Path("data/survey/07A_Global_Microscope_Slide_Collections_Survey.csv")
ACTIVE = Path("data/normalized/scope_19c_active_ids.json")
RECIPES = Path("data/survey/targeted_harvest_profiles.json")
OUT_ROOT = Path("outputs/targeted_harvest")
SKIP_AUTOMATION = {"manual only", "blocked"}
DEFAULT_MAX_PDF_BYTES = 5_000_000

INSTITUTION_GROUP_RULES = [
    (r"Farlow Herbarium", "farlow-herbarium"),
    (r"Mus[eéu-]*um national d.Histoire naturelle.*Paris|MNHN.*Paris", "mnhn-paris"),
    (r"Powerhouse", "powerhouse-collection"),
    (r"Royal College of Surgeons of England|Hunterian Museum.*Royal College of Surgeons", "rcs-hunterian"),
    (r"Naturhistorisches Museum Wien", "nhmw-vienna"),
    (r"Harvard(?: University)? Museum of Comparative Zoology|Harvard Museum of Comparative Zoology", "harvard-mcz"),
    (r"Museum f(?:u|ü|uer|ür) Naturkunde Berlin|Museum für Naturkunde Berlin", "museum-fuer-naturkunde-berlin"),
    (r"(?:University of Manchester,? )?Museum of Medicine and Health|Museum of Medicine and Health,? University of Manchester", "university-of-manchester-museum-of-medicine-and-health"),
    (r"National Library of New Zealand(?: / Alexander Turnbull Library)?|Alexander Turnbull Library", "national-library-of-new-zealand"),
]


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "institution"


def canonical_key(institution: str) -> str:
    for pattern, key in INSTITUTION_GROUP_RULES:
        if re.search(pattern, institution, flags=re.I):
            return key
    return slugify(institution)


def normalise_url(url: str, base: str = "") -> str:
    url = html.unescape((url or "").strip())
    if base:
        url = urllib.parse.urljoin(base, url)
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return ""
    return urllib.parse.urlunparse(parsed._replace(fragment=""))


def host_allowed(url: str, allowed_hosts: set[str]) -> bool:
    host = (urllib.parse.urlparse(url).hostname or "").lower()
    return bool(host) and any(host == allowed or host.endswith("." + allowed) for allowed in allowed_hosts)


def load_rows(institution_key: str) -> list[dict[str, str]]:
    with SURVEY.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if ACTIVE.exists():
        active = set(json.loads(ACTIVE.read_text(encoding="utf-8")).get("entry_ids", []))
        if active:
            rows = [row for row in rows if row.get("entry_id") in active]
    return [
        row for row in rows
        if row.get("automation_feasibility", "") not in SKIP_AUTOMATION
        and canonical_key(row.get("institution_current", "")) == institution_key
    ]


def response_length(headers: Any) -> int | None:
    try:
        value = int(headers.get("content-length", ""))
        return value if value >= 0 else None
    except (TypeError, ValueError):
        return None


def request_document(
    url: str,
    *,
    method: str = "GET",
    form_data: dict[str, Any] | None = None,
    max_bytes: int,
    max_pdf_bytes: int,
) -> tuple[bytes, str, str, dict[str, Any]]:
    data = None
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "text/html,application/json,application/ld+json,application/pdf,text/plain,text/csv;q=0.8,*/*;q=0.2",
    }
    if method == "POST":
        data = urllib.parse.urlencode(form_data or {}, doseq=True).encode("utf-8")
        headers["Content-Type"] = "application/x-www-form-urlencoded"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=40) as resp:  # noqa: S310
        ctype = resp.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        final_url = resp.geturl()
        content_length = response_length(resp.headers)
        is_pdf = "pdf" in ctype or final_url.lower().split("?", 1)[0].endswith(".pdf")
        if is_pdf and content_length is not None and content_length > max_pdf_bytes:
            return b"", ctype, final_url, {
                "skipped_large_pdf": True,
                "content_length": content_length,
                "reason": "content-length-over-limit",
            }
        limit = max_pdf_bytes if is_pdf else max_bytes
        body = resp.read(limit + 1)
    if is_pdf and len(body) > max_pdf_bytes:
        return b"", ctype, final_url, {
            "skipped_large_pdf": True,
            "content_length": content_length,
            "reason": "stream-over-limit",
        }
    truncated = (not is_pdf) and len(body) > max_bytes
    if truncated:
        body = body[:max_bytes]
    return body, ctype, final_url, {
        "skipped_large_pdf": False,
        "content_length": content_length,
        "truncated": truncated,
    }


def extract_title(raw: str) -> str:
    match = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw)
    return html_to_text(match.group(1)) if match else ""


def extract_links(raw: str, base_url: str) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    seen: set[str] = set()
    for href, label in re.findall(r"(?is)<a\b[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", raw):
        url = normalise_url(href, base_url)
        if url and url not in seen and not skip_binary(url):
            seen.add(url)
            out.append((url, html_to_text(label)[:300]))
    # SorbonNum result cards store record URLs in data-lnk rather than anchors.
    for href in re.findall(r"(?is)\bdata-lnk=[\"']([^\"']+)[\"']", raw):
        url = normalise_url(href, base_url)
        if url and url not in seen and not skip_binary(url):
            seen.add(url)
            out.append((url, "data-lnk record"))
    return out


def table_rows(raw: str, cap: int = 800) -> list[str]:
    out: list[str] = []
    for block in re.findall(r"(?is)<tr\b[^>]*>(.*?)</tr>", raw):
        text = html_to_text(block)
        if text:
            out.append(text[:2500])
        if len(out) >= cap:
            break
    return out


def page_relevant(text: str, recipe: dict[str, Any]) -> bool:
    terms = [term.lower() for term in recipe.get("relevance_terms", [])]
    if not terms:
        return True
    lower = text.lower()
    return any(term in lower for term in terms)


def link_allowed(url: str, label: str, recipe: dict[str, Any]) -> bool:
    hay = f"{url} {label}"
    patterns = recipe.get("follow_url_regex", [])
    return bool(patterns) and any(re.search(pat, hay, flags=re.I) for pat in patterns)


def parse_record(
    *,
    body: bytes,
    ctype: str,
    request_url: str,
    final_url: str,
    institution_key: str,
    adapter: str,
    method: str,
    request_label: str,
    form_data: dict[str, Any] | None,
    seed_entry_ids: list[str],
    fetch_meta: dict[str, Any],
    out_dir: Path,
    idx: int,
    text_sample_chars: int,
) -> tuple[dict[str, Any], list[tuple[str, str]], str]:
    raw_text = ""
    links: list[tuple[str, str]] = []
    suffix = ".html"
    record: dict[str, Any] = {
        "schema_version": "slide-survey-targeted-harvest-record-v1",
        "institution_key": institution_key,
        "adapter": adapter,
        "request_method": method,
        "request_label": request_label,
        "request_url": request_url,
        "final_url": final_url,
        "content_type": ctype,
        "byte_length": len(body),
        "response_content_length": fetch_meta.get("content_length"),
        "response_truncated": bool(fetch_meta.get("truncated")),
        "sha256": hashlib.sha256(body).hexdigest(),
        "seed_entry_ids": seed_entry_ids,
        "fetched_utc": datetime.now(timezone.utc).isoformat(),
    }
    if form_data:
        record["form_data"] = form_data

    if "json" in ctype or final_url.lower().endswith(".json"):
        suffix = ".json"
        raw_text = body.decode("utf-8", errors="replace")
        try:
            parsed = json.loads(raw_text)
            record["json_top_type"] = type(parsed).__name__
        except Exception as exc:
            record["json_parse_error"] = repr(exc)
    elif "pdf" in ctype or final_url.lower().split("?", 1)[0].endswith(".pdf"):
        suffix = ".pdf"
        try:
            from pypdf import PdfReader
            reader = PdfReader(BytesIO(body))
            raw_text = "\n".join((page.extract_text() or "") for page in reader.pages[:60])
            record["pages_total"] = len(reader.pages)
        except Exception as exc:
            record["pdf_parse_error"] = repr(exc)
    else:
        raw = body.decode("utf-8", errors="replace")
        raw_text = html_to_text(raw)
        record["title"] = extract_title(raw)
        record["table_rows"] = table_rows(raw)
        links = extract_links(raw, final_url)

    record["text_sample"] = raw_text[:text_sample_chars]
    record["quantity_candidates"] = quantity_candidates(raw_text)
    record["identifier_candidates"] = identifier_candidates(raw_text)

    raw_dir = out_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    stem = slugify(urllib.parse.urlparse(final_url).netloc + "-" + urllib.parse.urlparse(final_url).path)[:140] or "page"
    raw_path = raw_dir / f"{idx:03d}-{stem}{suffix}"
    raw_path.write_bytes(body)
    record["raw_path"] = str(raw_path)
    return record, links, raw_text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--institution-key", required=True)
    parser.add_argument("--adapter", required=True)
    parser.add_argument("--depth", choices=["quick", "balanced", "deep"], default="balanced")
    parser.add_argument("--delay", type=float, default=0.7)
    args = parser.parse_args()

    cfg = json.loads(RECIPES.read_text(encoding="utf-8"))
    defaults = cfg.get("defaults", {})
    recipe = cfg["adapters"].get(args.adapter)
    if not recipe:
        raise SystemExit(f"Unknown targeted adapter: {args.adapter}")
    if recipe.get("institution_key") != args.institution_key:
        raise SystemExit("Targeted adapter/institution mismatch")

    rows = load_rows(args.institution_key)
    if not rows:
        raise SystemExit(f"No active strict rows for {args.institution_key}")

    seed_to_ids: dict[str, list[str]] = {}
    for row in rows:
        url = normalise_url(row.get("source_url", ""))
        if url:
            seed_to_ids.setdefault(url, []).append(row.get("entry_id", ""))
    for url in recipe.get("extra_seed_urls", []):
        norm = normalise_url(url)
        if norm:
            seed_to_ids.setdefault(norm, [])

    allowed_hosts = {h.lower() for h in recipe.get("allowed_hosts", [])}
    for url in seed_to_ids:
        host = urllib.parse.urlparse(url).hostname
        if host:
            allowed_hosts.add(host.lower())

    factor = {"quick": 0.6, "balanced": 1.0, "deep": 1.2}[args.depth]
    request_budget = max(1, int(recipe.get("request_budget", 30) * factor))
    request_budget = min(request_budget, int(defaults.get("absolute_request_cap", 140)))
    max_bytes = int(defaults.get("max_bytes", 4_000_000))
    max_pdf_bytes = int(defaults.get("max_pdf_bytes", DEFAULT_MAX_PDF_BYTES))
    text_sample_chars = int(defaults.get("text_sample_chars", 24_000))

    out_dir = OUT_ROOT / args.institution_key
    out_dir.mkdir(parents=True, exist_ok=True)
    plan = {
        "schema_version": "slide-survey-targeted-harvest-plan-v1",
        "institution_key": args.institution_key,
        "institution_names": sorted({row.get("institution_current", "") for row in rows}),
        "adapter": args.adapter,
        "strategy": recipe.get("strategy"),
        "depth": args.depth,
        "request_budget": request_budget,
        "active_entry_ids": [row.get("entry_id") for row in rows],
        "seed_urls": list(seed_to_ids),
        "allowed_hosts": sorted(allowed_hosts),
    }
    (out_dir / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    queue: deque[dict[str, Any]] = deque()
    queued_keys: set[str] = set()
    for url, ids in seed_to_ids.items():
        key = "GET " + url
        queue.append({"method": "GET", "url": url, "label": "seed", "form_data": None, "seed_ids": ids, "key": key})
        queued_keys.add(key)
    for req in recipe.get("post_requests", []):
        url = normalise_url(recipe.get("post_url", ""))
        data = req.get("data", {})
        label = req.get("label", "POST search")
        key = "POST " + url + " " + json.dumps(data, sort_keys=True, ensure_ascii=False)
        queue.append({"method": "POST", "url": url, "label": label, "form_data": data, "seed_ids": [row.get("entry_id", "") for row in rows], "key": key})
        queued_keys.add(key)

    records: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    skipped_large_pdfs: list[dict[str, Any]] = []
    completed_keys: set[str] = set()

    strategy = recipe.get("strategy", "targeted_bfs")
    while queue and len(completed_keys) < request_budget:
        req = queue.popleft()
        key = req["key"]
        if key in completed_keys:
            continue
        completed_keys.add(key)
        url = req["url"]
        if skip_binary(url) or not host_allowed(url, allowed_hosts):
            continue
        try:
            body, ctype, final_url, fetch_meta = request_document(
                url,
                method=req["method"],
                form_data=req["form_data"],
                max_bytes=max_bytes,
                max_pdf_bytes=max_pdf_bytes,
            )
            if fetch_meta.get("skipped_large_pdf"):
                skipped_large_pdfs.append({
                    "url": url,
                    "reason": fetch_meta.get("reason"),
                    "content_length": fetch_meta.get("content_length"),
                    "limit_bytes": max_pdf_bytes,
                    "seed_entry_ids": req["seed_ids"],
                })
                continue
            record, links, page_text = parse_record(
                body=body,
                ctype=ctype,
                request_url=url,
                final_url=final_url,
                institution_key=args.institution_key,
                adapter=args.adapter,
                method=req["method"],
                request_label=req["label"],
                form_data=req["form_data"],
                seed_entry_ids=req["seed_ids"],
                fetch_meta=fetch_meta,
                out_dir=out_dir,
                idx=len(records) + 1,
                text_sample_chars=text_sample_chars,
            )
            record["page_relevant"] = page_relevant(page_text, recipe)
            records.append(record)

            if strategy != "fixed_pages":
                for link_url, label in links:
                    if not host_allowed(link_url, allowed_hosts) or skip_binary(link_url):
                        continue
                    if not link_allowed(link_url, label, recipe):
                        continue
                    next_key = "GET " + link_url
                    if next_key in queued_keys or next_key in completed_keys:
                        continue
                    queued_keys.add(next_key)
                    queue.append({
                        "method": "GET",
                        "url": link_url,
                        "label": f"follow:{label[:120]}",
                        "form_data": None,
                        "seed_ids": req["seed_ids"],
                        "key": next_key,
                    })
        except urllib.error.HTTPError as exc:
            errors.append({"method": req["method"], "url": url, "label": req["label"], "error": f"HTTP {exc.code}"})
        except Exception as exc:  # noqa: BLE001
            errors.append({"method": req["method"], "url": url, "label": req["label"], "error": repr(exc)})
        time.sleep(max(args.delay, 0.0))

    with (out_dir / "records.jsonl").open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")

    summary = {
        **plan,
        "status": "complete",
        "fetched": len(records),
        "errors": len(errors),
        "errors_detail": errors,
        "skipped_large_pdfs": len(skipped_large_pdfs),
        "skipped_large_pdf_detail": skipped_large_pdfs,
        "queued_remaining": len(queue),
        "request_budget_reached": len(completed_keys) >= request_budget,
        "relevant_pages": sum(1 for record in records if record.get("page_relevant")),
        "post_requests": sum(1 for record in records if record.get("request_method") == "POST"),
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"{args.institution_key}: targeted fetched={len(records)} errors={len(errors)} "
        f"relevant={summary['relevant_pages']} skipped_large_pdfs={len(skipped_large_pdfs)} "
        f"budget={request_budget}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
