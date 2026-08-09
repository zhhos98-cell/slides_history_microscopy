# Data layout

This repository keeps four evidence layers separate. They are related, but they have different authority and should not be merged into one table.

## `survey/` — frozen surviving-object survey

Canonical home of the global microscope-slide collection survey and its closure metadata.

- Frozen discovery layer: 307 canonical nodes.
- Frozen strict nineteenth-century layer: 155 nodes.
- Strict membership is reconstructed from batches `07K`–`07AQ` plus the `07AR` closure files.
- `07AR` adds no discovery rows.
- The survey is `CLOSED_2026-08-09`; new discoveries require a new explicit version rather than silent extension.

The modular CSV batches remain because they are the evidentiary/audit trail from which the closure is executable. They are not redundant exports.

## `analysis/` — derived research layers

Interpretive and routing outputs built over the frozen survey. These files may classify, crosswalk, prioritise or contextualise frozen nodes, but they do not rewrite source wording or membership.

Current modules include:

- `slide_155_analysis_v1/` — derived classifications over the frozen 155;
- `slide_155_corpus_expansion_v1/` — object-to-text routing, verified bridges, source targets, Naples catalogue parsing and circulation crosswalks.

## `evidence/` — normalised harvest evidence

Retained structured evidence from bounded harvesting. The current `targeted_deep_4/` layer records the final normalised harvest artifact and manual residuals. It is enrichment evidence, not a second census.

## `corpus/` — compact microscopy text/newspaper index

Site-facing metadata and results derived from seven canonical microscopy masters. This layer publishes document-level registry entries and compact BNA derived tables while leaving large OCR/full-text/article payloads in the source masters.

`corpus/CORPUS_MANIFEST_V5.json` is the current publication manifest. It fingerprints the seven canonical masters and defines what is present versus deliberately omitted.

## Authority order

When two layers appear to conflict, use this order:

1. original/canonical source master for source text and raw record payloads;
2. frozen survey source row plus `07AR` closure contract for object-census membership;
3. versioned evidence/analysis file for derived historical relations or classifications;
4. `corpus/` compact registry and GitHub Pages as navigation/presentation layers.

A Pages card, compact registry row or analytical label never silently overrides the source layer beneath it.

## Quantity discipline

Do not combine slide counts, preparation counts, specimen counts, catalogue offerings, serial positions, cabinet capacities, database rows, images or mixed-period aggregates unless a source explicitly establishes that they share a quantity namespace.

## Regeneration rule

Generated runtime directories (`outputs/`, `data/normalized/`, local artifacts and caches) are ignored by Git. A durable result enters the repository only when it has been reviewed and placed into a versioned survey, evidence, analysis or corpus layer.
