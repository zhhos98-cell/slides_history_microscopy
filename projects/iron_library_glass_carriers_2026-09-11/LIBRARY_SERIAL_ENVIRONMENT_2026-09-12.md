# Iron Library nineteenth-century serial environment

**Date:** 2026-09-12  
**Status:** ACTIVE LIBRARY-LEVEL CENSUS  
**Rule:** this is a holdings map, not a bibliography for a preselected topic.

## 1. Why serials are a collection block

Current official description: c.1,000 periodicals in the Iron Library, c.70 current. A historical profile described periodicals/series as roughly one third of the holdings, with around 700 periodical titles and many long/complete sequences; the historical-book census identifies **123 nineteenth-century periodical titles**.

A useful later cataloguing snapshot sharpens the scale: the Iron Library annual report for 2022 states that, on 31 December 2022, its catalogue contained **1,178 periodicals**, alongside 37,534 books, 9,885 articles and 134 online resources. The same report confirms that the Iron Library catalogues its holdings in the Southwest German Library Network (SWB) and that its holdings have also been represented in WorldCat since 2021.

For c.1850–1885, serials should therefore be treated as one of the Library's largest coherent research environments, not as individual journals selected around an author.

## 2. Critical distinction: publication run != Iron Library holding run

For every periodical record, keep separate fields for:

- `TITLE`
- `PUBLICATION_RUN`
- `IRON_LIBRARY_SHELFMARK`
- `IRON_LIBRARY_HOLDING_RUN`
- `RUN_COMPLETENESS`
- `LANGUAGE`
- `DISCIPLINARY_ORIENTATION`
- `ACQUISITION/PROVENANCE_NOTE` where known

Do not infer holding completeness from the historical publication dates of a journal.

Example: an Iron Library annual report describes the London *Mechanics' Magazine* as a rich research resource and notes that the periodical appeared 1823–1873; a separate Iron Library 'favorite book' page displays the bibliographic sequence `1.1823 - 69.1858`. Until IRONCAT's detailed holding statement is controlled, do not convert the publication end date 1873 into a claim that the Iron Library holds every volume through 1873.

By contrast, the official acquisition page explicitly states that the Iron Library now holds the **complete run** of the *Register of the Arts and Sciences*, published fortnightly 1823–1827.

## 3. Controlled nineteenth-century serial anchors

The following titles are explicitly documented by Iron Library / collection descriptions. They are anchors for reconstructing the larger serial environment, not a final shortlist.

| Title | Publication / described run | Iron Library status currently controlled | Structural role |
|---|---|---|---|
| *Dinglers Polytechnisches Journal* | 1820–1931 | explicitly named as a major Iron Library historical serial; exact issue completeness still to control | broad polytechnical / industrial information environment |
| *Annales des Mines* | nineteenth-century long run; official/historical descriptions name it as a core serial | explicitly held; exact library run/completeness to control | mining, metallurgy, geology, state technical knowledge |
| *Journal of the Iron and Steel Institute* | from 1871 | explicitly named as Iron Library serial | specialized iron/steel institutional science |
| *Stahl und Eisen* | from 1881 | explicitly named; later donations also added/backfilled holdings | specialized German iron/steel industrial-scientific communication |
| *Mechanics' Magazine* | publication 1823–1873 | Iron Library shelfmark `Per 254`; bibliographic page displays `1.1823–69.1858`; full holding endpoint OPEN | British engineering / invention / industrial information |
| *Register of the Arts and Sciences* | 1823–1827 | official page explicitly says complete run now in collection | broad invention/science/industry serial; early-century control |
| *Eisen-Hütten-Magazin* | from 1791 | Iron Library shelfmark `Per 27`; part of Johann Conrad Fischer book-context page | predecessor/early specialist metallurgical serial environment |

## 4. What the currently controlled anchors already show

Without selecting a research problem, the serial architecture visibly changes across the nineteenth century:

### Broad polytechnical / improvement press

Early-century holdings such as *Mechanics' Magazine*, *Register of the Arts and Sciences* and *Dinglers Polytechnisches Journal* organize industrial knowledge across inventions, machinery, chemistry, civil engineering and practical science.

### Mining / state technical science

*Annales des Mines* supplies a long specialist mining/metallurgical/geological axis with strong institutional connections.

### Specialized iron/steel institutional serials

By the later nineteenth century, *Journal of the Iron and Steel Institute* (from 1871) and *Stahl und Eisen* (from 1881) mark a much more specialized iron/steel communication environment.

This broad-to-specialized chronology is a **collection structure to test**, not yet a thesis.

## 5. Acquisition history matters

The present serial landscape is not identical to what the Iron Library possessed when it was founded or at any earlier date. Later donations have thickened/backfilled technical-journal holdings. Official donation records include, among others:

- 2003: Stadtbibliothek Schaffhausen — *Stahl und Eisen*;
- 2006: Maschinenfabrik Rieter AG — journals in materials engineering, metallography/material science, foundry and materials testing;
- 2006: Rudolf Burkolter — steel/iron, iron research, metallurgy and foundry journals;
- 2007: Vreni Nadig — *Stahl und Eisen*;
- 2014: George Mourlon — French foundry journals;
- 2019: GF Casting Solutions — foundry journals;
- later donations continue to add technical serials.

