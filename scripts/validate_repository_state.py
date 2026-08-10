#!/usr/bin/env python3
"""Validate cross-layer repository authority and current publication state.

This validator is intentionally structural and row-level. It does not re-research
historical claims and it does not rebuild the frozen survey. It checks that the
repository's current manifests agree about authority, counts, queues and published
files; that current bibliography/source IDs remain unique; and that committed JSON
files are syntactically valid.
"""

from __future__ import annotations

import csv
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r"https?://[^\s;]+", re.I)
DOI_RE = re.compile(r"https?://(?:dx\.)?doi\.org/([^\s;]+)", re.I)


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
        for rel in layer.get("related_files", []):
            assert_path(rel)
    assert len(repo["current_exact_source_requests"]) == 4
    assert repo["layers"]["survey"]["discovery_nodes"] == 307
    assert repo["layers"]["survey"]["strict_nineteenth_century_nodes"] == 155
    assert repo["layers"]["bibliography"]["total_entries"] == 206


def validate_all_json_syntax() -> None:
    failures: list[str] = []
    count = 0
    for path in ROOT.rglob("*.json"):
        if ".git" in path.parts:
            continue
        count += 1
        try:
            json.loads(path.read_text(encoding="utf-8-sig"))
        except Exception as exc:  # pragma: no cover - diagnostic message matters
            failures.append(f"{path.relative_to(ROOT)}: {exc}")
    assert not failures, "invalid JSON files:\n" + "\n".join(failures)
    print(f"  parsed {count} committed JSON files")


def validate_survey() -> None:
    closure = load_json("data/survey/07AR_CLOSURE_MANIFEST_2026-08-09.json")
    counts = closure["final_counts"]
    assert counts["canonical_discovery_entries"] == 307
    assert counts["canonical_strict_19c_entries"] == 155
    assert counts["rows_added_in_07AR"] == 0
    assert counts["raw_modular_ledger_rows_pre_closure"] == 328
    assert counts["superseded_distinct_alias_rows"] == 20


