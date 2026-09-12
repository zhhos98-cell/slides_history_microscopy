# Iron Library project map

This file is the navigation layer for `projects/iron_library_glass_carriers_2026-09-11/`. It does not replace the underlying research files.

## 1. Active research / application work — `main`

Start here for the current Iron Library residency / holdings argument:

1. `PINNED_APPLICATION_RESUME.md` — short authoritative application resume point.
2. `COLLECTION_FIRST_HOLDINGS_CENSUS_2026-09-12.md` — current collection-first holdings census; keep Library / EBA / GFA distinct.
3. `HOLDINGS_TIME_MAP_2026-09-12.md` — active time-aware map of where Library / EBA / GFA actually thicken, plus a prior-SiR overlay. Use this before inferring that a fonds start date means continuous nineteenth-century density.
4. `HOLDINGS_TIME_MAP_DENSITY_ADDENDUM_2026-09-12.md` — adds the contemporaneity/originality axis; records Rauschenbach governance correction, Traisen copies vs original plans, later personnel registers carrying earlier data, and the strengthened native-GF product/document cluster.
5. `HOLDINGS_HEATMAP_2026-09-12.md` — five-axis comparison of large holdings blocks: scale / seriality / date density / provenance coherence / contemporaneity-originality. Now includes EBA 1 Gotthardbahn maps and a demoted pre-1885 rating for GFA 8.
6. `LIBRARY_SERIAL_ENVIRONMENT_2026-09-12.md` — Library-only serial census; separates publication run from Iron Library holding run/completeness and records controlled nineteenth-century anchor titles and later backfilling donations.
7. `FELLOWSHIP_EARLY_MATERIALS_MICROSCOPY_LIBRARY_ARCHIVE_PIN_2026-09-12.md` — earlier methodological pin for early materials microscopy; useful framing, but subordinate to collection-first census/time map/heat map when they differ.
8. `FELLOWSHIP_HOLDINGS_AUDIT_2026-09-11.md`, `RESIDENCY_TRIAGE_2026-09-11.md`, `SOURCE_MAP.md` — supporting holdings and source audits.
9. `CURRENT_PROGRESS.md` — broad project progress narrative on `main`; do not use it as the sole authority for corrected-transcription progress.

Current research rule: **collection first; question second**. Treat the holdings as three evidence systems: **Library / EBA (Eisenbibliothek Archiv) / GFA (GF Corporate Archives)**. For chronology, use the time map rather than top-level fonds start dates alone. For archival strength, also distinguish the date of the historical content from the creation date/originality of the surviving carrier.

### Holdings originality rule

A source dated to an early historical period is not necessarily a contemporary surviving record. Classify surviving material where possible as:

- `ORIGINAL_CONTEMPORARY`
- `CONTEMPORARY_BUT_RETROSPECTIVELY_FILED`
- `LATER_COPY_OF_EARLIER_RECORD`
- `LATER_REGISTER_WITH_EARLIER_DATA`
- `RETROSPECTIVE_HISTORICAL_DOSSIER`
- `ORIGINALITY_OPEN`

Do not rank blocks by envelope dates alone.

### Library serial rule

Keep three things separate:

- `PUBLICATION_RUN`
- `IRON_LIBRARY_HOLDING_RUN`
- `RUN_COMPLETENESS`

A journal's publication dates are not evidence that the Library owns every volume for those dates. Later donations can also backfill or thicken historical runs.

## 2. Wedding manuscript correction — branch `ironlibrary-json-correction`

Start from `PINNED_TRANSCRIPTION_RESUME.md` on `main`, then switch to branch `ironlibrary-json-correction`.

Canonical correction workspace on that branch:

- `corrected_transcription/README.md` — human-readable quality and resume guide; **read this before treating any ledger row as transcription**.
- `corrected_transcription/README.json` — machine-readable historical coverage checkpoint and status lists.
- `corrected_transcription/WEDDING_MSS23_CORRECTED_TRANSCRIPTION.jsonl`
- `corrected_transcription/WEDDING_MSS24_CORRECTED_TRANSCRIPTION.jsonl`
- `corrected_transcription/WEDDING_MSS25_CORRECTED_TRANSCRIPTION.jsonl`
- branch-local `CURRENT_PROGRESS.md` — narrative checkpoint.

