# CURRENT PROGRESS — Iron Library / Wedding / Sheffield–Berlin

**Pinned continuation state — updated 2026-09-11 after full Wedding OCR routing + first image-controlled Mss 25 chronology pass.**

This is the authoritative resume point for the active Iron Library project. Read the detailed checkpoint files for evidence, but resume from the state below rather than from older OCR-only chronology.

## 1. Governing research problem

The project is no longer a generic Iron Library search and no longer a simple `Sorby → Wedding → Martens` diffusion story.

Controlled comparative sequence:

**industrial travel / works comparison → travelling sample → external test / expert judgement → numbering / provenance / collection → prepared specimen → microscopic field → microphotography → printed / institutional reference system.**

The core question is how material comparison changed scale, evidential carrier, access regime, preparation practice, institutional setting and reference structure while remaining a comparative activity. Geographic/institutional axis: **Sheffield ↔ Berlin/Charlottenburg**, with Schaffhausen/Fischer supplying the pre-Wedding baseline.

## 2. Wedding corpus: OCR pass complete at routing level

The three PaddleOCR JSONs are present in the repository root and are accepted as the discovery/indexing layer, not diplomatic transcription:

- `wedding_mss23.pdf_by_PaddleOCR-VL-1.6.json`
- `wedding_mss24.pdf_by_PaddleOCR-VL-1.6.json`
- `wedding_mss25.pdf_by_PaddleOCR-VL-1.6.json`

Full corpus: 740 OCR entries, 609 with non-empty text. Every entry has now been routed once for recognisable content.

Working indices:

- `WEDDING_MSS25_ITINERARY_AND_DOCUMENT_MODE_INDEX.tsv`
- `WEDDING_MSS24_ITINERARY_SKELETON.tsv`
- `WEDDING_MSS23_PROCESS_HEADING_INDEX.tsv`
- `WEDDING_FULL_OCR_READING_LOG_2026-09-11.md`

The longitudinal architecture remains useful:

**Mss 23: process decomposition / quantitative training → Mss 24: domestic cross-site comparison → Mss 25: transnational access + works/mining comparison + documentary/reference accumulation.**

## 3. Critical correction: Mss 25 is a multi-year working notebook

Image control has superseded the old assumption that the British material after the 1860 study journey can be read as one continuous itinerary.

Current controlled year layers:

### 1860 — long comparative study journey

The 1903 memoir retrospectively describes a long Belgium/England journey before the March 1861 Bergreferendar examination and says the examination included comparison of South-Welsh and Upper-Silesian blast-furnace practice. Mss 25 supplies the contemporary working record.

Image-controlled northern sequence now includes:

- **9–10 July 1860, Coventry**;
- **19–23 July, Manchester**, including **William Fairbairn**;
- **24 July, Leeds / Sheffield**, including **Turton & Sons**;
- **26 July, Leeds**, **Peter Fairbairn's Maschinenwerkstätte**;
- **Friday 27 July, Low Moor**, `Mr. Fenton`;
- **Saturday 28 July, Bowling Works**;
- **Tuesday 31 July, Newcastle upon Tyne**, **Losh, Wilson & Bell**;
- early August Scottish sequence culminating in **Monday 6 Aug., Govan Works in Glasgow**;
- **Gartsherrie Iron Works**, with `Mr. Whitelaw` and manager `G. Campbell` legible enough to route.

Earlier South-West / South-Wales / Abercarn material remains controlled at OCR-routing level and is queued for selective visual correction.

### 1862 — explicit Sheffield/Rotherham comparison/reference layer

Mss 25 entry 315 is image-controlled and explicitly headed **`1862`**. It is a mixed comparison/reference sheet, not a 1860 visit page.

Recognisable content includes:

- Low Moor / Cumberland comparison;
- a reference to `On the construction of hot blast ovens for iron furnaces by Henry Marten`;
- numbered **`9. Sheffield`** section;
- Brown/Atlas Works-type line still needing exact control;
- armour-plate dimensions and quantitative notes;
- **`bei Mr Beale in Rotherham bei Sheffield`**.

This page demonstrates that Wedding reused the notebook as a comparative/reference instrument after the 1860 journey.

### 1863 — explicit Krug von Nidda layer

Mss 25 entry 322 is image-controlled. A new section reads:

**`Mit Herrn von Krug: 1863.`**

followed by **`Cornwall`** and a Tavistock / **Great Devon Consols** section.

This is contemporary manuscript-level dating for at least the Cornwall segment of the Krug journey described retrospectively in the 1903 memoir. Do not automatically assign every later Cornwall page to this section until its forward boundary is controlled.

Detailed evidence:

- `WEDDING_MSS25_VISUAL_CONTROL_PASS1_2026-09-11.md`
- `WEDDING_1903_MEMOIR_CROSS_CONTROL_2026-09-11.md`

