# CURRENT PROGRESS — Iron Library / Wedding / Sheffield–Berlin

**Pinned continuation state — updated 2026-09-11 after full Wedding OCR routing + four selective Mss 25 image-control passes.**

This is the authoritative resume point. Read detailed checkpoint files for evidence, but do not resume from older OCR-only chronology.

## 1. Governing research problem

The project is not a simple `Sorby → Wedding → Martens` diffusion story. Controlled comparative sequence:

**industrial travel / works comparison → travelling sample → external test / expert judgement → numbering / provenance / collection → prepared specimen → microscopic field → microphotography → printed / institutional reference system.**

Core question: how did material comparison change scale, evidential carrier, access regime, preparation practice, institutional setting and reference structure while remaining comparative? Main axis: **Sheffield ↔ Berlin/Charlottenburg**, with Fischer 1845–46 as the pre-Wedding baseline.

## 2. Wedding corpus state

The three PaddleOCR JSONs are present and accepted as the discovery/indexing layer, not diplomatic transcription. Full corpus: **740 OCR entries, 609 non-empty**. Every entry has been routed once for recognisable content.

Working indices/checkpoints:

- `WEDDING_FULL_OCR_READING_LOG_2026-09-11.md`
- `WEDDING_MSS25_ITINERARY_AND_DOCUMENT_MODE_INDEX.tsv`
- `WEDDING_MSS24_ITINERARY_SKELETON.tsv`
- `WEDDING_MSS23_PROCESS_HEADING_INDEX.tsv`
- `WEDDING_MSS25_VISUAL_CONTROL_PASS1_2026-09-11.md`
- `WEDDING_MSS25_VISUAL_CONTROL_PASS2_2026-09-11.md`
- `WEDDING_MSS25_VISUAL_CONTROL_PASS3_2026-09-11.md`
- `WEDDING_MSS25_VISUAL_CONTROL_PASS4_2026-09-11.md`
- `WEDDING_MSS25_SOURCE_MODE_INDEX_1862_1863.tsv`
- `WEDDING_MSS25_TAIL_PROVENANCE_INDEX.tsv`

Longitudinal architecture:

**Mss 23: process decomposition / quantitative training → Mss 24: domestic cross-site comparison → Mss 25: transnational access + multi-year works/mining comparison + heterogeneous documentary/reference accumulation.**

## 3. Mss 25 is a multi-year comparative working notebook

Image control supersedes the old single-stream itinerary model.

### 1860 — long study journey

Image-controlled northern sequence:

- **9–10 July, Coventry**;
- **19–23 July, Manchester**, **William Fairbairn**;
- **24 July, Leeds / Sheffield**, **Turton & Sons**;
- **26 July, Leeds**, **Peter Fairbairn's Maschinenwerkstätte**;
- **27 July, Low Moor**, `Mr. Fenton`;
- **28 July, Bowling Works**;
- **31 July, Newcastle upon Tyne**, **Losh, Wilson & Bell**;
- early August Scotland, including **6 Aug. Govan Works in Glasgow**;
- **Gartsherrie Iron Works**, `Mr. Whitelaw`, manager `G. Campbell`.

Earlier South-West / South-Wales / Abercarn material remains at OCR-routing level and is still queued for selective image correction.

### 1862 — explicit Sheffield/Rotherham comparison layer

Entry 315 / PDF 316 is explicitly headed **`1862`** and contains Low Moor/Cumberland comparison, Henry Marten hot-blast-oven reference material, numbered **`9. Sheffield`**, Brown/Atlas Works-type material, armour-plate figures and **`bei Mr Beale in Rotherham bei Sheffield`**.

Entries 316–321 continue a dense **multi-site comparative technical block**: furnace profiles, burden recipes, hot-/cold-blast comparison, dimensions, labour/cost and output data. These are not clean itinerary pages.

Most important actor result: entry 316 / PDF 317 begins approximately **`Mit Alberts/Albers ... von Hoff`**. **`von Hoff` is manuscript-secure in the 1862 block.** The first companion is unresolved and must not be normalised to Daelen from expectation.

### 1863 — explicit Krug von Nidda layer

Entry 322 / PDF 323 explicitly begins a new section:

**`Mit Herrn von Krug: 1863.`**

followed by Cornwall / Tavistock / Great Devon Consols material. The Sheffield/Brown fragment above this heading most probably belongs to the preceding 1862 comparison layer.

