#!/usr/bin/env python3
"""Restrict the prepared runtime survey to the frozen 07AR strict membership.

Run after `audit_19c_scope.py`. The audit still classifies the full merged survey
diagnostically, while `data/normalized/scope_19c_active_ids.json` is now written
from the immutable 07K-07AQ + 07AR closure contract. This script therefore
filters to the frozen 155 rather than re-promoting rows from free-text dates.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

SURVEY_PATH = Path("data/survey/07A_Global_Microscope_Slide_Collections_Survey.csv")
ACTIVE_IDS_PATH = Path("data/normalized/scope_19c_active_ids.json")
FULL_SNAPSHOT_PATH = Path("outputs/full_merged_survey_before_19c_filter.csv")
FILTER_REPORT = Path("outputs/scope_19c_filter_report.json")
EXPECTED_FROZEN_STRICT = 155


def main() -> int:
    if not ACTIVE_IDS_PATH.exists():
        raise FileNotFoundError("Run scripts/audit_19c_scope.py before applying the frozen 19C filter")

    active_payload = json.loads(ACTIVE_IDS_PATH.read_text(encoding="utf-8"))
    active = set(active_payload.get("entry_ids", []))
    if active_payload.get("status") == "CLOSED_2026-08-09" and len(active) != EXPECTED_FROZEN_STRICT:
        raise ValueError(f"Frozen active-ID count drifted: {len(active)} != {EXPECTED_FROZEN_STRICT}")

    with SURVEY_PATH.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    FULL_SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with FULL_SNAPSHOT_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    kept = [row for row in rows if row.get("entry_id") in active]
    excluded = [row.get("entry_id", "") for row in rows if row.get("entry_id") not in active]

    if active_payload.get("status") == "CLOSED_2026-08-09" and len(kept) != EXPECTED_FROZEN_STRICT:
        missing = sorted(active - {row.get("entry_id", "") for row in rows})
        raise ValueError(f"Prepared survey does not contain the complete frozen strict set; missing={missing}")

    with SURVEY_PATH.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(kept)

    FILTER_REPORT.write_text(
        json.dumps(
            {
                "schema_version": "slide-survey-19c-runtime-filter-v2-07AR",
                "membership_status": active_payload.get("status", ""),
                "membership_schema": active_payload.get("schema_version", ""),
                "rows_before_filter": len(rows),
                "frozen_strict_rows_after_filter": len(kept),
                "excluded_from_downstream_harvest": len(excluded),
                "excluded_entry_ids": excluded,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"Frozen 19C runtime filter: {len(rows)} -> {len(kept)} active rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
