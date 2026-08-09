#!/usr/bin/env python3
"""Audit the merged microscope-slide survey for nineteenth-century scope.

This audit remains useful as a diagnostic classification over the full canonical
discovery layer. After the 07AR closure, however, its free-text date heuristics
do not define census membership. Downstream active IDs are reconstructed from
the frozen 07K-07AQ strict batches plus the 07AR canonicalisation contract.

Diagnostic classes:
- CORE_19C: explicit nineteenth-century evidence in the row or an override.
- POSSIBLE_19C: potentially relevant but not yet proved.
- MODERN_COMPARATOR: method/infrastructure comparator.
- OUT_OF_SCOPE: explicitly modern/non-nineteenth-century material.
"""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

from build_frozen_strict_membership import write_frozen_membership

SURVEY_PATH = Path("data/survey/07A_Global_Microscope_Slide_Collections_Survey.csv")
OVERRIDE_PATH = Path("data/survey/scope_19c_overrides.json")
CSV_OUT = Path("outputs/scope_19c_audit.csv")
JSON_OUT = Path("outputs/scope_19c_audit.json")
MD_OUT = Path("outputs/scope_19c_audit.md")
DIAGNOSTIC_CORE_IDS_OUT = Path("outputs/scope_19c_diagnostic_core_ids.json")

STATUSES = {"CORE_19C", "POSSIBLE_19C", "MODERN_COMPARATOR", "OUT_OF_SCOPE"}
NINETEENTH_PHRASES = (
    "nineteenth century",
    "nineteenth-century",
    "19th century",
    "19th-century",
    "victorian",
)
MODERN_PHRASES = (
    "twentieth century",
    "twentieth-century",
    "21st century",
    "21st-century",
    "twenty-first century",
    "twenty-first-century",
)


