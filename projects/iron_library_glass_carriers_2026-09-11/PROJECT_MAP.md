# Iron Library project map

This is the navigation layer for `projects/iron_library_glass_carriers_2026-09-11/`. Use pinned/current synthesis files before dated legacy passes.

## 1. Active research / application work — `main`

Read in this order:

1. **`PINNED_APPLICATION_RESUME.md`** — authoritative resume point.
2. **`ANTON_ARCHIVAL_SYSTEMS_MAP_2026-09-12.md`** — current retrieval architecture: Library + EBA / GFA / GFKS / GFD.
3. **`HOLDINGS_HEATMAP_2026-09-12.md`** — governing six-axis / five-system heat map.
4. **`EVIDENCE_REGIME_MAP_2026-09-12.md`** — cross-system map by record-generating activity rather than modern catalogue bucket.
5. **`TIER_A_CARRIER_PROVENANCE_AUDIT_2026-09-12.md`** — Haffter / Küderli / Rauschenbach carrier, accession and arrangement audit.
6. **`LIBRARY_LARGE_BLOCK_MORPHOLOGY_ADDENDUM_2026-09-12.md`** — Library-side large blocks: serials, technical subjects, materials/testing, geoscience, company/product grey literature, world exhibitions, research travel.
7. **`LIBRARY_REMOTE_SUBSTITUTABILITY_AUDIT_2026-09-12.md`** — access/rarity correction for Library grey literature and world-exhibition print; rarity is not the same as onsite necessity.
8. `HOLDINGS_TIME_MAP_2026-09-12.md` + `HOLDINGS_TIME_MAP_DENSITY_ADDENDUM_2026-09-12.md` + `CROSS_SYSTEM_OVERLAP_WINDOW_2026-09-12.md` — chronology/originality and overlap peaks c.1868–72 / c.1877–85.
9. **`ONSITE_VALUE_MAP_2026-09-12.md`** — source-access / residency-necessity map.
10. `COLLECTION_FIRST_HOLDINGS_CENSUS_2026-09-12.md` — broad census; later architecture/heat-map/evidence-regime/carrier audits override it where they differ.
11. `LIBRARY_SERIAL_ENVIRONMENT_2026-09-12.md`, `LIBRARY_SUBJECT_STRUCTURE_2026-09-12.md`, `LIBRARY_MANUSCRIPT_ESTATE_CENSUS_2026-09-12.md`, `LIBRARY_DIGITISED_MANUSCRIPT_LAYER_2026-09-12.md` — Library-specific controls.
12. `GFA1_PRE1896_CLASS_MORPHOLOGY_2026-09-12.md` + `GFA_PRE1900_FONDS_CENSUS_2026-09-12.md` — GFA pre-1896 controls.
13. `SIR_HOLDING_SYSTEM_OVERLAY_2026-09-12.md` — prior-SiR structural overlay.
14. **`COLLECTION_ACCESS_ENQUIRY_DRAFT_2026-09-12.md`** — **NOT SENT**; includes access/reproduction, physical retrieval units, Rauschenbach internal-file structure, current 66/3/300/80 mapping, current separately-listed Library collections, Library classification export and nineteenth-century periodical holding-run export.
15. `FELLOWSHIP_EARLY_MATERIALS_MICROSCOPY_LIBRARY_ARCHIVE_PIN_2026-09-12.md` and other Sheffield–Berlin/microscopy files — subordinate hypotheses only.
16. `CURRENT_PROGRESS.md` — broad narrative history; never use alone as an authoritative checkpoint.

Current research rule:

> **COLLECTION FIRST; QUESTION SECOND; ONSITE NECESSITY THIRD.**

## 2. Current collection architecture

- **LIBRARY / IRONCAT** — printed holdings, serials, rara, separately-listed manuscript/special-collection layer.
- **EBA / ANTON** — non-GF archival fonds/special collections.
- **GFA / ANTON** — GF family/company/subsidiary/admin/media/object provenance.
- **GFKS / ANTON** — physical art/maps/prints/views/objects.
- **GFD / ANTON** — modern digital documentation/reference-image layer.

Do not project current boundaries backward. Older institution-level counts can map into current EBA/GFKS and must not be naively added as separate holdings.

## 3. Current structural hierarchy

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

- GFD.

## 4. Current analytical corrections

### Six axes

Keep separate: scale / seriality / actual date density / provenance coherence / carrier originality / onsite value.

### Evidence regimes

Modern catalogue system is not the historical analytical unit. Distinguish specialist print, serial communication, iron-trade accounting/correspondence, product/order systems, industrial operations/labour administration, market/product communication, exhibition print, travel/observation, plans/maps, visual collecting, later governance, later photo systems and digital reference work.

### Tier-A source criticism

- Haffter: strong old business archive, but present arrangement is later; fonds described as originally unordered.
- Küderli: multi-accession historical company collection, not a single frozen archive.
- Rauschenbach: strongest seriality in bound registers; important present-day dossiers can contain mixed chronology.

### Library large blocks

Do not reduce Library to one generic subject shelf. Current controlled blocks include serials; metallurgy/iron/mining; historical Metallkunde/Werkstoffprüfung/foundry; geoscience/mineralogy/petrography; company/product grey literature; 95 nineteenth-century world-exhibition publications; 123 research-travel reports across centuries; and reference literature.

### Library access / rarity correction

`RARE != NON-SUBSTITUTABLE != ONSITE-NECESSARY`.

The Library's own grey-literature programme can preserve exceptionally rare items, but some highlighted rare examples are already fully digitised. Major official world-exhibition publications are also often remotely available in complete public facsimiles. Keep the Library Tier A structurally, but do not promote printed holdings to Tier O1 without demonstrating a genuinely non-substitutable or copy-specific subset.

## 5. Onsite-value result

Strongest provisional source-access candidates:

1. EBA 3 Haffter;
2. EBA 4 Küderli/Bär;
3. Rauschenbach operational/company records.

Wedding Mss 23–25 are pre-visit because full e-codices facsimiles exist. Library grey literature/world-exhibition print is mixed and must pass the substitutability test. GFKS is usually material/copy-specific onsite value; GFD has essentially none.

The institution-level `66 manuscripts + 3 estates` remains OPEN / potentially high. Do not calculate `52 undigitised manuscripts`.

## 6. Current public-web stop rules

Move these to staff/catalogue export rather than further brute force:

- exact current 2024 Library classification hierarchy;
- complete nineteenth-century local periodical title/run/gap data;
- exact identities/current mapping/digitisation of the 66 manuscripts / 3 estates and current separately-listed collections/bequests.

## 7. Wedding manuscript correction — separate workstream

Authoritative branch: `ironlibrary-json-correction`.

Start from `PINNED_TRANSCRIPTION_RESUME.md`, then correction-branch `corrected_transcription/README.md` + `QUALITY_STATUS.json` + ledgers.

Coverage checkpoint: Mss 23 textual sequence through PDF 210; Mss 24 through PDF 65; next unprocessed sequential page 66.

Quality override: Mss 24 PDFs 1–65 = **`LEGACY_MIXED_EXTRACTION_REQUIRES_CLEANUP`**. Before continuing PDF 66, calibrate the corrected layered schema on a small mixed batch such as PDFs 56–60.

## 8. Repository hygiene

- One pin per active workstream.
- Determine recency from branch HEAD + pin, not filename date.
- Preserve legacy passes but subordinate them to current syntheses.
- On concurrent writes, refetch current blob SHA and merge; never force a stale overwrite.

Last reconciled after six-axis heat map, Tier-A carrier audit, Library large-block/evidence-regime maps and Library remote-substitutability audit: 2026-09-12.
