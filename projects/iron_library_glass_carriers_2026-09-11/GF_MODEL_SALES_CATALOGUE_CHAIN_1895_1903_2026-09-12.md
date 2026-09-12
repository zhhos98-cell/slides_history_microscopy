# GF model–sales–catalogue carrier chain, 1895–1903

**Date:** 2026-09-12  
**Status:** STRONG PRODUCER-SIDE CARRIER CHAIN / IDENTIFIER CROSSWALK OPEN  
**Authority:** newest delta to `GF_SINGEN_PRODUCER_REFERENCE_CLUSTER_1893_1900_2026-09-12.md`; does **not** replace `PINNED_APPLICATION_RESUME.md`.

## 0. Current conclusion

The bounded Georg Fischer side now exposes not merely a contract and a model book, but a sequence of distinct information carriers close enough in time to test how a manufactured form moved between identification, production, sales accounting and printed reference:

`3 JAN 1895 BÄR–GF CONTRACT`
↔ **`GFA 22/1338 — NUMBERED MODEL BOOK`**
→ **`GFA 1/1742 — WAAREN-ABSATZ, JAN 1896–JUN 1903`**
→ **`GFA 1/2749 — GF / COMPETITOR FITTINGS CATALOGUES, ENVELOPE FROM 1899`**
↔ **`GFA 1/2695 — FITTINGS CATALOGUES / PRICE LISTS, ENVELOPE FROM 1899`**.

A possible earlier printed-carrier gate also begins in 1896:

- `GFA 1/650 — Sonderdrucke, Prospekte, Werbung Stahlgiesserei, Tempergiesserei`, 1896–1934.

This materially sharpens the residency test. The producer-side problem is no longer generic manufacture. It is whether the **same industrial form can be followed across model number, contract term, sales-statistical category and printed catalogue/price identity**.

The strongest cross-fonds test therefore becomes:

`BÄR PROFILE / DRAWING / ORDER ID`
↔ `1895 CONTRACT TERM / ANNEX / RIGHTS`
↔ `GF MODEL NO.`
↔ `GF SALES-STATISTIC KEY`
↔ `GF CATALOGUE / PRICE-LIST ID`.

No such crosswalk is yet proven. That absence is the main onsite research question, not a gap to be silently filled.

---

## 1. Carrier A — `GFA 22/1338`, producer model identity

See `GF_SINGEN_PRODUCER_REFERENCE_CLUSTER_1893_1900_2026-09-12.md`.

Catalogue-secure metadata:

- `Modellbuch für Temperguss`;
- one volume;
- archival envelope 1895–ca.1950;
- ordered by **model number**;
- model numbers **1–10553**;
- records `Verbleib` of models;
- records names, possibly customers;
- subject terms `Fitting :: Modelle`;
- Singen.

Critical source rule:

The contents are catalogued as `undatiert`. The 1895 envelope does **not** prove that low numbers or first entries were written in 1895. Internal chronology must be reconstructed physically.

---

## 2. Carrier B — `GFA 1/1742`, sales/statistical identity

Catalogue:
- https://archives.georgfischer.com/objects/10539

Identification:

- signature `GFA 1/1742`;
- title `Fittings Schaffhausen und Singen`;
- 14 volumes;
- dossier envelope 1900–1931 / unknown.

The archive description explicitly says the dossier contains:

1. records of costs, wages and calculations for Tempergussfittings in Schaffhausen and Singen, 1900–1931;
2. an `interessante Statistik` of Aktiengesellschaft der Eisen- und Stahlwerke von Georg Fischer titled **`Waaren-Absatz`**, covering **January 1896 to June 1903**.

This second item is now a high-priority gate because its chronology begins immediately after the 1895 Bär contract / Singen start and ends at essentially the same moment as `EBA 4/13` (1886–1903).

### What is secure

- a company `Waaren-Absatz` statistic survives inside `/1742`;
- stated period: Jan 1896–Jun 1903;
- it belongs in a dossier explicitly about Fittings Schaffhausen und Singen.

### What is open

- whether the statistic is contemporaneous or retrospectively compiled;
- exact physical form and date of compilation;
- row/column schema;
- whether it separates Singen and Schaffhausen;
- whether it records product classes, model numbers, catalogue numbers, values, weights, quantities, customers or destinations;
- whether `Geländerfittings` appear as a distinct category;
- whether Bär/Baer appears.

### Fast onsite capture

