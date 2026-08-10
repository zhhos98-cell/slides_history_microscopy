# Microscopy corpus publication layer

Compact repository/Pages export derived from seven canonical microscopy masters. This directory is a navigation/results layer, not a replacement for the source masters, the frozen surviving-object survey, or the current analysis authority.

## Current manifest

`CORPUS_MANIFEST_V6.json` is the current publication contract. It preserves the V5 corpus/BNA counts and source-master fingerprints while refreshing the public research-output index to the 2026-08-10 repository state.

Current published counts are:

- 142 core document/bibliographic entries;
- 60 extension document entries;
- 2 structured-OCR source entries;
- 43 BNA query-yield rows;
- 71 BNA year-yield rows;
- 930 compact BNA event clusters;
- 995 compact newspaper-yield rows;
- 41 curated current/foundational research outputs.

The seven canonical source-master byte sizes and SHA-256 fingerprints are unchanged from V5.

## Published compact files

### Publication registry

- `CORE_DOCUMENTS_V4_01.json` … `CORE_DOCUMENTS_V4_07.json` — all 142 core document-level entries.
- `EXTENDED_DOCUMENTS_V4_01.json` … `EXTENDED_DOCUMENTS_V4_04.json` — all 60 extension entries plus 2 structured-OCR sources.

The V4 filenames are deliberately retained because those registry chunks did not change when later manifest/BNA publication contracts advanced. Suffix differences preserve derivation history rather than indicating competing current datasets.

### BNA compact layers

- `BNA_META_V4.json` — source-master counts and omission ledger.
- `BNA_QUERY_YIELD_V4.json` — all 43 query-yield rows.
- `BNA_YEAR_YIELD_V4.json` — all 71 year-yield rows.
- `BNA_DERIVED_INDEX_V5.json` — file map for the full compact derived tables.
- `BNA_EVENT_CLUSTERS_COMPACT_V5_01.json` … `_05.json` — all 930 event clusters.
- `BNA_NEWSPAPER_YIELD_COMPACT_V5_01.json` … `_05.json` — all 995 newspaper-yield rows.

### Research outputs

`RESEARCH_OUTPUTS_V6.json` is the current curated research-output index. It includes top-level/current-state manifests, frozen-survey closure files, object↔text work, Cole/material-publication analysis, Balfour, Challenger, Elcock, Naples, trade/addressing infrastructure, reverse-index bridges, harvest evidence, bibliography/source manifests and site architecture.

`RESEARCH_OUTPUTS_V4.json` is the 2026-08-09 22-output predecessor snapshot and remains for provenance. A transient 2026-08-10 draft between V4 and V6 was removed during repository cleanup because it was never an authoritative publication state.

## Deliberately omitted bulk

The following remain only in the canonical masters:

- 49,277 core page-text records / 50,744 occurrences;
- 73,073,904 extension full-text characters;
- structured-OCR page arrays;
- 9,365 article-level BNA record payloads and raw OCR.

This is a duplication rule, not a loss rule. The manifest fingerprints the source masters so the compact publication layer remains traceable to the bulky canonical data.

## Authority order

For source text and raw record payloads, use the canonical masters. For frozen object membership, use `data/survey/07AR_CLOSURE_MANIFEST_2026-08-09.json`. For current derived research status, use `data/analysis/CURRENT_STATE.json`. `CORPUS_MANIFEST_V6.json` and the compact files here are publication/navigation derivatives.

The frozen 155 object catalogue is therefore separate from this corpus publication layer; no compact-corpus row changes frozen membership.

## Validation and predecessors

`PUBLICATION_CHECK_V5_2026-08-09.json` remains the last count check for the unchanged core/extension/BNA compact payload. `CORPUS_MANIFEST_V4.json` and `CORPUS_MANIFEST_V5.json` remain dated predecessors. Repository-level structural consistency is checked by `scripts/validate_repository_state.py`.