def validate_bibliography() -> None:
    manifest = load_json("bibliography/bibliography-manifest.json")
    assert manifest["total_entries"] == 206
    assert manifest["research"] + manifest["primary"] == manifest["total_entries"]
    assert manifest["research"] == 88 and manifest["primary"] == 118
    assert len(manifest["chunks"]) == 22

    expected_fields = manifest["schema_fields"]
    seen: set[str] = set()
    rows: list[dict[str, str]] = []
    row_by_id: dict[str, dict[str, str]] = {}
    url_to_ids: dict[str, list[str]] = defaultdict(list)
    doi_to_ids: dict[str, list[str]] = defaultdict(list)

    for name in manifest["chunks"]:
        path = ROOT / "bibliography" / name
        assert path.exists(), f"missing bibliography chunk: {name}"
        with path.open(newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            assert reader.fieldnames == expected_fields, f"bibliography schema drift in {name}: {reader.fieldnames}"
            for row in reader:
                ident = (row.get("id") or "").strip()
                assert ident and ident not in seen, f"duplicate/blank bibliography id: {ident!r}"
                seen.add(ident)
                row_by_id[ident] = row
                for required in ["year", "section", "title", "citation", "verification"]:
                    assert (row.get(required) or "").strip(), f"blank bibliography {required}: {ident}"
                section = (row.get("section") or "").strip().lower()
                assert section in {"research", "primary", "primary/object", "primary_object"}, f"unexpected bibliography section {section!r}: {ident}"
                links = row.get("links") or ""
                for url in URL_RE.findall(links):
                    url_to_ids[url.rstrip(".,)")].append(ident)
                for doi in DOI_RE.findall(links):
                    doi_to_ids[doi.rstrip(".,)").lower()].append(ident)
                rows.append(row)

    assert len(rows) == 206, f"bibliography row count {len(rows)} != 206"
    research = sum((r.get("section") or "").strip().lower() == "research" for r in rows)
    primary = len(rows) - research
    assert research == 88, f"bibliography research rows {research} != 88"
    assert primary == 118, f"bibliography primary rows {primary} != 118"

    legacy = manifest.get("legacy_files", {})
    assert "bibliography.csv" in legacy, "legacy static bibliography.csv must be explicitly quarantined"
    assert_path("bibliography/README.md")

    duplicate_dois = {doi: sorted(set(ids)) for doi, ids in doi_to_ids.items() if len(set(ids)) > 1}
    duplicate_urls = {url: sorted(set(ids)) for url, ids in url_to_ids.items() if len(set(ids)) > 1}
    if duplicate_dois:
        print(f"  NOTE bibliography repeated DOI routes: {len(duplicate_dois)}")
        for doi, ids in sorted(duplicate_dois.items()):
            labels = " | ".join(f"{ident} :: {row_by_id[ident]['title']}" for ident in ids)
            print(f"    DOI {doi} => {labels}")
    if duplicate_urls:
        print(f"  NOTE bibliography repeated URLs: {len(duplicate_urls)}")
        for url, ids in sorted(duplicate_urls.items()):
            labels = " | ".join(f"{ident} :: {row_by_id[ident]['title']}" for ident in ids)
            print(f"    URL {url} => {labels}")


def validate_analysis() -> None:
    state = load_json("data/analysis/CURRENT_STATE.json")
    assert state["repository_authority"] == "REPOSITORY_STATE.json"
    assert state["frozen_survey"]["discovery_nodes"] == 307
    assert state["frozen_survey"]["strict_nineteenth_century_nodes"] == 155
    assert state["bibliography"]["total_entries"] == 206
    assert state["public_web_discovery_queue"] == []
    queue = state["exact_source_request_queue"]
    assert len(queue) == 4
    assert [item["rank"] for item in queue] == [1, 2, 3, 4]
    assert not any("Naples" in item["target"] for item in queue)
    for rel in state["current_authority_files"].values():
        assert_path(rel)

    slide155 = load_json("data/analysis/slide_155_analysis_v1/manifest.json")
    assert slide155["frozen_membership_rows"] == 155
    assert slide155["committed_row_output"] is None
    assert slide155["generated_row_output"] == "outputs/SLIDE_155_ANALYSIS_LAYER_V1.csv"

    targets = ROOT / "data/analysis/slide_155_corpus_expansion_v1/OPEN_PRIMARY_SOURCE_TARGETS_V1.csv"
    with targets.open(newline="", encoding="utf-8-sig") as handle:
        target_rows = list(csv.DictReader(handle))
    statuses = {row["status"] for row in target_rows}
    forbidden = {"OPEN", "LOCATED_VOLUME_TEXT_PENDING", "LOCATED_TRANSCRIPTION_SCAN_PENDING"}
    assert not statuses.intersection(forbidden), f"legacy corpus-expansion queue still looks active: {statuses & forbidden}"
    assert any(row["object_entry_id"] == "UK-STANDREWS-NAPOLI-FRITZ-MEYER-SLIDES-1881" and row["status"].startswith("CLOSED") for row in target_rows)

    naples = load_json("data/analysis/naples_row383_object_catalogue_closure_v4.json")
    assert naples["status"] == "CATALOGUE_OFFERING_IDENTITY_CLOSED__INDIVIDUAL_COPY_HISTORY_OPEN"
    assert "Penis" in " ".join(naples["decisive_source"]["verbatim_sequence"])
    assert naples["surviving_object"]["right_label_public_transcription"] == "Panis 383"


def validate_source_registry() -> None:
    manifest = load_json("sources/source-registry-manifest.json")
    chunks = manifest["chunks"]
    seen: set[str] = set()
    record_by_id: dict[str, dict] = {}
    url_to_ids: dict[str, list[str]] = defaultdict(list)
    record_count = 0
    allowed_relations = set(manifest["relation_values"])

    for name in chunks:
        assert_path(f"sources/{name}")
        payload = load_json(f"sources/{name}")
        records = payload.get("records")
        assert isinstance(records, list), f"source registry chunk {name} has no records list"
        for record in records:
            record_count += 1
            ident = (record.get("id") or "").strip()
            assert ident and ident not in seen, f"duplicate/blank source-registry id: {ident!r}"
            seen.add(ident)
            record_by_id[ident] = record
            for required in ["collection", "type", "relation", "url"]:
                assert record.get(required), f"blank source-registry {required}: {ident}"
            assert record["relation"] in allowed_relations, f"invalid source relation {record['relation']!r}: {ident}"
            url_to_ids[record["url"]].append(ident)
            if record.get("secondary_url"):
                url_to_ids[record["secondary_url"]].append(ident)

    assert record_count > 0
    assert_path("sources/README.md")
    duplicate_urls = {url: sorted(set(ids)) for url, ids in url_to_ids.items() if len(set(ids)) > 1}
    if duplicate_urls:
        print(f"  NOTE source-registry repeated URLs: {len(duplicate_urls)}")
        for url, ids in sorted(duplicate_urls.items()):
            labels = " | ".join(f"{ident} :: {record_by_id[ident]['collection']}" for ident in ids)
            print(f"    URL {url} => {labels}")
    print(f"  checked {record_count} source-registry records")


def validate_corpus_publication() -> None:
    manifest = load_json("data/corpus/CORPUS_MANIFEST_V6.json")
    outputs_name = manifest["files"]["research_outputs"]
    assert outputs_name == "RESEARCH_OUTPUTS_V6.json"
    outputs = load_json(f"data/corpus/{outputs_name}")
    assert outputs["output_count"] == len(outputs["outputs"])
    assert manifest["counts"]["research_outputs"] == outputs["output_count"] == 41
    paths = [item["path"] for item in outputs["outputs"]]
    assert len(paths) == len(set(paths)), "duplicate path in RESEARCH_OUTPUTS_V6"
    for rel in paths:
        assert_path(rel)
    for name in manifest["files"]["core_document_chunks"]:
        assert_path(f"data/corpus/{name}")
    for name in manifest["files"]["extension_document_chunks"]:
        assert_path(f"data/corpus/{name}")
    for key in ["bna_meta", "bna_query_yield", "bna_year_yield", "bna_derived_index"]:
        assert_path(f"data/corpus/{manifest['files'][key]}")
    assert not (ROOT / "data/corpus/RESEARCH_OUTPUTS_V5.json").exists(), "transient RESEARCH_OUTPUTS_V5 draft should remain removed"


def validate_current_presentation_links() -> None:
    index = (ROOT / "index.html").read_text(encoding="utf-8")
    sources = (ROOT / "sources/index.html").read_text(encoding="utf-8")
    pages = (ROOT / "docs/PAGES.md").read_text(encoding="utf-8")
    version = (ROOT / "pages-version.txt").read_text(encoding="utf-8")

    assert "data/corpus/CORPUS_MANIFEST_V6.json" in index
    assert "data/corpus/CORPUS_MANIFEST_V5.json" not in index
    assert 'href="bibliography/bibliography.csv"' not in index
    assert "../data/corpus/CORPUS_MANIFEST_V6.json" in sources
    assert "../data/corpus/CORPUS_MANIFEST_V5.json" not in sources
    assert "CORPUS_MANIFEST_V6.json" in pages
    assert "research-outputs: 41" in version
    assert "corpus-manifest: data/corpus/CORPUS_MANIFEST_V6.json" in version


def main() -> int:
    checks = [
        validate_repository_manifest,
        validate_all_json_syntax,
        validate_survey,
        validate_bibliography,
        validate_analysis,
        validate_source_registry,
        validate_corpus_publication,
        validate_current_presentation_links,
    ]
    for check in checks:
        check()
        print(f"OK {check.__name__}")
    print("Repository state validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
