# Thomas Davies disambiguation — British Museum mineralogist vs Warrington microscopist

**Date:** 2026-09-08  
**Status:** repository authority note.

## Correction

Two nineteenth-century British microscopical actors named **Thomas Davies** must be kept separate.

### A. Thomas Davies, 1837–1892 — British Museum mineralogist

Identity:
- born 29 Dec 1837;
- British Museum Department of Mineralogy from 1858;
- trained by Nevil Story-Maskelyne in microscopic recognition of minerals in meteorite/rock thin sections;
- attended evening classes at the Working Men's College, Great Ormond Street, acquiring French and German;
- later 1st Class Assistant and practical petrologist.

Authority:
- NHM Archives `PX1373`;
- L. Fletcher obituary, *Mineralogical Magazine* 10 (1893), 161–164.

**Do not attribute *The Preparation and Mounting of Microscopic Objects* (1863) to this Davies.**

### B. Thomas Davies, c.1831–1876 — Warrington microscopist

Identity:
- resident of Warrington;
- active in the Microscopical Section of the Manchester Literary and Philosophical Society;
- specialist in crystallization/polarized-light microscopy and practical mounting;
- author of *The Preparation and Mounting of Microscopic Objects* (1863), expanded second edition 1873 edited by John Matthews.

Project Gutenberg now catalogues the author as `Davies, Thomas, 1831?-1876`.

Brian Stevenson's detailed disambiguation assembles the strongest public case: the 1873 preface identifies the author's residence as Warrington, Manchester microscopical-society reports name `Thomas Davies of Warrington`, and the extensive 1893 obituaries of the British Museum Davies do not attribute the mounting book to him.

Sources:
- https://www.gutenberg.org/ebooks/60225
- https://microscopist.net/DaviesT.html

## Direct periodical anchor for the Warrington Davies

Reports of the Manchester Microscopical Section explicitly identify **Thomas Davies of Warrington**. His work included crystallization under the microscope. A reported method placed a saturated salt solution on a **glass slide**, dried/fused the deposit, then allowed moisture to return while crystal growth was observed microscopically.

This places the Warrington Davies squarely inside practical glass-slide manipulation, but independently of the British Museum / Maskelyne / WMC biography.

## Why the confusion persists

The conflation is old and survives in modern metadata. Some Google Books records for the second edition still display the author as `Thomas Davies (of the British Museum.)`, while other records correctly describe him simply as the microscopist. Older biographical dictionaries helped establish the mistaken identification.

Repository rule:

```text
Thomas Davies + 1863 mounting manual / Warrington / Manchester microscopy
    = DAVIES_WARRINGTON_c1831_1876

Thomas Davies + British Museum / Maskelyne / meteorites / WMC / mineralogy
    = DAVIES_BM_1837_1892
```

No source or entity record may merge these identities merely because both practised microscopy and mineral/crystal work.

## Consequence for the current projects

### `slides_history_microscopy`

- The 1863 statement that ordinary glass slides were `almost always` 3 x 1 inches belongs to **Thomas Davies of Warrington**.
- The WMC + meteorite thin-section case belongs to **Thomas Davies of the British Museum**.

### `Henry_Clifton_Sorby`

`SLIDES_CORPUS_SORBY_CROSSWALK.md` currently uses `Thomas Davies's 1863 preparation manual` as a comparator for the dominant British 3 x 1 inch slide format. The factual statement is usable, but the author must henceforth be named **Thomas Davies of Warrington (c.1831–1876), not the British Museum mineralogist Thomas Davies (1837–1892)**.

A companion correction note should be added to the Sorby repository so later network analysis cannot silently identify the manual's author with Maskelyne's assistant.

## Evidential lesson

This is not a trivial prosopographical cleanup. The mistaken merger would manufacture a historically false chain:

`Working Men's College -> British Museum Davies -> mounting manual -> popular slide craft`.

The evidence instead gives two different forms of microscopy:

1. **British Museum Davies:** adult general education + occupational museum apprenticeship + thin-section mineralogy;
2. **Warrington Davies:** provincial microscopical society + experimental crystallization + codification of slide preparation techniques.

Keeping them separate preserves exactly the distinction this project is trying to study between educational institutions, workplaces, societies and preparation craft.
