# Nineteenth-Century Microscope Slides

**GitHub Pages:** https://zhhos98-cell.github.io/slides_history_microscopy/

Standalone research repository for the global nineteenth-century microscope-slide survey, its surviving-object/provenance catalogue, derived analytical layers, and object-to-text corpus expansion work.

This repository was separated on 2026-08-09 from the former `slide-survey-actions-pilot` branch of `zhhos98-cell/Blachka_corpus`. From this migration onward, **this repository and its `main` branch are the canonical home of the microscope-slide project**. The Blaschka project is not part of this repository.

## Frozen global survey — 2026-08-09

- Status: **CLOSED_2026-08-09**.
- Spatial scope: global.
- Historical scope: **1800–1899**.
- Frozen canonical discovery layer: **307 unique collection/subcollection/batch/database entries**.
- Frozen strict nineteenth-century layer: **155 entries**.
- Strict data batches: `07K`–`07AQ`.
- `07AR` is closure/audit metadata only and adds no discovery rows.
- Raw modular ledger immediately before closure canonicalisation: **328 rows**.
- The raw-to-canonical difference is explained by 20 superseded alias IDs plus one repeated Hubrecht `entry_id` occurrence.
- Pieter Harting remains in discovery as `POSSIBLE_19C` and is outside the strict 155.

The human-readable closure audit is `data/survey/07AR_CLOSURE_AUDIT_2026-08-09.md`. The machine-readable alias map is `data/survey/07AR_SUPERSEDED_ALIASES_2026-08-09.json`; the closure manifest is `data/survey/07AR_CLOSURE_MANIFEST_2026-08-09.json`; final catalogue QC is recorded in `data/survey/07AR_FINAL_QC_2026-08-09.md`.

**New discoveries do not silently extend this frozen version.** Any substantive addition to the census requires an explicit reopening/new version.

### Executable frozen membership

`scripts/build_frozen_strict_membership.py` reconstructs membership directly from the frozen `07K`–`07AQ` strict batches and applies the `07AR` closure rules. It removes twenty superseded distinct-ID aliases, collapses the repeated same-ID Hubrecht occurrence, applies the Harting demotion, asserts the closure arithmetic `177 → 155`, and writes the downstream active-ID set.

`scripts/audit_19c_scope.py` remains useful as a diagnostic classifier over the larger discovery layer. Its heuristic `CORE_19C` output is **diagnostic only** and cannot enlarge the frozen census. `scripts/apply_19c_scope.py` uses the closure-derived 155 active IDs.

## Research method

The survey works backwards from surviving microscope slides, preparations, sets, cases, cabinets, numbered series, institutional records and current collection catalogues. The textual/event corpus works forwards from journals, catalogues, archives, correspondence, advertisements, society proceedings and institutional documentation. The two sides are designed to meet at explicit historical relations.

Core rule: **current museum custody is not historical ownership**. Preserve source relations such as `prepared by`, `mounted by`, `collected by`, `assembled by`, `used by`, `sent to`, `received by`, `exchanged by`, `presented to`, `donated by`, `purchased by`, `sold by`, `distributed by`, `lent by`, `transferred from`, `from the collection of`, `belonging to`, `held by`, `catalogued by`, `digitised by`, `labelled/inscribed by`, `part of`, and `from the period of` as distinct claims whenever the source distinguishes them.

Quantity namespaces also remain separate. A slide count, microscopic-preparation count, specimen count, serial-set position, historical inventory state, current surviving total, box/tray/drawer count, cabinet capacity, catalogue/accession/register number, database row, image count and mixed-period aggregate are not interchangeable. Serial endpoints and register ranges are never converted into physical-slide totals without explicit evidence.

## Repository structure

### Survey and closure

- `data/survey/07A_Global_Microscope_Slide_Collections_Survey.csv` — canonical runtime survey input.
- `data/survey/07B_*` onward — modular discovery/expansion batches retained as the audit trail.
- `data/survey/07AR_SUPERSEDED_ALIASES_2026-08-09.json` — frozen duplicate-alias map.
- `data/survey/07AR_CLOSURE_MANIFEST_2026-08-09.json` — closure arithmetic and frozen counts.
- `data/survey/07AR_FINAL_QC_2026-08-09.md` — final sealed-catalogue QC.
- `data/survey/scope_19c_overrides.json` — conservative temporal/medium overrides.
- `data/survey/site_adapters*.json` — site-specific extraction adapters.
- `data/survey/harvest_families*.json` — shared extraction contracts.
- `data/survey/institution_harvest_profiles.json` — institution/fallback harvest profiles.

