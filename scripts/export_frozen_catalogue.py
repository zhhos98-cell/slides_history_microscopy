#!/usr/bin/env python3
"""Export the CLOSED_2026-08-09 155-entry microscope-slide catalogue.

This exporter does not use the heuristic CORE_19C classifier to decide
membership. It reads the closure-derived active IDs produced by
`build_frozen_strict_membership.py`, filters the prepared canonical survey,
applies the 07AR final-QC export overlay, runs hard catalogue checks, and writes
both a full backend export and a compact research-facing export.

Use `--prepare` on a clean checkout to merge the modular survey batches first.
The preparation step mutates the runtime 07A file in the checkout but does not
commit it. The final-QC overlay is export-only: it does not rewrite the modular
audit trail or alter the frozen membership.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from build_frozen_strict_membership import write_frozen_membership

SURVEY = Path("data/survey/07A_Global_Microscope_Slide_Collections_Survey.csv")
ACTIVE = Path("data/normalized/scope_19c_active_ids.json")
QC_OVERLAY = Path("data/survey/07AR_FINAL_QC_OVERRIDES_2026-08-09.json")
OUT_DIR = Path("outputs/final_catalogue")
EXPECTED_COUNT = 155

COMPACT_FIELDS = [
    "entry_id",
    "country",
    "institution_current",
    "institution_historical",
    "collection_title_or_search_entry",
    "source_type",
    "source_url",
    "stable_id_pattern",
    "slide_certainty",
    "stated_count",
    "harvestable_item_count",
    "person_or_collection_name",
    "relationship_phrase",
    "date_range",
    "subject_scope",
    "physical_structure",
    "provenance_value",
    "event_side_hooks",
    "notes",
]

QC_REQUIRED_FIELDS = [
    "entry_id",
    "country",
    "institution_current",
    "collection_title_or_search_entry",
    "source_type",
    "source_url",
    "slide_certainty",
    "stated_count",
    "harvestable_item_count",
    "person_or_collection_name",
    "relationship_phrase",
    "date_range",
    "subject_scope",
    "physical_structure",
    "provenance_value",
    "event_side_hooks",
    "notes",
]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_survey() -> tuple[list[str], list[dict[str, str]]]:
    with SURVEY.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        return fields, list(reader)


def load_qc_overlay() -> dict[str, Any]:
    if not QC_OVERLAY.exists():
        raise FileNotFoundError(f"Missing final QC overlay: {QC_OVERLAY}")
    payload = json.loads(QC_OVERLAY.read_text(encoding="utf-8"))
    if payload.get("status") != "CLOSED_2026-08-09":
        raise ValueError("Final QC overlay does not match closure status")
    return payload


def apply_qc_overlay(rows: list[dict[str, str]], active_ids: list[str]) -> tuple[list[dict[str, str]], dict[str, Any]]:
    payload = load_qc_overlay()
    institution_map = payload.get("institution_value_map", {})
    entry_overrides = payload.get("entry_field_overrides", {})
    active = set(active_ids)

    unknown_override_ids = sorted(set(entry_overrides) - active)
    if unknown_override_ids:
        raise ValueError(f"Final QC overlay references IDs outside frozen 155: {unknown_override_ids}")

    changed_institution_rows = 0
    changed_entry_fields = 0
    touched_entry_ids: set[str] = set()
    out: list[dict[str, str]] = []

    for source_row in rows:
        row = dict(source_row)
        original_institution = row.get("institution_current", "")
        canonical = institution_map.get(original_institution)
        if canonical and canonical != original_institution:
            row["institution_current"] = str(canonical)
            changed_institution_rows += 1
            touched_entry_ids.add(row.get("entry_id", ""))

        overrides = entry_overrides.get(row.get("entry_id", ""), {})
        for field, value in overrides.items():
            if field not in row:
                raise ValueError(f"QC override field does not exist: {field}")
            if row[field] != str(value):
                row[field] = str(value)
                changed_entry_fields += 1
                touched_entry_ids.add(row.get("entry_id", ""))
        out.append(row)

    stats = {
        "overlay": str(QC_OVERLAY),
        "schema_version": payload.get("schema_version", ""),
        "institution_rows_normalised": changed_institution_rows,
        "entry_fields_clarified": changed_entry_fields,
        "touched_entries": len(touched_entry_ids),
        "touched_entry_ids": sorted(touched_entry_ids),
    }
    return out, stats


def run_final_qc(rows: list[dict[str, str]]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    ids = [row.get("entry_id", "") for row in rows]
    if len(rows) != EXPECTED_COUNT:
        errors.append(f"row count {len(rows)} != {EXPECTED_COUNT}")
    if len(set(ids)) != EXPECTED_COUNT:
        errors.append(f"unique entry_id count {len(set(ids))} != {EXPECTED_COUNT}")

    for row in rows:
        entry_id = row.get("entry_id", "")
        country = row.get("country", "")
        if entry_id and country and entry_id.split("-", 1)[0] != country:
            errors.append(f"country/entry_id prefix mismatch: {entry_id} vs {country}")

        for field in QC_REQUIRED_FIELDS:
            if not str(row.get(field, "")).strip():
                errors.append(f"blank required field {field}: {entry_id}")

        url = row.get("source_url", "").strip()
        parsed = urlparse(url)
        if parsed.scheme != "https" or not parsed.netloc:
            errors.append(f"non-HTTPS or malformed source_url: {entry_id}: {url}")

        if row.get("provenance_value", "") not in {"A", "B"}:
            errors.append(f"unexpected provenance grade in frozen strict set: {entry_id}: {row.get('provenance_value')}")

        for field, value in row.items():
            if value != value.strip():
                errors.append(f"edge whitespace in {field}: {entry_id}")
            if any(ch in value for ch in ("\n", "\r", "\t", "\ufffd")):
                errors.append(f"control/replacement character in {field}: {entry_id}")

    # Same source URL can legitimately support multiple rows (distributed copies,
    # parent/child nodes, collection/subcollection nodes). Report this for audit,
    # but never collapse on URL alone.
    url_groups: dict[str, list[str]] = {}
    for row in rows:
        url_groups.setdefault(row["source_url"], []).append(row["entry_id"])
    repeated_urls = {url: entry_ids for url, entry_ids in url_groups.items() if len(entry_ids) > 1}
    if repeated_urls:
        warnings.append(
            f"{len(repeated_urls)} source URLs support more than one retained row; reviewed as evidence sharing, not automatic duplicates"
        )

    if errors:
        raise ValueError("Final catalogue QC failed:\n- " + "\n- ".join(errors))

    return {
        "status": "PASS",
        "rows": len(rows),
        "unique_entry_ids": len(set(ids)),
        "required_field_blanks": 0,
        "malformed_or_non_https_urls": 0,
        "country_prefix_mismatches": 0,
        "unexpected_provenance_grades": 0,
        "repeated_source_url_groups": len(repeated_urls),
        "repeated_source_url_rows": sum(len(v) for v in repeated_urls.values()),
        "warnings": warnings,
    }


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_jsonl(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prepare",
        action="store_true",
        help="Run prepare_survey_inputs.py before export; useful on a clean checkout.",
    )
    parser.add_argument("--output", type=Path, default=OUT_DIR)
    args = parser.parse_args()

    if args.prepare:
        subprocess.run([sys.executable, "scripts/prepare_survey_inputs.py"], check=True)

    frozen_report = write_frozen_membership()
    active_payload = json.loads(ACTIVE.read_text(encoding="utf-8"))
    active_ids = list(active_payload.get("entry_ids", []))
    if len(active_ids) != EXPECTED_COUNT or len(set(active_ids)) != EXPECTED_COUNT:
        raise ValueError(f"Frozen active membership is not exactly {EXPECTED_COUNT} unique IDs")

    fields, all_rows = read_survey()
    by_id = {row.get("entry_id", ""): row for row in all_rows}
    missing = [entry_id for entry_id in active_ids if entry_id not in by_id]
    if missing:
        raise ValueError(f"Prepared survey is missing frozen IDs: {missing}")

    # Preserve closure/batch order rather than sorting alphabetically.
    rows = [by_id[entry_id] for entry_id in active_ids]
    if len(rows) != EXPECTED_COUNT:
        raise ValueError(f"Final export count drifted: {len(rows)}")

    for required in COMPACT_FIELDS:
        if required not in fields:
            raise ValueError(f"Compact export field missing from survey schema: {required}")

    rows, qc_overlay_stats = apply_qc_overlay(rows, active_ids)
    qc_result = run_final_qc(rows)

    out = args.output
    out.mkdir(parents=True, exist_ok=True)
    full_csv = out / "GLOBAL_MICROSCOPE_SLIDE_CATALOGUE_19C_BACKEND.csv"
    compact_csv = out / "GLOBAL_MICROSCOPE_SLIDE_CATALOGUE_19C.csv"
    jsonl = out / "GLOBAL_MICROSCOPE_SLIDE_CATALOGUE_19C.jsonl"
    manifest_path = out / "GLOBAL_MICROSCOPE_SLIDE_CATALOGUE_19C_MANIFEST.json"

    write_csv(full_csv, fields, rows)
    write_csv(compact_csv, COMPACT_FIELDS, rows)
    write_jsonl(jsonl, rows)

    manifest: dict[str, Any] = {
        "schema_version": "global-microscope-slide-catalogue-19c-export-v2-final-qc-07AR",
        "status": "CLOSED_2026-08-09",
        "historical_scope": "1800-1899",
        "canonical_discovery_entries": 307,
        "frozen_strict_entries": len(rows),
        "membership_source": "07K-07AQ provisional strict batches + 07AR canonicalisation contract",
        "membership_schema": active_payload.get("schema_version", ""),
        "membership_report": "outputs/frozen_strict_membership.json",
        "row_order": "frozen closure/batch order",
        "files": {
            full_csv.name: {"rows": len(rows), "sha256": sha256(full_csv)},
            compact_csv.name: {"rows": len(rows), "sha256": sha256(compact_csv)},
            jsonl.name: {"rows": len(rows), "sha256": sha256(jsonl)},
        },
        "final_qc": qc_result,
        "final_qc_overlay": qc_overlay_stats,
        "quantity_rule": "Counts, serial positions, identifiers, containers, cabinet capacities, current aggregates and database rows remain separate namespaces.",
        "relationship_rule": "Relationship phrases are preserved as source claims and are not flattened into ownership or preparation attribution.",
        "reopening_policy": "Any new discovery or corrected attribution belongs to a later version/reopening and does not silently alter this export.",
        "frozen_membership_counts": frozen_report.get("counts", {}),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Final catalogue QC: {qc_result['status']} ({qc_result['rows']} rows, {qc_result['unique_entry_ids']} unique IDs)")
    print(
        "QC overlay: "
        f"{qc_overlay_stats['institution_rows_normalised']} institution strings normalised; "
        f"{qc_overlay_stats['entry_fields_clarified']} entry fields clarified"
    )
    print(f"Exported frozen microscope-slide catalogue: {len(rows)} rows -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
