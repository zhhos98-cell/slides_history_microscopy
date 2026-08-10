# Duplicate DOI / URL semantic audit — 2026-08-10

Status: **SEMANTIC AUDIT COMPLETE / CANONICAL SOURCE ROUTES NORMALIZED**

This audit follows the repository-wide row-level QC. It reviews repeated DOI and URL routes semantically rather than deleting rows merely because two records share a link.

The governing distinction is simple:

- a repeated **item identifier** such as a DOI can corrupt citation exports if it is attached to the wrong bibliographic row;
- a repeated **verification or institutional URL** can legitimately support multiple distinct records;
- a repeated **primary collection URL** can indicate a real duplicate route when the records describe the same institutional endpoint at the same evidentiary level.

## 1. Bibliography DOI audit

The initial mechanical scan found two DOI routes repeated across distinct rows. Both were secondary verification routes, not DOIs belonging to every row in which they appeared. Because the public exporter treats any `doi.org` link in the row as that row's item DOI, leaving them in place risked producing false CSL JSON, BibTeX and RIS identifiers.

### DOI `10.11646/zootaxa.4322.1.1`

This DOI belongs to Birger Neuhaus, Thomas Schmid and Jens Riedel, *Collection management and study of microscope slides: Storage, profiling, deterioration, restoration procedures, and general recommendations* (2017).

It also appeared in `lit_allington_jones_2008` because Neuhaus et al.'s bibliography cites Lu Allington-Jones, *A new method for the restoration of palaeontological specimens mounted in Canada balsam* (2008). That made the DOI useful for verification but not an identifier for the Allington-Jones article.

**Disposition:** removed the Neuhaus DOI from `lit_allington_jones_2008`; retained the NatSCA archive route. No bibliographic row was deleted.

### DOI `10.1177/007327537701500201`

This DOI belongs to Brian Bracegirdle, *The History of Histology: A Brief Survey of Sources* (1977).

It appeared in both `src_cole_studies_1883` and `src_smith_beck_transparent_1861` because Bracegirdle's survey/bibliography refers to those historical sources. Again, the link was a verification route rather than the DOI of the nineteenth-century item.

**Disposition:** removed the Bracegirdle DOI from both historical rows. Cole retains BHL and Cambridge/Beiermann verification; Smith & Beck retains the Howard Lynk reconstruction/bibliography route.

### Result

The current 206-row bibliography now has **zero repeated DOI routes across distinct rows**. The manifest states explicitly that a `doi.org` URL may be stored in a row only when it identifies that row's own bibliographic item.

## 2. Bibliography repeated non-DOI URLs

After removing the two non-item DOI routes, **20 repeated non-DOI URLs** remain. These were reviewed as documentary functions rather than as string duplicates. None requires row collapse.

1. `antipa.ro/colectiientomologice/alte-ordine-de-insecte/` — one Antipa institutional page supports two distinct named slide collections, Thysanoptera and Siphonaptera. **KEEP SHARED ROUTE.**
2. `consellodacultura.gal/...bio=22444` — one Caballero biobibliographical route supports distinct 1918/1925 primary texts and the modern MNCN collection record. **KEEP SHARED ROUTE.**
3. `dicionario.ciuhct.org/zimmermann-carlos-karl-zimmermann/` — one Zimmermann biographical route supports two distinct primary manuals/articles and one research study. **KEEP SHARED ROUTE.**
4. `info.igme.es/biblio/r.asp?IdAutor=16606` — one author bibliography supports Caballero's distinct 1897 and 1925 preparation texts. **KEEP SHARED ROUTE.**
5. `microscopist.net/Tempere.html` — one maker/research page verifies several distinct Tempère series, catalogues, exchange notices and later scholarship. **KEEP SHARED ROUTE.**
6. `microscopist.net/Thiersch.html` — one reconstruction supports the 1861 Smith & Beck historical item and the later Lynk study. **KEEP SHARED ROUTE.**
7. `microscopist.net/ToppingCM.html` — one maker research page supports several distinct studies of Topping slides. **KEEP SHARED ROUTE.**
8. `mncn.bmtest.es/.../una-coleccion-unica...` — one MNCN collection article supports the modern Caballero collection record and a separate research study. **KEEP SHARED ROUTE.**
9. `biotaxa.org/Phytotaxa/article/view/phytotaxa.629.1.4` — one modern bibliographic/research route documents multiple distinct Möller price-list editions. **KEEP SHARED ROUTE.**
10. `eoas.info/biogs/P001250b.htm` — one Grayson biographical route supports two different primary technical publications. **KEEP SHARED ROUTE.**
11. `gutenberg.org/ebooks/48450.html.images` — one digitised historical volume provides verification for two distinct Klönne & Müller catalogue/advertising records. **KEEP SHARED ROUTE.**
12. `huh.harvard.edu/published-collections-bibliography-and-locations` — one Harvard distributed-collection page supports distinct Cleve/Möller and Eulenstein slide-series records. **KEEP SHARED ROUTE.**
13. `ioc.fiocruz.br/lames?num_for=2` — one Fiocruz slide portal supports three separately named pathology/histology collections. **KEEP SHARED ROUTE.**
14. `microscopist.net/BourgogneJoseph.html` — one maker reconstruction supports multiple distinct Bourgogne catalogues, exhibitions, advertisements and correspondence records. **KEEP SHARED ROUTE.**
15. `microscopist.net/ThumE.html` — one maker page supports two distinct 1880 Thum publications. **KEEP SHARED ROUTE.**
16. `microscopy-uk.org.uk/mag/artjan10/bs-bourgogne.html` — one Bourgogne historical/research page supports a primary 1862 catalogue and separate modern studies. **KEEP SHARED ROUTE.**
17. `nhm-wien.ac.at/.../annalen_serie_b/125_2023` — one journal/issue route supports a modern Grunow catalogue study and a distinct historical Delogne record used within that documentary context. **KEEP SHARED ROUTE.**
18. `quekett.org/about/journal` — the general Quekett journal access route supports several distinct Topping studies. **KEEP SHARED ROUTE.**
19. `quekett.org/about/journal/contents/journal-41` — one issue-contents page supports several separate articles in that volume. **KEEP SHARED ROUTE.**
20. `quekett.org/about/journal/contents/journal-42` — one issue-contents page supports two separate articles. **KEEP SHARED ROUTE.**

