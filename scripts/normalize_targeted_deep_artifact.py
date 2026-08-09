#!/usr/bin/env python3
"""Normalise the final targeted-deep Actions artifact without reopening the census.

Input is the extracted root of `slide-metadata-targeted-deep-4`. The script keeps
only evidence types that the final harvest demonstrated are useful:

- Copenhagen: de-duplicate repeated species rows to physical SNM slide IDs while
  retaining every species label attached to the same ID.
- Farlow/Cheever: preserve public box/slide table rows exactly, with collision
  flags. The collection is mixed-period, so these rows are position evidence and
  are never auto-promoted to nineteenth-century object dates.
- St Andrews: preserve Bell-Pettigrew child-group hierarchy rows.
- ANSP: retain Symbiota output only as a review pool because the site's nominal
  pre-1900 query returned later records.
- UCL, Whipple and MCZ: retain compact page-level identifier/relationship/count
  candidates for contextual review.
- Sorbonne: intentionally ignored because run 4 ended during that job and its
  partial output lacks a complete summary/records layer.

The output is an enrichment/evidence package. It does not alter the frozen
307-entry discovery layer or the frozen 155-entry strict layer.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, OrderedDict
from pathlib import Path
from typing import Any

RUN_ID = 31287016342
RUN_NUMBER = 4
COMBINED_ARTIFACT = "slide-metadata-targeted-deep-4"
COMBINED_ARTIFACT_ID = 9030222733
COMBINED_ARTIFACT_SHA256 = "96d06a4077b2af803959e536cb66c7509b5058f418879429cc77e4d8bca64808"
SORBONNE_ARTIFACT_ID = 9030220884

INST_COPENHAGEN = "institution-natural-history-museum-of-denmark-university-of-copenhagen"
INST_FARLOW = "institution-farlow-herbarium"
INST_ANSP = "institution-academy-of-natural-sciences-of-drexel-university"
INST_ST_ANDREWS = "institution-university-of-st-andrews-libraries-and-museums"
INST_UCL = "institution-ucl-grant-museum-of-zoology"
INST_WHIPPLE = "institution-whipple-museum-of-the-history-of-science-university-of-cambridge"
INST_MCZ = "institution-harvard-mcz"


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def find_one(root: Path, institution_dir: str, filename: str) -> Path:
    base = root / institution_dir
    matches = list(base.rglob(filename))
    if len(matches) != 1:
        raise FileNotFoundError(f"Expected one {filename} under {base}; found {len(matches)}")
    return matches[0]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def normalise_copenhagen(root: Path) -> list[dict[str, Any]]:
    rows = load_jsonl(find_one(root, INST_COPENHAGEN, "catalogue_rows.jsonl"))
    grouped: OrderedDict[str, dict[str, Any]] = OrderedDict()
    for row in rows:
        cells = row.get("cells") or []
        if len(cells) != 2 or not re.fullmatch(r"C-A-\d+", str(cells[0])):
            continue
        snm_id, species = str(cells[0]), str(cells[1])
        item = grouped.setdefault(
            snm_id,
            {
                "snm_id": snm_id,
                "collection_query": str(row.get("request_label", "")),
                "species_labels": [],
                "institution": "Natural History Museum of Denmark / University of Copenhagen",
                "collection": "Desmid collection",
                "object_type": "microscope slide",
                "evidence_type": "enumerated_public_catalogue_object",
                "source_url": str(row.get("source_url", "")),
                "scope_note": "Physical slide identifier enumerated; one slide may carry multiple species labels.",
            },
        )
        if item["collection_query"] != str(row.get("request_label", "")):
            raise ValueError(f"SNM ID appeared in more than one collection query: {snm_id}")
        if species and species not in item["species_labels"]:
            item["species_labels"].append(species)
    out = list(grouped.values())
    counts = Counter(item["collection_query"] for item in out)
    if len(out) != 510 or counts != Counter({"Hoff collection": 400, "Boergesen collection": 110}):
        raise ValueError(f"Unexpected Copenhagen normalisation result: total={len(out)} counts={dict(counts)}")
    return out


def normalise_cheever(root: Path) -> tuple[list[dict[str, Any]], dict[str, int]]:
    rows = load_jsonl(find_one(root, INST_FARLOW, "catalogue_rows.jsonl"))
    selected: list[dict[str, Any]] = []
    keys: list[tuple[str, str]] = []
    for row in rows:
        cells = [str(x) for x in (row.get("cells") or [])]
        if len(cells) < 2 or not re.fullmatch(r"B\d+", cells[0]):
            continue
        keys.append((cells[0], cells[1]))
        selected.append(
            {
                "box": cells[0],
                "slide_token": cells[1],
                "cells": cells,
                "source_url": str(row.get("source_url", "")),
                "evidence_type": "enumerated_public_table_row",
                "scope_note": "Cheever is mixed-period; this is current indexed-position evidence, not automatic nineteenth-century dating.",
            }
        )
    collisions = Counter(keys)
    for item in selected:
        item["position_collision"] = collisions[(item["box"], item["slide_token"])] > 1
    if len(selected) != 3363 or len(set(keys)) != 3362:
        raise ValueError(
            f"Unexpected Cheever normalisation result: rows={len(selected)} unique_positions={len(set(keys))}"
        )
    if collisions[("B16", "97")] != 2:
        raise ValueError("Expected B16/97 source-table collision was not recovered")
    box_counts = Counter(item["box"] for item in selected)
    return selected, dict(box_counts)


def normalise_st_andrews(root: Path) -> list[dict[str, Any]]:
    rows = load_jsonl(find_one(root, INST_ST_ANDREWS, "catalogue_rows.jsonl"))
    out: list[dict[str, Any]] = []
    for row in rows:
        cells = [str(x) for x in (row.get("cells") or [])]
        if not cells or cells[0] == "ID" or not cells[0].startswith("BPM/"):
            continue
        out.append(
            {
                "institution": "University of St Andrews Libraries and Museums",
                "parent_collection": "Bell-Pettigrew zoology microscope slide collection",
                "catalogue_id": cells[0],
                "title": cells[1] if len(cells) > 1 else "",
                "date_text": cells[2] if len(cells) > 2 else "",
                "source_url": str(row.get("source_url", "")),
                "evidence_type": "collection_hierarchy_row",
                "scope_note": "Hierarchy evidence; source date wording does not by itself date every physical slide.",
            }
        )
    if len(out) != 20:
        raise ValueError(f"Unexpected St Andrews hierarchy row count: {len(out)}")
    return out


def normalise_ansp_review(root: Path) -> list[dict[str, Any]]:
    rows = load_jsonl(find_one(root, INST_ANSP, "catalogue_rows.jsonl"))
    out = [
        {
            "cells": row.get("cells") or [],
            "request_label": str(row.get("request_label", "")),
            "source_url": str(row.get("source_url", "")),
            "review_required": True,
            "review_reason": "Symbiota query label 'pre-1900' is not a reliable date filter; run 4 returned post-1900 rows including 1938 Preston Smith records. Do not promote without object-level date/person review.",
        }
        for row in rows
    ]
    if len(out) != 749:
        raise ValueError(f"Unexpected ANSP review-pool row count: {len(out)}")
    return out


def compact_page_records(root: Path) -> list[dict[str, Any]]:
    specs = [
        (INST_UCL, "UCL Grant Museum of Zoology"),
        (INST_WHIPPLE, "Whipple Museum of the History of Science, University of Cambridge"),
        (INST_MCZ, "Harvard MCZ"),
    ]
    out: list[dict[str, Any]] = []
    for institution_dir, institution_label in specs:
        rows = load_jsonl(find_one(root, institution_dir, "records.jsonl"))
        for row in rows:
            out.append(
                {
                    "institution": institution_label,
                    "title": str(row.get("title", "")),
                    "url": str(row.get("url") or row.get("final_url") or ""),
                    "final_url": str(row.get("final_url", "")),
                    "identifier_candidates": row.get("identifier_candidates", []),
                    "relationship_candidates": row.get("relationship_candidates", []),
                    "quantity_candidates": row.get("quantity_candidates", []),
                    "seed_entry_ids": row.get("seed_entry_ids", []),
                    "sha256": str(row.get("sha256", "")),
                    "evidence_type": "targeted_public_metadata_page",
                    "scope_note": "Relationship/count candidates require source-context review before canonical promotion.",
                }
            )
    if len(out) != 12:
        raise ValueError(f"Unexpected UCL/Whipple/MCZ compact page count: {len(out)}")
    return out


def split_cheever(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    groups = {
        "B01-B10": set(range(1, 11)),
        "B11-B20": set(range(11, 21)),
        "B26-B30": set(range(26, 31)),
        "B31-B40": set(range(31, 41)),
    }
    out: dict[str, list[dict[str, Any]]] = {key: [] for key in groups}
    for row in rows:
        number = int(row["box"][1:])
        for key, allowed in groups.items():
            if number in allowed:
                out[key].append(row)
                break
    if sum(len(v) for v in out.values()) != len(rows):
        raise ValueError("Unexpected Cheever box outside the harvested groups")
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact_root", type=Path, help="Extracted combined artifact root")
    parser.add_argument("--output", type=Path, default=Path("outputs/targeted_deep_4_normalized"))
    args = parser.parse_args()
    root = args.artifact_root
    out = args.output
    out.mkdir(parents=True, exist_ok=True)

    copenhagen = normalise_copenhagen(root)
    cheever, box_counts = normalise_cheever(root)
    st_andrews = normalise_st_andrews(root)
    ansp = normalise_ansp_review(root)
    page_records = compact_page_records(root)

    write_jsonl(out / "copenhagen_desmid_objects.jsonl", copenhagen)
    for label, rows in split_cheever(cheever).items():
        write_jsonl(out / f"farlow_cheever_{label}.jsonl", rows)
    write_jsonl(out / "st_andrews_bell_pettigrew_hierarchy.jsonl", st_andrews)
    write_jsonl(out / "ansp_symbiota_review_pool.jsonl", ansp)
    write_jsonl(out / "ucl_whipple_mcz_targeted_pages.jsonl", page_records)

    partial = {box: count for box, count in sorted(box_counts.items(), key=lambda kv: int(kv[0][1:])) if count != 100}
    manifest = {
        "schema_version": "slide-survey-targeted-deep-normalisation-v1",
        "run_id": RUN_ID,
        "run_number": RUN_NUMBER,
        "workflow_conclusion": "cancelled",
        "combined_artifact": COMBINED_ARTIFACT,
        "combined_artifact_id": COMBINED_ARTIFACT_ID,
        "combined_artifact_sha256": COMBINED_ARTIFACT_SHA256,
        "normalisation_policy": "Evidence enrichment only; do not extend CLOSED_2026-08-09 membership.",
        "datasets": {
            "copenhagen_desmid_objects": {
                "records": len(copenhagen),
                "hoff_unique_ids": sum(1 for x in copenhagen if x["collection_query"] == "Hoff collection"),
                "boergesen_unique_ids": sum(1 for x in copenhagen if x["collection_query"] == "Boergesen collection"),
            },
            "farlow_cheever_position_rows": {
                "source_rows": len(cheever),
                "unique_box_slide_tokens": len({(x["box"], x["slide_token"]) for x in cheever}),
                "position_collision": {"box": "B16", "slide_token": "97", "source_rows": 2},
                "boxes_not_harvested": ["B21", "B22", "B23", "B24", "B25"],
                "partial_or_non_100_row_boxes": partial,
            },
            "st_andrews_bell_pettigrew_hierarchy": {"rows": len(st_andrews)},
            "ansp_symbiota_review_pool": {"rows": len(ansp), "review_only": True},
            "ucl_whipple_mcz_targeted_pages": {"rows": len(page_records)},
        },
        "sorbonne": {
            "disposition": "ignored_partial_run",
            "artifact_id": SORBONNE_ARTIFACT_ID,
            "reason": "Interrupted job; partial raw pages only, no complete normalised records layer.",
        },
        "closure_boundary": {"canonical_discovery_entries": 307, "frozen_strict_19c_entries": 155},
    }
    (out / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"Normalised targeted-deep run 4: Copenhagen={len(copenhagen)}; "
        f"Cheever={len(cheever)} rows; St Andrews={len(st_andrews)}; "
        f"ANSP review={len(ansp)}; compact pages={len(page_records)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
