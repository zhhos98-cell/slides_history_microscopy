# Repository organization audit — 2026-08-10

Status: **WHOLE-REPOSITORY AUTHORITY NORMALIZED / ROW-LEVEL + SEMANTIC ROUTE + LINK QC PASSED**

This pass reviews the repository as a system rather than only the analysis folder. The aim is to make every layer legible as one of: canonical source/frozen data, current derived authority, compact publication layer, generated runtime artifact, or historical/audit snapshot. The cleanup deliberately avoids deleting modular survey batches, dated research states or bounded negative checks.

## 1. Top-level authority

`REPOSITORY_STATE.json` is the repository-wide authority map. It points to:

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

`bibliography/README.md` and `bibliography-manifest.json` identify the manifest plus 22 chunks as the current authority. The old static `bibliography/bibliography.csv` is a **legacy partial index**. It remains for compatibility/audit history but is not the 206-row bibliography and must not be used for current totals or complete exports. The public bibliography page loads the manifest/chunks and generates portable exports from the same rows.

The semantic route audit corrected the DOI rule. A DOI link now belongs in a row only when it identifies that row's own bibliographic item. Two later-work DOI links that had been used merely as citation/verification routes were removed from three historical/research rows because the exporter would otherwise misidentify those rows in CSL JSON, BibTeX and RIS. Bibliography membership remains unchanged at 206.

## 4. Source registry canonicalized and scope-filtered

`sources/source-registry-manifest.json` remains the authority across `source-registry.json` and chunks 02–12. The raw chunks preserve **87 routing records**. Semantic review identified **3 same-endpoint duplicate IDs**:

- `ZA-IZIKO-ENTOMOLOGY` → `ZA-IZIKO-ENTOMOLOGY-SLIDES`;
- `AR-LAPLATA-FYCOLOGY` → `AR-MLP-FICOLOGIA-DIATOMS`;
- `NZ-TEPAPA-COLLECTIONS-ARCHIVES` → `NZ-TEPAPA-NATURAL-HISTORY-ARCHIVES`.

A later scope pass also identified **1 cross-project residue**, `GB-SHEFFIELD-SORBY`. This row is not a duplicate and therefore remains separately classified under `excluded_ids` rather than `superseded_ids`.

The raw chunks remain unchanged as audit history. Current/public source-registry arithmetic is therefore:

- 87 raw rows;
- 3 superseded duplicate routes;
- 1 excluded out-of-scope route;
- **83 canonical source routes**.

Three shared canonical URLs remain deliberately separate because they represent parent/subcollection or primary/secondary documentary relations rather than duplicate endpoints: Bell Pettigrew ↔ Elcock/Naples, Challenger sediments ↔ CT reassessment, and the broader NHM Heron-Allen collection ↔ the Heron-Allen & Earland Type Slide system.

Source-registry records remain research routes, not frozen object-census rows and not automatically nineteenth-century corpus text.

## 5. Public Sources page corrected

The semantic audit exposed a publication-layer bug: `sources/sources.js` still hard-coded only `source-registry.json`, `source-registry-02.json` and `source-registry-03.json`, even though the manifest contains twelve chunks. The later source records existed in the repository but were not being rendered by the public page.

The loader now:

- fetches `source-registry-manifest.json`;
- loads all twelve manifest chunks;
- suppresses both `superseded_ids` and `excluded_ids`;
- asserts **83 canonical records** before rendering/exporting.

This fixes presentation coverage and project scope without changing the frozen object census or deleting raw source-registry history.

## 6. Derived 155 analysis ambiguity removed

`data/analysis/slide_155_analysis_v1/manifest.json` explicitly records:

- expected frozen membership = 155;
- generator = `scripts/build_slide_analysis_layer.py`;
- generated output = `outputs/SLIDE_155_ANALYSIS_LAYER_V1.csv`;
- no canonical row-level derived CSV is currently committed.

This prevents a reader from assuming that a missing committed CSV was accidentally lost or that README prose itself is the data layer.

## 7. Object→text expansion queue normalized

`data/analysis/slide_155_corpus_expansion_v1/README.md` distinguishes historical v1 routing from current closure state. `OPEN_PRIMARY_SOURCE_TARGETS_V1.csv` is retained as an audit table but no longer behaves as a live queue: H. L. Smith, Collins and Kitton residuals are optional; Naples is closed at supported levels; UCL is parked.

The Naples wording distinguishes two claims. The June 1880 RMS shipment remains unconnected to any specific surviving museum copy. Catalogue offering 383 is independently closed to St Andrews `BPM/1/T8/6` at catalogue-offering identity level.

The central exact-source queue remains four items only: Elcock `ms21974–ms21975`, the NHM Challenger current binary, ZEISS/Balfour objective-accessory evidence, and the St Andrews Norman item/export layer.

## 8. Compact corpus publication layer advanced to V6

`CORPUS_MANIFEST_V6.json` is the current compact publication contract and `RESEARCH_OUTPUTS_V6.json` is the 41-item curated current/foundational research-output index. V6 preserves the V5 core/extension/BNA counts and all seven source-master byte sizes/SHA-256 fingerprints. The corpus payload itself was not rebuilt.

