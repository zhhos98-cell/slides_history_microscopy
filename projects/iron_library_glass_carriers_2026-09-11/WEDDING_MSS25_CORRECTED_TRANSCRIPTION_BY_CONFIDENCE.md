# Wedding Mss 25 — corrected transcription layer by confidence

**Branch:** `research/wedding-mss25-json-correction`  
**Authority order:** original PDF image > corrected transcription > PaddleOCR JSON.  
**Status:** active side-stream begun 2026-09-11.

This file is the single correction/transcription layer for `wedding_mss25.pdf_by_PaddleOCR-VL-1.6.json`. The raw PaddleOCR JSON is preserved unchanged as a discovery/indexing artifact. Corrections are entered only after direct comparison with the original PDF image.

## Confidence protocol

- **A — secure:** directly legible in the manuscript image; letterforms and local context agree. Safe for factual citation at the manuscript-reading level.
- **B — probable:** the reading is strongly favoured, but one or more letters/word boundaries remain ambiguous. May guide searching; do not silently promote to A.
- **C — tentative:** plausible working reading only. Keep out of substantive claims until rechecked against a better image/context.

Each correction records OCR entry, PDF page, raw OCR state, image-controlled reading, confidence, and a short note. Page numbering here is the PDF page number, not manuscript foliation.

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

### A315.4 — printed-reference title / author
- **Raw OCR:** `On the construction of hot black ovens for six furnaces by Henry Martea.`
- **Corrected reading:** `On the construction of hot blast ovens for iron furnaces by Henry Marten.`
- **Confidence:** A
- **Note:** `black`→`blast`, `six`→`iron`, `Martea`→`Marten` are OCR failures.

### A315.5 — place/reference continuation
- **Raw OCR:** `(Wolverhampton)` partially preserved.
- **Corrected reading:** `(Wolverhampton)`
- **Confidence:** A

### A315.6 — Sheffield section number
- **Raw OCR:** section heading lost/corrupted.
- **Corrected reading:** `9. Sheffield:`
- **Confidence:** A

### A315.7 — Rotherham / Sheffield actor-place line
- **Raw OCR:** `— Bat Mr Reale ji Dofuchuan lai Sheffield`
- **Corrected reading:** `bei Mr Beale in Rotherham bei Sheffield`
- **Confidence:** A
- **Note:** bottom line of page; anchors Beale/Rotherham to the 1862 comparison layer.

## OCR entry 316 / PDF 317

### A316.1 — actor name omitted by OCR
- **Raw OCR:** top line omitted entirely.
- **Corrected reading:** `von Hoff`
- **Confidence:** A
- **Note:** final actor name in the opening line is manuscript-secure.

### A316.2 — works/place heading
- **Raw OCR:** not reliably recovered.
- **Corrected reading:** `Ebbw Vale`
- **Confidence:** A

## OCR entry 317 / PDF 318

### A317.1 — repeated/reused page heading
- **Raw OCR:** heading omitted.
- **Corrected reading:** `Abercarn near Newport. Mon.`
- **Confidence:** A
- **Note:** recurrence of the heading does not by itself prove that every datum below it is a fresh Abercarn site note.

### A317.2 — works/place name
- **Raw OCR:** corrupted in surrounding text.
- **Corrected reading:** `Ebbw Vale`
- **Confidence:** A

### A317.3 — material line
- **Raw OCR:** `Raw Welsh Mike = 32,05` / corrupted variants.
- **Corrected reading:** `Raw Welsh Mine = 32,05`
- **Confidence:** A

### A317.4 — material line
- **Raw OCR:** `Black band = 2,94`
- **Corrected reading:** `Black band = 2,94`
- **Confidence:** A

### A317.5 — blast headings
- **Raw OCR:** headings not reliably preserved as structure.
- **Corrected reading:** `Hot blast` / `Cold blast`
- **Confidence:** A
- **Note:** distinct lower-page comparison headings.

## OCR entry 318 / PDF 319

### A318.1 — works/place heading
- **Raw OCR:** garbled/omitted.
- **Corrected reading:** `Cyfarthfa`
- **Confidence:** A
- **Note:** underlined heading in lower-middle page.

### A318.2 — actor pair
- **Raw OCR:** `Eylartuga Mr. Morgan so Mr. Jones.`
- **Corrected reading:** `Cyfarthfa. Mr. Morgan und Mr. Jones`
- **Confidence:** A

### A318.3 — works/place heading
- **Raw OCR:** corrupted in following technical block.
- **Corrected reading:** `Dowlais`
- **Confidence:** A
- **Note:** underlined heading directly below the Cyfarthfa actor block.

## OCR entry 319 / PDF 320

