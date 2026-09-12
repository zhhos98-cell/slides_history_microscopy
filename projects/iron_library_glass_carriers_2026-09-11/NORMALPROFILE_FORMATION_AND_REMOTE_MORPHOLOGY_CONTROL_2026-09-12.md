# Normalprofile formation and remote morphology control

**Date:** 2026-09-12  
**Status:** TARGETED REMOTE CONTROL / ONSITE RECOGNITION AID  
**Purpose:** define what to look for in `EBA 4/14 Profileisenalbum` without assuming in advance that the albums contain formal Normalprofile.

## 0. Result

The 1879–81 German Normalprofil episode should be treated as a **market-data-mediated reduction of pre-existing profile heterogeneity**, not as a standard imposed on an otherwise unstructured field.

This sharpens the Küderli test. The onsite question is not merely:

> does `EBA 4/14` contain Normalprofile?

It is:

> **what kind of comparison system is present on each layer of the album, and does its morphology change as formal Normalprofile are being constructed and disseminated?**

---

## 1. Formation process: formal standardization absorbed market evidence

A historical account in *Deutsche Bauzeitung* records the following sequence:

- on 7 April 1878, civil engineer Scharowsky proposed that the Verband deutscher Architekten- und Ingenieur-Vereine take up the establishment of Normalprofile for rolled iron;
- Intze separately addressed Normalprofile for I-beams;
- a joint process with the Verein deutscher Ingenieure followed;
- the commission circulated **eight questionnaires to German rolling works** to obtain statistical evidence on sales of individual `Façoneisen`, explicitly to learn demand and their relative importance;
- profile families were then assigned to referees/co-referees for technical work.

Remote OCR source:
- *Deutsche Bauzeitung* digitized volume, searchable result: https://upload.wikimedia.org/wikipedia/commons/7/73/Deutsche_Bauzeitung_%28IA_bub_gb_sprmAAAAMAAJ%29.pdf

A separate VDI historical account confirms that Intze's 1878 Normalprofile intervention and the architects'/engineers' association initiative led to the joint committee.

Remote OCR source:
- historical VDI volume: https://repozytorium.biblos.pk.edu.pl/redo/resources/37495/file/scans/DEFAULT/OCR_rezultaty/100000300181_A_v1_200dpi_q60.pdf

### Consequence

The formal normal-series project was itself trying to convert dispersed producer/market variety into a reduced set. Therefore **merchant albums, producer profile books, sales evidence and formal standards belong to adjacent but non-identical information layers**.

The relevant sequence is:

`PRODUCER PROFILE VARIETY -> MARKET/SALES OBSERVATION -> TECHNICAL SELECTION -> NORMAL SERIES -> PRODUCER/MERCHANT/USER UPTAKE`.

Küderli may preserve evidence on both sides of the formal selection event.

---

## 2. What a late-1870s profile universe looked like

Near-contemporary reference literature classifies rolled iron by cross-section into multiple named families: round, square, flat, hexagonal/octagonal, and `Façon-`/`Profileisen`, including angle/L, T, I/double-T, U, C, S, Z, Zores, rails and sleepers.

Control:
- `Walzeisen`, *Meyers Konversations-Lexikon*, 4th ed., vol. 16 (1885–90), p. 376: https://de.wikisource.org/wiki/MKL1888%3AWalzeisen

The point is morphological: an album may organize by **shape family** before it organizes by a cross-producer standard number.

### Onsite recognition fields

Record whether a page is principally organized by:

1. named shape family;
2. supplier / rolling mill;
3. proprietary profile number;
4. dimensions;
5. linear weight;
6. structural properties / load-bearing values;
7. price;
8. stock/order notation;
9. normal-profile number or explicit `Normalprofil` terminology;
10. pasted producer sheet versus merchant-generated manuscript table.

The same album can contain more than one regime.

---

## 3. What formal Normalprofile should look like conceptually

Later technical reference literature describes German Normalprofile as a deliberately restricted/regularized set of rolled-iron cross-sections. The first `Deutsches Normalprofilbuch` is associated with Heinzerling and Intze and the 1879–80 commission; the first edition appeared in Aachen in 1881.

Control:
- https://technik.de-academic.com/16508/Normalprofile

The source emphasizes that formal normal profiles had to reconcile:

- theory / calculation;
- construction needs;
- rolling technology.

It also explicitly notes that adoption of Normalprofile did **not** eliminate non-normal profiles; works' own `Profilbücher` continued to document other products.

This is crucial for classification of `EBA 4/14`.

### Recognition rule

Do not code a neat dimensional table as `ASSOCIATION_NORMALPROFILE` merely because it looks standardized.

Require at least one of:

- explicit `Normalprofil` / `Normalprofilbuch` wording;
- recognizable normal-series numbering tied to an external control;
- explicit association/committee attribution;
- exact match to a controlled Normalprofil table.

Otherwise code:

- `PROPRIETARY_SERIES`,
- `MERCHANT_EQUIVALENCE`,
- `AMBIGUOUS`, or
- `MIXED_COEXISTENCE`.

---

## 4. Normalprofile did not end proprietary plurality

A 1905 engineering `Träger-Tabelle` retrospectively states that German Normalprofile gained broad acceptance, while also discussing the persistence/reappearance of divergent profiles. Later technical summaries likewise state that manufacture of other profiles remained possible and that works' profile books documented them.

Controls:
- Gustav Schimpff, *Träger-Tabelle* (1905), preview: https://api.pageplace.de/preview/DT0400.9783486732290_A40941481/preview-9783486732290_A40941481.pdf
- technical summary: https://technik.de-academic.com/16508/Normalprofile

