# CURRENT PROGRESS — Iron Library / Wedding / Sheffield–Berlin

**Pinned continuation state — updated 2026-09-11 during sequential PDF-controlled transcription.**

This is the authoritative resume point. Older OCR-only Bessemer chronology is superseded by the image-controlled 1860 identification below.

## 1. Governing problem

The project is not a simple `Sorby → Wedding → Martens` diffusion story. Current transformation sequence:

**industrial travel / works comparison → heterogeneous portable research container → travelling sample / test / expert judgement → standardized prepared object → numbering / collection → microscopic field → microphotography → institutional reference system.**

Main axis: **Sheffield ↔ Berlin/Charlottenburg**, with Fischer 1845–46 as the pre-Wedding comparison baseline.

## 2. Wedding corpus state

All three Wedding PaddleOCR JSONs have been routed once: **740 entries, 609 non-empty**. All 740 PDF pages have also received a structural visual survey, but that survey is not counted as transcription. OCR remains discovery/navigation, not diplomatic transcription.

Major working files now include:

- `WEDDING_FULL_OCR_READING_LOG_2026-09-11.md`
- `WEDDING_MSS25_ITINERARY_AND_DOCUMENT_MODE_INDEX.tsv`
- `WEDDING_MSS25_VISUAL_CONTROL_PASS1_2026-09-11.md` through `PASS4`
- `WEDDING_MSS25_SOURCE_MODE_INDEX_1862_1863.tsv`
- `WEDDING_MSS25_TAIL_PROVENANCE_INDEX.tsv`
- `corrected_transcription/README.json`
- `corrected_transcription/WEDDING_MSS23_CORRECTED_TRANSCRIPTION.jsonl`
- `corrected_transcription/WEDDING_MSS24_CORRECTED_TRANSCRIPTION.jsonl`
- `corrected_transcription/WEDDING_MSS25_CORRECTED_TRANSCRIPTION.jsonl`
- **`WEDDING_1860_BESSEMER_MANUSCRIPT_BREAKTHROUGH_2026-09-11.md`**
- `WEDDING_1903_MEMOIR_CROSS_CONTROL_2026-09-11.md`

Longitudinal architecture remains:

**Mss 23: process decomposition / quantitative training → Mss 24: domestic cross-site comparison → Mss 25: transnational, multi-year, heterogeneous research container.**

### Corrected-transcription ledger checkpoint

All 740 PDF pages now have stable rows in the separate JSONL ledgers; the PaddleOCR JSON remains immutable. Each row carries `status`, `confidence`, `transcription`, `secure_anchors`, `doubtful_readings`, OCR-noise flags and a page-level note. A row counts as substantively transcribed only when actual readable wording has been entered from the PDF. Generic structural descriptions are marked `IMAGE_REVIEWED_AWAITING_TRANSCRIPTION`, not as completed transcription.

The **Mss 23 textual sequence is complete through PDF 210**. Work has continued into **Mss 24 through PDF 25**. PDFs 6-15 contain substantive image-controlled transcriptions of the Thüringer-Wald/Franken itinerary, route maps, geological profiles, lithological legends, measured dips/elevations and fossil lists. PDFs 16-25 add Nürnberg-Bamberg-Frankfurt-Heidelberg travel observations and a dense Saarbrücken coalfield sequence: seam-thickness tables, basin dimensions, mine-roadway sections, pillar extraction, gradients, haulage apparatus, ventilation, fire control, wages and the full-page coalfield map. The final Mss 23 batch transcribes PDFs 191-203 and the complete bibliographic note on PDF 206; PDFs 204-205 and 207-210 are confirmed blank, and PDFs 211-223 are object/digitisation views. Sequential work now resumes at **Mss 24 PDF 26**. The remaining Mss 24 text and most of Mss 25 still await page-level substantive transcription. The out-of-sequence Mss 25 Bessemer cluster at PDFs 295-300 and the source heading at PDF 340 retain their separately verified readings. Any earlier statement that all 740 pages had been fully transcribed is superseded by this checkpoint.

