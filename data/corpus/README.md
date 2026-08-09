# Microscopy corpus publication layer

Compact repository/Pages export derived from seven canonical microscopy masters. This directory is a navigation and results layer, not a replacement for the source masters or the frozen surviving-object survey.

## Current manifest

`CORPUS_MANIFEST_V5.json` is the current publication contract. It records:

- 142 core document/bibliographic entries;
- 60 extension document entries;
- 2 structured-OCR source entries;
- 43 BNA query-yield rows;
- 71 BNA year-yield rows;
- 930 compact BNA event clusters;
- 995 compact newspaper-yield rows;
- 22 indexed research outputs.

The manifest also records byte sizes and SHA-256 fingerprints for all seven canonical source masters.

## Published compact files

### Publication registry

- `CORE_DOCUMENTS_V4_01.json` … `CORE_DOCUMENTS_V4_07.json` — all 142 core document-level entries.
- `EXTENDED_DOCUMENTS_V4_01.json` … `EXTENDED_DOCUMENTS_V4_04.json` — all 60 extension entries plus 2 structured-OCR sources.

The `V4` filenames are retained deliberately: those registry chunks were unchanged when the publication contract advanced to V5. V5 composes the unchanged V4 registries with the later complete BNA-derived export; the mixed suffixes therefore preserve derivation history rather than indicating two competing current datasets.

### BNA compact layers

- `BNA_META_V4.json` — source-master counts and omission ledger.
- `BNA_QUERY_YIELD_V4.json` — all 43 query-yield rows.
- `BNA_YEAR_YIELD_V4.json` — all 71 year-yield rows.
- `BNA_DERIVED_INDEX_V5.json` — file map for the full derived tables.
- `BNA_EVENT_CLUSTERS_COMPACT_V5_01.json` … `_05.json` — all 930 event clusters.
- `BNA_NEWSPAPER_YIELD_COMPACT_V5_01.json` … `_05.json` — all 995 newspaper-yield rows.

Event-cluster rows preserve cluster ID, type, record count, representative BNA record ID and exceptional clustering basis. Repeated standard clustering/review prose is stored once per chunk rather than copied into every row. Newspaper-yield rows preserve newspaper title plus A/B/C/X grade counts.

### Research outputs

`RESEARCH_OUTPUTS_V4.json` indexes the current closure/audit files, 155-derived analysis, object-to-text bridges, source targets, Naples catalogue/circulation work, harvesting evidence and research logs. As with the registry chunks, the V4 filename is retained because the ledger itself did not change when the BNA-derived publication layer advanced to V5.

## Deliberately omitted bulk

The following remain only in the canonical masters:

- 49,277 core page-text records / 50,744 occurrences;
- 73,073,904 extension full-text characters;
- structured-OCR page arrays;
- 9,365 article-level BNA record payloads and raw OCR.

This is a duplication rule, not a loss rule: the V5 manifest fingerprints the source masters so the compact layer remains traceable to the bulky canonical data.

## Schema notes

Core and extension registries preserve source-level identifiers and document/bibliographic metadata needed for navigation. They do not reconstruct omitted page/article/full-text payloads. BNA query/year report values remain strings when that is how the canonical report tables export them; downstream consumers may cast numeric cells for aggregation.

The frozen 155 object catalogue is a separate evidence layer with its own closure contract. No compact-corpus row changes frozen object membership.

## Validation

`PUBLICATION_CHECK_V5_2026-08-09.json` records the current compact-publication counts. `CORPUS_MANIFEST_V4.json` is retained as a dated predecessor manifest for provenance; V5 is current.
