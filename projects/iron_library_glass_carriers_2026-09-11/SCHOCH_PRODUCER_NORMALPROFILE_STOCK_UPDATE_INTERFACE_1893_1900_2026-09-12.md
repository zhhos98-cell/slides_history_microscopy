# Julius Schoch producer / Normalprofile / stock-update interface, 1893–1900

**Date:** 2026-09-12  
**Status:** MAJOR COMPETITOR STRUCTURAL CONTROL / MERCHANT-MEDIATION MODEL SECURE IN COMPARABLE ZÜRICH FIRM  
**Purpose:** demonstrate, without projecting the result onto Schinz & Bär, that a directly comparable Zürich iron merchant could simultaneously mediate named producer-specific profile systems, formal Normalprofile, local warehouse stock, illustrated price/reference carriers and recurrent stock-list updates.

## 0. Current conclusion

Repeated 1893 advertisements by **Julius Schoch & Co., Schwarzhorn, Zürich** place several distinct information/product regimes inside a single merchant ordering interface:

1. **named producer-specific profile universe** — decorative rolled iron from **L. Mannstädt & Co.**;
2. **formal Normalprofile stock** — numbered standard sections;
3. **local warehouse availability** — immediate stock in Zürich;
4. **illustrated price/reference distribution** — `Illustrierte Preislisten gratis`;
5. **rapid project-scale fulfilment** — material for whole buildings deliverable from stock within days.

By 1900 the same merchant advertises an expanded numbered German Normalprofile range and explicitly offers **`Monatliche Lagerlisten`**.

This supplies a direct historical model of the operation now being tested in Iron Library `EBA 4`:

`PRODUCER-SPECIFIC PROFILE SYSTEM`
+ `FORMAL NORMALPROFILE SYSTEM`
→ `MERCHANT STOCK / LOCAL AVAILABILITY`
→ `ILLUSTRATED PRICE/REFERENCE CARRIER`
→ `PROJECT ORDER / DELIVERY`
→ `RECURRENT STOCK-LIST UPDATE`.

It does **not** prove that Schinz & Bär used the same producer, page forms or numbering system.

---

## 1. 1893: producer-specific system inside a Zürich merchant stock interface

Repeated *Schweizerische Bauzeitung* advertisements in 1893 identify Julius Schoch & Co. as an outlet/depot for decorative rolled iron from **L. Mannstädt & Co.**

The advertisement states in substance that:

- all profiles of the works (`sämtliche Profile des Werkes`) are held in stock;
- these profiles are suitable for decorative cornices, bases, frames, cladding, gate decoration and related uses;
- the products are rolled iron;
- **illustrated price lists are supplied free**.

Primary controls:
- *Schweizerische Bauzeitung*, 31 Mar. 1893.
- *Schweizerische Bauzeitung*, 8 Jul. 1893.
- further repeated 1893 instances.

Digital controls:
- https://selfranga-prod11.ethz.ch/cntmng?pid=sbz-002%3A1893%3A21%3A%3A145
- https://selfranga-prod11.ethz.ch/cntmng?pid=sbz-002%3A1893%3A21%3A%3A285

### Structural importance

This is not a generic merchant selling `iron`.

A named producer's complete profile repertoire is being translated into:

- merchant stock;
- a public application vocabulary;
- an illustrated price/reference carrier;
- local availability.

That is a concrete example of **producer-to-merchant reference mediation**.

---

## 2. 1893: formal Normalprofile coexist in the same merchant interface

The same advertisement also states that Julius Schoch has in stock:

`Normalprofile Nr. 8, 10, 12, 14, 15, 16, 18, 20, 22, 24, 26, 30 und 32`

in lengths up to **12 metres**.

The advertisement further claims that, because of mechanical handling arrangements, deliveries for whole buildings can be dispatched from stock within a few days.

### Consequence

The merchant stock system is visibly **plural**:

- producer-specific Mannstädt profiles;
- numbered Normalprofile;
- other iron/material goods.

Formal Normalprofile therefore do not appear as a replacement for all producer-specific profile systems. They coexist at the point of merchant stock, reference and ordering.

This is exactly the kind of mixed state that the EBA 4 onsite protocol should be able to detect if `/14` or `/13` contain heterogeneous producer sheets or mixed numbering regimes.

---

## 3. 1900: numbered Normalprofile linked to recurrent stock-list maintenance

A 14 Jul. 1900 *Schweizerische Bauzeitung* advertisement for Julius Schoch & Cie. advertises:

- German Normalprofile (`I-Eisen in den deutschen Normalprofilen`);
- numbered range **8, 10, 12, 13, 14, 15, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40**;
- lengths up to **14 metres**;
- explicitly: **`Monatliche Lagerlisten`**.

Primary digital control:
- https://www.e-periodica.ch/cntmng?pid=sbz-002%3A1900%3A35%3A%3A363