### A319.1 — repeated/reused page heading
- **Raw OCR:** omitted.
- **Corrected reading:** `Abercarn near Newport. Mon.`
- **Confidence:** A
- **Note:** page is furnace/charge/labour/cost comparison with diagrams; classify the content separately from the inherited heading.

## OCR entry 320 / PDF 321

### A320.1 — works heading
- **Raw OCR:** OCR produces multiple distorted forms.
- **Corrected reading:** `Govan Iron Works`
- **Confidence:** A
- **Note:** underlined works name in the middle-left region.

### A320.2 — actor surname
- **Raw OCR:** partially distorted.
- **Corrected reading:** `Campbell`
- **Confidence:** A
- **Note:** secure surname in the actor/works line above the Govan block; surrounding names remain to be controlled.

### A320.3 — works heading
- **Raw OCR:** `Gartskerrie` / similar variants.
- **Corrected reading:** `Gartsherrie`
- **Confidence:** A
- **Note:** underlined in lower-left page.

### A320.4 — material term
- **Raw OCR:** `Blackbaw` / related corruption.
- **Corrected reading:** `Blackband`
- **Confidence:** A
- **Note:** occurs in the Gartsherrie charge/material notes.

## OCR entry 321 / PDF 322

### A321.1 — works/place continuation
- **Raw OCR:** page is largely hallucinated/garbled.
- **Corrected reading:** `Gartsherrie`
- **Confidence:** A
- **Note:** secure in the upper technical context.

### A321.2 — regional/place anchor
- **Raw OCR:** not reliably preserved.
- **Corrected reading:** `Newcastle`
- **Confidence:** A
- **Note:** secure inside the central works/place line; the full institutional name around it remains unresolved.

## OCR entry 322 / PDF 323

### A322.1 — dated companion heading
- **Raw OCR:** `Nur garon von Thurg: 1869.`
- **Corrected reading:** `Mit Herrn von Krug: 1863.`
- **Confidence:** A
- **Note:** decisive OCR failure; manuscript explicitly dates the Krug layer to 1863.

### A322.2 — regional heading
- **Raw OCR:** `Lornwal`
- **Corrected reading:** `Cornwall`
- **Confidence:** A

### A322.3 — place
- **Raw OCR:** `Taviock`
- **Corrected reading:** `Tavistock`
- **Confidence:** A

### A322.4 — mine name
- **Raw OCR:** `Great Seven Comets`
- **Corrected reading:** `Great Devon Consols`
- **Confidence:** A

### A322.5 — preceding comparison heading
- **Raw OCR:** `Steffeld Brown:`
- **Corrected reading:** `Sheffield Brown:`
- **Confidence:** A
- **Note:** precedes `Mit Herrn von Krug: 1863.` and should not automatically be assigned to the Cornwall section.

---

# B — probable readings

## OCR entry 316 / PDF 317

### B316.1 — opening companion phrase
- **Raw OCR:** line omitted entirely.
- **Corrected reading:** `Mit Alberts … von Hoff.`
- **Confidence:** B
- **Note:** `von Hoff` is A-secure; the first companion reads most plausibly as `Alberts` (possibly `Albers`/another close form). Preserve the ambiguity. **Do not normalize this name to Daelen from expectation.**

## OCR entry 317 / PDF 318

### B317.1 — Ebbw Vale technical sentence
- **Raw OCR:** heavily corrupted.
- **Corrected reading:** sentence begins `Die Ebbw Vale ...`
- **Confidence:** B
- **Note:** remainder requires a closer crop before diplomatic transcription.

## OCR entry 321 / PDF 322

### B321.1 — Newcastle works line
- **Raw OCR:** not trustworthy.
- **Corrected reading:** full line contains `Newcastle`, but first word/institutional name is unresolved.
- **Confidence:** B
- **Note:** retain only `Newcastle` at A until the whole line is crop-controlled.

---

# C — tentative readings

No C-level readings have yet been promoted into this file. Add them only when useful enough to preserve but still too uncertain for B.

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
9. Repeated page headings such as `Abercarn near Newport. Mon.` are stored separately from document mode; heading recurrence is not automatic evidence that all underlying content is direct site observation.

## Current correction frontier

Image-controlled correction now spans PDF 316–323 at anchor level. The highest-priority unresolved reading remains the first companion beside `von Hoff`, plus any occurrence of `Daelen`, `Hörde`, `Bessemer`, `Zeichnung`, converter or plant-arrangement language in the 1862 technical block. Next pass should use tighter crops on PDF 317–322 to convert selected B-level proper nouns and technical lines to A, then continue into the South-Wales/Abercarn block with the same provenance-aware protocol.
