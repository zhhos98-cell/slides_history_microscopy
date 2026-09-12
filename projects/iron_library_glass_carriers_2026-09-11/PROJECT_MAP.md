# Iron Library project map

This is the navigation layer for `projects/iron_library_glass_carriers_2026-09-11/`. Use pinned/current synthesis files before dated legacy passes.

## 1. Active research / application work — `main`

Read in this order:

1. **`PINNED_APPLICATION_RESUME.md`** — short authoritative application resume point.
2. **`ANTON_ARCHIVAL_SYSTEMS_MAP_2026-09-12.md`** — current total retrieval architecture: Library + EBA / GFA / GFKS / GFD.
3. **`HOLDINGS_HEATMAP_2026-09-12.md`** — current **six-axis / five-system** comparison: scale, seriality, date density, provenance coherence, carrier originality, onsite value. GFKS/GFD migration is complete.
4. **`TIER_A_CARRIER_PROVENANCE_AUDIT_2026-09-12.md`** — source-critical audit of Haffter / Küderli / Rauschenbach carrier morphology and arrangement history.
5. `HOLDINGS_TIME_MAP_2026-09-12.md` + `HOLDINGS_TIME_MAP_DENSITY_ADDENDUM_2026-09-12.md` + `CROSS_SYSTEM_OVERLAP_WINDOW_2026-09-12.md` — chronology, originality and the two current overlap peaks c.1868–72 / c.1877–85.
6. **`ONSITE_VALUE_MAP_2026-09-12.md`** — source-access / residency-necessity map.
7. `COLLECTION_FIRST_HOLDINGS_CENSUS_2026-09-12.md` — broad collection-first census; later architecture/time/heat-map/carrier audits override it where they differ.
8. `LIBRARY_SERIAL_ENVIRONMENT_2026-09-12.md`, `LIBRARY_SUBJECT_STRUCTURE_2026-09-12.md`, `LIBRARY_MANUSCRIPT_ESTATE_CENSUS_2026-09-12.md`, `LIBRARY_DIGITISED_MANUSCRIPT_LAYER_2026-09-12.md` — Library morphology and claim ceilings.
9. `GFA1_PRE1896_CLASS_MORPHOLOGY_2026-09-12.md` + `GFA_PRE1900_FONDS_CENSUS_2026-09-12.md` — GFA pre-1896 controls.
10. `SIR_HOLDING_SYSTEM_OVERLAY_2026-09-12.md` — prior-SiR overlap by period/holding system; absence from public descriptions is only a public-description gap.
11. **`COLLECTION_ACCESS_ENQUIRY_DRAFT_2026-09-12.md`** — **NOT SENT**; staff access/catalogue questions.
12. `FELLOWSHIP_EARLY_MATERIALS_MICROSCOPY_LIBRARY_ARCHIVE_PIN_2026-09-12.md` and other Sheffield–Berlin/microscopy files — subordinate hypotheses only.
13. `CURRENT_PROGRESS.md` — broad narrative history; never use alone as an authoritative checkpoint.

Current research rule:

> **COLLECTION FIRST; QUESTION SECOND; ONSITE NECESSITY THIRD.**

## 2. Current collection architecture

Use current retrieval boundaries:

- **LIBRARY / IRONCAT** — printed holdings, serials, rara, and separately-listed manuscript/special-collection layer.
- **EBA / ANTON** — non-GF archival fonds/special collections.
- **GFA / ANTON** — GF family/company/subsidiary/admin/media/object provenance.
- **GFKS / ANTON** — physical art/maps/prints/views/objects.
- **GFD / ANTON** — modern digital documentation/reference-image layer.

Do not project current boundaries backward. Older institution-level counts can include material now catalogued in EBA/GFKS. Map them before adding totals.

## 3. Holdings source-critical rules

### Six-axis rule

For every candidate block keep separate:

- scale;
- internal seriality;
- actual date density;
- provenance coherence;
- surviving-carrier originality/contemporaneity;
- onsite value / remote substitutability.

### Carrier status

Use:

- `ORIGINAL_CONTEMPORARY`
- `CONTEMPORARY_BUT_RETROSPECTIVELY_FILED`
- `LATER_COPY_OF_EARLIER_RECORD`
- `LATER_REGISTER_WITH_EARLIER_DATA`
- `RETROSPECTIVE_HISTORICAL_DOSSIER`
- `ORIGINALITY_OPEN`