`PHYSICAL_DATE / TITLE / AUTHORING_UNIT / CONTEMPORARY_OR_RETROSPECTIVE / PERIOD / SINGEN-SCHAFFHAUSEN_SEPARATION / PRODUCT_CLASS / MODEL_NO / CATALOGUE_NO / QUANTITY / WEIGHT / VALUE / DESTINATION / CUSTOMER / MONTH-YEAR GRANULARITY / NOTES / CROSS_REFERENCE`.

### Stop rule

If `Waaren-Absatz` is aggregate tonnage/value only, retain it as production/sales scale context and do **not** force it into the identifier crosswalk.

---

## 3. Carrier C — `GFA 1/2749`, printed catalogue identity

Public archive listings identify:

- `GFA 1/2749 — Tempergussfittings Kataloge GF, W&E, Saunders, Bunn & Johnson`;
- envelope **1899–1965**;
- one file.

This is currently the strongest catalogue gate because the title explicitly includes **GF** among the represented catalogue producers.

### Secure

- the dossier contains GF fittings catalogue material as well as W&E, Saunders, Bunn & Johnson material;
- the dossier envelope begins 1899.

### Open — important claim ceiling

Do **not** yet write:

- `GF issued a surviving catalogue in 1899`;
- `the earliest item in /2749 is a GF catalogue`;
- `the 1899 catalogue uses the /1338 model numbers`.

The envelope beginning in 1899 only proves the dossier contains material dated as early as 1899 somewhere within the mixed catalogue file.

### Onsite gate

First establish an item-level inventory:

`MAKER / TITLE / DATE / EDITION / PRINTER / LANGUAGE / PAGE-SHEET COUNT / MODEL_OR_ARTICLE_NUMBER / DRAWING / DIMENSIONS / WEIGHT / MATERIAL / PRODUCT CLASS / PRICE / ORDER KEY / MAKER MARK / GELÄNDER TERM / SINGEN-SCHAFFHAUSEN IMPRINT`.

Priority: isolate all **GF** items dated 1899–1903 before reading later material.

---

## 4. Carrier D — `GFA 1/2695`, catalogue / price-list identity

Public archive listings identify:

- `GFA 1/2695 — Tempergussfittings: Kataloge, Preislisten`;
- envelope **1899–1973**;
- one file.

### Secure

Only title, envelope and file-level extent are currently secure from public metadata.

### Open

- which firms are represented;
- whether the earliest item is GF;
- whether a 1899 GF price list survives;
- whether article/model numbers occur;
- whether prices are keyed to the same numbers used in `/1338` or `/2749`.

### Role

Use `/2695` only after maker/date triage. If early GF price material exists, it becomes the strongest possible route to:

`MODEL NUMBER -> PRINTED ARTICLE NUMBER -> PRICE`.

If it is mainly competitor/later material, demote immediately.

---

## 5. Possible earlier printed-carrier gate — `GFA 1/650`

Public archive listing:

- `GFA 1/650 — Sonderdrucke, Prospekte, Werbung Stahlgiesserei, Tempergiesserei`;
- **1896–1934**;
- one file.

This begins earlier than `/2749` and `/2695` and therefore merits a very fast item-level gate.

Open:

- whether 1896–99 pieces actually survive in the file;
- whether they concern fittings rather than Stahlguss / generic Temperguss;
- whether they contain product drawings, model/article numbers or prices;
- whether Singen appears.

Do not promote `/650` until an early item is identified.

---

## 6. Demotion / reordering of earlier gates

### `GFA 1/311 — Warenausgang Singen und Schaffhausen`, 1896–1953

Still potentially useful, but `/1742` now has a much more explicit early-period statistical description. Therefore:

- `/1742` moves ahead of `/311`;
- inspect `/311` only if `/1742` lacks product/model granularity or directly points to a source series behind the statistic.

### `GFA 1/1736 — Warenausgangsstatistiken`, 1900–1946, 4 vols

Potential continuation/control only. Do not add unless `/1742` generates a specific comparison need.

### `GFA 1/2811 — Werbung/Prospekte/Inserate Stahlguss, Temperguss, Räder, Fittings`, 1902–1917

Useful later printed reference carrier if 1899 gates fail or if 1902–03 terminal comparison with `EBA 4/13` becomes necessary. Not primary while `/2749` and `/2695` remain unresolved.

---

## 7. New four-carrier producer protocol

### Step 1 — model

`GFA 22/1338`

Ask:
- what is a model number?
- how is model identity maintained?
- can Bär/Geländer/customer/disposition language be found?

### Step 2 — contract

`GFA 1/171`

Ask:
- does the 3 Jan 1895 contract define product form or only commercial responsibility?
- are there drawing/model/sample/number annexes?
- who defines, owns, manufactures and sells the form?

### Step 3 — sales statistic

`GFA 1/1742`

