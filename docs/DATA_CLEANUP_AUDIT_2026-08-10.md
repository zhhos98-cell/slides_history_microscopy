# Data cleanup audit — 2026-08-10

Status: **CLEANED / CURRENT AUTHORITY NORMALIZED**

This cleanup does not reopen the frozen 307/155 surviving-object survey and does not delete versioned research snapshots. Its purpose is to remove routing ambiguity, make supersession explicit, preserve quantity namespaces and ensure that historical intermediate files cannot be mistaken for the current research state.

## What was cleaned

### 1. One canonical current-state manifest

Added `data/analysis/CURRENT_STATE.json` as the single machine-readable pointer to the current analytical state. It records:

- frozen survey state: 307 discovery / 155 strict nineteenth-century nodes;
- bibliography state: pass 19 / 206 entries = 88 research + 118 primary/object, 19 publication languages;
- public-web discovery queue: 0;
- exact-source request queue: 4;
- current authority files;
- supersession map for dated/versioned snapshots;
- quantity invariants and cleanup policy.

### 2. Analysis authority order

Updated `data/analysis/README.md` and `data/README.md` so that a reader or script must resolve current authority before using an older versioned analytical file. The operative order is now:

1. source master / frozen survey source row for source claims and census membership;
2. `data/analysis/CURRENT_STATE.json` for current derived-state authority;
3. the target-specific file named there;
4. older versioned analysis files as audit/history only;
5. site/corpus presentation layers last.

### 3. Stale routing removed from the object-to-corpus map

Updated `data/analysis/uk_us_object_to_corpus_expansion_v1.json` from a mixed closure/incomplete state to the current request-only state. In particular:

- Naples 383 is no longer marked as an unresolved candidate;
- Norman, Challenger and Elcock are explicitly request-only at their remaining granularities;
- H. L. Smith and Kitton residual prospectus/notice work is explicitly optional;
- Pritchard remains corrected to the 1835 preparation-list date;
- live authority pointers now resolve to `CURRENT_STATE.json` and the `_CURRENT` router.

### 4. Naples contradiction removed

The earlier `naples_row383_page_verification_v3.json` is retained as a bounded negative web/page-retrieval check but is marked superseded by `naples_row383_object_catalogue_closure_v4.json`.

The current result is based on the locally held primary catalogue OCR:

- 382: `Delphinus phocaena L. Milz`
- 383: `-- Penis`
- 384: `-- Hode`
- 385: `-- Niere`

The surviving St Andrews object `BPM/1/T8/6` has Stazione Zoologica Napoli labels, `Delphinus phocaena`, and the public right-label transcription `Panis 383`. Catalogue offering 383 is therefore closed to the surviving slide at catalogue-offering identity level. `Panis` and `Penis` remain separate source readings; no silent normalization was applied.

### 5. Historical direction note quarantined

`docs/UK_US_RETURN_TO_CORE_2026-08-10.md` is retained because it records the pass-17 decision point, but it is now explicitly marked **HISTORICAL SNAPSHOT — SUPERSEDED**. It also carries the Pritchard correction: the preparation-list target is 1835, not 1837.

### 6. Root direction cleaned

`CURRENT_DIRECTION.md` now points first to `data/analysis/CURRENT_STATE.json` and the live `_CURRENT` router. Batch v1/v2 and residual v3 files are listed as audit snapshots rather than active task queues.

## Deliberately not deleted

The following classes remain in place:

- dated closure batches;
- failed bounded verification files;
- predecessor analytical versions;
- bibliography pass audit documents;
- older routing snapshots.

They are evidentiary history. Deleting them would remove the record of negative checks, earlier decision states and the path by which a relation became closed. The cleanup therefore uses authority/supersession metadata rather than destructive pruning.

## Count and namespace checks

Current manifest-level arithmetic is internally consistent:

- bibliography: 88 + 118 = 206;
- frozen survey: 307 discovery nodes and 155 strict nineteenth-century nodes remain separate namespaces;
- Naples: 423 catalogue offerings remain an offering count, not a surviving-slide count;
- Challenger: 4,723 dataset records remain distinct from 4,713 physical containers/objects.

No count was silently converted across namespaces.

## Current terminal state

There are no active public-web discovery targets. Four exact-source requests remain:

1. St Andrews `ms21974–ms21975` page images/transcription;
2. current NHM Challenger 4,723-row resource binary;
3. ZEISS archive/accessory evidence for Balfour objective engravings `573, 1295, 710, 780, 542`;
4. complete St Andrews Norman item/export layer.

The repository should remain in analysis/writing mode until one of those exact sources arrives or produces a new bounded identifier.
