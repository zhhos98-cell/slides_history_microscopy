# Data layout

The repository keeps source/frozen data, derived analysis, bounded harvest evidence and compact publication data separate. They are related, but they have different authority and should not be merged into one table.

At repository level, consult `../REPOSITORY_STATE.json` first. It maps the current authority file for every layer.

## `survey/` — frozen surviving-object survey

Canonical home of the global microscope-slide collection survey and its closure metadata.

- Frozen discovery layer: 307 canonical nodes.
- Frozen strict nineteenth-century layer: 155 nodes.
- Strict membership is reconstructed from batches `07K`–`07AQ` plus the `07AR` closure files.
- `07AR` adds no discovery rows.
- The survey is `CLOSED_2026-08-09`; new discoveries require a new explicit version rather than silent extension.

The modular CSV batches remain because they are the evidentiary/audit trail from which the closure is executable. They are not redundant exports and should not be destructively deduplicated in place.

## `analysis/` — derived research layers

Interpretive and routing outputs built over the frozen survey. These files may classify, crosswalk, prioritise or contextualise frozen nodes, but they do not rewrite source wording or membership.

`analysis/CURRENT_STATE.json` is the canonical pointer for the present analytical state. Because the repository deliberately preserves dated/versioned research snapshots, consult this manifest before treating a dated analysis file as current.

Current modules include:

- `slide_155_analysis_v1/` — derived classification schema over the frozen 155; its `manifest.json` records that the row-level CSV is generated/reproducible but not committed as canonical data;
- `slide_155_corpus_expansion_v1/` — object-to-text bridges, historical routing data, Naples catalogue/circulation crosswalks and current target dispositions;
- target-specific closure files for Cole, Challenger, Balfour, Elcock and Naples;
- `global_archive_research_priority_CURRENT.json` — current operational router.

Current operational state: public-web discovery queue = **0**; exact-source request queue = **4**. Historical versioned files remain for audit and may contain superseded intermediate conclusions.

## `evidence/` — normalised harvest evidence

Retained structured evidence from bounded harvesting. `targeted_deep_4/manifest.json` is the current retained evidence manifest. This layer enriches frozen nodes and cannot reopen census membership.

## `corpus/` — compact microscopy text/newspaper publication layer

Site-facing metadata and results derived from seven canonical microscopy masters. It publishes document-level registry entries and compact BNA derived tables while leaving large OCR/full-text/article payloads in the source masters.

`corpus/CORPUS_MANIFEST_V6.json` is the current publication manifest. It preserves the V5 core/extension/BNA payload counts and source-master fingerprints, while `RESEARCH_OUTPUTS_V6.json` refreshes the public research-output index to 41 current/foundational outputs.

V4/V5 corpus manifests and older research-output indexes remain dated predecessor snapshots.

## Authority order

When two layers appear to conflict, use this order:

1. original/canonical source master for source text and raw record payloads;
2. frozen survey source row plus `07AR` closure contract for object-census membership;
3. `analysis/CURRENT_STATE.json` to identify the current derived authority;
4. the target-specific current analysis/evidence file named there;
5. older versioned analytical snapshots for audit/history only;
6. `corpus/` compact registry and GitHub Pages as navigation/presentation layers.

A Pages card, compact registry row, old routing snapshot or analytical label never silently overrides the source layer beneath it.

## Quantity discipline

Do not combine slide counts, preparation counts, specimen counts, catalogue offerings, serial positions, cabinet capacities, database rows, images or mixed-period aggregates unless a source explicitly establishes that they share a quantity namespace.

Important current examples:

- 307 discovery nodes ≠ 155 strict nineteenth-century nodes;
- 206 bibliography records ≠ physical objects;
- 423 Naples catalogue offerings ≠ surviving slides;
- 4,723 Challenger dataset rows ≠ 4,713 physical containers/objects.

## Regeneration rule

Generated runtime directories (`outputs/`, `data/normalized/`, local artifacts and caches) are ignored by Git. A durable result enters the repository only when it has been reviewed and placed into a versioned survey, evidence, analysis or corpus layer.

## Cleanup rule

Do not delete versioned analytical files simply because a later pass supersedes them. They document negative checks, decision states and the path by which a relation was closed. Cleaning means making authority and supersession explicit, removing stale routing from current manifests, and preserving quantity namespaces rather than erasing the audit trail.

Repository-wide structural consistency is checked by `../scripts/validate_repository_state.py`.
