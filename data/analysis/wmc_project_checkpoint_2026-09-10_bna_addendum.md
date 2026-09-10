# WMC / microscopy project checkpoint — BNA addendum, 2026-09-10

Updated: 2026-09-10
Status: `CHECKPOINT_ADDENDUM__CONTEMPORARY_PRESS_BRIDGE_ADDED__GENERAL_DISCOVERY_STILL_PAUSED`
Scope: same-day addendum to `wmc_project_checkpoint_2026-09-10.md` after ingest of the uploaded British Newspaper Archive preview export. This file changes only the statuses explicitly named below. All other stop rules and evidence boundaries in the main checkpoint remain in force.

Primary intake control: `data/analysis/wmc_bna_previews_intake_2026-09-10.md`.
Audit tables:

- `data/corpus/bna_working_mens_college_priority_previews_2026-09-10.csv` — 24 manually selected high-value rows with preview snippets and BNA locators.
- `data/corpus/bna_working_mens_college_science_previews_2026-09-10.csv` — 102 Great-Ormond-anchored science/materiality rows as a compact discovery index.

## 1. Status changes

### 1871 microscope practice

New status:

`WMC_MICROSCOPE_PRACTICAL_DEMONSTRATIONS_BY_1871 = CONTEMPORARY_EXTERNAL_PRESS_SECURE_AT_PREVIEW_LEVEL`

A syndicated October 1871 `LONDON CORRESPONDENCE` item states that practical microscope-demonstration classes were occasionally formed at the Working Men's College, Great Ormond Street. Multiple newspaper copies preserve OCR-near variants of the same passage.

This does not replace the 1861 internal curriculum control. It adds a different institutional format: occasional practical demonstration rather than only a scheduled course title.

### 1873 microscopical display

New status:

`WMC_MICROSCOPICAL_DISPLAY_AT_CONVERSAZIONE_1873 = CONTEMPORARY_PRESS_SECURE_AT_PREVIEW_LEVEL`

The *Globe*, 3 January 1873, reports a WMC conversazione in the new Great Ormond Street buildings whose programme included an `exhibition of microscopical...` material. The preview truncates the object description, so page-image inspection remains required before quoting or specifying what was exhibited.

### 1874 Natural History Society and Field Club

Previous working status: the 1873 Natural History Social/Society and Field Club line depended principally on later institutional/secondary reconstruction for existence and material practice.

Revised status:

- `WMC_NATURAL_HISTORY_SOCIETY_AND_FIELD_CLUB_EXISTS_BY_JAN_1874 = CONTEMPORARY_EXTERNAL_PRESS_SECURE`
- `WMC_FIELD_CLUB_MUSEUM_WORK_AND_SPECIMEN_MOUNTING_1874 = CONTEMPORARY_EXTERNAL_PRESS_SECURE`
- `WMC_FIELD_CLUB_FORMED_IN_1873 = RETROSPECTIVE_PRIMARY__CONSTITUTIVE_SOURCE_STILL_OPEN`

The *Academy*, 31 January 1874, identifies the Natural History Society and Field Club of the Working Men's College, Great Ormond Street and prints programme elements including H. G. Seeley's `The Method of Studying Geology` and `Museum work, Mounting Specimens, &c.` A second *Academy* notice, 13 June 1874, explicitly names the `Working Men's College Natural History Society and Field Club` and gives a recurring monthly `scheme of work` including lecture activity and repeated `Museum Work`.

The evidential gap is therefore narrower than in the earlier WMC notes. A constitutive 1873 source is still needed for exact formation date, constitution, officers, rules, and relation to earlier Sunday walking parties. It is no longer needed merely to establish that the named body existed and organized museum/specimen work by early 1874.

### 1894 microscopy

New status:

`WMC_MICROSCOPICAL_OBSERVATION_PUBLIC_LECTURE_1894 = CONTEMPORARY_PRESS_SECURE`

Press notices/reporting on 14–15 April 1894 place Charters White's lecture on `Microscopical Observation` at the Working Men's College. This is chronologically adjacent to the later internally reported 1893 Lubbock Field Club foundation but should not be assigned to the Club without explicit programme-level evidence.

### 1898–1900 laboratory planning

New status:

`WMC_LABORATORY_INFRASTRUCTURE_PUBLICLY_PLANNED_BY_1898 = CONTEMPORARY_PRESS_SECURE`

The 1898 building appeal explicitly includes a laboratory among WMC's stated needs; a 1900 Thomas Hughes memorial building scheme again includes lecture rooms and a laboratory. These notices provide an infrastructure prehistory for the `new Laboratory` documented internally in 1907–08, while exact construction/opening chronology remains open.

## 2. Revised first-order sequence

The longitudinal sequence now has additional contemporary external control between the already secure internal nodes:

`1861 differentiated curriculum`
→ `1869–70 museum/classroom building + botany/physiology`
→ `1871 occasional microscope practical demonstrations`
→ `1873 conversazione microscopical display`
→ `1874 named Natural History Society and Field Club + museum/specimen work`
→ `1893 Lubbock Field Club retrospective formation control`
→ `1894 public Microscopical Observation lecture`
→ `1898–1900 laboratory planning`
→ `1903–08 internal microscopy / museum / laboratory / field-club operations`.

The analytical object remains the changing institutional placement of microscopic and natural-historical practice across course, demonstration, display, museum, specimen preparation, field organization, public lecture and laboratory. The BNA pass strengthens the intermediate placements; it does not establish one continuous administrative lineage.

## 3. Acquisition consequence

`GENERAL_DISCOVERY = PAUSE` remains unchanged.

The 28,646-row BNA export should not be treated as a coherent London-WMC corpus. The phrase `working men's college` is institutionally noisy and OCR-sensitive. Reopen BNA only for named page-level targets that can change an explicit claim.

Highest-value page targets now are:

1. *Academy*, 31 Jan. 1874, BNA `BL/0006027/18740131/078` — complete the February programme after `Feb. 17`.
2. *Academy*, 13 Jun. 1874, BNA `BL/0006027/18740613/064` — complete `Museum Work (naming...` and recover any excursion/officer details.
3. *Globe*, 3 Jan. 1873, BNA `BL/0001652/18730103/015` — resolve the object after `exhibition of microscopical...`.
4. One clean October 1871 syndicated copy — fix exact wording and context for the practical microscope-demonstration statement.
5. *Lloyd's Weekly Newspaper*, 15 Apr. 1894, BNA `BL/0000079/18940415/120` — inspect the full Charters White lecture report.

No broader newspaper acquisition is required before writing.