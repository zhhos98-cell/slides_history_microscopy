# CURRENT PROGRESS — Iron Library / Wedding / Sheffield–Berlin

**Pinned continuation state — updated 2026-09-11 after full Wedding OCR routing + three selective Mss 25 image-control passes.**

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
- `WEDDING_MSS25_SOURCE_MODE_INDEX_1862_1863.tsv`

Longitudinal architecture:

**Mss 23: process decomposition / quantitative training → Mss 24: domestic cross-site comparison → Mss 25: transnational access + multi-year works/mining comparison + documentary/reference accumulation.**

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

Most important new actor result: entry 316 / PDF 317 begins approximately **`Mit Alberts/Albers ... von Hoff`**. **`von Hoff` is manuscript-secure in the 1862 block.** The first companion is unresolved and must not be normalised to Daelen from expectation.

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

Detailed files:

- `WEDDING_1903_MEMOIR_CROSS_CONTROL_2026-09-11.md`
- `WEDDING_BESSEMER_TARGETED_OCR_PASS1_2026-09-11.md`
- visual-control passes 2–3.

## 5. Major provenance result: Wedding explicitly marks copied authority

Entry 339 / PDF 340 is a divider/title leaf reading clearly:

**`Cornwall aus de la Beche.`**

This is first-order actor evidence for source provenance inside the notebook.

Entry 341 / PDF 342 can be cross-controlled directly against Henry De la Beche, *Report on the Geology of Cornwall, Devon and West Somerset* (1839):

- de la Beche p. 596: copper ores after being dressed, sampled and sold at ticketings before shipment to South Wales;
- de la Beche p. 618: stannary jurisdiction, twenty-four stannators, their parliament and speaker.

Wedding's page reproduces/selects these passages closely enough to classify it as a controlled **PRINT_COPY** layer.

Crucially, this copied-reference mode is interleaved with dated technical notes rather than forming one clean terminal appendix:

- entry 343 / PDF 344: **`8ten August 63.`**, Great Devon Consols bei Tavistock, vein/depth/working/production detail;
- entry 346 / PDF 347: literal **`16t. August.`**, Menheniot bei Liskeard, Wheal Mary Ann and a second probable Wheal Trelawny-type mine name. The year `1863` comes from section context and must remain separate from the literal date transcription.

This strengthens the project's central methodological point: chronology and datum provenance are different variables.

## 6. Revised extraction schema

For consequential Mss 25 rows, store separately:

- OCR entry / PDF page / manuscript marker;
- year layer;
- literal date wording;
- place/work/mine;
- people and functional roles;
- document mode;
- datum source: `DIRECT_OR_SITE_NOTE | ORAL_REPORT | WORKS_DOCUMENT | DRAWING/SKETCH | PRINT_COPY | COMPARATIVE_REASSEMBLY | UNCERTAIN`;
- named source when explicit (e.g. `de la Beche`);
- operations (`SEE | COUNT | MEASURE | WEIGH | CALCULATE | APPARATUS_TEST | EXPERT_JUDGEMENT | ...`);
- confidence and image-control flag.

A place/date alone is insufficient: Mss 25 shifts among named print authority, dated site note, comparison table, calculation and diagram within a few leaves.

## 7. Immediate resume point

Do **not** return to broad searching or blanket OCR.

Priority sequence:

1. keep working the **1862 block** with actor names open: visually search for Daelen / Hörde / Bessemer / converter / `Zeichnung` / plant-arrangement language;
2. continue the **1863 Cornwall** pages while assigning datum provenance page by page;
3. use `Cornwall aus de la Beche` as the first controlled template for `PRINT_COPY` provenance and identify additional named printed sources;
4. then return to the 1860 South-Wales/Abercarn visual-control queue;
5. after those controls, compare early composite comparison practice against Wedding 1885 / Martens specimen-image-reference systems.

Highest-value unresolved question remains:

> **Can the Bessemer / Daelen / von Hoff / Hörde / drawings episode be located precisely in the 1862 manuscript layer, and can Mss 25 show the material form of the technical information carried between Sheffield and German works?**

## 8. Claim ceilings

Secure:

- Mss 25 has distinct 1860, 1862 and 1863 working layers;
- `von Hoff` occurs in the image-controlled 1862 block;
- `Mit Herrn von Krug: 1863` is explicit;
- `Cornwall aus de la Beche` is explicit;
- at least one following page copies/selects identifiable passages from de la Beche 1839;
- the notebook mixes direct/site-oriented, comparative, diagrammatic and printed-reference modes.

Open:

- Daelen in Mss 25;
- Hörde in Mss 25;
- Bessemer by name in Mss 25;
- exact plant/converter drawing corresponding to the 1903 memoir;
- precise identity of the first companion beside von Hoff (`Alberts/Albers`-like);
- direct Wedding–Sorby co-presence/contact.

## Resume order

1. `CURRENT_PROGRESS.md`
2. `WEDDING_MSS25_VISUAL_CONTROL_PASS3_2026-09-11.md`
3. `WEDDING_MSS25_SOURCE_MODE_INDEX_1862_1863.tsv`
4. `WEDDING_MSS25_VISUAL_CONTROL_PASS2_2026-09-11.md`
5. `WEDDING_MSS25_VISUAL_CONTROL_PASS1_2026-09-11.md`
6. `WEDDING_BESSEMER_TARGETED_OCR_PASS1_2026-09-11.md`
7. `WEDDING_1903_MEMOIR_CROSS_CONTROL_2026-09-11.md`
8. Mss 25 OCR JSON/PDF as needed.

**Immediate resume condition: continue image-controlled actor/provenance extraction from the 1862–63 Mss 25 block.**