### Evidence and analysis

- `data/evidence/targeted_deep_4/` — final targeted-harvest evidence normalization and manual residuals; enrichment only, never census reopening.
- `data/analysis/slide_155_analysis_v1/` — read-only analytical classification layer over the 155 surviving-object/provenance nodes.
- `data/analysis/slide_155_corpus_expansion_v1/` — object-to-text routing, verified bridges, source targets, Naples catalogue parsing, and circulation crosswalks.

### Documentation and scripts

- `docs/19C_SCOPE_RULES.md` — nineteenth-century scope rules.
- `docs/SLIDE_SURVEY_PRIORITY_RULES.md` — survey/priority rules.
- `docs/BIBLIOGRAPHY_PASS12_FRANCE_BELGIUM_AUSTRIA_2026-08-10.md` — pass-12 bibliography audit and exclusions.
- `docs/BIBLIOGRAPHY_PASS13_COLONIAL_TROPICAL_MEDICINE_2026-08-10.md` — pass-13 colonial/tropical-medicine material-object audit and exclusions.
- `scripts/prepare_survey_inputs.py` — merges modular inputs while applying frozen alias handling.
- `scripts/build_frozen_strict_membership.py` — rebuilds and asserts the immutable 155-entry membership.
- `scripts/export_frozen_catalogue.py` — exports the sealed 155-row catalogue and manifest.
- `scripts/build_slide_analysis_layer.py` — builds the derived analysis layer.
- `scripts/validate_survey.py` — validates survey schema and evidential language.
- `scripts/audit_19c_scope.py` — diagnostic temporal/medium classifier.
- `scripts/apply_19c_scope.py` — restricts runtime processing to the frozen membership.
- `scripts/build_harvest_batches.py` — builds nineteenth-century harvest batches.
- `scripts/build_institution_matrix.py` — builds institution-level Actions matrices.
- `scripts/harvest_catalogue.py` — bounded catalogue metadata harvesting.
- `scripts/harvest_institution.py` / `scripts/harvest_targeted.py` / `scripts/harvest_targeted_institution.py` — institution and targeted adapters.
- `scripts/aggregate_institution_harvest.py` — combines per-institution outputs.
- `scripts/normalize_targeted_deep_artifact.py` — normalizes the final targeted-deep artifact.

## Harvesting status

General reconnaissance/enumeration is complete for the frozen version. Four manual workflow runs tested and narrowed the public-metadata harvesting strategy. Run #4 (`31287016342`) was the final `targeted-deep` pass in the predecessor repository. Its overall GitHub conclusion was `cancelled` because the Sorbonne branch was interrupted, while the combined artifact was successfully produced for seven completed institutions. The useful normalized evidence is retained under `data/evidence/targeted_deep_4/`; the partial Sorbonne output is intentionally ignored.

High-value structured evidence includes Copenhagen's 510 unique SNM slide identifiers, the Farlow/Cheever position tables, and the St Andrews hierarchy. ANSP Symbiota output is retained as a review pool because its nominal pre-1900 filtering returned later material. No further general-purpose crawling is recommended for the closed version.

## Derived 155 analysis layer

The frozen catalogue is treated as a **read-only object/provenance corpus**. Analytical fields live in a separate layer and never rewrite the source wording or frozen membership.

The first derived layer classifies nodes by unit level, production period, subject cluster, institutional/commercial context, circulation mode, count namespace and historical actor role. It is intended to support comparative research without pretending that single slides, bounded sets, cabinets, named collections and mixed-period institutional layers are commensurable counts.

## Slide-locked bibliography — pass 13 (2026-08-10)

The public bibliography is now at **`slide-locked-pass-13`**: **135 verified entries**, comprising **74 research/collection/conservation studies** and **61 historical primary/object records**, across **11 publication languages**. The machine-readable source of truth is `bibliography/bibliography-manifest.json`; the row data are split across `bibliography-01.csv` through `bibliography-15.csv`. The Pages bibliography reads the manifest dynamically and exports CSV, TSV, JSON, CSL JSON, BibTeX and RIS from the same rows.

The admission rule remains deliberately narrow: **physical slide first**. A source enters only when microscope slides, slide-mounted preparations, their mounting/material system, a dedicated preparation catalogue/series, a surviving slide collection, a preparation-centred register/file, or a direct transfer/request for slides does substantive evidentiary work. General microscopy histories, laboratory regulations, instrument histories, disease reports and broad manuals remain outside the bibliography when preparations are only incidental.