Ask:
- what unit is counted as `Waaren-Absatz`?
- can the sales statistic see the same product/model identity?
- is the unit a model, product family, weight, value or destination category?

### Step 4 — printed catalogue / price

`GFA 1/2749`, then `/2695`, fast gate `/650`

Ask:
- what identifier reaches the public/buyer-facing carrier?
- does model number survive as article/order number?
- are drawings and dimensions sufficient to crosswalk even if numbering changes?

---

## 8. Explicit ontology warning: do not equate counting units

Current GF evidence uses several different numerical languages:

- later GF company history: first fittings price list with 91 `Modelle`; about 750 by 1890; 8,615 by 1925;
- 1891 contemporary advertising: about 2,000 `Gattungen` / `Formen und Combinationen`;
- `GFA 22/1338`: model numbers run 1–10553 across the volume's long life.

These are **not demonstrated to be the same unit**.

Do not equate:

`GATTUNG = FORM = COMBINATION = MODELLNUMMER = KATALOGARTIKEL = VERKAUFSARTIKEL`.

This is not merely a nuisance. It is a core research question about industrial identity:

> Which numbering or classificatory unit belonged to design/model management, which to manufacturing, which to catalogue representation, and which to sales accounting?

---

## 9. Cross-fonds concordance table to build onsite

Use one row per candidate matching form:

`DATE | BÄR_VOLUME | BÄR_PAGE/SHEET | BÄR_PROFILE_NO | BÄR_PRODUCT_TERM | BÄR_SHAPE | DIMENSIONS | CONTRACT_TERM | CONTRACT_DRAWING/SAMPLE | GF_MODEL_NO | GF_MODEL_DESCRIPTION | GF_VERBLEIB/CUSTOMER | WAAREN-ABSATZ_KEY | GF_CATALOGUE_DATE | GF_CATALOGUE_NO/PAGE | GF_PRODUCT_TERM | PRICE | MAKER_MARK | CONFIDENCE | BASIS_OF_MATCH`.

### Match levels

**Level 1 — direct identifier:** same number/reference explicitly cross-cited.

**Level 2 — direct drawing/sample reference:** contract/catalogue/model book explicitly links carrier to carrier.

**Level 3 — morphology + dimensions + terminology:** strong but inferential match.

**Level 4 — product-family adjacency only:** context, not identity.

Never promote Level 4 into a genealogy.

---

## 10. Residency geometry consequence

The producer-side addition remains bounded and feasible.

### Mandatory

1. `GFA 1/171` — one dossier;
2. `GFA 22/1338` — one model-book volume;
3. `GFA 1/1742` — first isolate the 1896–1903 `Waaren-Absatz` statistic within the 14-volume dossier.

### Fast catalogue gates

4. `GFA 1/2749` — isolate GF items dated 1899–1903;
5. `GFA 1/2695` — maker/date triage, early GF price-list test;
6. `GFA 1/650` — 1896–99 item-level gate only.

### Conditional only

7. `/311`, `/1736`, `/2811` if mandatory/gate material points there.

This does **not** justify browsing the whole GFA 22 fonds or the whole GFA 1 historical archive.

---

## 11. Application consequence

Do not yet replace the EBA 4-centered application pin.

But the producer side is now strong enough to support a sharper onsite necessity claim:

> Remote evidence can establish that Bär maintained changing profile-reference systems and that Georg Fischer operated a numbered model system and a large fittings business. Only co-located onsite inspection can determine whether the 1895 contract and the surviving sales/catalogue carriers actually translated one firm's product identity into the other's.

If identifier concordance closes, the project can move from:

`PROFILE IDENTITY WITHIN A MERCHANT REFERENCE SYSTEM`

to:

**`INDUSTRIAL IDENTITY ACROSS MERCHANT, CONTRACTUAL, MANUFACTURING, SALES AND CATALOGUE SYSTEMS`**.

If it does not close, the negative result remains strong: different organisations could coordinate manufacture and sale while preserving **non-interoperable identity systems**.

---

## Resume point

**Resume here:**

`EBA 4/13 + EBA 4/15 c.1894–97`
↔ `GFA 1/171 CONTRACT`
↔ `GFA 22/1338 MODEL BOOK`
↔ **`GFA 1/1742 WAAREN-ABSATZ 1896–1903`**
↔ **`GFA 1/2749 GF CATALOGUE GATE FROM 1899`**
↔ `GFA 1/2695 PRICE-LIST GATE FROM 1899`
↔ fast `GFA 1/650` early printed-carrier gate.

**Primary unresolved test:** can one product identity be cross-walked across at least three of these carriers without relying on product-family adjacency alone?