### Consequence

The strongest possible onsite finding would **not necessarily** be a clean replacement:

`proprietary -> normal`.

Historically richer possibilities include:

- normal and proprietary tables pasted side by side;
- merchant annotations mapping one onto another;
- normal profile terminology appearing only for selected product families;
- supplier-specific numbers surviving while dimensions/weights become aligned;
- normal tables used for technical recognition while price/order systems remain supplier-specific.

Such mixed states are evidence, not noise.

---

## 5. Küderli chronology now becomes unusually diagnostic

Official EBA 4 catalogue:

- `EBA 4/5 Convention der Zürcher Eisenhändler` — 1854, 1 file;
- `EBA 4/7 Korrespondenz` — 1858–72, 1 file;
- `EBA 4/14 Profileisenalbum` — 1877–85, 3 vols;
- `EBA 4/6 Preislisten` — 1878–80, 2 files;
- `EBA 4/4 Kassabuch` — 1884–89, 2 vols;
- `EBA 4/15 Verkaufsjournal` — 1885–97, 11 vols;
- `EBA 4/13 Profileisenalbum` — 1886–1903, 2 vols.

Official fonds description:
- 4 linear metres;
- c.10 files + c.150 books / c.20 description units;
- firm founded 1852;
- from 1870 supply emphasis shifted from France to Germany, with Basel becoming more important as an import gateway;
- fonds chiefly consists of business books, sales journals, profile albums, price lists and product programmes;
- original fonds was unordered.

Source:
- https://archives.georgfischer.com/objects/EBA%204

### New implication

The `1886–1903` profile albums (`EBA 4/13`) should be used as a **post-transition control**, even if the application concentrates on 1877–85.

A compact onsite comparison can therefore be:

`EBA 4/14 early pages 1877–78`  
vs. `EBA 4/14 transition layers 1879–81`  
vs. `EBA 4/14 late layers 1882–85`  
vs. **small control sample from `EBA 4/13`, 1886–90**.

If a recognizably stable normal-profile morphology only becomes clear in `/13`, that is itself evidence against teleological back-projection into `/14`.

---

## 6. Re-evaluate EBA 4/5, but do not overclaim it

`EBA 4/5`, **Convention der Zürcher Eisenhändler**, dated 1854, is a potentially important institutional baseline because it sits at the very beginning of the fonds and predates the correspondence/profile sequence.

At present public metadata exposes only the title/date/extent (`1 Akte`). It does **not** establish its content.

Later EBA 6 material shows that a `Zürcher Eisenhändler-Konvention` existed as an organized trade body in later decades; EBA 6/1 includes a 1927 copy of an 1890 agreement between Zürich iron merchants and the Verband Ostschweizerischer Eisenhändler, plus the VOE statutes of 1889. This proves later convention-based market coordination, not continuity from the 1854 file.

Source:
- https://archives.georgfischer.com/objects/show?collection=0&context=tectonical&fonds=0&index=1&parent=15&perPage=50&recordgroup=0&sortAsc=1&sortField=position

### Onsite rule

Inspect `EBA 4/5` early and code its actual operation:

- price agreement?
- payment/credit terms?
- territorial/customer allocation?
- units/measures?
- freight terms?
- product nomenclature?
- discount/rebate rules?
- competition/non-compete arrangement?
- merely an unrelated or later-filed document?

Do not call it a standardization institution until content is seen.

---

## 7. Revised minimal onsite packet for Küderli

### Must-open first

1. `EBA 4/5` — 1854 convention file: determine what kind of coordination it is.
2. `EBA 4/14` — all three 1877–85 profile albums: map physical layers and chronology.
3. `EBA 4/6` — 1878–80 price lists: identify producer/place/product/units and links to profile albums.
4. `EBA 4/7` — especially 1868–72 correspondence: supply-geography hinge.

### Transaction linkage

5. `EBA 4/4` — 1884–89 cashbook: small 1884–86 sample.
6. `EBA 4/15` — 1885–97 sales journal: 1885–87 sample.

### Post-transition control

7. `EBA 4/13` — 1886–1903 profile albums: small 1886–90 morphology control.

This is compact enough to execute as a coherent residency unit without pretending that all ~150 surviving books need to be read.

---

## 8. Falsification conditions

The Küderli hypothesis weakens materially if:

- `/14` is only a passive scrapbook of producer sheets with no internal annotations/ordering/revision;
- dated layers cannot be distinguished;
- profile sheets cannot be linked to suppliers, correspondence, prices or transactions;
- 1879–81 produces no observable change **and** proprietary/merchant equivalence work is absent;
- `/6`, `/4`, `/15` use product categories too coarse to link back to profile albums.

Even then, the albums remain evidence of information reception, but the strong claim about merchant commensurability would need to be reduced.

The hypothesis strengthens sharply if the albums contain:

- handwritten cross-supplier equivalences;
- corrections or replacement layers;
- product numbers linked across profile and price sheets;
- mixed French/German supplier systems across the 1870 hinge;
- explicit normal/non-normal distinctions;
- stable identifiers that reappear in sales/accounting records.

---

## 9. Current strongest corpus statement

After this control pass, the cleanest compact material group is:

> **Küderli/Bär 1854 + 1858–72 + 1877–90:** one early convention file, one correspondence block crossing the 1870 France-to-Germany supply shift, three 1877–85 profile albums plus two 1878–80 price-list files, followed by transaction books from 1884/85 and two later profile albums as a post-transition control.

Haffter remains the deeper comparative infrastructure, but Küderli currently supplies the tighter chronological experiment.
