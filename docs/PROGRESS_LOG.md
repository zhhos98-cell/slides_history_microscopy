# Progress log

This file is the human-readable running status log for the microscope-slide project. For machine-readable authority, use `REPOSITORY_STATE.json` and `data/analysis/CURRENT_STATE.json`. Dated audit files remain part of the evidentiary history and should not be treated as current merely because their filename has a higher version number.

## 2026-08-10 15:19 +08:00 — repository/data cleanup and link audit closed

### Current research state

- Frozen global survey remains **CLOSED_2026-08-09**: **307 canonical discovery nodes / 155 strict nineteenth-century nodes**.
- Slide-locked bibliography remains **pass 19**: **206 entries = 88 research + 118 primary/object**, across **19 publication languages**.
- Current compact corpus/publication authority is `data/corpus/CORPUS_MANIFEST_V6.json`; `RESEARCH_OUTPUTS_V6.json` contains **41 curated current/foundational outputs**.
- Public-web discovery queue is **0**. General geographic expansion and bibliography expansion remain parked.
- Active research mode is **analysis/writing plus exact-source access only**.

### Exact-source request queue

Only four request-only residuals remain:

1. **Charles Elcock / St Andrews `ms21974–ms21975`** — page images or transcription of the two letters.
2. **NHM HMS Challenger** — current **4,723-row** resource binary.
3. **Balfour / ZEISS** — archive/accessory evidence for surviving objective engravings **573, 1295, 710, 780, 542**.
4. **John Thomas Norman / St Andrews** — complete item/export layer with current addresses and label transcriptions.

Do not reopen broad discovery searches for these. Resume a chain only when the exact requested source arrives or produces a new bounded identifier.

### Repository/data cleanup completed

The 2026-08-10 cleanup normalized authority without destructively deleting historical research states.

- `data/analysis/CURRENT_STATE.json` is the canonical current analysis-state pointer and supersession map.
- `REPOSITORY_STATE.json` remains the repository-wide authority map.
- Historical closure batches, residual files, failed page checks and earlier routers remain as audit history rather than parallel current authorities.
- `scripts/validate_repository_state.py` performs structural and row-level checks across repository authority, JSON syntax, frozen-survey arithmetic, bibliography schema/IDs, analysis queues, source-registry canonicalization, corpus publication pointers and current site links.
- The frozen 307/155 survey membership was not rewritten.
- Quantity namespaces remain separate: catalogue offerings, physical slides, preparations, specimens, accession/register numbers, dataset rows and cabinet capacities are not normalized into one count.

### Bibliography duplicate-route QC

The 206-row bibliography was checked semantically for repeated DOI/URL routes.

- Repeated DOI routes attached only as later-work verification links were removed from the historical rows they did not identify.
- Current bibliography now has **zero repeated DOI routes across distinct records**.
- Remaining repeated non-DOI URLs were reviewed as shared verification/access routes and retained where they support distinct records.
- Bibliography membership remains **206**; no record was removed by this cleanup.

### Source-registry normalization

`sources/source-registry-manifest.json` now distinguishes raw history from canonical/public routing:

- **87 raw rows** across 12 chunks;
- **3 superseded same-endpoint duplicate routes**;
- **1 excluded out-of-scope route** (`GB-SHEFFIELD-SORBY`), retained only as raw audit history;
- **83 canonical/public source routes**.

The public Sources loader is manifest-driven, loads all 12 registry chunks, and suppresses both `superseded_ids` and `excluded_ids` before rendering/exporting.

### External-link / dead-pointer audit

A refined GitHub Actions link audit checked the current public bibliography and canonical source-registry routes.

Run `31364908904` checked **384 unique URLs**:

- bibliography unique URLs: **269**;
- canonical source-registry unique URLs: **122**;
- `ok`: **263**;
- `reachable_but_restricted`: **75**;
- network/TLS/timeout/server review states: **45**;
- `dead_candidate`: **1**;
- redirects followed: **49**.

The only 404/410 candidate, Utrecht's **Collectie Zoölogisch Museum** route, was manually recovered as a live page. Therefore the current public layers have **0 confirmed dead pointers** among the 404/410 candidates.

The checker now retries 404/410/416 without the Range header and treats automated 404/410 only as `dead_candidate`, never as an automatic deletion decision. 401/403/429 remain reachable-but-restricted; TLS, timeout, DNS, connection reset and 5xx responses remain review states.

Two stale verification routes were refreshed during this pass:

- Croatian National Collection of Diatoms: old `camen.pmf.unizg.hr` history route replaced by the current Faculty of Science page; the dated 2019 >6,000 preparation statement and current >4,000 statement remain separate temporal count states.
- Cajal / Simurg: old item-style secondary route replaced by the current **Espacio Cajal** collection-level route.

The remaining host/network review states are bounded infrastructure/client failures and do not justify destructive source cleanup.

### Integrity status

The repository-integrity workflow completed successfully after the progress/audit changes. The latest recorded run at this checkpoint is **31365173237**, conclusion **success**.

### Closed or substantially closed analytical chains

Current analysis can proceed from the already-closed material rather than opening another discovery frontier. The strongest available chains include:

- Arthur C. Cole vols. I–II material-publication architecture and the surviving 52-slide counterpart;
- Charles Collins Jr. 1884/1885 series/event/survival chain;
- H. L. Smith and Frederic Kitton serial-set architectures;
- Andrew Pritchard's corrected **1835** preparation-list/object bridge;
- John Thomas Norman at collection level;
- HMS Challenger address/dataset architecture and named diagnostic preparations;
- Balfour objective designation to publication-caption layer;
- Harvard Embryological Collection / Minot as a control architecture;
- Naples 1880 catalogue and British circulation evidence;
- Naples catalogue offering **383 → St Andrews `BPM/1/T8/6`** at catalogue-offering identity level.

For Naples, retain the distinction between printed **`Penis`** and the St Andrews public label transcription **`Panis 383`**. Offering identity does not establish manufacture date, preparator, shipment-copy identity or complete individual-copy chronology.

### Next operational move

**Stop repository hygiene here unless a concrete defect appears.** Structural normalization, duplicate-route QC, scope cleanup and current-link checking are complete enough for the present research stage.

The next default move is analysis/writing from closed chains. Exact-source work resumes only when one of the four requested sources becomes available.