`RESEARCH_OUTPUTS_V4.json` remains the 22-output predecessor. A transient V5 research-output draft created during cleanup was removed because it was never an authoritative publication state.

## 9. Research-state invariants preserved

The cleanup keeps count namespaces separate:

- 307 discovery nodes ≠ 155 strict nineteenth-century nodes;
- 206 bibliography records ≠ physical objects;
- 83 canonical source routes ≠ object-census rows;
- 423 Naples catalogue offerings ≠ surviving-slide total;
- 4,723 Challenger dataset records ≠ 4,713 physical containers/objects;
- serial positions, catalogue numbers, accession numbers, cabinet capacities, preparation counts and slide counts remain distinct.

Current public-web discovery queue remains zero. Current exact-source request queue remains four.

## 10. Repository-wide validation

`scripts/validate_repository_state.py` and `.github/workflows/repository_integrity.yml` check structural and row-level integrity, including:

- top-level authority pointers and related presentation files;
- syntax of every committed JSON file;
- frozen 307/155 closure arithmetic and the 328-row pre-closure ledger state;
- bibliography manifest arithmetic, all 22 chunks, schema headers, required fields and unique IDs;
- **zero repeated DOI routes across distinct bibliography rows**;
- analysis queue = 0 public-web / 4 exact-source requests;
- Naples absent from the request queue while v4 preserves `Penis` and `Panis 383`;
- source-registry raw/canonical arithmetic = 87 / 83 with 3 superseded duplicate route IDs and 1 excluded out-of-scope ID;
- the only canonical source-registry URL reuse is the three explicitly classified parent/secondary relations;
- corpus V6 research-output count, unique output paths and all indexed paths;
- the public Sources loader is manifest-driven rather than a three-file hard-coded subset;
- live Pages/source links point to the current publication manifests.

The normal validator runs on relevant pushes and pull requests. The external-link audit is separately gated so ordinary repository changes do not repeatedly hammer external institutional sites.

## 11. Semantic duplicate-route audit result

Full dispositions are recorded in `docs/DUPLICATE_ROUTE_SEMANTIC_AUDIT_2026-08-10.md`.

The original mechanical warning set was:

- 2 repeated DOI routes across bibliography rows;
- 22 repeated bibliography URLs total;
- 6 repeated source-registry URLs.

After semantic review:

- the 2 repeated DOI routes were removed from rows for which they were only later-work verification links;
- the remaining **20 bibliography URL repetitions** were retained as legitimate shared verification/access routes;
- **3 source-registry URL groups** proved to be true same-endpoint duplicates and were canonicalized through aliases;
- **3 source-registry URL groups** were retained as legitimate parent/subcollection or primary/secondary relations;
- the later Sorby row was excluded as cross-project contamination rather than misclassified as a duplicate.

No bibliography record was removed. No frozen survey member changed.

## 12. External-link / dead-pointer audit

Full method and dispositions are recorded in `docs/EXTERNAL_LINK_AUDIT_2026-08-10.md`.

The refined GitHub Actions audit run `31364908904` checked **384 unique current URLs**: 269 bibliography routes and 122 canonical source-registry routes, with overlap between the layers. Results were:

- 263 `ok`;
- 75 `reachable_but_restricted`;
- 1 `dead_candidate` after a 404/410 retry;
- 45 network/TLS/timeout/server review states;
- 49 redirects.

The sole dead candidate, the Utrecht Repertorium Zoölogisch Museum page, was manually verified as live. The pass therefore produced **zero confirmed dead current pointers**.

Two stale/current-route problems were corrected directly:

- the Croatian National Collection of Diatoms current history link was moved from the old `camen.pmf.unizg.hr` host to the current `www.pmf.unizg.hr` institutional route;
- the Cajal source-registry secondary route was updated from an old Simurg item-style path to the current `Espacio Cajal` collection path.

The remaining review states are retained for bounded/manual follow-up only. Connection resets, TLS errors, timeouts, 403/429 and 5xx responses are not treated as evidence that an institutional source has disappeared.

## 13. What remains intentionally historical

No destructive pruning was performed on evidentiary history. The following remain because they document the research process:

- old global/archive priority routers;
- closure batch v1/v2 and residual v3 snapshots;
- failed page-retrieval checks;
- bibliography pass audits;
- old corpus manifests and the V4 research-output predecessor;
- modular survey batches and adapter expansions;
- superseded or excluded source-registry rows retained inside their original chunks;
- dated progress logs.

A historical file may contain a conclusion later narrowed or superseded. Current authority must therefore be resolved through `REPOSITORY_STATE.json` and layer-specific manifests rather than by filename recency alone.

## Terminal organization state

The repository hierarchy is now:

**source masters / frozen survey → current derived authority → canonicalized routing/publication layers → website presentation**.

Structural, row-level, duplicate-route and immediate dead-pointer cleanup are complete. Further maintenance should be bounded: periodic link audits, exact-source arrivals, and semantic corrections where a verified replacement becomes available. It should not reopen broad discovery or rewrite raw audit evidence merely because an automated HTTP client has difficulty reaching a site.
