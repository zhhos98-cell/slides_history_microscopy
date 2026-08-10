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
    assert not duplicate_dois, f"repeated DOI routes must be semantically resolved before export: {duplicate_dois}"
    if duplicate_urls:
        print(f"  NOTE bibliography repeated non-DOI URLs: {len(duplicate_urls)}")
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
    records: list[dict] = []
    allowed_relations = set(manifest["relation_values"])

    for name in chunks:
        assert_path(f"sources/{name}")
        payload = load_json(f"sources/{name}")
        chunk_records = payload.get("records")
        assert isinstance(chunk_records, list), f"source registry chunk {name} has no records list"
        for record in chunk_records:
            ident = (record.get("id") or "").strip()
            assert ident and ident not in seen, f"duplicate/blank source-registry id: {ident!r}"
            seen.add(ident)
            for required in ["collection", "type", "relation", "url"]:
                assert record.get(required), f"blank source-registry {required}: {ident}"
            assert record["relation"] in allowed_relations, f"invalid source relation {record['relation']!r}: {ident}"
            records.append(record)

    counts = manifest["counts"]
    superseded = manifest.get("superseded_ids", {})
    excluded = manifest.get("excluded_ids", {})
    assert len(records) == counts["raw_records_across_chunks"] == 87
    assert len(superseded) == counts["superseded_duplicate_route_ids"] == 3
    assert len(excluded) == counts["excluded_out_of_scope_ids"] == 1
    assert not set(superseded).intersection(excluded), "source ID cannot be both superseded duplicate and excluded"
    for old_id, meta in superseded.items():
        assert old_id in seen, f"superseded source id missing: {old_id}"
        assert meta["canonical_id"] in seen, f"canonical source id missing: {meta['canonical_id']}"
        assert old_id != meta["canonical_id"]
    for excluded_id in excluded:
        assert excluded_id in seen, f"excluded source id missing from raw audit layer: {excluded_id}"

    suppressed = set(superseded) | set(excluded)
    canonical_records = [record for record in records if record["id"] not in suppressed]
    assert len(canonical_records) == counts["canonical_records"] == 83

    record_by_id = {record["id"]: record for record in canonical_records}
    url_to_uses: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for record in canonical_records:
        url_to_uses[record["url"]].append((record["id"], "primary"))
        if record.get("secondary_url"):
            url_to_uses[record["secondary_url"]].append((record["id"], "secondary"))

    duplicate_urls = {url: uses for url, uses in url_to_uses.items() if len({ident for ident, _ in uses}) > 1}
    retained = {item["url"] for item in manifest.get("retained_shared_url_relations", [])}
    assert set(duplicate_urls) == retained, f"unclassified canonical source-registry URL reuse: {set(duplicate_urls) ^ retained}"
    if duplicate_urls:
        print(f"  NOTE canonical source-registry shared URLs: {len(duplicate_urls)}")
        for url, uses in sorted(duplicate_urls.items()):
            labels = " | ".join(f"{ident} [{role}] :: {record_by_id[ident]['collection']}" for ident, role in uses)
            print(f"    URL {url} => {labels}")
    print(f"  checked {len(records)} raw source-registry records / {len(canonical_records)} canonical / {len(superseded)} superseded duplicates / {len(excluded)} excluded")
    assert_path("sources/README.md")


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
    sources_index = (ROOT / "sources/index.html").read_text(encoding="utf-8")
    sources_js = (ROOT / "sources/sources.js").read_text(encoding="utf-8")
    pages = (ROOT / "docs/PAGES.md").read_text(encoding="utf-8")
    version = (ROOT / "pages-version.txt").read_text(encoding="utf-8")

    assert "data/corpus/CORPUS_MANIFEST_V6.json" in index
    assert "data/corpus/CORPUS_MANIFEST_V5.json" not in index
    assert 'href="bibliography/bibliography.csv"' not in index
    assert "../data/corpus/CORPUS_MANIFEST_V6.json" in sources_index
    assert "../data/corpus/CORPUS_MANIFEST_V5.json" not in sources_index
    assert "source-registry-manifest.json" in sources_js
    assert "const sourceFiles=['source-registry.json','source-registry-02.json','source-registry-03.json']" not in sources_js
    assert "superseded_ids" in sources_js and "excluded_ids" in sources_js
    assert "CORPUS_MANIFEST_V6.json" in pages
    assert "research-outputs: 41" in version
    assert "source-registry: 83 canonical / 87 raw / 3 superseded duplicate routes / 1 excluded out-of-scope" in version
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