The first direct PDF-control batch covers Mss 25 PDFs 295–300. It rejects Paddle hallucination on PDF 297, secures `Mittwoch 25 Juli 1860`, `Sheffield White Lead Works`, `Barker & Sons`, `Bessemer's Stahlwerk`, the Cumberland pig-iron statement, `Der ganze Prozeß dauert cca 19-24 Minuten`, `Cammells Maschinen (Cyclops Works)`, and the transition to `Donnerstag 26 Juli. Leeds` / `Peter Fairbairn's Maschinenwerkstätte`. Continuous technical Kurrent remains selectively transcribed and ellipsed rather than guessed. The supplied `10598` JSON remains outside this correction ledger because the corresponding PDF was not supplied.

## 3. Critical breakthrough: Bessemer encounter is 1860, and the notebook section is found

A first-person retrospective by Wedding in *Stahl und Eisen*, 15 May 1896, reporting the Iron and Steel Institute London meeting of 7–8 May, fixes the chronology. Wedding says that long stays at English ironworks in **1860 and 1862** plus the Krug journey gave him technical experience; he then says that **already in 1860**, through Sir Henry Bessemer's extraordinary kindness, he came to know Bessemer's new process **in Sheffield**. In the same reply he says the Hörde Bessemer works was built on his urgent initiative and the Königshütte works according to his designs.

This is stronger chronological control than the later 1903 memoir alone.

### Mss 25 July 1860 sequence

Image control now gives:

- **24 July — Leeds / Sheffield**, Turton & Sons;
- **Wednesday 25 July 1860 — Sheffield White Lead Works**, Rawson/Barker-type firm wording;
- continuation of White Lead Works process notes;
- **`Bessemer's Stahlwerk`** — dedicated section, manuscript p.149 / PDF 298;
- continuation of Bessemer process notes, manuscript p.150 / PDF 299;
- Cammell / **Cyclops Works**-type Sheffield heading;
- **Thursday 26 July — Leeds**, Peter Fairbairn's Maschinenwerkstätte.

The Bessemer heading itself does not repeat the date. Strict claim: it lies between the explicit 25 July Sheffield entry and explicit 26 July Leeds entry. Strong folio-sequence inference: **the Bessemer visit belongs to 25 July 1860**.

## 4. Contemporary Bessemer technical inscription is now visible

PDF 298 / manuscript p.149 is headed clearly:

**`Bessemer's Stahlwerk`**

It contains:

- a large **pear-shaped tilting converter/vessel drawing on a horizontal trunnion axis**;
- sectional/base/tuyere-type diagramming;
- multiple grouped blast/opening marks;
- technical operational prose;
- a clear raw-material statement beginning **`Es wird Roheisen meist aus Cumberland verbraucht ...`**.

PDF 299 continues the process and includes another vessel/spout sketch. One highly legible sentence reads:

**`Der ganze Prozeß dauert cca 19–24 Minuten.`**

Surrounding prose divides the blow/process into stages and comments on gas/flame behaviour. Exact transcription remains selective.

This substantially answers the previous carrier question: Mss 25 preserves a **contemporary portable technical inscription package** made at/for Bessemer's Sheffield works: converter drawing + process geometry + Cumberland material specification + timing/stage notes.

Claim ceiling: these leaves have not yet been proven to be the exact later `Entwürfe` used for Königshütte/Hörde. They are, however, securely contemporary Bessemer works drawings and process notes in Wedding's 1860 travel notebook.

## 5. Revised relation to the 1862 and 1863 layers

The 1862 and 1863 discoveries remain important but they are no longer the primary place to date the first Bessemer encounter.

### 1862