Pass 10 added institutional catalogue/register and surviving-object layers: the Bailey collection catalogue, the Army Medical Museum Microscopical Section III logbook, Arthur C. Cole & Son's 1867 commercial slide case, the Frank Horrocks collection record, and the Manchester Gibson collection study.

Pass 11 is a deliberately large German-speaking trade, production and teaching module. It reconstructs a dated commercial sequence rather than collecting generic microscopy literature. Möller's specialist price lists of 1877, 1883, 1889 and 1897 are treated as changing states of a preparation business and extend the already-listed 1868 catalogue. Eduard Kaiser's 1877 Institut für Mikroskopie advertisement and surviving address-labelled preparations create a commerce-to-object bridge. Klönne & Müller are anchored by their 1879 advertisement for `Duncker'sche` preparations and their 1885 catalogue distinguishing `Einzelpräparate`, `Sammelpräparate`, `Test-platten`, `Typenplatten` and `Salonpräparate`. Otto Bachmann's 1880 Landsberg catalogue supplies school-use rationale, slide formats, labelling, protective packaging, approval shipments, replacement terms and category prices. Ludwig Klein's two 1888 papers add an explicitly slide-making technical sequence for freshwater-algae permanent preparations. Möller's 1891 phototype atlas and 1892 species index close a particularly strong physical preparation → plate publication → textual index system. Modern object scholarship adds Andreas Heller's reconstruction of Hermann Welcker's rediscovered Halle preparation collection and Beate Kunst's object-history of Virchow-associated Trichinella slides.

Pass 12 completed a France/Belgium/Austria module with 19 additional verified records. The French layer reconstructs professional preparation as a changing market through Bourgogne, Marchand and Tempère; the Belgian layer adds Delogne, Van Heurck & Grunow and Drosten; the Austrian layer begins with Ferdinand I's surviving preparations and closes with modern reconstruction of Albert Grunow's Vienna collection and handwritten catalogue. Full pass-12 inclusion/exclusion notes are in `docs/BIBLIOGRAPHY_PASS12_FRANCE_BELGIUM_AUSTRIA_2026-08-10.md`.

Pass 13 adds **8 verified colonial/tropical-medicine material-object records** without admitting tropical-medicine literature merely for geographic coverage. The India layer begins with the British Library's 1851 India Office file `Wax models of diseases of the skin and microscopic preparations` and D. D. Cunningham's 1873 Calcutta air study, where the microscopic glass support participates in particle collection. Patrick Manson's 1879–1883 `Scientific artefacts` series contributes a surviving set of slides and glass vials while preserving the catalogue's uncertainty about individual contents and locality.

The strongest chain is Ronald Ross: LSHTM identifies his surviving malarial slides as originals created in India during the research culminating in the 1897 mosquito-malaria discovery; Patrick Wilkins O'Gorman's 1903 letter asks Ross for a dozen Romanowsky-stained malarial blood slides, making preparations visible as requested and transferable medical objects; LSHTM's 2016 re-examination of the nineteenth-century box recovered still-legible oocysts, gametocytes and historical staining. The module therefore closes a research-object → circulation request → archival custody → modern re-observation sequence.

The afterlife layer adds the Wellcome Historical Medical Museum's 1958 exhibition record for apparatus and microscope slides belonging to Timothy Lewis and the Science Museum Group's surviving J. C. Wagner cabinet, made in Johannesburg and Llandough and including original histological material associated with the 1960 asbestos/mesothelioma case series. These records keep museum survival separate from historical preparation place when the catalogue does not support the latter.

This pass also records a comparatively low yield from broad African and Indian medical searching. Lewis and Cunningham cholera reports, Hyderabad Medical School records, Ross photographs/lantern derivatives, Dutton and Todd drawings from African spirochaete slides, Donovan watercolours, and generic malaria/sleeping-sickness expedition literature were screened but excluded where the verified record did not put the physical slide itself at the centre. Full inclusion/exclusion notes are in `docs/BIBLIOGRAPHY_PASS13_COLONIAL_TROPICAL_MEDICINE_2026-08-10.md`.

Current search frontier: **East and Southeast Asian institutional collections**, especially Japan, China, Hong Kong and Singapore; residual South Asian pathological museums and named preparation cabinets; and residual African slide-register/object searches. The threshold stays unchanged: geographic balance is not produced by admitting sources that merely mention microscopic preparations.