These are therefore **shared verification/access routes**, not duplicated bibliographic records. Bibliography membership remains **206 = 88 research + 118 primary/object**.

## 3. Source-registry repeated URLs

The original 87-row raw source registry produced six repeated URL groups. Here the distinction between duplicate endpoint and parent/secondary relation matters.

### Three true duplicate routes — canonicalized

- `ZA-IZIKO-ENTOMOLOGY` → `ZA-IZIKO-ENTOMOLOGY-SLIDES`.
- `AR-LAPLATA-FYCOLOGY` → `AR-MLP-FICOLOGIA-DIATOMS`.
- `NZ-TEPAPA-COLLECTIONS-ARCHIVES` → `NZ-TEPAPA-NATURAL-HISTORY-ARCHIVES`.

In all three cases the later record describes the same institutional endpoint and same primary URL with fuller scope/access metadata. The older row remains in the raw chunk as audit history and is suppressed in canonical/public consumption.

### Three legitimate shared URLs — retained as separate records

- **St Andrews Bell Pettigrew hierarchy:** the parent collection URL is primary for `GB-STANDREWS-BELL-PETTIGREW-SLIDES` and secondary for distinct Elcock and Stazione Zoologica Napoli subcollection records.
- **NHM Challenger:** the sediment dataset is primary for the historical preparation/collection route and secondary for the distinct CT-reassessment record.
- **NHM Heron-Allen:** the foraminifera landing page is primary for the broader collection and secondary for the more specific Type Slide system.

These records remain separate because they perform different evidentiary work.

## 4. Post-audit scope exclusion

A later whole-registry link/scope pass identified one additional problem that is conceptually different from duplication: `GB-SHEFFIELD-SORBY` was a **cross-project residue**. It is not a duplicate route and is therefore not entered in `superseded_ids`. Instead, it is now listed under `excluded_ids` in `source-registry-manifest.json`.

The raw chunks remain unchanged as an audit trail:

- raw records across 12 chunks: **87**;
- superseded same-route IDs: **3**;
- excluded out-of-scope IDs: **1**;
- current canonical source routes: **83**.

Current/public consumers must suppress both `superseded_ids` and `excluded_ids` rather than simply concatenating the raw chunks.

## 5. Public-site loader state

The public `sources/sources.js` previously contained a historical hard-coded list of only three registry chunks even though the manifest contains twelve. It now loads `source-registry-manifest.json`, fetches all twelve chunks, suppresses the three superseded IDs and the one excluded ID, and asserts the manifest's **83 canonical records** before rendering/exporting them.

This was a publication-layer bug and scope-cleanup issue, not source-data loss: the later chunks and excluded raw row remain in the repository as audit history.

## 6. Resulting policy

Going forward:

1. repeated DOI across different bibliography rows is an error until reviewed;
2. a DOI in `links` must identify the row's own item, because citation-manager export treats it as an item identifier;
3. repeated non-DOI URL is only a review trigger;
4. source-registry rows sharing a primary URL are collapsed only when they describe the same endpoint at the same evidentiary level;
5. parent/subcollection, primary/secondary and collection/analytical-afterlife relations remain separate even when they share a URL;
6. raw source-registry rows can remain for audit, but canonical/public consumers must apply both the duplicate-supersession map and explicit scope exclusions.

This completes the semantic duplicate/scope cleanup without changing the frozen 307/155 object census or the 206-entry bibliography membership.