def safe(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " | ".join(safe(v) for v in value)
    return str(value)


def load_rows() -> list[dict[str, str]]:
    with SURVEY_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_overrides() -> dict[str, dict[str, str]]:
    if not OVERRIDE_PATH.exists():
        return {}
    data = json.loads(OVERRIDE_PATH.read_text(encoding="utf-8"))
    overrides = data.get("overrides", {})
    for entry_id, item in overrides.items():
        status = safe(item.get("status"))
        if status not in STATUSES:
            raise ValueError(f"Invalid 19C scope override for {entry_id}: {status!r}")
    return overrides


def years(text: str) -> list[int]:
    return [int(x) for x in re.findall(r"(?<!\d)(1[6-9]\d{2}|20\d{2})(?!\d)", text)]


def nineteenth_hits(text: str) -> list[str]:
    lower = text.lower()
    hits = [p for p in NINETEENTH_PHRASES if p in lower]
    hits.extend(str(y) for y in years(text) if 1800 <= y <= 1899)
    ys = years(text)
    if ys and min(ys) < 1800 and max(ys) > 1899:
        hits.append("date range crosses 1800-1899")
    if "eighteenth century onward" in lower or "18th century onward" in lower:
        hits.append("eighteenth century onward")
    return sorted(set(hits))


def classify(row: dict[str, str], overrides: dict[str, dict[str, str]]) -> tuple[str, str, list[str]]:
    entry_id = safe(row.get("entry_id"))
    if entry_id in overrides:
        item = overrides[entry_id]
        return safe(item.get("status")), f"manual override: {safe(item.get('reason'))}", []

    provenance = safe(row.get("provenance_value"))
    exclude_reason = safe(row.get("exclude_reason")).lower()

    if provenance == "D" or "method comparator" in exclude_reason or "method-only" in exclude_reason:
        return "MODERN_COMPARATOR", "survey row is explicitly method/comparator grade", []

    date_text = safe(row.get("date_range"))
    support_text = " | ".join(
        [
            safe(row.get("collection_title_or_search_entry")),
            safe(row.get("person_or_collection_name")),
            safe(row.get("notes")),
            safe(row.get("event_side_hooks")),
        ]
    )

    date_hits = nineteenth_hits(date_text)
    support_hits = nineteenth_hits(support_text)
    if date_hits:
        return "CORE_19C", "explicit nineteenth-century evidence in date_range", date_hits
    if support_hits:
        return "CORE_19C", "explicit nineteenth-century evidence in collection/person/notes/event fields", support_hits

    date_years = years(date_text)
    date_lower = date_text.lower()
    if date_years and min(date_years) >= 1900:
        return "OUT_OF_SCOPE", "date_range contains only twentieth/twenty-first-century years", [str(y) for y in date_years]
    if any(p in date_lower for p in MODERN_PHRASES) and not any(p in date_lower for p in NINETEENTH_PHRASES):
        return "OUT_OF_SCOPE", "date_range explicitly describes modern-period material", []

    if "modern reference collection" in date_lower or "current ongoing" in date_lower:
        return "OUT_OF_SCOPE", "date_range explicitly identifies a modern/current-only collection", []

    return "POSSIBLE_19C", "no explicit nineteenth-century object/collection/provenance anchor recovered from current row", []


def main() -> int:
    rows = load_rows()
    overrides = load_overrides()
    audit: list[dict[str, Any]] = []

    for row in rows:
        status, reason, hits = classify(row, overrides)
        audit.append(
            {
                "entry_id": safe(row.get("entry_id")),
                "scope_19c_status": status,
                "scope_19c_reason": reason,
                "scope_19c_hits": "; ".join(hits),
                "country": safe(row.get("country")),
                "institution_current": safe(row.get("institution_current")),
                "collection_title_or_search_entry": safe(row.get("collection_title_or_search_entry")),
                "date_range": safe(row.get("date_range")),
                "person_or_collection_name": safe(row.get("person_or_collection_name")),
                "source_url": safe(row.get("source_url")),
                "site_adapter": safe(row.get("site_adapter")),
                "provenance_value": safe(row.get("provenance_value")),
                "automation_feasibility": safe(row.get("automation_feasibility")),
            }
        )

    counts = Counter(item["scope_19c_status"] for item in audit)
    diagnostic_core_ids = [item["entry_id"] for item in audit if item["scope_19c_status"] == "CORE_19C"]

    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(audit[0].keys()) if audit else []
    with CSV_OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(audit)

    frozen_report = write_frozen_membership()
    frozen_count = int(frozen_report["counts"]["frozen_strict_entries"])

    payload = {
        "schema_version": "slide-survey-19c-audit-v2-07AR",
        "temporal_scope": "1800-1899",
        "rule": "Diagnostic heuristic classification over the 307-entry discovery layer. After CLOSED_2026-08-09, downstream membership is the separately reconstructed frozen 07AR strict set and is not altered by heuristic CORE_19C results.",
        "rows": len(audit),
        "status_counts": dict(counts),
        "diagnostic_core_19c_count": len(diagnostic_core_ids),
        "frozen_strict_active_count": frozen_count,
        "frozen_membership_report": "outputs/frozen_strict_membership.json",
        "entries": audit,
    }
    JSON_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    DIAGNOSTIC_CORE_IDS_OUT.write_text(
        json.dumps(
            {
                "schema_version": "slide-survey-19c-diagnostic-core-ids-v1",
                "warning": "Diagnostic only. These IDs do not define the CLOSED_2026-08-09 strict census.",
                "entry_count": len(diagnostic_core_ids),
                "entry_ids": diagnostic_core_ids,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    lines = [
        "# Nineteenth-century scope audit",
        "",
        "Historical scope: **1800-1899**.",
        "",
        "This file is now a diagnostic audit over the full discovery layer. The frozen census membership is reconstructed separately from the 07AR closure contract.",
        "",
        f"Survey rows audited: {len(audit)}",
        f"Diagnostic CORE_19C: {counts.get('CORE_19C', 0)}",
        f"POSSIBLE_19C: {counts.get('POSSIBLE_19C', 0)}",
        f"MODERN_COMPARATOR: {counts.get('MODERN_COMPARATOR', 0)}",
        f"OUT_OF_SCOPE: {counts.get('OUT_OF_SCOPE', 0)}",
        f"Frozen strict active set: **{frozen_count}**",
        "",
        "`CORE_19C` above is a heuristic diagnostic label. It does not add entries to the frozen 155 after closure.",
        "",
        "## Review queue",
        "",
    ]
    for item in audit:
        if item["scope_19c_status"] == "POSSIBLE_19C":
            lines.append(
                f"- `{item['entry_id']}` | {item['country']} | {item['institution_current']} | {item['collection_title_or_search_entry']}"
            )
    MD_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"19C diagnostic audit: {dict(counts)}")
    print(f"Diagnostic CORE_19C entries: {len(diagnostic_core_ids)}")
    print(f"Frozen 07AR strict active entries: {frozen_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