The 1863 Cornwall notes are not strictly chronological in notebook order. Preserve literal dates separately from folio sequence.

## 4. Bessemer / Daelen / von Hoff / Hörde problem

The 1903 memoir securely states that Wedding:

- was instructed by **Bessemer himself in Sheffield**;
- brought **drawings** back from England;
- connected those drawings with Königshütte and Hörde Bessemer installations;
- travelled to Sheffield with Hörde leaders **Daelen and von Hoff**;
- advocated **Cumberland pig iron**, later contrasted with Upper-Silesian material.

Current manuscript control:

- **von Hoff: secure in the 1862 block**;
- **Daelen: not yet found**. Earlier OCR fuzzy candidates at entries 124, 128 and 268 collapse under visual inspection;
- **Hörde: not yet found**. The entry-316 OCR `Börde` candidate does not survive visual control as Hörde;
- **Bessemer: no secure notebook name hit yet**;
- **drawings: no checked 1862 diagram can yet be identified securely as a Bessemer converter/plant drawing**. The visually obvious diagrams are predominantly blast-furnace/oven/works sections.

Therefore the 1903 retrospective chain is increasingly anchored to the right manuscript environment, but the exact Bessemer episode/page remains open.

## 5. Major provenance result: explicit copied authority and source interleaving

Entry 339 / PDF 340 is a divider/title leaf reading clearly:

**`Cornwall aus de la Beche.`**

Entry 341 / PDF 342 can be cross-controlled directly against Henry De la Beche, *Report on the Geology of Cornwall, Devon and West Somerset* (1839), including the copper-ore ticketing passage and stannary/parliament material.

Copied-reference mode is interleaved with dated technical notes:

- entry 343 / PDF 344: **`8ten August 63.`**, Great Devon Consols bei Tavistock;
- entry 346 / PDF 347: literal **`16t. August.`**, Menheniot bei Liskeard, Wheal Mary Ann plus a second mine name still to control.

Chronology and datum provenance must remain separate fields.

## 6. Tail provenance pass: Mss 25 is a heterogeneous portable research container

The tail has now been visually controlled through the end of substantive manuscript content.

### Reused leaf / copied social reference

Entry 357 / PDF 358 retains an **`Abercarn near Newport. Mon.`** heading, while the main English prose concerns miners' `field club` / sick-life-club arrangements and relief for injured/killed workers, with a bibliographic note to a Benefit Societies item in *The People's Journal* (1847; exact author wording still B-level).

Do not assign that prose automatically to an Abercarn visit. The leaf itself has been reused across source modes.

### Physically inserted printed map/catalogue object

Entry 369 / PDF 370 is an actual printed Geological Survey / Ordnance Survey index map, not Wedding handwriting. It includes:

- Geological Survey publication/index information;
- `INDEX MAP OF THE ORDNANCE SURVEY OF ENGLAND AND WALES`;
- **Edward Stanford, 6 Charing Cross**.

This requires a new document mode: **`INSERTED_PRINT_OBJECT / PRINTED_MAP_CATALOGUE`**.

It is one of the strongest carrier examples in the project: an external national reference/index system is literally incorporated into Wedding's working notebook.

### Bibliographic routing and source synthesis

Entry 373 / PDF 374 explicitly routes to the **Transactions of the Geological Society of Cornwall** and **de la Beche 1839**.

Entry 378 / PDF 379 is a compiled Cornwall mineral/locality list, not one visit.

Entry 381 / PDF 382 closely matches de la Beche's mine-structure and labour-organisation sections: cross-courses, sump, captains/agents, **tributers, tutworkmen & labourers**, adventurers.

Entry 382 / PDF 383 continues strongly de la Beche-aligned technical extraction: water/steam, roads/carts, blasting with gunpowder, dressing tin ores, stamping and roasting.

PDFs 384–387 continue geological/vein synthesis; **PDF 387 is the last substantive manuscript page in the main sequence**.

PDF 388 onward consists of blank endpaper, covers, spine/fore-edge views, oblique object photography, ruler/colour-checker shots and later photographic documentation. These are digitisation/object records, not new textual pages.

Detailed file: `WEDDING_MSS25_VISUAL_CONTROL_PASS4_2026-09-11.md`.

## 7. Revised extraction/document-mode schema

For consequential Mss 25 rows, store separately:

