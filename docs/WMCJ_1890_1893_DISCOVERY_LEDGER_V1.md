# WMCJ 1890–1893 discovery ledger v1

**Date:** 2026-09-09  
**Branch:** `research/working-mens-microscopy-19c`  
**Purpose:** control the immediate pre-/formation-period search for the Lubbock Field Club and botanical-walk material in *The Working Men's College Journal* without back-filling missing primary pages from the 1904 retrospective history.

## Governing question

Recover contemporary WMCJ evidence for:

- botanical walks under Alfred Grugeon;
- formation/name of the Lubbock Field Club;
- Alfred Grugeon as President;
- A. E. Shurlock as Secretary;
- first programme / excursions / meetings;
- microscope / microscopic observations;
- specimen exhibition;
- natural-history club reporting.

## 1. What is already closed outside the target window

### Journal launch

Secondary research gives *The Working Men's College Journal* as beginning in **February 1890**.

### 1904 WMC retrospective

R. H. Marks's `The College Clubs` says College Journal(s) recorded botanical walks under Alfred Grugeon before the new Lubbock Field Club, and later explicitly points readers to the Journal as evidence of the Club's activity since formation.

Thus:

`WMCJ_DOCUMENTATION_LOOP_EXISTENCE = CLOSED_RETROSPECTIVE`

but

`CONTEMPORARY_ENTRY_EXTRACTION = OPEN`

### Founding-date conflict

Current states:

- 1904 WMC OCR: March 1892, but with internal `1890 -> following year -> 1892` anomaly;
- Peter Ayres: Grugeon retired in 1892 and became President of the newly formed Club;
- Marcella Sutcliffe: club established in 1893, archive ref `LMA 4535/E/02/06/001`.

Do not normalize.

## 2. Current direct-web search result

Repeated exact-phrase and actor searches for:

- `Working Men's College Journal` + `Lubbock Field Club` + 1892 / 1893;
- `Working Men's College Journal` + `Grugeon`;
- `botanical walks` + WMC;
- `Lubbock Field Club` + `A. E. Shurlock`;
- `Lubbock Field Club` + `Alfred Grugeon`;

have **not** produced directly readable 1890–93 WMCJ issue pages in the current public search index.

State:

`INDEX_ACCESS_GAP / PRIMARY_VOLUME_NOT_YET_LOCATED`

This is not evidence that the entries do not exist; the 1904 WMC history explicitly says they do.

## 3. Volume chronology anchors

### Volume III — hard bibliographic anchor

Bookseller/auction records independently identify:

> *The Working Men's College Journal. Conducted by Members of the College. Volume III, 1894–95.*

Published by Working Men's College, London, 1895.

A surviving copy description gives:

- **292 pages** of main text;
- additional sections of **reports, examination papers, and accounts reports**;
- octavo-size bound volume.

Evidence state:

`CLOSED_BIBLIOGRAPHIC_PHYSICAL_DESCRIPTION`

This is highly relevant to RSVP materiality because the bound Journal volume demonstrably contains institutional matter beyond ordinary article pages.

### Volume V — 1898 anchor

Scholarly citations give:

- vol.5 no.75, Feb 1898;
- vol.5 no.76, Mar 1898;
- vol.5 no.77, Apr–May 1898.

### Volume X — 1907 anchor

Digitized Google/Play volume:

- vol.10, issues 167–188;
- Jan 1907 volume metadata;
- title says `Conducted by Members of the Working Men's College, London`.

## 4. Do not infer Volume I / II dates mechanically

Volume III = 1894–95 strongly suggests Volumes I–II cover the earlier 1890–94 run, but exact boundaries must not be invented from arithmetic.

Potential causes of irregular boundaries:

- launch in February 1890;
- combined issues;
- irregular publication frequency;
- volume boundaries not aligned to calendar years;
- later rebinding / cataloguing.

Therefore:

`VOL_I_DATE_RANGE = PENDING`

`VOL_II_DATE_RANGE = PENDING`

## 5. External contemporary press search

Exact web searches for `Lubbock Field Club` in 1892–93 and combinations with:

- Working Men's College;
- Great Ormond Street;
- Grugeon;
- A. E. Shurlock;

have not yet produced a contemporaneous 1892/93 newspaper or journal notice in the open index.

Current strongest date witnesses remain:

1. 1904 WMC self-history;
2. Ayres's 1892 biographical reconstruction;
3. Sutcliffe's 1893 archival-reference reconstruction.

State:

`CONTEMPORARY_FORMATION_NOTICE = NOT_YET_RECOVERED`

This should become a BNA/full-access target rather than being forced through generic web search indefinitely.

## 6. LMA archival reference

Exact web search for `4535/E/02/06/001` currently returns Sutcliffe's citation but not an independent catalogue title/type/date.

State:

`LMA_ITEM_REFERENCE_EXACT / CATALOGUE_METADATA_NOT_WEB_RECOVERED`

Do not call it rules/minutes/prospectus until catalogue or item inspection.

## 7. Search matrix for physical / catalogue discovery

Priority identifiers:

- title exact: `The Working Men's College Journal`;
- publisher: Working Men's College, London;
- `Conducted by Members of the College`;
- Volume I / Volume II;
- date range 1890–1894;
- likely institutional holdings: WMC/LMA, British Library, Guildhall/Goldsmiths-related collections, major research libraries;
- bound-volume catalogue descriptions;
- auction/bookseller copies as secondary physical controls.

Once a volume is found, extract:

`volume | issue no. | issue date | printed page | title/heading | genre | actor | club | science term | pre/post event | report/notice | binding section | source state`

## 8. RSVP consequence

The unresolved WMCJ 1890–93 window is now a clearly bounded grant target, not a vague research wish.

The grant-funded physical/holdings survey should prioritize:

1. Volume I–II bibliographic boundaries;
2. botanical-walk entries immediately before Club formation;
3. first Lubbock Field Club notice/report;
4. officer list with Grugeon/Shurlock;
5. first stated objects/rules/programme;
6. specimen/microscope language;
7. reports/examination/account sections bound outside ordinary Journal pagination;
8. wrappers, contents, supplements, advertisements and institutional inserts.

## Stop rule

Do not convert the 1904 retrospective statement into invented 1892/93 WMCJ page citations. Do not infer volume boundaries from Volume III arithmetic. Do not call failure of public indexing a negative corpus result. Current state is **primary-volume access gap with retrospective existence proof**.
