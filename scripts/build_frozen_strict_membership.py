#!/usr/bin/env python3
"""Reconstruct the immutable 07AR strict nineteenth-century membership.

The 2026-08-09 closure froze the strict catalogue at 155 canonical entries.
That membership is defined by the provisional strict batches 07K-07AQ, then the
07AR canonicalisation rules: remove the twenty superseded distinct-ID aliases,
collapse repeated identical entry IDs, and apply explicit non-CORE scope
overrides (principally Pieter Harting's closure-stage demotion).

This script deliberately does not infer membership from free-text dates. It
turns the closure decision into an executable, count-checked contract and writes
the downstream active-ID file used by harvest/export code.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Any

SURVEY_DIR = Path("data/survey")
ALIAS_PATH = SURVEY_DIR / "07AR_SUPERSEDED_ALIASES_2026-08-09.json"
OVERRIDE_PATH = SURVEY_DIR / "scope_19c_overrides.json"
CLOSURE_MANIFEST = SURVEY_DIR / "07AR_CLOSURE_MANIFEST_2026-08-09.json"
ACTIVE_IDS_OUT = Path("data/normalized/scope_19c_active_ids.json")
REPORT_OUT = Path("outputs/frozen_strict_membership.json")

EXPECTED_PROVISIONAL_OCCURRENCES = 177
EXPECTED_SUPERSEDED_DISTINCT_IDS = 20
EXPECTED_SAME_ID_DUPLICATE_OCCURRENCES = 1
EXPECTED_NON_CORE_DEMOTIONS = 1
EXPECTED_FROZEN_STRICT = 155

STRICT_LABELS = [chr(c) for c in range(ord("K"), ord("Z") + 1)] + [
    f"A{chr(c)}" for c in range(ord("A"), ord("Q") + 1)
]
STRICT_LABEL_ORDER = {label: i for i, label in enumerate(STRICT_LABELS)}
BATCH_RE = re.compile(r"^07([K-Z]|A[A-Q])_Global_Microscope_Slide_Collections.*\.csv$")


def strict_batch_paths() -> list[Path]:
    found: dict[str, Path] = {}
    for path in SURVEY_DIR.glob("07*_Global_Microscope_Slide_Collections*.csv"):
        match = BATCH_RE.match(path.name)
        if not match:
            continue
        label = match.group(1)
        if label in found:
            raise ValueError(f"More than one strict batch for 07{label}: {found[label]} and {path}")
        found[label] = path
    missing = [label for label in STRICT_LABELS if label not in found]
    if missing:
        raise FileNotFoundError(f"Missing frozen strict batches: {', '.join('07' + x for x in missing)}")
    return [found[label] for label in STRICT_LABELS]


def read_entry_ids(path: Path) -> list[str]:
    """Read only the first CSV field, so legacy trailing-note overflow is irrelevant."""
    ids: list[str] = []
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader, None)
        if not header or header[0] != "entry_id":
            raise ValueError(f"Unexpected first column in {path}: {header!r}")
        for line_number, row in enumerate(reader, start=2):
            if not row:
                continue
            entry_id = row[0].strip()
            if not entry_id:
                raise ValueError(f"Blank entry_id in {path}:{line_number}")
            ids.append(entry_id)
    return ids


def load_aliases() -> dict[str, dict[str, str]]:
    payload = json.loads(ALIAS_PATH.read_text(encoding="utf-8"))
    aliases = payload.get("superseded_entry_ids", {})
    if not isinstance(aliases, dict):
        raise ValueError("Invalid 07AR alias map")
    return aliases


def load_overrides() -> dict[str, dict[str, str]]:
    if not OVERRIDE_PATH.exists():
        return {}
    payload = json.loads(OVERRIDE_PATH.read_text(encoding="utf-8"))
    overrides = payload.get("overrides", {})
    if not isinstance(overrides, dict):
        raise ValueError("Invalid scope override map")
    return overrides


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_frozen_ids() -> tuple[list[str], dict[str, Any]]:
    manifest = json.loads(CLOSURE_MANIFEST.read_text(encoding="utf-8"))
    if manifest.get("status") != "CLOSED_2026-08-09":
        raise ValueError("07AR closure manifest is not in the expected frozen state")
    manifest_expected = int(manifest.get("final_counts", {}).get("canonical_strict_19c_entries", -1))
    if manifest_expected != EXPECTED_FROZEN_STRICT:
        raise ValueError(f"Closure manifest strict count changed: {manifest_expected}")

    paths = strict_batch_paths()
    occurrences: list[tuple[str, str]] = []
    for path in paths:
        for entry_id in read_entry_ids(path):
            occurrences.append((entry_id, path.name))

    if len(occurrences) != EXPECTED_PROVISIONAL_OCCURRENCES:
        raise ValueError(
            f"Frozen provisional strict occurrence count drifted: {len(occurrences)} "
            f"!= {EXPECTED_PROVISIONAL_OCCURRENCES}"
        )

    aliases = load_aliases()
    if len(aliases) != EXPECTED_SUPERSEDED_DISTINCT_IDS:
        raise ValueError(
            f"07AR superseded distinct-ID count drifted: {len(aliases)} "
            f"!= {EXPECTED_SUPERSEDED_DISTINCT_IDS}"
        )
    overrides = load_overrides()

    kept: list[str] = []
    seen: set[str] = set()
    skipped_aliases: list[str] = []
    duplicate_occurrences: list[str] = []
    demoted_by_override: list[dict[str, str]] = []

    for entry_id, _batch in occurrences:
        if entry_id in aliases:
            skipped_aliases.append(entry_id)
            continue
        if entry_id in seen:
            duplicate_occurrences.append(entry_id)
            continue
        seen.add(entry_id)

        override = overrides.get(entry_id)
        if override and str(override.get("status", "")) != "CORE_19C":
            demoted_by_override.append(
                {
                    "entry_id": entry_id,
                    "status": str(override.get("status", "")),
                    "reason": str(override.get("reason", "")),
                }
            )
            continue
        kept.append(entry_id)

    if len(set(skipped_aliases)) != EXPECTED_SUPERSEDED_DISTINCT_IDS:
        raise ValueError(
            f"Strict batches did not contain all 07AR aliases exactly as expected: "
            f"{len(set(skipped_aliases))} distinct aliases found"
        )
    if len(duplicate_occurrences) != EXPECTED_SAME_ID_DUPLICATE_OCCURRENCES:
        raise ValueError(
            f"Same-ID duplicate occurrence count drifted: {len(duplicate_occurrences)} "
            f"!= {EXPECTED_SAME_ID_DUPLICATE_OCCURRENCES}"
        )
    if len(demoted_by_override) != EXPECTED_NON_CORE_DEMOTIONS:
        raise ValueError(
            f"Closure-stage non-CORE demotion count drifted: {len(demoted_by_override)} "
            f"!= {EXPECTED_NON_CORE_DEMOTIONS}"
        )
    if len(kept) != EXPECTED_FROZEN_STRICT:
        raise ValueError(f"Frozen strict count drifted: {len(kept)} != {EXPECTED_FROZEN_STRICT}")

    report = {
        "schema_version": "slide-survey-frozen-strict-membership-v1-07AR",
        "status": "CLOSED_2026-08-09",
        "rule": "07K-07AQ provisional strict occurrences, minus 07AR superseded aliases, repeated identical entry IDs, and explicit non-CORE closure overrides. Free-text date heuristics do not alter membership.",
        "counts": {
            "provisional_occurrences": len(occurrences),
            "superseded_distinct_ids": len(set(skipped_aliases)),
            "same_id_duplicate_occurrences": len(duplicate_occurrences),
            "non_core_demotions": len(demoted_by_override),
            "frozen_strict_entries": len(kept),
        },
        "strict_batches": [path.name for path in paths],
        "duplicate_occurrences": duplicate_occurrences,
        "demoted_by_override": demoted_by_override,
        "source_hashes": {
            "closure_manifest_sha256": sha256(CLOSURE_MANIFEST),
            "alias_map_sha256": sha256(ALIAS_PATH),
            "scope_overrides_sha256": sha256(OVERRIDE_PATH),
        },
        "entry_ids": kept,
    }
    return kept, report


def write_frozen_membership() -> dict[str, Any]:
    entry_ids, report = build_frozen_ids()
    ACTIVE_IDS_OUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT_OUT.parent.mkdir(parents=True, exist_ok=True)
    ACTIVE_IDS_OUT.write_text(
        json.dumps(
            {
                "schema_version": "slide-survey-19c-active-ids-frozen-v1-07AR",
                "status": "CLOSED_2026-08-09",
                "membership_source": "07AR closure contract; see outputs/frozen_strict_membership.json",
                "entry_count": len(entry_ids),
                "entry_ids": entry_ids,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    REPORT_OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    report = write_frozen_membership()
    counts = report["counts"]
    print(
        "Frozen 07AR strict membership: "
        f"{counts['provisional_occurrences']} provisional occurrences -> "
        f"{counts['frozen_strict_entries']} canonical strict entries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
