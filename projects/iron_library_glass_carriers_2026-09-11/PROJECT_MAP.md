# Iron Library project map

This file is the navigation layer for `projects/iron_library_glass_carriers_2026-09-11/`. It does not replace the underlying research files.

## 1. Active research / application work — `main`

Start here for the current Iron Library residency / holdings argument:

1. `PINNED_APPLICATION_RESUME.md` — short authoritative application resume point.
2. `COLLECTION_FIRST_HOLDINGS_CENSUS_2026-09-12.md` — current collection-first holdings census; keep Library / EBA / GFA distinct.
3. `FELLOWSHIP_EARLY_MATERIALS_MICROSCOPY_LIBRARY_ARCHIVE_PIN_2026-09-12.md` — earlier methodological pin for early materials microscopy; useful framing, but subordinate to collection-first census when the two differ.
4. `FELLOWSHIP_HOLDINGS_AUDIT_2026-09-11.md`, `RESIDENCY_TRIAGE_2026-09-11.md`, `SOURCE_MAP.md` — supporting holdings and source audits.
5. `CURRENT_PROGRESS.md` — broad project progress narrative on `main`; do not use it as the sole authority for corrected-transcription progress.

Current research rule: **collection first; question second**. Treat the holdings as three evidence systems: **Library / EBA (Eisenbibliothek Archiv) / GFA (GF Corporate Archives)**.

## 2. Corrected Wedding transcription — branch `ironlibrary-json-correction`

Start from `PINNED_TRANSCRIPTION_RESUME.md` on `main`, then switch to branch `ironlibrary-json-correction`.

Canonical correction workspace on that branch:

- `corrected_transcription/README.md` — human-readable resume guide.
- `corrected_transcription/README.json` — machine-readable checkpoint and status taxonomy.
- `corrected_transcription/WEDDING_MSS23_CORRECTED_TRANSCRIPTION.jsonl`
- `corrected_transcription/WEDDING_MSS24_CORRECTED_TRANSCRIPTION.jsonl`
- `corrected_transcription/WEDDING_MSS25_CORRECTED_TRANSCRIPTION.jsonl`
- branch-local `CURRENT_PROGRESS.md` — narrative checkpoint.

Verified substantive checkpoint at time of this map: **Mss 23 textual sequence through PDF 210; Mss 24 through PDF 65; resume at Mss 24 PDF 66.**

A page counts as transcribed only when readable wording has been entered after PDF control. Routing, generic page descriptions and visual review alone do not count.

## 3. Supporting / historical Wedding logs

These files remain useful as evidence, indexes or retrieval aids, but are **not authoritative transcription checkpoints**:

- `WEDDING_FULL_OCR_READING_LOG_*`
- `WEDDING_OCR_FIRST_PASS_*`
- `WEDDING_BESSEMER_TARGETED_OCR_*`
- `WEDDING_MSS25_VISUAL_CONTROL_PASS*`
- itinerary / process-heading / source-mode TSV indexes
- Bessemer manuscript/publication comparison notes

Use them to locate pages and secure anchors; resolve progress against the correction branch.

## 4. Fischer / earlier industrial-travel research

Files beginning `FISCHER_*` form a separate research cluster on travel, observation, testing, samples, secrecy, networks and 1845–1846 event reconstruction. They are research inputs, not current application or transcription resume points.

## 5. External-source expansion and legacy passes

`EXTERNAL_SOURCE_EXPANSION*` and other dated/pass-numbered research files are cumulative research history. Preserve them for provenance. New work should normally update an active synthesis/pin rather than create another unindexed pass file.

## 6. Repository hygiene rule going forward

- Every active workstream gets exactly one pinned resume file.
- Data ledgers stay in dedicated subdirectories; narrative research stays outside them.
- A dated/pass file is supporting history unless a pin explicitly promotes it.
- Do not infer recency from filename alone; use the pinned resume and branch HEAD.
- Avoid moving or deleting legacy files solely for cosmetic cleanup because existing notes may cite their paths.

Last organized: 2026-09-12.