Explicit `1862` comparison block includes Sheffield/Rotherham, Low Moor/Cumberland, Henry Marten reference material, armour-plate data and a manuscript-secure **`von Hoff`**. Earlier fuzzy Daelen and Hörde OCR candidates failed visual control.

Interpretation now: the 1862 layer may document **later comparison/reuse/networking around British iron and Sheffield/Hörde actors**, while the first Bessemer process encounter is already secured in 1860.

### 1863

Explicit **`Mit Herrn von Krug: 1863.`** section begins a Cornwall/Tavistock/Great Devon Consols layer, with direct/site notes interleaved with copied-reference material.

## 6. Provenance / carrier architecture of Mss 25

Separate image-control passes establish that Mss 25 mixes:

- dated site/works notes;
- comparative reassembly;
- diagrams and sketches;
- copied printed authority;
- bibliographic routing;
- reused leaves / residual headings;
- compiled locality/mineral lists;
- physically inserted printed objects.

Key examples:

- **`Cornwall aus de la Beche.`** explicit source-provenance heading;
- pages that can be matched to de la Beche 1839;
- PDF 370: physically inserted **Geological Survey / Ordnance Survey / Edward Stanford** index-map/catalogue object;
- PDF 387: last substantive manuscript page; PDF 388 onward is object/digitisation photography.

Working concept: Mss 25 is a **portable heterogeneous research container**, not a diary.

## 7. New strongest transformation chain

The project can now test a much more concrete sequence:

**Sheffield works access, 1860 → direct Bessemer process observation → converter/process sketching + Cumberland pig-iron specification + timed operational notes → later German Hörde/Königshütte installation/design claims → later material comparison / metallography → numbered specimen and image reference systems.**

This is an evidence-carrier history rather than a generic influence story.

## 8. Immediate next work

Continue substantive PDF-controlled transcription in physical order, beginning with **Mss 24 PDF 26**, and synchronize each completed batch. Do not count page labels, document-mode descriptions or OCR routing text as transcription.

Highest-value question has changed from `when/where did Wedding meet Bessemer?` to:

> **How exactly did Wedding encode the 1860 Bessemer process in his notebook, through whom did he gain access, and how much of that portable technical inscription can be connected to the later Hörde/Königshütte installations?**

## 9. Claim ceilings

Secure:

- Wedding publicly dated his Sheffield Bessemer-process encounter to **1860** in 1896;
- Mss 25 contains a dedicated **`Bessemer's Stahlwerk`** section in the late-July 1860 Sheffield sequence;
- the section contains converter/process drawings, Cumberland pig-iron material information and process timing;
- `Der ganze Prozeß dauert cca 19–24 Minuten` is image-legible;
- 1862 `von Hoff`, 1863 Krug, de la Beche provenance and inserted Stanford map findings remain secure.

Strong inference, not yet literal manuscript date:

- the Bessemer section belongs to **25 July 1860**, because it falls after the explicit Wednesday 25 July Sheffield entry and before the explicit Thursday 26 July Leeds entry.

Open:

- exact guide/contact who enabled Bessemer access;
- whether Bessemer himself is named in the prose beyond the works heading;
- whether these exact sketches are the `Entwürfe` later used in German plants;
- Daelen in Mss 25;
- exact relation between the 1860 Bessemer notes and the separate 1862 von Hoff block;
- direct Wedding–Sorby co-presence/contact.

## Resume order

1. `CURRENT_PROGRESS.md`
2. **`WEDDING_1860_BESSEMER_MANUSCRIPT_BREAKTHROUGH_2026-09-11.md`**
3. `WEDDING_MSS25_VISUAL_CONTROL_PASS4_2026-09-11.md`
4. `WEDDING_MSS25_VISUAL_CONTROL_PASS3_2026-09-11.md`
5. `WEDDING_1903_MEMOIR_CROSS_CONTROL_2026-09-11.md`
6. Corrected-transcription ledger at Mss 24 PDF 26.

**Immediate resume condition: continue at Mss 24 PDF 26.**