## Object-to-text corpus expansion

`data/analysis/slide_155_corpus_expansion_v1/` uses the surviving-object corpus to decide what textual material is worth reading or adding next. Early bounded verification produced object↔text bridges for Theodor Eulenstein, Charles Collins Jr., Hamilton Lanphere Smith, Frederic Kitton, and the Stazione Zoologica Napoli / Fritz Meyer preparation programme.

The working principle is bidirectional:

- **text → object**: a historical source records manufacture, sale, exchange, use, gift, transfer or exhibition; surviving objects are sought;
- **object → text**: a surviving node supplies actors, dates, series names, taxa or relations that generate bounded textual searches.

Positive OCR/name matches are routing signals only until the actual historical context is read.

## Naples 1880 catalogue module

The Naples microscope-slide price catalogue in *Mittheilungen aus der Zoologischen Station zu Neapel*, Bd. II, is signed **Neapel, August 1880**. Its numbered list contains **423 historical catalogue offerings**. `423` is an offering count, not a surviving-slide total.

The uploaded primary text was parsed at row level. Historical major-group counts are Protozoa 4, Coelenterata 33, Echinodermata 49, Vermes 33, Arthropoda 57, `Mollusca` in the source classification 54, and Vertebrata 193. Price extraction remains deliberately partial: 148 row prices are securely aligned and 275 remain unresolved where OCR detached or reordered table columns.

The catalogue establishes Fritz Meyer as director/organizer of the preparation department. It does **not** establish that he personally prepared every one of the 423 offerings.

### Naples → Britain circulation

The bounded UK crosswalk currently records **eleven distinct object/specimen circulation or exhibition events**, plus separate catalogue-reception and method-circulation evidence. It distinguishes finished-slide circulation, preserved/biological specimen circulation, British remanufacture of Naples specimens, and circulation of preparation methods.

A reverse taxon/preparation pass produced the first item-level catalogue-to-Britain closure. For the **9 June 1880 Royal Microscopical Society** shipment:

- `R24204`, JRMS p. 733 records `Zoological Station of Naples—12 slides`, sent through A. W. Waters and exhibited under microscopes;
- `R24207`, JRMS p. 736 lists the twelve physical slides individually.

Comparison with the 423 offerings yields **nine exact/strong item matches**: `42, 43, 67, 68, 71, 72, 86, 182, 186`.

Three further slides remain bounded: `5|6`, `43–49`, and `231|232`.

The row-level mapping is `data/analysis/slide_155_corpus_expansion_v1/NAPLES_1880_RMS_12_SLIDES_ITEM_CROSSWALK_V1.csv`.

This is a defensible `catalogue offering → named British physical slide shipment/exhibition` closure. It does **not** establish that any of those 1880 RMS slides is the same physical object as a surviving St Andrews slide. That third identity point remains `NOT_ASSERTED`.

The same audit separates the February 1883 Zoological Society Bell event from the 14 March 1883 RMS nineteen-slide event, and preserves later source language such as `preserved specimens` and `Marine Objects` without silently converting it into slide status.

A compact research log is maintained at `data/analysis/slide_155_corpus_expansion_v1/PROGRESS_LOG_2026-08-09.md`.

## GitHub Actions

The standalone repository keeps Actions as reproducible infrastructure, not as a mandate for further crawling:

- `slide-survey` — validation/planning over the frozen survey.
- `slide-export-frozen-catalogue` — reproduces the sealed 155-entry catalogue and membership audit.
- `slide-institution-harvest` — bounded institution metadata harvesting retained for explicit future research uses.

All workflows operate on this repository's `main` branch. They no longer depend on the predecessor repository or the former `slide-survey-actions-pilot` branch.

## Closure discipline

The `07AR` audit identified twenty distinct-ID rediscoveries of already catalogued nodes and one same-ID repeated Hubrecht occurrence. These are canonicalized rather than counted twice. Parent/child structures, distributed copies, bounded subseries and separate custody nodes remain distinct where they represent different physical or evidentiary relations.

Held-out cases remain held out unless a later version explicitly reopens them. Pieter Harting remains discovery-only; Walther Flemming is excluded because the relevant Kiel preparations were reported lost in 1944; KCL's generic historical-slide lead remains unresolved; the named Dawes cabinets are twentieth-century; Perroncito remains unclosed at object level.

The frozen state is therefore:

**307 discovery nodes / 155 strict nineteenth-century nodes — CLOSED_2026-08-09.**