## 4. Bessemer / Daelen / von Hoff / Hörde problem: current state

The 1903 memoir securely states that Wedding:

- was instructed by **Bessemer himself in Sheffield** about the arrangement/execution of the process/plant;
- brought **drawings** back from England;
- says those drawings were used in connection with Königshütte and Hörde installations;
- travelled to Sheffield with Hörde leaders **Daelen and von Hoff**;
- advocated **Cumberland pig iron**, later contrasting its performance with Upper-Silesian material.

The memoir supplies the retrospective chain, but not the exact notebook date.

A complete targeted OCR/fuzzy pass has now been run over Mss 25:

- no literal `Bessemer` hit is secure;
- no Daelen or von Hoff candidate can yet be promoted;
- no reliable `Zeichnung(en)` hit anchors the retrospective drawings in the 1862–63 block;
- the most important candidate is **entry 316**, immediately after the explicit 1862 Sheffield/Rotherham page, where OCR gives **`Von Börde Muster (Re...)`** amid Cumberland / Forest of Dean comparison material. This could be an OCR corruption of `Hörde`, but this is **not yet evidence** and requires image control.

Detailed routing note:

`WEDDING_BESSEMER_TARGETED_OCR_PASS1_2026-09-11.md`

## 5. Immediate resume point

Do **not** return to broad searching and do **not** reopen blanket OCR.

Priority sequence:

1. visually control **Mss 25 entry 316** and resolve `Von Börde Muster` / possible Hörde;
2. walk entries **317–321** page by page to establish the full 1862 block and inspect specifically for Bessemer / converter / Daelen / von Hoff / plant arrangement / drawings;
3. control the transition immediately above `Mit Herrn von Krug: 1863` on entry 322;
4. follow entries **323–330** to map the early 1863 Krug layer and separate direct visit notes from copied/reference material;
5. only after this, date the retrospective Bessemer episode if the manuscript permits it;
6. then return to the South-Wales/Abercarn visual-control queue and the Mss 24/Mss 23 selective checks.

Highest-value unresolved question:

> **Can the Bessemer / Daelen / von Hoff / Hörde / drawings episode be located inside the 1862 or 1863 Mss 25 layer, and can the notebook show the form of the portable technical inscription Wedding later said he carried back from England?**

## 6. Claim ceilings

Secure now:

- current OCR is adequate as a routing/indexing layer;
- Mss 25 contains distinct image-controlled **1860, 1862 and 1863** British layers;
- William Fairbairn, Peter Fairbairn, Turton & Sons, Low Moor, Bowling Works, Losh/Wilson/Bell, Govan and Gartsherrie are image-controlled anchors in the 1860 northern sequence;
- the 1862 page contains Sheffield/Rotherham + Cumberland comparison material;
- `Mit Herrn von Krug: 1863` is explicit in the manuscript;
- the 1903 memoir claims personal Bessemer instruction in Sheffield and a Sheffield journey with Daelen/von Hoff.

Still open:

- exact date/year of the Bessemer instruction episode;
- whether entry 316 actually reads Hörde;
- whether Daelen/von Hoff are present in Mss 25 under corrupted OCR;
- whether Wedding's England-derived drawings survive as drawings/copies in the notebook;
- whether the retrospective Bessemer episode belongs to 1862, 1863 or another section;
- any direct Wedding–Sorby co-presence/contact claim.

## 7. Background files to retain

For the Fischer baseline, external controls, later Wedding/Martens visual-evidence sequence, and onsite logic, retain:

- `FISCHER_1845_1846_EVENT_INDEX.tsv` and associated Fischer analysis files;
- `EXTERNAL_SOURCE_EXPANSION_2026-09-11.md` + later passes;
- `WEDDING_NOTEBOOK_CITATION_AUDIT.md`;
- Wedding 1885 / Martens reference-system research notes;
- `RESIDENCY_TRIAGE_2026-09-11.md`;
- `PUBLIC_DIGITAL_CORPUS.md`;
- `SOURCE_MAP.md`.

The later endpoint remains analytically important: prepared physical sections and microphotographic image collections become distinct institutional reference systems at Berlin/Charlottenburg. The immediate work, however, stays on the page-level Wedding manuscript bridge.

## Resume order

1. `CURRENT_PROGRESS.md`
2. `WEDDING_MSS25_VISUAL_CONTROL_PASS1_2026-09-11.md`
3. `WEDDING_BESSEMER_TARGETED_OCR_PASS1_2026-09-11.md`
4. `WEDDING_1903_MEMOIR_CROSS_CONTROL_2026-09-11.md`
5. `WEDDING_MSS25_ITINERARY_AND_DOCUMENT_MODE_INDEX.tsv`
6. `WEDDING_FULL_OCR_READING_LOG_2026-09-11.md`
7. Mss 25 OCR JSON / images as needed.

**Immediate resume condition: visually resolve entry 316 and continue the 1862 block.**