Therefore present completeness can be the product of **retrospective collecting**. This does not reduce research value, but it means the Library serial environment must be described as a present specialist collection, not naïvely as one historically contemporaneous institutional reading room.

## 6. Union-catalog recovery route now controlled

The serial corpus is not limited to manual browsing in IRONCAT.

### Institutional identity

The Iron Library's institutional identifier is:

- **ISIL: `CH-000728-7`**

The Library's own annual reports confirm participation in SWB; K10plus is the successor/common union-catalog environment for these data, and the holdings are also represented in WorldCat.

### ZDB route

The German Zeitschriftendatenbank (ZDB) documentation explicitly states that researchers can retrieve the periodical titles associated with one institution by choosing the **ISIL** index and entering the institution's ISIL. Its CQL documentation exposes at least these useful indices:

- `isil` — institution identifier;
- `eje` — first publication year;
- `ejl` — last publication year;
- `tit` / `tst` — title fields;
- `sgn` — shelfmark;
- `bbi` — holding institution.

ZDB also exposes a JSON API (`/api/tit.jsonld`) with pagination.

**Practical implication:** a machine-assisted census by `CH-000728-7` is technically plausible. The current browsing/runtime path has not yet yielded a clean parse/export of the institution-filtered result set, so no complete title list is claimed here. Do not replace this limitation with guessed titles.

### Recovery target

The desired export table should contain at minimum:

`ZDB_ID | TITLE | PUBLICATION_FIRST_YEAR | PUBLICATION_LAST_YEAR | IRON_LIBRARY_HOLDING_STATEMENT | SHELFMARK | LANGUAGE | NOTES`

Then filter/inspect for titles whose actual holdings intersect 1800–1900, rather than filtering only by journal publication history.

## 7. Classification PDFs: controlled existence, contents not yet harvested

The current Library page exposes two 2024 downloads:

- `Systematik des Bibliotheksbestands`
- `Systematik des Rarabestands`

Their existence is controlled from the official page. Automated retrieval currently returned a cache miss, so their internal classification hierarchy has **not** yet been harvested in this pass. Do not invent class labels from expectation.

## 8. Current claim ceiling

Secure:

- current Library description: c.1,000 periodicals;
- 2022 catalogue snapshot: 1,178 periodicals;
- historical census identifies 123 nineteenth-century periodical titles;
- serials are a major systematic collection block;
- the named anchor titles above are documented holdings;
- *Register of the Arts and Sciences* is explicitly described as complete;
- later donations materially shape present serial depth;
- SWB/K10plus/WorldCat provide external union-catalog infrastructure for the holdings;
- ZDB documentation supports institution-level serial retrieval by ISIL, and the Iron Library ISIL is `CH-000728-7`.

Not yet secure:

- complete list of all 123 nineteenth-century titles;
- exact holding run/completeness for *Dinglers*, *Annales des Mines*, JISI, *Stahl und Eisen*, *Mechanics' Magazine*, or other anchors unless separately stated;
- full language distribution;
- exact disciplinary distribution;
- whether microscopy/material-testing serials form a distinct nineteenth-century cluster;
- whether the ZDB institution result reproduces every Iron Library serial record present in SWB/IRONCAT without omissions.

## 9. Next Library-level actions

1. Recover/export the institution-level serial result set using ISIL `CH-000728-7` through ZDB/SWB/K10plus/WorldCat, preferring a reproducible holdings export over manual title searches.
2. Reconcile that result set against the historical statement of 123 nineteenth-century titles; differences may reflect later acquisitions, cataloguing changes or title/series splitting.
3. Record actual holding statements and gaps for every title whose holdings intersect 1800–1900.
4. Code title-level broad orientation without topic cherry-picking: `polytechnical`, `mining/geology`, `metallurgy/iron-steel`, `mechanical/civil engineering`, `chemistry/physics`, `materials/testing`, `microscopy/optics`, `trade/industry`, `other`.
5. Plot first-year / last-year / completeness by category and language.
6. Only after that plot exists, test whether early materials microscopy appears as a natural concentration rather than a researcher-imposed keyword cluster.

## Official/public sources controlled in this pass

- Iron Library current Library page: https://www.eisenbibliothek.ch/de/ressources/library.html
- Iron Library Annual Report 2022: SWB/WorldCat cataloguing context and 1,178-periodical snapshot.
- Iron Library digital resources page: IRONCAT / WorldCat access.
- Iron Library, Register of the Arts and Sciences: https://www.eisenbibliothek.ch/de/ressources/recent-aquisitions/register.html
- Iron Library, favorite book episode on Mechanics' Magazine: https://www.eisenbibliothek.ch/de/research/favorite/episode13.html
- Iron Library donations: https://www.eisenbibliothek.ch/de/ressources/donations.html
- Iron Library Johann Conrad Fischer books: https://www.eisenbibliothek.ch/de/ressources/library/jcfbooks.html
- ZDB WebCat documentation: institution holdings can be searched by ISIL.
- ZDB CQL index documentation and JSON-API documentation.
- historical collection overview quoted in Kultur & Technik 2006, including major serial examples.
