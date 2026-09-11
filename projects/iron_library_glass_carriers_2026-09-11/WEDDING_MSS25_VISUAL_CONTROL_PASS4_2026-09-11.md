# Wedding Mss 25 — selective visual-control pass 4

Date: 2026-09-11

Status: IMAGE-CONTROLLED TAIL / PROVENANCE PASS. This checkpoint follows the Cornwall/reference tail of Mss 25 to the end of substantive manuscript content. It distinguishes handwritten excerpt, compiled reference note, inserted printed object and later photographic documentation. It also cross-controls a small number of passages against externally digitised sources where the wording is sufficiently distinctive.

## 1. Entry 357 / PDF 358: `Abercarn near Newport. Mon.` sits above a copied/social-reference block

The page top is clearly headed **`Abercarn near Newport. Mon.`**, but the main text beneath is English prose on miners' clubs and relief arrangements, not a normal dated works-visit narrative.

Recognisable content includes:

- `The field club` / miners' medical attendance and sick pay;
- compulsory contributions stopped from wages;
- separate voluntary `sick or life club` arrangements;
- relief for men wounded or killed in service and for widows/children;
- a bottom bibliographic note that appears to cite **`On Benefit Societies` by Dr. Beard in `the people's journal` 1847** (author/title wording B-level; image is clearer than OCR but still retain caution).

Document-mode consequence: **do not infer that the social-club prose was observed at Abercarn merely because the old Abercarn heading remains at the top of the reused leaf.** The page demonstrates physical reuse and superposition of source modes.

Recommended tag: `REUSED_LEAF | COPIED_SOCIAL_REFERENCE | HEADING_RESIDUE`.

## 2. Entry 369 / PDF 370: an actual printed Geological Survey / Edward Stanford map is bound or inserted into the notebook

This is not Wedding handwriting and not a handwritten copy. The page is a printed map/catalogue object.

Visible printed text includes:

- **`GEOLOGICAL SURVEY — FOR DETAILED LISTS OF THE MAPS SECTIONS AND BOOKS — SEE STANFORD'S GEOLOGICAL CATALOGUE`**;
- numerical list of Survey sections;
- publication information for England, Scotland and Ireland;
- **`INDEX MAP OF THE ORDNANCE SURVEY OF ENGLAND AND WALES`**;
- **`LONDON — EDWARD STANFORD, 6 CHARING CROSS`**, wholesale and retail mapseller / agent for Ordnance and Geological Survey maps.

This materially changes the notebook architecture. Mss 25 does not merely contain field notes + copied prose. It physically incorporates a **portable printed reference object** that supplies a national spatial/indexing system.

New document mode required:

`INSERTED_PRINT_OBJECT` / `PRINTED_MAP_CATALOGUE`.

Analytical sequence:

**field route / mine notes ↔ copied textual authority ↔ physically inserted map-index object.**

This is especially important for the project's carrier question: comparison is not only remembered or rewritten; an external published reference system is literally carried inside the working notebook.

## 3. Entry 373 / PDF 374: bibliography/source-routing page

The page is German handwritten synthesis with explicit references at the bottom. Readable source-routing elements include:

- **`Transactions of the Geological Society of Cornwall`** with volume/page references and named authors/readings still requiring exact palaeographic control;
- **`Report on the Geology of Cornwall ... H. de la Beche 1839`**.

The exact first cited author(s) should not be normalised from OCR alone, but the bibliographic function is secure.

Document-mode consequence: this is not simply geological content. It is a **source-navigation / citation apparatus** inside the notebook.

Recommended tag: `BIBLIOGRAPHIC_ROUTING | PRINT_REFERENCE_INDEX`.

## 4. Entry 378 / PDF 379: mineral/locality compilation rather than a single visit

The page is a compact German locality/mineral list for Cornwall. Stable or near-stable anchors include:

- north Cornwall / **Launceston**;
- **St Austell**;
- `Black Jack`;
- brown haematite;
- lead occurrences;
- multiple named localities/mines and cross-course / vein language.

The layout and density support a compiled geological/mineral reference function rather than one dated site visit.

Recommended tag: `GEOLOGICAL_LOCALITY_COMPILATION | COMPARATIVE_REFERENCE`.

## 5. Entry 381 / PDF 382: direct match to de la Beche's mining-organisation and mine-structure sections

The page contains a mixed English/German glossary/excerpt layer. Image-controlled readings include:

