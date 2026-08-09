#!/usr/bin/env python3
"""Validate the global microscope-slide survey table.

The survey is not an ownership table. It keeps source relationship phrases
intact so that "belonging to", "prepared by", "mounted by", "donated by",
"lent by", "held by", "used by", "produced by", and "digitised by" are not
flattened into one ownership field.

The validator deliberately reads `data/survey/site_adapters.json` at runtime.
That makes the CSV and adapter registry the two active sources of truth: adding
a new institution means adding a survey row and a registry adapter, not editing a
hard-coded Python allow-list.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

SURVEY_PATH = Path("data/survey/07A_Global_Microscope_Slide_Collections_Survey.csv")
ADAPTER_REGISTRY_PATH = Path("data/survey/site_adapters.json")
REPORT_PATH = Path("outputs/run_report.md")
COVERAGE_PATH = Path("outputs/coverage_summary.json")
PRIORITY_PATH = Path("outputs/priority_queue.md")

REQUIRED_COLUMNS = [
    "entry_id",
    "country",
    "institution_current",
    "institution_historical",
    "collection_title_or_search_entry",
    "source_type",
    "source_url",
    "stable_id_pattern",
    "site_adapter",
    "slide_certainty",
    "stated_count",
    "harvestable_item_count",
    "person_or_collection_name",
    "relationship_phrase",
    "date_range",
    "subject_scope",
    "physical_structure",
    "image_level",
    "label_visibility",
    "provenance_value",
    "automation_feasibility",
    "event_side_hooks",
    "exclude_reason",
    "notes",
]

ALLOWED_PROVENANCE = {"A", "B", "C", "D"}
ALLOWED_AUTOMATION = {
    "manual only",
    "static HTML",
    "paginated HTML",
    "API",
    "downloadable finding aid",
    "IIIF",
    "blocked",
}
RISK_TERMS = ("lantern slide", "photographic slide", "glass plate negative", "35mm slide")
OWNERSHIP_COLLAPSE_TERMS = ("owner", "owned by", "ownership")
RELATIONSHIP_TERMS = (
    "prepared by",
    "mounted by",
    "collected by",
    "from the collection of",
    "belonging to",
    "donated by",
    "transferred from",
    "presented to",
    "lent by",
    "assembled by",
    "received by",
    "held by",
    "digitised by",
    "developed by",
    "produced by",
    "used by",
    "inscribed names",
    "part of",
    "hosted by",
    "re-arranged by",
    "inventoried by",
    "collection of",
)

AUTOMATION_SCORE = {
    "API": 4,
    "IIIF": 4,
    "downloadable finding aid": 3,
    "paginated HTML": 3,
    "static HTML": 2,
    "manual only": 0,
    "blocked": -2,
}
PROVENANCE_SCORE = {"A": 5, "B": 3, "C": 1, "D": -4}


def safe_text(value: Any) -> str:
    """Return a stable string for CSV cells and malformed extra-field lists."""
    if value is None:
        return ""
    if isinstance(value, list):
        return " | ".join(safe_text(v) for v in value)
    return str(value)


def is_valid_country_scope(value: str) -> bool:
    """Accept ISO-like country tags plus GLOBAL and multi-country tags.

    Examples: UK, US, DE, AU, NL, FR, GLOBAL, UK-US, FR/DE.
    The field is a survey-scope marker rather than a diplomatic country name.
    """
    return bool(re.fullmatch(r"GLOBAL|[A-Z]{2,3}([-/][A-Z]{2,3})*", value))


def load_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Survey table not found: {path}")
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != REQUIRED_COLUMNS:
            missing = [c for c in REQUIRED_COLUMNS if c not in (reader.fieldnames or [])]
            extra = [c for c in (reader.fieldnames or []) if c not in REQUIRED_COLUMNS]
            raise ValueError(f"Unexpected columns. Missing={missing}; extra={extra}")
        return list(reader)


def load_adapter_registry(path: Path) -> tuple[dict[str, dict[str, Any]], list[str], list[str]]:
    """Return adapter records, duplicate adapter keys, and registry structural errors."""
    if not path.exists():
        raise FileNotFoundError(f"Adapter registry not found: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    adapters = data.get("adapters", [])
    if not isinstance(adapters, list):
        raise ValueError("Adapter registry field `adapters` must be a list")

    keys: list[str] = []
    errors: list[str] = []
    registry: dict[str, dict[str, Any]] = {}
    for idx, item in enumerate(adapters, start=1):
        if not isinstance(item, dict):
            errors.append(f"adapter row {idx}: must be an object")
            continue
        key = safe_text(item.get("site_adapter"))
        if not key:
            errors.append(f"adapter row {idx}: missing site_adapter")
            continue
        keys.append(key)
        registry[key] = item
        if not safe_text(item.get("status")):
            errors.append(f"adapter {key}: missing status")
        if not isinstance(item.get("expected_terms", []), list):
            errors.append(f"adapter {key}: expected_terms must be a list")
        if not safe_text(item.get("promotion_rule")):
            errors.append(f"adapter {key}: missing promotion_rule")

    duplicates = [key for key, count in Counter(keys).items() if count > 1]
    return registry, duplicates, errors


def validate(rows: list[dict[str, Any]], adapter_registry: dict[str, dict[str, Any]], duplicate_adapters: list[str], registry_errors: list[str]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    errors.extend(f"adapter registry: {err}" for err in registry_errors)
    errors.extend(f"adapter registry: duplicate site_adapter {key}" for key in duplicate_adapters)

    ids = Counter(safe_text(row.get("entry_id")) for row in rows)
    for entry_id, count in ids.items():
        if count > 1:
            errors.append(f"Duplicate entry_id: {entry_id}")

    row_adapters = Counter(safe_text(row.get("site_adapter")) for row in rows)
    for adapter_key in sorted(set(adapter_registry) - set(row_adapters)):
        warnings.append(f"adapter registry: adapter currently unused by survey CSV: {adapter_key}")

    for i, row in enumerate(rows, start=2):
        rid = safe_text(row.get("entry_id")) or f"row {i}"

        if None in row:
            errors.append(f"{rid}: malformed CSV row has extra values beyond header: {safe_text(row[None])}")

        country = safe_text(row.get("country"))
        if not is_valid_country_scope(country):
            errors.append(f"{rid}: country must be ISO-like scope or GLOBAL, got {country!r}")

        provenance = safe_text(row.get("provenance_value"))
        automation = safe_text(row.get("automation_feasibility"))
        adapter_key = safe_text(row.get("site_adapter"))
        exclude_reason = safe_text(row.get("exclude_reason"))

        if provenance not in ALLOWED_PROVENANCE:
            errors.append(f"{rid}: provenance_value must be A/B/C/D, got {provenance!r}")
        if automation not in ALLOWED_AUTOMATION:
            errors.append(f"{rid}: unsupported automation_feasibility {automation!r}")
        if adapter_key not in adapter_registry:
            errors.append(f"{rid}: site_adapter missing from registry: {adapter_key!r}")

        joined = " ".join(safe_text(v) for v in row.values()).lower()
        if any(term in joined for term in RISK_TERMS) and not exclude_reason:
            warnings.append(f"{rid}: slide-media risk term present; add exclude_reason or clarify microscope-slide certainty.")

        relationship = safe_text(row.get("relationship_phrase")).lower()
        if any(term in relationship for term in OWNERSHIP_COLLAPSE_TERMS):
            warnings.append(f"{rid}: avoid flattening relations into ownership; preserve source phrase.")
        if relationship and not any(term in relationship for term in RELATIONSHIP_TERMS):
            warnings.append(f"{rid}: relationship_phrase may need normalization or source-language preservation: {safe_text(row.get('relationship_phrase'))!r}")

        if automation not in {"manual only", "blocked"} and not safe_text(row.get("source_url")):
            errors.append(f"{rid}: automated row lacks source_url")
        if automation == "manual only" and adapter_key.endswith("_search"):
            warnings.append(f"{rid}: manual-only row uses a search adapter name; use a *_manual adapter or enable harvesting.")

        if provenance in {"A", "B"} and not (
            safe_text(row.get("person_or_collection_name"))
            or safe_text(row.get("physical_structure"))
            or safe_text(row.get("stated_count"))
        ):
            warnings.append(f"{rid}: A/B row should preserve person, count, or physical batch structure.")

        slide_certainty = safe_text(row.get("slide_certainty")).lower()
        if "slide" not in slide_certainty and not exclude_reason:
            warnings.append(f"{rid}: slide_certainty does not explicitly say slide/slides.")

        if provenance == "D" and not exclude_reason:
            warnings.append(f"{rid}: D-grade row should state why it is method-only, weak, or excluded.")
        if provenance == "D" and automation != "manual only" and "method" not in exclude_reason:
            warnings.append(f"{rid}: D-grade automated row should usually be a method/comparator row, not collection evidence.")

        if country == "GLOBAL" and provenance != "D" and not exclude_reason:
            warnings.append(f"{rid}: GLOBAL row should normally be method/infrastructure unless a physical collection is specified.")

    return errors, warnings


def priority_score(row: dict[str, Any]) -> int:
    provenance = safe_text(row.get("provenance_value"))
    automation = safe_text(row.get("automation_feasibility"))
    score = PROVENANCE_SCORE.get(provenance, 0) + AUTOMATION_SCORE.get(automation, 0)

    if safe_text(row.get("stated_count")):
        score += 1
    if safe_text(row.get("person_or_collection_name")):
        score += 1
    if safe_text(row.get("relationship_phrase")):
        score += 1
    if safe_text(row.get("physical_structure")):
        score += 1
    if safe_text(row.get("label_visibility")).lower() not in {"", "none", "not applicable", "unknown"}:
        score += 1
    if safe_text(row.get("event_side_hooks")):
        score += 1
    if safe_text(row.get("exclude_reason")):
        score -= 2

    return score


def build_priority_queue(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    queue: list[dict[str, Any]] = []
    for row in rows:
        if safe_text(row.get("provenance_value")) == "D":
            continue
        if safe_text(row.get("automation_feasibility")) == "blocked":
            continue
        if safe_text(row.get("exclude_reason")):
            continue
        queue.append(
            {
                "entry_id": safe_text(row.get("entry_id")),
                "score": priority_score(row),
                "country": safe_text(row.get("country")),
                "institution_current": safe_text(row.get("institution_current")),
                "collection_title_or_search_entry": safe_text(row.get("collection_title_or_search_entry")),
                "provenance_value": safe_text(row.get("provenance_value")),
                "automation_feasibility": safe_text(row.get("automation_feasibility")),
                "site_adapter": safe_text(row.get("site_adapter")),
                "stated_count": safe_text(row.get("stated_count")),
                "relationship_phrase": safe_text(row.get("relationship_phrase")),
            }
        )
    queue.sort(key=lambda item: (-int(item["score"]), item["country"], item["entry_id"]))
    return queue


def write_report(rows: list[dict[str, Any]], adapter_registry: dict[str, dict[str, Any]], errors: list[str], warnings: list[str]) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    country_counts = Counter(safe_text(row.get("country")) for row in rows)
    value_counts = Counter(safe_text(row.get("provenance_value")) for row in rows)
    automation_counts = Counter(safe_text(row.get("automation_feasibility")) for row in rows)
    adapter_counts = Counter(safe_text(row.get("site_adapter")) for row in rows)
    adapter_status_counts = Counter(safe_text(item.get("status")) for item in adapter_registry.values())
    priority_queue = build_priority_queue(rows)

    coverage = {
        "rows": len(rows),
        "countries_or_scopes": dict(country_counts),
        "provenance_values": dict(value_counts),
        "automation_feasibility": dict(automation_counts),
        "survey_site_adapters": dict(adapter_counts),
        "registry_adapter_statuses": dict(adapter_status_counts),
        "registry_adapter_count": len(adapter_registry),
        "priority_queue_count": len(priority_queue),
        "top_priority_entries": priority_queue[:10],
        "errors": errors,
        "warnings": warnings,
    }
    COVERAGE_PATH.write_text(json.dumps(coverage, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# Slide survey validation report",
        "",
        f"Rows: {len(rows)}",
        f"Countries/scopes: {dict(country_counts)}",
        f"Provenance values: {dict(value_counts)}",
        f"Automation feasibility: {dict(automation_counts)}",
        f"Survey site adapters: {dict(adapter_counts)}",
        f"Registry adapter statuses: {dict(adapter_status_counts)}",
        f"Priority queue entries: {len(priority_queue)}",
        "",
        f"Errors: {len(errors)}",
    ]
    lines.extend(f"- {e}" for e in errors)
    lines.append("")
    lines.append(f"Warnings: {len(warnings)}")
    lines.extend(f"- {w}" for w in warnings)
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    queue_lines = [
        "# Global microscope-slide survey priority queue",
        "",
        "This queue is generated from the survey CSV. It excludes D-grade method-only rows, blocked rows, and explicitly excluded candidates.",
        "",
        "| Rank | Score | Entry | Scope | Institution | Provenance | Automation | Adapter | Count / relation |",
        "|---:|---:|---|---|---|---|---|---|---|",
    ]
    for rank, item in enumerate(priority_queue, start=1):
        count_relation = "; ".join(part for part in [item["stated_count"], item["relationship_phrase"]] if part)
        queue_lines.append(
            "| {rank} | {score} | `{entry}` | {country} | {inst} | {prov} | {auto} | `{adapter}` | {count_relation} |".format(
                rank=rank,
                score=item["score"],
                entry=item["entry_id"],
                country=item["country"],
                inst=item["institution_current"].replace("|", "/"),
                prov=item["provenance_value"],
                auto=item["automation_feasibility"],
                adapter=item["site_adapter"],
                count_relation=count_relation.replace("|", "/"),
            )
        )
    PRIORITY_PATH.write_text("\n".join(queue_lines) + "\n", encoding="utf-8")


def main() -> int:
    try:
        rows = load_rows(SURVEY_PATH)
        adapter_registry, duplicate_adapters, registry_errors = load_adapter_registry(ADAPTER_REGISTRY_PATH)
        errors, warnings = validate(rows, adapter_registry, duplicate_adapters, registry_errors)
        write_report(rows, adapter_registry, errors, warnings)
    except Exception as exc:  # noqa: BLE001
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        return 2

    print(f"Validated {len(rows)} rows. Report: {REPORT_PATH}")
    print(f"Coverage summary: {COVERAGE_PATH}")
    print(f"Priority queue: {PRIORITY_PATH}")
    if warnings:
        print(f"Warnings: {len(warnings)}")
    if errors:
        print(f"Errors: {len(errors)}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