- OCR entry / PDF page / manuscript marker;
- year layer;
- literal date wording;
- place/work/mine;
- people and functional roles;
- document mode;
- datum source: `DIRECT_OR_SITE_NOTE | ORAL_REPORT | WORKS_DOCUMENT | DRAWING/SKETCH | PRINT_COPY | COMPARATIVE_REASSEMBLY | INSERTED_PRINT_OBJECT | UNCERTAIN`;
- named source when explicit (e.g. `de la Beche`);
- operations (`SEE | COUNT | MEASURE | WEIGH | CALCULATE | APPARATUS_TEST | EXPERT_JUDGEMENT | ...`);
- confidence and image-control flag.

Additional document modes now required:

`BIBLIOGRAPHIC_ROUTING | REUSED_LEAF | HEADING_RESIDUE | GEOLOGICAL_LOCALITY_COMPILATION | OBJECT_DOCUMENTATION_IMAGE`.

A place/date alone is insufficient. Mss 25 shifts among named print authority, dated site note, comparison table, calculation, diagram and inserted printed object within a few leaves.

## 8. Working interpretation sharpened

Mss 25 now looks less like a diary than a **portable heterogeneous research container**. It makes direct/site observations, copied textual authority, bibliographic routing, compiled locality data, diagrams, quantitative comparison and a physically inserted printed map/index co-present in one object.

For the later metallography problem, the more precise transformation is therefore:

**heterogeneous portable research container → selected/standardized prepared object → numbered specimen collection → shared microscopic image → microphotographic / institutional reference system.**

This is stronger than a generic `travel → microscopy` narrative because the earlier comparison regime already has explicit carrier engineering.

## 9. Immediate resume point

Do **not** return to broad searching or blanket OCR.

Priority sequence now:

1. return to the **1862 actor block** and continue visual search for Daelen / Hörde / Bessemer / converter / `Zeichnung` / plant-arrangement language;
2. use the new tail provenance ontology when visually controlling the **1860 South-Wales/Abercarn** block, especially watching for reused headings versus actual visit prose;
3. preserve PDF 370 as a priority object example for the carrier argument;
4. after South-Wales control, compare this early composite research-container practice against Wedding 1885 / Martens specimen-image-reference systems.

Highest-value unresolved question remains:

> **Can the Bessemer / Daelen / von Hoff / Hörde / drawings episode be located precisely in the 1862 manuscript layer, and can Mss 25 show the material form of the technical information carried between Sheffield and German works?**

## 10. Claim ceilings

Secure:

- Mss 25 has distinct 1860, 1862 and 1863 working layers;
- `von Hoff` occurs in the image-controlled 1862 block;
- `Mit Herrn von Krug: 1863` is explicit;
- `Cornwall aus de la Beche` is explicit;
- multiple tail pages are source/reference rather than itinerary evidence;
- PDF 370 is a physically inserted Edward Stanford / Geological Survey-Ordnance Survey printed index-map object;
- PDF 387 is the last substantive manuscript page in the main sequence; later PDF pages are object/digitisation documentation;
- the notebook mixes direct/site-oriented, comparative, diagrammatic, copied-reference, bibliographic and inserted-print modes.

Open:

- Daelen in Mss 25;
- Hörde in Mss 25;
- Bessemer by name in Mss 25;
- exact plant/converter drawing corresponding to the 1903 memoir;
- precise identity of the first companion beside von Hoff (`Alberts/Albers`-like);
- direct Wedding–Sorby co-presence/contact.

## Resume order

1. `CURRENT_PROGRESS.md`
2. `WEDDING_MSS25_VISUAL_CONTROL_PASS4_2026-09-11.md`
3. `WEDDING_MSS25_TAIL_PROVENANCE_INDEX.tsv`
4. `WEDDING_MSS25_VISUAL_CONTROL_PASS3_2026-09-11.md`
5. `WEDDING_MSS25_SOURCE_MODE_INDEX_1862_1863.tsv`
6. `WEDDING_MSS25_VISUAL_CONTROL_PASS2_2026-09-11.md`
7. `WEDDING_MSS25_VISUAL_CONTROL_PASS1_2026-09-11.md`
8. `WEDDING_BESSEMER_TARGETED_OCR_PASS1_2026-09-11.md`
9. `WEDDING_1903_MEMOIR_CROSS_CONTROL_2026-09-11.md`
10. Mss 25 OCR JSON/PDF as needed.

**Immediate resume condition: continue image-controlled actor extraction in the 1862 block, then apply the new provenance-aware method to South Wales/Abercarn.**