### Tier-A morphology correction

Do not call Haffter, Küderli and Rauschenbach three equivalent company archives.

- **Haffter:** old iron-trade business archive with very strong bound-series/correspondence survival; public fonds description says it was originally unordered, so present ANTON arrangement is not demonstrated as original nineteenth-century filing order.
- **Küderli/Bär:** multi-accession historical company collection (1980 / 1986 / 2006) with especially strong bound profile/cash/sales series.
- **Rauschenbach:** acquired-company evidence dispersed through retrospective GF systems; strongest true serial carriers are bound registers, while several important present-day dossiers contain broad or mixed chronology.

Use `TIER_A_CARRIER_PROVENANCE_AUDIT_2026-09-12.md` for details.

## 4. Current structural result

### Tier A

- Library nineteenth-century subject + serial environment;
- EBA 3 Haffter;
- EBA 4 Küderli/Bär;
- Rauschenbach operational/company records.

### Tier B

- native GF c.1865–83 product/market-document regime;
- EBA 1 engineering/Gotthard maps;
- Traisen;
- GFKS c.1850–85 visual/map layer.

### Tier C / controls

- EBA 2 Gonzen for c.1850–85;
- EBA 6 before 1889/90;
- broad GFA 8 pre-1885;
- EBA 8 representation collection;
- later photo/glass systems.

### Tier D

- GFD digital/reference layer.

Natural collection-driven windows remain **c.1868–72** and **c.1877–85**. Native-GF systematic governance thickens sharply in **1896**.

## 5. Onsite-value result

Strongest provisional onsite candidates:

1. EBA 3 Haffter;
2. EBA 4 Küderli/Bär;
3. Rauschenbach operational/company records.

Wedding Mss 23–25 are fully available through e-codices and belong primarily to the pre-visit corpus. GFKS onsite value is mainly physical/material/copy-specific because many visible objects are digitised. GFD contributes essentially no original-source onsite necessity.

The institution-level `66 manuscripts + 3 estates` remains OPEN/potentially high because current identities, chronology, digitisation state and Library/EBA/GFKS mapping are unresolved. Do not calculate `52 undigitised manuscripts`.

## 6. Current public-web stop rules

- Current 2024 Library classification PDFs are officially linked but their bodies are not reproducibly retrievable through the present route; do not reconstruct the hierarchy from expectation.
- Complete current nineteenth-century serial title/holding-run/gap export is not reproducibly recoverable from public interfaces.
- Public interfaces do not supply a reliable complete inventory of the 66 manuscripts / 3 estates.
- Do not brute-force catalogue suffixes or manuscript numbers after these stop rules are reached.

The correct next route is an **existing staff/catalogue export**, not staff historical research.

## 7. Wedding manuscript correction — separate workstream

Authoritative branch: `ironlibrary-json-correction`.

Start from `PINNED_TRANSCRIPTION_RESUME.md` on `main`, then read on the correction branch:

- `corrected_transcription/README.md`
- `corrected_transcription/QUALITY_STATUS.json`
- `corrected_transcription/README.json`
- the three corrected-transcription JSONL ledgers
- branch-local `CURRENT_PROGRESS.md`

Coverage checkpoint: Mss 23 textual sequence through PDF 210; Mss 24 through PDF 65; next unprocessed sequential page PDF 66.

Quality override: Mss 24 PDFs 1–65 = **`LEGACY_MIXED_EXTRACTION_REQUIRES_CLEANUP`**. Coverage is not citation-ready transcription. Before continuing PDF 66, calibrate the corrected layered schema on a small mixed batch such as PDFs 56–60.

## 8. Repository hygiene

- Every active workstream gets one pinned resume.
- Use branch HEAD + pin, not filename date, to determine recency.
- Preserve legacy passes for provenance but subordinate them to active syntheses.
- Do not move/delete legacy files merely for cosmetic cleanup when other notes may cite their paths.
- On concurrent writes, refetch the current blob SHA and merge; never force a stale overwrite.

Last reconciled after six-axis heat-map migration and Tier-A carrier/provenance audit: 2026-09-12.
