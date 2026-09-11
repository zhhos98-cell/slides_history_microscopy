# Wedding Mss 25 — corrected transcription layer by confidence

**Branch:** `research/wedding-mss25-json-correction`  
**Authority order:** original PDF image > corrected transcription > PaddleOCR JSON.  
**Status:** active side-stream begun 2026-09-11.

This file is a correction/transcription layer for `wedding_mss25.pdf_by_PaddleOCR-VL-1.6.json`. The raw PaddleOCR JSON is preserved unchanged as a discovery/indexing artifact. Corrections are entered only after direct comparison with the original PDF image.

## Confidence protocol

- **A — secure:** directly legible in the manuscript image; letterforms and local context agree. Safe for factual citation at the manuscript-reading level.
- **B — probable:** the reading is strongly favoured, but one or more letters/word boundaries remain ambiguous. May guide searching; do not silently promote to A.
- **C — tentative:** plausible working reading only. Keep out of substantive claims until rechecked against a better image/context.

Each correction records: OCR entry, PDF page, raw OCR state, image-controlled reading, confidence, and a short note. Page numbering here is the PDF page number, not manuscript foliation.

---

# A — secure readings

## OCR entry 315 / PDF 316

### A315.1 — heading omitted by OCR
- **Raw OCR:** heading not recovered.
- **Corrected reading:** `Abercarn near Newport. Mon.`
- **Confidence:** A
- **Note:** large heading at top of page.

### A315.2 — year omitted/corrupted by OCR
- **Raw OCR:** opening OCR begins with noise (`I am full...`) and does not preserve the year heading.
- **Corrected reading:** `1862`
- **Confidence:** A
- **Note:** underlined year below the Abercarn heading.

### A315.3 — comparison label
- **Raw OCR:** `B — Low Moor`
- **Corrected reading:** `B — Low Moor`
- **Confidence:** A
- **Note:** OCR happened to preserve this short label adequately.

### A315.4 — printed-reference title / author
- **Raw OCR:** `On the construction of hot black ovens for six furnaces by Henry Martea.`
- **Corrected reading:** `On the construction of hot blast ovens for iron furnaces by Henry Marten.`
- **Confidence:** A
- **Note:** handwritten English bibliographic reference; `black`→`blast`, `six`→`iron`, `Martea`→`Marten` are OCR failures.

### A315.5 — place/reference continuation
- **Raw OCR:** `(Wolverhampton)` is partially preserved after a corrupted preceding phrase.
- **Corrected reading:** `(Wolverhampton)`
- **Confidence:** A

### A315.6 — Sheffield section number
- **Raw OCR:** `2. Difficult:` / later Brown material; section heading lost.
- **Corrected reading:** `9. Sheffield:`
- **Confidence:** A
- **Note:** underlined section heading in lower half of page.

### A315.7 — Rotherham / Sheffield actor-place line
- **Raw OCR:** `— Bat Mr Reale ji Dofuchuan lai Sheffield`
- **Corrected reading:** `bei Mr Beale in Rotherham bei Sheffield`
- **Confidence:** A
- **Note:** bottom line of page. This anchors Beale/Rotherham to the 1862 comparison layer.

## OCR entry 316 / PDF 317

### A316.1 — actor name omitted by OCR
- **Raw OCR:** top line omitted entirely.
- **Corrected reading:** `von Hoff`
- **Confidence:** A
- **Note:** final actor name in the opening line is manuscript-secure. Do not infer the preceding companion from the 1903 memoir.

### A316.2 — works/place heading
- **Raw OCR:** appears only indirectly in corrupted technical text.
- **Corrected reading:** `Ebbw Vale`
- **Confidence:** A
- **Note:** underlined heading in the upper-middle part of the page.

## OCR entry 322 / PDF 323

### A322.1 — dated companion heading
- **Raw OCR:** `Nur garon von Thurg: 1869.`
- **Corrected reading:** `Mit Herrn von Krug: 1863.`
- **Confidence:** A
- **Note:** decisive OCR failure. The manuscript explicitly dates the Krug layer to 1863.

### A322.2 — regional heading
- **Raw OCR:** `Lornwal`
- **Corrected reading:** `Cornwall`
- **Confidence:** A
- **Note:** underlined heading directly below the Krug line.

### A322.3 — place
- **Raw OCR:** `Taviock`
- **Corrected reading:** `Tavistock`
- **Confidence:** A

### A322.4 — mine name
- **Raw OCR:** `Great Seven Comets`
- **Corrected reading:** `Great Devon Consols`
- **Confidence:** A
- **Note:** the mine name is clear enough on the original image even though the OCR is severely distorted.

### A322.5 — preceding comparison heading
- **Raw OCR:** `Steffeld Brown:`
- **Corrected reading:** `Sheffield Brown:`
- **Confidence:** A
- **Note:** this material precedes `Mit Herrn von Krug: 1863.` and should not automatically be assigned to the Cornwall section.

---

# B — probable readings

## OCR entry 316 / PDF 317

### B316.1 — opening companion phrase
- **Raw OCR:** line omitted entirely.
- **Corrected reading:** `Mit Alberts … von Hoff.`
- **Confidence:** B
- **Note:** `von Hoff` is A-secure; the first companion reads most plausibly as `Alberts` (possibly `Albers`/another close form). Preserve the ambiguity. **Do not normalize this name to Daelen from expectation.**

---

# C — tentative readings

No C-level readings have yet been promoted into this file. Add them only when they are useful enough to preserve but still too uncertain for B.

---

# Working rules for the side-stream

1. Do not edit or overwrite the raw PaddleOCR JSON.
2. Use JSON only to route candidate pages; adjudication comes from the original PDF image.
3. Record omissions as corrections, not only wrong OCR strings.
4. Split mixed-confidence phrases when necessary (`von Hoff` A; preceding companion B).
5. Keep literal manuscript wording separate from contextual normalization.
6. Dates inferred from section context must be labelled as inference; literal dates remain literal.
7. Named entities that matter to the Bessemer/Hörde problem receive priority visual checking: `Daelen`, `von Hoff`, `Hörde`, `Bessemer`, `Zeichnung`, converter/plant-arrangement language.
8. Continue sequentially through the 1862 block before broadening to South Wales/Abercarn, except where an obvious high-value correction appears during routing.

## Current correction frontier

Initial controlled anchors entered from PDF 316, 317 and 323. Next pass should continue image-controlled comparison through the intervening 1862 technical pages, then return to the South-Wales/Abercarn block using the provenance-aware distinction between visit note, reused heading, copied source, diagram and comparative reassembly.
