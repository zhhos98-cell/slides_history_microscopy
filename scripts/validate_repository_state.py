#!/usr/bin/env python3
"""Validate cross-layer repository authority and current publication state.

This validator is intentionally structural. It does not re-research historical
claims and it does not rebuild the frozen survey. It checks that the repository's
current manifests agree about authority, counts, queues and published files.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(rel: str):
    path = ROOT / rel
    if not path.exists():
        raise AssertionError(f"missing required file: {rel}")
    return json.loads(path.read_text(encoding="utf-8"))


def assert_path(rel: str) -> None:
    if not (ROOT / rel).exists():
        raise AssertionError(f"manifest pointer does not exist: {rel}")


def validate_repository_manifest() -> None:
    repo = load_json("REPOSITORY_STATE.json")
    assert repo["status"] == "CANONICAL_REPOSITORY_STATE"
    for layer in repo["layers"].values():
        assert_path(layer["authority"])
    assert len(repo["current_exact_source_requests"]) == 4


def validate_survey() -> None:
    closure = load_json("data/survey/07AR_CLOSURE_MANIFEST_2026-08-09.json")
    counts = closure["final_counts"]
    assert counts["canonical_discovery_entries"] == 307
    assert counts["canonical_strict_19c_entries"] == 155
    assert counts["rows_added_in_07AR"] == 0


def validate_bibliography() -> None:
    manifest = load_json("bibliography/bibliography-manifest.json")
    assert manifest["total_entries"] == 206
    assert manifest["research"] + manifest["primary"] == manifest["total_entries"]
    assert len(manifest["chunks"]) == 22
    seen: set[str] = set()
    row_count = 0
    research = 0
    primary = 0
    for name in manifest["chunks"]:
        path = ROOT / "bibliography" / name
        assert path.exists(), f"missing bibliography chunk: {name}"
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                row_count += 1
                ident = row.get("id", "")
                assert ident and ident not in seen, f"duplicate/blank bibliography id: {ident!r}"
                seen.add(ident)
                section = (row.get("section") or "").strip().lower()
                if section == "research":
                    research += 1
                elif section in {"primary", "primary/object", "primary_object"}:
                    primary += 1
    assert row_count == 206, f"bibliography row count {row_count} != 206"
    # Section spellings are historically heterogeneous; manifest arithmetic is authoritative.
    assert manifest["research"] == 88 and manifest["primary"] == 118
    legacy = manifest.get("legacy_files", {})
    assert "bibliography.csv" in legacy, "legacy static bibliography.csv must be explicitly quarantined"


def validate_analysis() -> None:
    state = load_json("data/analysis/CURRENT_STATE.json")
    assert state["frozen_survey"]["discovery_nodes"] == 307
    assert state["frozen_survey"]["strict_nineteenth_century_nodes"] == 155
    assert state["bibliography"]["total_entries"] == 206
    assert state["public_web_discovery_queue"] == []
    queue = state["exact_source_request_queue"]
    assert len(queue) == 4
    assert not any("Naples" in item["target"] for item in queue)
    for rel in state["current_authority_files"].values():
        assert_path(rel)

    slide155 = load_json("data/analysis/slide_155_analysis_v1/manifest.json")
    assert slide155["frozen_membership_rows"] == 155
    assert slide155["committed_row_output"] is None
    assert slide155["generated_row_output"] == "outputs/SLIDE_155_ANALYSIS_LAYER_V1.csv"

    targets = ROOT / "data/analysis/slide_155_corpus_expansion_v1/OPEN_PRIMARY_SOURCE_TARGETS_V1.csv"
    with targets.open(newline="", encoding="utf-8") as handle:
        statuses = {row["status"] for row in csv.DictReader(handle)}
    forbidden = {"OPEN", "LOCATED_VOLUME_TEXT_PENDING", "LOCATED_TRANSCRIPTION_SCAN_PENDING"}
    assert not statuses.intersection(forbidden), f"legacy corpus-expansion queue still looks active: {statuses & forbidden}"


def validate_source_registry() -> None:
    manifest = load_json("sources/source-registry-manifest.json")
    chunks = manifest.get("chunks") or manifest.get("files") or manifest.get("parts")
    if isinstance(chunks, list):
        names = []
        for item in chunks:
            if isinstance(item, str):
                names.append(item)
            elif isinstance(item, dict):
                names.append(item.get("file") or item.get("path") or item.get("name"))
        for name in filter(None, names):
            assert_path(f"sources/{name}")
    assert_path("sources/README.md")


def validate_corpus_publication() -> None:
    manifest = load_json("data/corpus/CORPUS_MANIFEST_V6.json")
    outputs_name = manifest["files"]["research_outputs"]
    assert outputs_name == "RESEARCH_OUTPUTS_V6.json"
    outputs = load_json(f"data/corpus/{outputs_name}")
    assert outputs["output_count"] == len(outputs["outputs"])
    assert manifest["counts"]["research_outputs"] == outputs["output_count"]
    for item in outputs["outputs"]:
        assert_path(item["path"])
    for name in manifest["files"]["core_document_chunks"]:
        assert_path(f"data/corpus/{name}")
    for name in manifest["files"]["extension_document_chunks"]:
        assert_path(f"data/corpus/{name}")
    for key in ["bna_meta", "bna_query_yield", "bna_year_yield", "bna_derived_index"]:
        assert_path(f"data/corpus/{manifest['files'][key]}")


def main() -> int:
    checks = [
        validate_repository_manifest,
        validate_survey,
        validate_bibliography,
        validate_analysis,
        validate_source_registry,
        validate_corpus_publication,
    ]
    for check in checks:
        check()
        print(f"OK {check.__name__}")
    print("Repository state validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
