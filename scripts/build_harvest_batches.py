#!/usr/bin/env python3
"""Build batch harvest plans from the merged slide survey and harvest-family contracts.

Run after `prepare_survey_inputs.py`, so the canonical 07A CSV already contains
all modular expansion batches for this workflow run.

The base harvest-family contract lives in `harvest_families_v1.json`. Small
assignment expansions can be added as `harvest_families_expansion_*.json`, so
new survey waves do not require rewriting the whole base contract.
"""

from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

SURVEY_PATH = Path("data/survey/07A_Global_Microscope_Slide_Collections_Survey.csv")
FAMILY_PATH = Path("data/survey/harvest_families_v1.json")
FAMILY_EXPANSION_GLOB = "harvest_families_expansion_*.json"
JSON_OUT = Path("outputs/harvest_batches.json")
MD_OUT = Path("outputs/harvest_batches.md")

PROVENANCE_SCORE = {"A": 4, "B": 3, "C": 2, "D": 0}
AUTOMATION_SCORE = {
    "API": 4,
    "IIIF": 4,
    "downloadable finding aid": 4,
    "paginated HTML": 3,
    "static HTML": 2,
    "manual only": 0,
    "blocked": -10,
}


def load_rows() -> list[dict[str, str]]:
    with SURVEY_PATH.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_families() -> tuple[dict[str, dict[str, Any]], dict[str, str], list[str]]:
    data = json.loads(FAMILY_PATH.read_text(encoding="utf-8"))
    families: dict[str, dict[str, Any]] = {}
    adapter_to_family: dict[str, str] = {}
    duplicates: dict[str, list[str]] = defaultdict(list)
    expansion_sources: list[str] = []

    def assign(adapter: str, family_name: str) -> None:
        if adapter in adapter_to_family and adapter_to_family[adapter] != family_name:
            duplicates[adapter].extend([adapter_to_family[adapter], family_name])
        adapter_to_family[adapter] = family_name

    for family in data.get("families", []):
        name = family["family"]
        families[name] = family
        for adapter in family.get("adapter_keys", []):
            assign(adapter, name)

    for path in sorted(FAMILY_PATH.parent.glob(FAMILY_EXPANSION_GLOB)):
        expansion_sources.append(str(path))
        expansion = json.loads(path.read_text(encoding="utf-8"))
        for family_name, adapters in expansion.get("assignments", {}).items():
            if family_name not in families:
                raise ValueError(f"Unknown harvest family in {path}: {family_name}")
            for adapter in adapters:
                assign(str(adapter), family_name)

    if duplicates:
        detail = "; ".join(f"{k}: {sorted(set(v))}" for k, v in duplicates.items())
        raise ValueError(f"Adapter assigned to multiple harvest families: {detail}")

    return families, adapter_to_family, expansion_sources


def score_row(row: dict[str, str], family: str) -> int:
    score = PROVENANCE_SCORE.get(row.get("provenance_value", ""), 0) * 10
    score += AUTOMATION_SCORE.get(row.get("automation_feasibility", ""), 0)
    if row.get("stated_count"):
        score += 3
    if row.get("person_or_collection_name"):
        score += 2
    if row.get("physical_structure"):
        score += 2
    if row.get("event_side_hooks"):
        score += 2
    if family in {"dataset_api_or_dwca", "specialized_collection_catalogue", "collection_page_plus_search_portal"}:
        score += 2
    if row.get("exclude_reason"):
        score -= 100
    return score


def main() -> int:
    rows = load_rows()
    families, adapter_to_family, family_expansion_sources = load_families()

    batches: dict[str, list[dict[str, Any]]] = defaultdict(list)
    unassigned: list[dict[str, str]] = []

    for row in rows:
        adapter = row.get("site_adapter", "")
        family = adapter_to_family.get(adapter)
        if not family:
            unassigned.append(row)
            continue
        item = {
            "entry_id": row.get("entry_id"),
            "country": row.get("country"),
            "institution": row.get("institution_current"),
            "collection": row.get("collection_title_or_search_entry"),
            "site_adapter": adapter,
            "source_url": row.get("source_url"),
            "provenance_value": row.get("provenance_value"),
            "automation_feasibility": row.get("automation_feasibility"),
            "stated_count": row.get("stated_count"),
            "relationship_phrase": row.get("relationship_phrase"),
            "physical_structure": row.get("physical_structure"),
            "event_side_hooks": row.get("event_side_hooks"),
            "exclude_reason": row.get("exclude_reason"),
            "priority_score": score_row(row, family),
        }
        batches[family].append(item)

    for items in batches.values():
        items.sort(key=lambda x: (-int(x["priority_score"]), str(x["entry_id"])))

    payload = {
        "schema_version": "slide-survey-harvest-batches-v2-modular-families",
        "survey_rows": len(rows),
        "assigned_rows": sum(len(v) for v in batches.values()),
        "unassigned_rows": len(unassigned),
        "country_counts": dict(Counter(row.get("country", "") for row in rows)),
        "family_expansion_sources": family_expansion_sources,
        "batches": [
            {
                "family": name,
                "phase": families[name].get("phase"),
                "strategy": families[name].get("strategy"),
                "fields": families[name].get("fields", []),
                "row_count": len(batches.get(name, [])),
                "entries": batches.get(name, []),
            }
            for name in families
        ],
        "unassigned": [
            {
                "entry_id": row.get("entry_id"),
                "site_adapter": row.get("site_adapter"),
                "institution": row.get("institution_current"),
            }
            for row in unassigned
        ],
    }

    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    lines = [
        "# Microscope-slide harvest batches",
        "",
        f"Survey rows: {len(rows)}",
        f"Assigned to a harvest family: {payload['assigned_rows']}",
        f"Unassigned: {payload['unassigned_rows']}",
        f"Family assignment expansions: {len(family_expansion_sources)}",
        "",
    ]

    for family in families:
        contract = families[family]
        items = batches.get(family, [])
        lines.extend([
            f"## {family}",
            "",
            f"Phase: {contract.get('phase', '')}",
            f"Strategy: {contract.get('strategy', '')}",
            f"Rows: {len(items)}",
            "",
        ])
        for item in items:
            exclusion = " [excluded]" if item.get("exclude_reason") else ""
            lines.append(
                f"- {item['priority_score']:>3} | {item['entry_id']} | {item['country']} | "
                f"{item['institution']} | {item['automation_feasibility']}{exclusion}"
            )
        lines.append("")

    if unassigned:
        lines.extend(["## Unassigned adapters", ""])
        for row in unassigned:
            lines.append(f"- {row.get('entry_id')} | {row.get('site_adapter')} | {row.get('institution_current')}")
        lines.append("")

    MD_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Built harvest batches: {JSON_OUT}, {MD_OUT}")
    if family_expansion_sources:
        print(f"Loaded {len(family_expansion_sources)} harvest-family expansion file(s)")
    if unassigned:
        print(f"Warning: {len(unassigned)} survey rows have unassigned adapters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
