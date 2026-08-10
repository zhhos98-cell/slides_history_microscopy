# Repository organization audit — 2026-08-10

Status: **WHOLE-REPOSITORY AUTHORITY NORMALIZED / NON-DESTRUCTIVE CLEANUP**

This pass reviews the repository as a system rather than only the analysis folder. The aim is to make every layer legible as one of: canonical source/frozen data, current derived authority, compact publication layer, generated runtime artifact, or historical/audit snapshot. The cleanup deliberately avoids deleting modular survey batches, dated research states or bounded negative checks.

## 1. Top-level authority

Added `REPOSITORY_STATE.json` as the repository-wide authority map. It points to:

- frozen survey authority: `data/survey/07AR_CLOSURE_MANIFEST_2026-08-09.json`;
- bibliography authority: `bibliography/bibliography-manifest.json`;
- analysis authority: `data/analysis/CURRENT_STATE.json`;
- corpus publication authority: `data/corpus/CORPUS_MANIFEST_V6.json`;
- source-registry authority: `sources/source-registry-manifest.json`;
- retained bounded-harvest evidence: `data/evidence/targeted_deep_4/manifest.json`.

This separates research authority from filename recency. Older `v1/v2/v3/...` files can remain in place without competing with the current state.

## 2. Frozen survey left intact

No survey batch was deleted, re-deduplicated or rewritten. The existing `07AR` closure remains authoritative:

- 307 canonical discovery nodes;
- 155 strict nineteenth-century nodes;
- 20 superseded distinct-ID aliases;
- one repeated Hubrecht `entry_id` occurrence collapsed by runtime de-duplication;
- no rows added by 07AR.

The modular `07A`–`07AQ` CSVs, adapter expansions and harvest-family expansions remain as provenance/audit infrastructure. `scripts/prepare_survey_inputs.py` continues to build runtime merged inputs without committing those generated merges back into the repository.

## 3. Bibliography authority clarified

The live bibliography remains pass 19:

- 206 records;
- 88 research/collection/conservation;
- 118 primary/object;
- 19 publication languages;
- 22 authoritative row chunks.

Added `bibliography/README.md` and expanded `bibliography-manifest.json` with an explicit authority note. The old static `bibliography/bibliography.csv` is now classified as a **legacy partial index**. It remains for compatibility/audit history but is not the 206-row bibliography and must not be used for current totals or complete exports. The public bibliography page already loads the manifest/chunks and generates full portable exports dynamically.

## 4. Source registry documented

Added `sources/README.md`. `source-registry-manifest.json` remains the additive authority across `source-registry.json` and chunks 02–12. The documentation now makes explicit that source-registry records are research routes, not frozen object-census rows and not automatically nineteenth-century corpus text.

## 5. Derived 155 analysis ambiguity removed

`data/analysis/slide_155_analysis_v1/` previously contained only a README even though the build script generates a 155-row CSV under `outputs/`. Added `manifest.json` stating explicitly:

- expected frozen membership = 155;
- generator = `scripts/build_slide_analysis_layer.py`;
- generated output = `outputs/SLIDE_155_ANALYSIS_LAYER_V1.csv`;
- no canonical row-level derived CSV is currently committed.

This prevents a reader from assuming that a missing file was accidentally lost or that README prose itself is the data layer.

## 6. Object→text expansion queue normalized

`data/analysis/slide_155_corpus_expansion_v1/README.md` had become misleading because it mixed the original v1 routing state with later closure results. It has been rewritten to distinguish:

- historical v1 routing counts and methods;
- current closures;
- optional residual source work;
- the four exact-source requests that now live in the central router.

`OPEN_PRIMARY_SOURCE_TARGETS_V1.csv` is retained as a historical target table but its dispositions now reflect current status:

- H. L. Smith Century III: optional reception chronology;
- Collins p.109 primary scan: optional;
- Naples catalogue/object relations: closed at their supported levels;
- Kitton III–IV prospectus: optional chronology;
- UCL institutional records: parked, not active.

The Naples wording now distinguishes two separate claims: the June 1880 RMS shipment remains unconnected to any specific surviving museum copy, while catalogue offering 383 is independently closed to St Andrews `BPM/1/T8/6` at catalogue-offering identity level.

## 7. Compact corpus publication layer advanced to V6

`CORPUS_MANIFEST_V5.json` correctly published the document/BNA compact layer but its research-output ledger remained a 2026-08-09 22-output snapshot. The corpus payload itself did not need rebuilding.

Added:

- `data/corpus/RESEARCH_OUTPUTS_V6.json` — 41 curated current/foundational outputs;
- `data/corpus/CORPUS_MANIFEST_V6.json` — current compact publication contract.

V6 preserves the V5 core/extension/BNA counts and all seven source-master byte sizes/SHA-256 fingerprints. The change is limited to the research-output publication index. `RESEARCH_OUTPUTS_V4.json` remains the 22-output predecessor. `RESEARCH_OUTPUTS_V5.json` is a transient draft superseded by V6. `data/corpus/README.md` now states this authority chain explicitly.

## 8. Research-state invariants preserved

The cleanup keeps the major count namespaces separate:

- 307 discovery nodes ≠ 155 strict nineteenth-century nodes;
- 206 bibliography records ≠ physical objects;
- 423 Naples catalogue offerings ≠ surviving-slide total;
- 4,723 Challenger dataset records ≠ 4,713 physical containers/objects;
- serial positions, catalogue numbers, accession numbers, cabinet capacities, preparation counts and slide counts remain distinct.

Current public-web discovery queue remains zero. Current exact-source request queue remains four: Elcock manuscript images/transcription, NHM Challenger binary, ZEISS/Balfour accessory evidence, and St Andrews Norman item/export data.

## 9. Repository-wide validation added

Added `scripts/validate_repository_state.py` and `.github/workflows/repository_integrity.yml`. The validator checks:

- top-level authority pointers exist;
- frozen 307/155 closure counts;
- bibliography manifest arithmetic and all 22 chunk files;
- analysis queue = 0 public-web / 4 exact-source requests;
- Naples is absent from the request queue;
- the derived 155 analysis manifest explicitly records its noncommitted generated row artifact;
- legacy corpus-expansion targets are no longer marked OPEN;
- source-registry manifest chunks exist;
- corpus V6 research-output count matches the indexed output list and every indexed path exists.

The workflow is manual and pull-request driven. It does not initiate new harvesting or geographic discovery.

## 10. What remains intentionally historical

No destructive pruning was performed. The following remain because they document the research process:

- old global/archive priority routers;
- closure batch v1/v2 and residual v3 snapshots;
- failed page-retrieval checks;
- bibliography pass audits;
- old corpus manifests and research-output indexes;
- modular survey batches and adapter expansions;
- dated progress logs.

A historical file may contain a conclusion that was later narrowed or superseded. Current authority must therefore be resolved through `REPOSITORY_STATE.json` and layer-specific manifests rather than by searching for the newest-looking filename.

## Terminal organization state

The repository now has a clear hierarchy:

**source masters / frozen survey → current derived authority → compact publication/index layers → website presentation**.

Further cleanup should be row-level QC rather than another structural redesign: duplicate IDs/URLs/DOIs within the 206 bibliography rows, field nulls and schema drift, stale/dead external pointers, and contradiction scans across historical snapshots. Those checks should report discrepancies without silently rewriting source evidence.