Verified workflow coverage at time of this map: **Mss 23 textual sequence through PDF 210; Mss 24 through PDF 65; next unprocessed sequential page Mss 24 PDF 66.**

### Quality audit override — 2026-09-12

Do **not** interpret the coverage checkpoint above as a claim of citation-ready transcription quality.

A quality audit found that Mss 24 PDFs 1–65 use a legacy mixed data model: literal manuscript readings, diagram labels, normalized entities, editorial visual description and reconstructed/analytical prose are sometimes stored together in `transcription` and `secure_anchors`. English editorial terms such as `cross-section`, `columnar basalt`, `country rock`, `circular plan`, `bell`, `gas outlet`, `blast-furnace section` and `pile diagram` demonstrably entered `secure_anchors`; these are not literal Wedding source readings.

Therefore:

- Mss 24 PDFs 1–65 status = **`LEGACY_MIXED_EXTRACTION_REQUIRES_CLEANUP`**.
- They are useful for retrieval, routing, technical-topic discovery, entities and many numerical anchors.
- They are **not safe for exact quotation, terminology history or wording-sensitive analysis without direct manuscript-image control**.
- Coverage and transcription quality must be reported separately.
- Do not blindly continue PDF 66 with the old semantics. First calibrate a corrected layered schema on a small mixed batch (recommended PDFs 56–60), then continue.

Corrected future layers are: `literal_transcription`, `diagram_labels`, `editorial_description`, `normalized_entities`, `uncertain_readings`, `research_summary`; `secure_anchors` may derive only from literal source wording and literal diagram labels.

Mss 25's controlled Bessemer/Sheffield cluster is generally closer to the desired selective-transcription standard; Mss 23 is generally more conservative than Mss 24, but neither should be quoted without image control.

## 3. Supporting / historical Wedding logs

These files remain useful as evidence, indexes or retrieval aids, but are **not authoritative transcription checkpoints**:

- `WEDDING_FULL_OCR_READING_LOG_*`
- `WEDDING_OCR_FIRST_PASS_*`
- `WEDDING_BESSEMER_TARGETED_OCR_*`
- `WEDDING_MSS25_VISUAL_CONTROL_PASS*`
- itinerary / process-heading / source-mode TSV indexes
- Bessemer manuscript/publication comparison notes

Use them to locate pages and possible anchors. Resolve progress and quality against the pinned transcription resume plus the correction-branch README.

## 4. Fischer / earlier industrial-travel research

Files beginning `FISCHER_*` form a separate research cluster on travel, observation, testing, samples, secrecy, networks and 1845–1846 event reconstruction. They are research inputs, not current application or transcription resume points.

## 5. External-source expansion and legacy passes

`EXTERNAL_SOURCE_EXPANSION*` and other dated/pass-numbered research files are cumulative research history. Preserve them for provenance. New work should normally update an active synthesis/pin rather than create another unindexed pass file.

## 6. Repository hygiene rule going forward

- Every active workstream gets exactly one pinned resume file.
- Data ledgers stay in dedicated subdirectories; narrative research stays outside them.
- A dated/pass file is supporting history unless a pin explicitly promotes it.
- Do not infer recency or quality from filename/status label alone; use the pinned resume and branch HEAD.
- For manuscript work, keep **coverage**, **literal transcription**, **editorial visual description**, and **research interpretation** as separate layers.
- For holdings work, keep **Library / EBA / GFA** separate and distinguish **fonds envelope dates**, **actual series-level date density**, and **surviving-carrier originality/contemporaneity**.
- For serials, distinguish **publication chronology**, **library holding chronology**, and **holding completeness**.
- Avoid moving or deleting legacy files solely for cosmetic cleanup because existing notes may cite their paths.

Last organized / quality-audited / holdings-heat-map and serial-environment updated: 2026-09-12.