- lower part of the engine/shaft as the **sump**;
- **cross courses** traversing the lode;
- uncut / untouched cross-course terminology;
- `Captains or agents`;
- **`Tributers, Tutworkmen & Labourers`**;
- large-mine administrative structure with clerks, captains/agents, miners/labourers;
- shares / `adventurers`;
- tutworkmen paid by piece / by the fathom.

External cross-control: de la Beche's 1839 *Report on the Geology of Cornwall, Devon and West Somerset* contains the same technical architecture. Its economic-geology section discusses cross-courses (around p. 559) and classifies mine labour as tributers, tutworkmen and labourers (around p. 567). This match is strong enough to treat the page as a **de la Beche-derived extraction/synthesis layer**, not generic mining lore.

Recommended tag: `PRINT_COPY / SOURCE_SYNTHESIS — de la Beche 1839`.

## 6. Entry 382 / PDF 383: de la Beche-derived technical operations continue

The next page continues the same reference architecture. Image-controlled anchors include:

- `Tribute`;
- water wheels / steam;
- underground roads and carts;
- safety fuse / boring / blasting with gunpowder;
- air-piping;
- `Dressing of tin ores`;
- stamping mill;
- roasting furnace and dimensional notes.

The sequence aligns closely with the mining-operation and tin-dressing subjects indexed in de la Beche's 1839 report (mine workings, blasting by gunpowder, dressing tin ores, roasting/smelting). It is safer to call this **strongly de la Beche-derived / de la Beche-aligned** rather than a line-for-line copy until the exact passages are collated.

## 7. PDFs 384–387: final handwritten geological synthesis; no new itinerary layer detected

The remaining substantive leaves are dense German geological/vein notes with orientations, measurements, cross-course/vein reasoning and references. They do not present a new clearly dated British itinerary section on this pass.

Use them as `GEOLOGICAL_SYNTHESIS / REFERENCE_COMPARISON` pending sentence-level palaeography.

Crucially, **PDF 387 is the last page with substantive manuscript writing** in the main sequence.

## 8. PDFs 388 onward are object/documentation views, not new notebook content

From PDF 388 onward the digitisation switches to blank endpaper, covers, spine/fore-edge views, oblique object photographs, ruler/colour-checker shots and calibration photography. Some later images reproduce already-scanned internal pages for documentation.

Therefore the current substantive-content boundary of Mss 25 is controlled as:

**manuscript/reference content through PDF 387; object/documentation photography from PDF 388 onward.**

This prevents the 401 OCR entries from being mistaken for 401 pages of independent textual content.

## 9. Revised document-mode ontology forced by the tail

Mss 25 now requires at least the following distinct modes:

1. `DATED_VISIT / SITE_TECHNICAL_NOTE`
2. `COMPARATIVE_REFERENCE_BLOCK`
3. `PRINT_COPY / EXCERPT`
4. `BIBLIOGRAPHIC_ROUTING`
5. `INSERTED_PRINT_OBJECT`
6. `REUSED_LEAF / HEADING_RESIDUE`
7. `GEOLOGICAL_LOCALITY_COMPILATION`
8. `OBJECT_DOCUMENTATION_IMAGE` (digitisation metadata, not manuscript evidence)

The notebook therefore behaves less like a diary than like a **portable heterogeneous research container**.

## 10. Stronger analytical consequence

The most important finding from the tail is material, not merely textual:

> Wedding's comparative infrastructure includes direct observations, copied excerpts, explicit source citations, compiled locality lists and a physically inserted printed Geological Survey / Stanford index map inside the same notebook object.

That matters for the later metallographic comparison. Long before prepared sections and microphotographs become institutional reference objects, Wedding is already working with a composite carrier in which **place, printed authority, index, diagram and quantitative note are made co-present**.

The relevant transformation is therefore not simply `travel note → microscopy` but:

**heterogeneous portable research container → increasingly standardized prepared/reference object and image system.**

## 11. Immediate resume point

The Mss 25 tail is now controlled at document-mode level through the end of substantive content. Next high-value work should return to one of two fronts:

1. continue the **1862 actor/Bessemer block** visually for Daelen / Hörde / converter / drawing evidence; or
2. visually control the earlier **South-Wales / Abercarn 1860** block, now with stricter page-level provenance tagging so reused headings and copied prose are not collapsed into visit evidence.

For the project's carrier argument, preserve PDF 370 as a priority image/object example: it is the clearest case yet of an external printed reference system physically entering Wedding's notebook.