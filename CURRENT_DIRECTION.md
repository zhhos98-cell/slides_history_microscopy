# Current direction

Updated: 2026-08-10

The discovery phase is parked. The public indexed closure pass is now also **exhausted**: the remaining UK / narrowly linked US / already-open European edges are exact-source access problems rather than search problems.

- Frozen surviving-object survey: **307 discovery nodes / 155 strict nineteenth-century nodes — CLOSED_2026-08-09**.
- Public slide bibliography: **pass 19, 206 verified entries (88 research + 118 primary/object), 19 publication languages**. Passes 18–19 remain completed audit history and do not generate a new geographic search frontier.
- No new geographic infrastructure is active. The repository should not increase coverage merely to add countries, institutions or collection counts.
- The analytical priority remains **object↔text↔register closure**. Public-web work stops when it ceases to change attribution, chronology, object identity or historical mechanism.
- The GitHub collection layer remains a **reverse index into the historical corpus**, not a second general corpus.

## Current authority

Use `REPOSITORY_STATE.json` as the top-level authority map for the whole repository. Within the analysis layer, use `data/analysis/CURRENT_STATE.json` as the canonical machine-readable analysis-state manifest and `data/analysis/global_archive_research_priority_CURRENT.json` as the live operational router. Older versioned batch/residual files remain in the repository as audit snapshots and are explicitly mapped as superseded where appropriate.

Current public-layer authorities are:

- survey: `data/survey/07AR_CLOSURE_MANIFEST_2026-08-09.json`
- bibliography: `bibliography/bibliography-manifest.json`
- analysis: `data/analysis/CURRENT_STATE.json`
- corpus publication: `data/corpus/CORPUS_MANIFEST_V6.json`
- source registry: `sources/source-registry-manifest.json`
- bounded harvest evidence: `data/evidence/targeted_deep_4/manifest.json`

Current target-specific authority files include:

- `data/analysis/naples_row383_object_catalogue_closure_v4.json`
- `data/analysis/cole_studies_vol1_2_structured_reading_v1.json`
- `data/analysis/challenger_dataset_row_harvest_v2.json`
- `data/analysis/balfour_plate_caption_objective_harvest_v2.json`
- `data/analysis/elcock_standrews_1884_letters_v5.json`
- `data/analysis/exact_source_local_availability_audit_2026-08-10_v1.json`

The earlier closure-batch and residual snapshots are retained for audit but are not live queues:

- `data/analysis/uk_us_europe_closure_batch_2026-08-10_v1.json`
- `data/analysis/uk_us_europe_closure_batch_2026-08-10_v2.json`
- `data/analysis/uk_us_europe_closure_residuals_2026-08-10_v3.json`
- `data/analysis/four_target_execution_status_2026-08-10.json`

The closed architecture now covers Cole, Collins, H. L. Smith, Kitton, Pritchard, Norman at collection level, Challenger at address/dataset level, Balfour at publication/designation level, Minot/HEC as a control, and Naples catalogue offering 383 to surviving St Andrews `BPM/1/T8/6`.

For Naples 383, the locally held primary catalogue OCR reads `382. Delphinus phocaena L. Milz / 383. -- Penis / 384. -- Hode / 385. -- Niere`. By ditto continuation, offering **383 = Delphinus phocaena L., Penis**. The St Andrews slide independently carries Stazione Zoologica Napoli labels, `Delphinus phocaena`, and the public right-label transcription `Panis 383`. The one-letter `Panis` / `Penis` discrepancy is preserved as a source-level transcription issue; catalogue-offering identity does not establish manufacturing date, preparator, price, or identity with a particular shipment copy.

## Remaining request-only queue

1. St Andrews `ms21974–ms21975`: page images/transcription. The public catalogue securely records a reference to Challenger expedition samples, but the correspondence is principally antiquarian/medal discussion; sender, sample, station and purpose remain inside the letters.
2. NHM Challenger: current 4,723-row resource binary. The public dataset/address architecture and named diagnostic preparation examples are already structured; the residual task is mechanical full-table ingestion.
3. Balfour/ZEISS: archive guidance for objective engravings `573, 1295, 710, 780, 542`. ZEISS's public production lists are organized around microscope/stand dispatch records and accessories; the objective engravings must not be treated as stand serials without archive evidence.
4. St Andrews Norman: complete item/export layer. The public record confirms the 1872 catalogue of 2,584 mounts and says the Norman slides remain scattered in situ, but it does not expose a usable child-item list.

Do not repeat broad searches for these four targets. Resume one only when the exact requested source arrives or produces a new bounded identifier. Otherwise the useful next move is historical analysis/writing from the chains already closed.