### Major consequence

The reference problem is not only classification or catalogue publication. It includes **maintaining the truth of stock availability over time**.

The operational chain can be stated as:

`STABLE FORMAL PROFILE NUMBER`
↔ `VARIABLE LOCAL STOCK`
→ `MONTHLY STOCK LIST`
→ `ORDER / PROJECT SUPPLY`.

This is a clean competitor control for the Bär 1903 `new albums` and 1907 supplement-sheet sequence.

---

## 4. Relation to the Schoch 1899 catalogue-use control

A separate note documents the 1899 Julius Schoch `Muster-Buch über Stab- und Profil-Eisen` (`ETH Rar 9483`) and later architectural selection of profiles **3507** and **3517** by geometry/dimensions beyond their original `Fenstereisen` category.

Together the two controls show different sides of a merchant reference infrastructure:

### Merchant / warehouse side

`PRODUCER PROFILE + NORMALPROFILE NUMBER + STOCK + PRICE LIST + MONTHLY UPDATE`.

### Downstream user side

`CATALOGUE NUMBER + SHAPE + DIMENSIONS → SELECTION / REPURPOSING`.

Do not collapse the numbered systems: the high `3507/3517` product identifiers in the 1899 catalogue need not be the same semantic numbering regime as the German Normalprofile numbers `8–40`.

That distinction is itself analytically useful.

---

## 5. New recognition rule for EBA 4

When a number appears in `EBA 4/14` or `/13`, do **not** simply code `PROFILE_NUMBER`.

First classify its likely numbering ontology:

- `FORMAL_NORMALPROFILE_NUMBER`;
- `PRODUCER_PROFILE_NUMBER`;
- `MERCHANT_LOCAL_PRODUCT_NUMBER`;
- `CATALOGUE_PAGE/FIGURE_NUMBER`;
- `PRICE_LIST_ORDER_NUMBER`;
- `UNKNOWN_NUMBERING_SYSTEM`.

Then test mappings between them.

Add fields:

`NUMBER_VALUE / NUMBER_TYPE / AUTHORITY_OR_PRODUCER / EXTERNAL_MATCH / LOCAL_CROSSWALK / STOCK_STATUS / STOCK_LIST_DATE`.

This guards against a false equivalence in which every number is treated as the same kind of identity.

---

## 6. Implication for the Schinz & Bär supplier-sheet hypothesis

This competitor case makes the following mechanism historically plausible in the same Zürich merchant environment:

`NAMED GERMAN PRODUCER'S COMPLETE PROFILE RANGE`
→ `ZÜRICH MERCHANT DEPOT / STOCK`
→ `ILLUSTRATED PRICE LIST`
→ `LOCAL PROJECT DELIVERY`.

But Schinz & Bär must be tested independently.

Strong EBA 4 evidence would include:

- named rolling-mill imprints;
- complete or partial producer profile sheets;
- pasted producer price lists;
- local Schinz/Bär over-stamps;
- translations or relabelling;
- local stock/price annotations;
- crosswalks from producer number to merchant number;
- simultaneous Normalprofile and proprietary/producer systems.

Until such traces are seen:

> **SCHOCH PROVES THE COMPARABLE MERCHANT OPERATION; EBA 4 MUST PROVE WHETHER SCHINZ/BÄR DID IT.**

---

## 7. Application-level consequence

The strongest project object becomes less abstract:

> **merchant reference infrastructure as the interface where producer-specific forms, formal standards and changing local stock were made jointly orderable.**

A sharper question is:

> **How did Zürich iron merchants keep different kinds of product identity interoperable — producer profile numbers, Normalprofile numbers, local stock categories and catalogue/order identifiers — while physical availability and editions changed?**

This is not a story in which standards simply erase producer plurality. The competitor evidence directly shows coexistence.

## Claim ceiling

Secure for Julius Schoch:

- 1893 advertisements link the merchant to named L. Mannstädt & Co. decorative profiles;
- the merchant advertises all profiles of that works as stocked and offers illustrated price lists;
- the same advertisement lists numbered Normalprofile held in stock;
- by 1900 Schoch advertises German Normalprofile 8–40 and monthly stock lists.

Open for Schinz/Bär:

- named German producer identities;
- whether `/14` or `/13` contain producer sheets;
- whether Schinz/Bär used crosswalks among producer / Normalprofile / local identifiers;
- whether Bär generated recurrent stock lists comparable to Schoch;
- whether the 1885/1896 public albums derive from merchant compilations of producer systems.

## Resume point

Use Schoch as a **structural control for merchant mediation**, not as a substitute for Schinz/Bär evidence. Resume EBA 4 with the question:

`WHICH NUMBERING AUTHORITY? → WHICH PRODUCER? → WHICH LOCAL STOCK/PRICE KEY? → WHICH PUBLIC/UPDATED CARRIER?`