# Wedding Mss 25 — selective visual-control pass 3

Date: 2026-09-11

Status: IMAGE-CONTROLLED + EXTERNAL SOURCE CROSS-CONTROL. This checkpoint continues the 1862 actor search and then follows the 1863 Cornwall material far enough to distinguish dated technical notes from explicit copied/reference material. Manuscript readings control chronology; external printed sources are used only to identify copied passages.

## 1. The earlier fuzzy Daelen candidates are false positives

The three OCR candidates previously routed as possible `Daelen` forms were rechecked against the manuscript pages:

- OCR entry 124 / PDF 125 (`Dalyen`-like OCR): the manuscript is a technical/process page with furnace diagrams and no controlled Daelen name at the OCR location.
- OCR entry 128 / PDF 129 (`D'anlen`-like OCR): the manuscript is technical prose around Marchienne/Charleroi-type material; no controlled Daelen reading appears.
- OCR entry 268 / PDF 269 (`Dalsen`-like OCR): the manuscript is a rolling/technical note page; the supposed name is not Daelen.

Controlled result: **none of the current OCR fuzzy Daelen hits survives visual inspection.** Daelen remains absent at manuscript-controlled level.

This matters because the 1903 memoir explicitly names `dem alten Daelen und von Hoff`; the notebook search must therefore continue without forcing a retrospective name into ambiguous handwriting.

## 2. The entry-316 OCR `Börde` candidate does not establish Hörde

Entry 316 / PDF 317 has now been read at high resolution. The top line securely ends in **`von Hoff`** and begins approximately `Mit Alberts/Albers ...`; the first companion remains unresolved.

The separate OCR fragment previously rendered as `Von Börde Muster ...` cannot be visually promoted to **Hörde**. At manuscript level the relevant word-form is too different/unclear to sustain that identification.

Controlled result:

- **von Hoff: secure in the 1862 block**;
- **Hörde: still unresolved in Mss 25**;
- **first companion beside von Hoff: looks Alberts/Albers, not yet identifiable; do not silently replace with Daelen.**

## 3. Negative visual check on the 1862 diagrams

Entries 316–321 contain many furnace profiles, sections, burden recipes, hot-/cold-blast comparison, dimensions, labour/cost data and works names. On the present visual pass, no diagram can yet be securely identified as a Bessemer converter or as the specific portable plant drawing described retrospectively in 1903.

Use this only as a routing negative:

> the visually obvious diagrams in the checked 1862 pages are predominantly blast-furnace/oven/works sections; the Bessemer plant drawing, if present, has not yet been isolated.

Do not convert this into an absence claim for the notebook as a whole.

## 4. Explicit source-mode boundary: `Cornwall aus de la Beche`

OCR entry 339 / PDF 340 is a nearly blank title/divider leaf with a completely clear manuscript heading:

**`Cornwall aus de la Beche.`**

This is first-order evidence that Wedding deliberately marked a Cornwall knowledge layer as derived **from de la Beche**, rather than from immediate site observation.

The heading is analytically stronger than an inferred `copied-reference` tag: Wedding himself marks provenance at the section level.

## 5. Entry 341 / PDF 342 can be tied directly to de la Beche's 1839 report

The following written leaf is headed **`Cornwall 4.`** and begins with `Vanning`. It then contains English prose on copper ores being dressed, sampled and sold at ticketings, followed by a passage on the Duchy of Cornwall, stannary jurisdiction, twenty-four stannators and their parliament/speaker.

External source cross-control identifies both passages in Henry De la Beche, *Report on the Geology of Cornwall, Devon and West Somerset* (1839):

- p. 596: copper ores `After being dressed, sampled, and sold at the ticketings...` before export to South Wales;
- p. 618: the tinners' exemption from other jurisdiction except cases affecting land/life/limb; consent of twenty-four stannators from four divisions; their meeting termed a parliament and their choosing a speaker.

The wording and order are close enough to treat entry 341 as a **controlled de la Beche extraction/copy layer**, not merely a generic Cornwall reference page.

This gives a concrete source transformation:

**printed geological/economic report → selected notebook excerpt → juxtaposition with field/works technical notes.**

## 6. The 1863 Cornwall material is source-mode interleaved, not one homogeneous section

The de la Beche divider does not mean all subsequent Cornwall pages are copied from print. Image control shows a rapid return to dated technical/site notes:

### Entry 343 / PDF 344

A clear top-right date reads approximately **`8ten August 63.`**. The German text immediately discusses **Great Devon Consols bei Tavistock**, vein geometry, depth/length, underground working and quantitative production/technical details.

Tag provisionally as `1863_DATED_SITE_TECHNICAL_NOTE`; whether every datum is direct observation, oral report or copied from mine documentation still requires sentence-level source tagging.

### Entry 346 / PDF 347

The page has a clear **`16t. Aug. 63.`** heading. It describes a Cornwall mine north of **Menheniot bei Liskeard**, with readable mine names including **Wheal Mary Ann** and a second `Wheal ...` name still requiring palaeographic control, plus strike/dip and mine-operation detail.

Tag as `1863_DATED_SITE_TECHNICAL_NOTE` with exact second mine name pending.

Therefore the correct architecture is not `Krug field notes → de la Beche copied section` as two clean consecutive blocks. Rather, **dated technical notes and copied/reference leaves are interleaved inside the same reused notebook**.

## 7. Consequence for the project's datum-source schema

Mss 25 now forces a stricter distinction between chronology and provenance. For every technical datum, maintain separate fields for:

- year/date layer;
- place/work/mine;
- document mode;
- datum source: `DIRECT_OR_SITE_NOTE | ORAL_REPORT | WORKS_DOCUMENT | DRAWING/SKETCH | PRINT_COPY | COMPARATIVE_REASSEMBLY | UNCERTAIN`;
- named source when explicit (`de la Beche`);
- image-control confidence.

A place/date alone is insufficient. The same Cornwall sequence can move between named printed authority, dated mine note, comparative calculation and diagram within a handful of leaves.

## 8. Revised Bessemer actor status

Secure now:

- the 1903 memoir states personal Bessemer instruction in Sheffield and a Sheffield journey with Daelen and von Hoff;
- `von Hoff` is manuscript-secure in the 1862 Mss 25 comparison layer;
- the 1862 block also contains Sheffield/Rotherham, Cumberland, Ebbw Vale and furnace/comparison material.

Still open:

- Daelen in the notebook;
- Hörde in the notebook;
- Bessemer by name in the notebook;
- the specific plant/converter drawing carried back from England;
- whether the `Alberts/Albers` companion beside von Hoff is historically relevant to the Bessemer episode.

## 9. Immediate resume point

1. Continue through the 1862 block with the actor names held open rather than normalised.
2. Search the manuscript visually, not just OCR, for Daelen/Hörde/Bessemer/converter/`Zeichnung` around the 1862 Sheffield/Rotherham comparison pages.
3. Continue the 1863 Cornwall sequence while tagging datum provenance page by page.
4. Use `Cornwall aus de la Beche` as the first controlled exemplar of explicit **PRINT_COPY provenance** inside Mss 25.

Most important additions from this pass:

> **The fuzzy Daelen and Hörde OCR candidates collapse under image control, while `von Hoff` survives.**

> **Wedding explicitly labels a notebook knowledge layer `Cornwall aus de la Beche`, and at least one following page can be matched directly to de la Beche's 1839 printed report.**
