#!/usr/bin/env python3
"""Custom metadata harvest for global microscope-slide survey entries.

This is not a universal crawler. It reads a versioned registry of small site
adapters for known collection entrances. Each adapter preserves collection-
scale evidence: counts, collection names, relationship phrases, source URLs,
object-page patterns, physical structure, and warning flags.

Safety limits:
- dry-run is the default;
- full mode fetches public metadata HTML/text only;
- no login, paywall, anti-bot, robots, IIIF image, or bulk-image bypass;
- every fetched page is capped at MAX_BYTES;
- failed fetches are written into the plan rather than hidden.
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
import urllib.request
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SURVEY_PATH = Path("data/survey/07A_Global_Microscope_Slide_Collections_Survey.csv")
ADAPTER_REGISTRY_SOURCE_PATH = Path("data/survey/site_adapters.json")
RAW_DIR = Path("data/raw/catalogue_pages")
NORMALIZED_DIR = Path("data/normalized")
REPORT_PATH = Path("outputs/harvest_plan.json")
REGISTRY_PATH = Path("outputs/adapter_registry_snapshot.json")

USER_AGENT = "Blachka-corpus-slide-survey/0.3 (+global site-adapter metadata-only; no image bulk download)"
SKIP_AUTOMATION = {"manual only", "blocked"}
MAX_BYTES = 2_000_000


@dataclass(frozen=True)
class Adapter:
    key: str
    label: str
    expected_terms: tuple[str, ...]
    item_url_pattern: str = ""
    status: str = ""
    promotion_rule: str = ""


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "entry"


def safe_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " | ".join(safe_text(v) for v in value)
    return str(value)


def load_adapter_registry(path: Path = ADAPTER_REGISTRY_SOURCE_PATH) -> dict[str, Adapter]:
    data = json.loads(path.read_text(encoding="utf-8"))
    adapters: dict[str, Adapter] = {}
    for item in data.get("adapters", []):
        key = safe_text(item.get("site_adapter"))
        if not key:
            continue
        adapters[key] = Adapter(
            key=key,
            label=safe_text(item.get("institution_scope")) or key,
            expected_terms=tuple(safe_text(t) for t in item.get("expected_terms", [])),
            item_url_pattern=safe_text(item.get("item_url_pattern")),
            status=safe_text(item.get("status")),
            promotion_rule=safe_text(item.get("promotion_rule")),
        )
    return adapters


def load_rows() -> list[dict[str, str]]:
    with SURVEY_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def iter_selected(rows: Iterable[dict[str, str]], entry_ids: set[str], adapters: set[str]) -> Iterable[dict[str, str]]:
    for row in rows:
        if entry_ids and row.get("entry_id") not in entry_ids:
            continue
        if adapters and row.get("site_adapter") not in adapters:
            continue
        yield row


def fetch_url(url: str) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310 - public metadata fetcher
        content_type = resp.headers.get("content-type", "")
        body = resp.read(MAX_BYTES)
    return body, content_type


def html_to_text(raw: str) -> str:
    raw = re.sub(r"(?is)<script.*?</script>", " ", raw)
    raw = re.sub(r"(?is)<style.*?</style>", " ", raw)
    raw = re.sub(r"(?is)<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    raw = re.sub(r"\s+", " ", raw)
    return raw.strip()


def extract_title(raw: str) -> str:
    match = re.search(r"(?is)<title[^>]*>(.*?)</title>", raw)
    if not match:
        return ""
    return html_to_text(match.group(1))


def extract_urls(raw: str, source_url: str) -> list[str]:
    hrefs = re.findall(r"(?i)href=[\"']([^\"']+)[\"']", raw)
    urls: list[str] = []
    for href in hrefs:
        if href.startswith("#") or href.lower().startswith(("javascript:", "mailto:")):
            continue
        if href.startswith("/"):
            base = re.match(r"^(https?://[^/]+)", source_url)
            if base:
                href = base.group(1) + href
        urls.append(href)
    seen: set[str] = set()
    out: list[str] = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            out.append(url)
    return out[:200]


def find_term_hits(text: str, expected_terms: Iterable[str]) -> tuple[list[str], list[str]]:
    text_lower = text.lower()
    found: list[str] = []
    missing: list[str] = []
    for term in expected_terms:
        if term and term.lower() in text_lower:
            found.append(term)
        elif term:
            missing.append(term)
    return found, missing


def count_candidates(text: str) -> list[str]:
    patterns = [
        r"\b(?:about|approximately|approx\.?|around|over|c\.|circa)\s+[\d,]+\b",
        r"\b[\d,]+\s+(?:microscope slides|slides|specimens|objects|drawers|cabinets|boxes|trays)\b",
        r"\b(?:one|two|three|four|five|six|seven|eight|nine|ten|fifty)\s+(?:drawers|cabinets|slides|objects|boxes|trays)\b",
    ]
    candidates: list[str] = []
    for pattern in patterns:
        candidates.extend(re.findall(pattern, text, flags=re.I))
    seen: set[str] = set()
    out: list[str] = []
    for cand in candidates:
        normal = " ".join(cand.split())
        if normal.lower() not in seen:
            seen.add(normal.lower())
            out.append(normal)
    return out[:20]


def classify_media_risks(text: str) -> list[str]:
    risks = []
    text_lower = text.lower()
    for risk in ("lantern slide", "photographic slide", "glass plate negative", "35mm slide"):
        if risk in text_lower:
            risks.append(risk)
    return risks


def build_record(row: dict[str, str], adapter: Adapter, raw_text: str, body: bytes, content_type: str, fetched_utc: str) -> dict[str, Any]:
    text = html_to_text(raw_text)
    found, missing = find_term_hits(text, adapter.expected_terms)
    urls = extract_urls(raw_text, row.get("source_url", ""))

    return {
        "schema_version": "slide-survey-site-adapter-record-v2-global",
        "entry_id": row.get("entry_id"),
        "country": row.get("country"),
        "institution_current": row.get("institution_current"),
        "institution_historical": row.get("institution_historical"),
        "collection_title_or_search_entry": row.get("collection_title_or_search_entry"),
        "source_type": row.get("source_type"),
        "source_url": row.get("source_url"),
        "site_adapter": adapter.key,
        "adapter_label": adapter.label,
        "adapter_status": adapter.status,
        "adapter_promotion_rule": adapter.promotion_rule,
        "item_url_pattern": adapter.item_url_pattern or row.get("stable_id_pattern"),
        "relationship_phrase": row.get("relationship_phrase"),
        "person_or_collection_name": row.get("person_or_collection_name"),
        "slide_certainty": row.get("slide_certainty"),
        "stated_count": row.get("stated_count"),
        "harvestable_item_count": row.get("harvestable_item_count"),
        "date_range": row.get("date_range"),
        "subject_scope": row.get("subject_scope"),
        "physical_structure": row.get("physical_structure"),
        "label_visibility": row.get("label_visibility"),
        "provenance_value": row.get("provenance_value"),
        "automation_feasibility": row.get("automation_feasibility"),
        "event_side_hooks": row.get("event_side_hooks"),
        "exclude_reason": row.get("exclude_reason"),
        "content_type": content_type,
        "byte_length": len(body),
        "source_sha256": hashlib.sha256(body).hexdigest(),
        "fetched_utc": fetched_utc,
        "extracted_title": extract_title(raw_text),
        "adapter_expected_terms_found": found,
        "adapter_expected_terms_missing": missing,
        "count_candidates": count_candidates(text),
        "media_risk_terms_found": classify_media_risks(text),
        "sample_urls": urls[:25],
        "text_sample": text[:4000],
    }


def build_plan_record(row: dict[str, str], adapter: Adapter | None, mode: str, fetched_utc: str) -> dict[str, Any]:
    automation = row.get("automation_feasibility", "")
    source_url = row.get("source_url", "")
    if adapter is None:
        action = "skip_unknown_adapter"
    elif automation in SKIP_AUTOMATION:
        action = "skip_manual_or_blocked"
    elif not source_url:
        action = "skip_missing_source_url"
    elif mode == "dry-run":
        action = "would_fetch_with_site_adapter"
    else:
        action = "fetch_with_site_adapter"

    return {
        "entry_id": row.get("entry_id"),
        "country": row.get("country"),
        "institution_current": row.get("institution_current"),
        "collection_title_or_search_entry": row.get("collection_title_or_search_entry"),
        "source_url": source_url,
        "automation_feasibility": automation,
        "site_adapter": row.get("site_adapter"),
        "adapter_label": adapter.label if adapter else "",
        "adapter_status": adapter.status if adapter else "",
        "mode": mode,
        "action": action,
        "fetched_utc": fetched_utc,
    }


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + "\n")


def parse_csv_set(values: list[str] | None) -> set[str]:
    out: set[str] = set()
    for value in values or []:
        for part in value.split(","):
            part = part.strip()
            if part:
                out.add(part)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["dry-run", "full"], default="dry-run")
    parser.add_argument("--delay", type=float, default=2.0)
    parser.add_argument("--entry-id", action="append", help="Limit to one or more entry_id values. Comma-separated values are accepted.")
    parser.add_argument("--adapter", action="append", help="Limit to one or more site_adapter keys. Comma-separated values are accepted.")
    parser.add_argument("--fail-on-fetch-error", action="store_true")
    args = parser.parse_args()

    registry_raw = json.loads(ADAPTER_REGISTRY_SOURCE_PATH.read_text(encoding="utf-8"))
    adapters_by_key = load_adapter_registry()
    rows = load_rows()
    entry_ids = parse_csv_set(args.entry_id)
    adapter_filter = parse_csv_set(args.adapter)
    selected = list(iter_selected(rows, entry_ids, adapter_filter))
    now = datetime.now(timezone.utc).isoformat()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    NORMALIZED_DIR.mkdir(parents=True, exist_ok=True)

    plan: list[dict[str, Any]] = []
    collection_records: list[dict[str, Any]] = []
    fetch_errors = 0

    for row in selected:
        adapter = adapters_by_key.get(row.get("site_adapter", ""))
        plan_record = build_plan_record(row, adapter, args.mode, now)
        plan.append(plan_record)

        if plan_record["action"] != "fetch_with_site_adapter" or adapter is None:
            continue

        try:
            body, content_type = fetch_url(row["source_url"])
            sha256 = hashlib.sha256(body).hexdigest()
            raw_path = RAW_DIR / f"{slugify(row['entry_id'])}.html"
            raw_path.write_bytes(body)
            raw_text = body.decode("utf-8", errors="replace")
            record = build_record(row, adapter, raw_text, body, content_type, now)
            record["raw_path"] = str(raw_path)
            collection_records.append(record)
            plan_record.update(
                {
                    "action": "fetched_with_site_adapter",
                    "content_type": content_type,
                    "byte_length": len(body),
                    "source_sha256": sha256,
                    "raw_path": str(raw_path),
                }
            )
        except urllib.error.HTTPError as exc:
            fetch_errors += 1
            plan_record.update({"action": "fetch_failed", "error": f"HTTP {exc.code}"})
        except Exception as exc:  # noqa: BLE001
            fetch_errors += 1
            plan_record.update({"action": "fetch_failed", "error": repr(exc)})

        time.sleep(max(args.delay, 0))

    registry_snapshot = {
        "schema_version": registry_raw.get("schema_version", "slide-survey-site-adapter-registry"),
        "purpose": registry_raw.get("purpose", ""),
        "guards": registry_raw.get("guards", []),
        "adapters": {
            key: {
                "label": adapter.label,
                "status": adapter.status,
                "expected_terms": list(adapter.expected_terms),
                "item_url_pattern": adapter.item_url_pattern,
                "promotion_rule": adapter.promotion_rule,
            }
            for key, adapter in adapters_by_key.items()
        },
    }

    write_json(REPORT_PATH, plan)
    write_json(REGISTRY_PATH, registry_snapshot)
    write_jsonl(NORMALIZED_DIR / "collections_seed.jsonl", collection_records)

    print(f"Mode: {args.mode}")
    print(f"Rows: {len(rows)}; selected: {len(selected)}; fetched records: {len(collection_records)}")
    print(f"Plan: {REPORT_PATH}")
    print(f"Adapter registry: {REGISTRY_PATH}")
    if fetch_errors:
        print(f"Fetch errors: {fetch_errors}")
    if fetch_errors and args.fail_on_fetch_error:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
