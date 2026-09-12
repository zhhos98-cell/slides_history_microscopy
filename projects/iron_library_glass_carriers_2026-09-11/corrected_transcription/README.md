# Corrected transcription workspace

This directory is the authoritative Wedding Mss 23–25 correction workspace on branch `ironlibrary-json-correction`, but the ledgers are **not uniformly citation-ready transcriptions**.

## QUALITY WARNING — 2026-09-12

A direct audit of the existing ledgers found that the Mss 24 work through PDF 65 often mixes several layers inside the same `transcription` / `secure_anchors` fields:

- literal manuscript readings;
- literal diagram/map/table labels;
- normalized names and technical terminology;
- editorial descriptions of diagrams and page structure;
- reconstructed or summarized modern prose explaining machinery, routes, geology or layout.

Some editorial image descriptions were incorrectly included in `secure_anchors`, including English terms such as `cross-section`, `columnar basalt`, `country rock`, `circular plan`, `bell`, `gas outlet`, `blast-furnace section`, and `pile diagram`. These cannot be Wedding's literal source wording and demonstrate field contamination.

Therefore the historical checkpoint **Mss 24 through PDF 65** records workflow coverage only. It does **not** certify PDFs 1–65 as scholarly verbatim transcription.

## Current workflow checkpoint

- Mss 23 textual sequence processed through PDF 210; PDFs 211–223 are object/digitisation views.
- Mss 24 has legacy mixed coverage through PDF 65, with PDFs 56–60 recalibrated into the corrected layered schema on 2026-09-12.
- Mss 24 PDFs 66–87 have now been selectively transcribed under that layered schema after direct image control.
- Mss 24 textual sequence is complete through PDF 87.
- PDFs 88–103 are image-controlled blank leaves; PDFs 104–116 are image-controlled object views.

The required five-page calibration is complete, and the same separation has been applied to PDFs 66–87. Sequential transcription should now return to the legacy mixed pages identified below, not to the blank or object-view tail.

## Quality status by corpus

### Mss 24 PDFs 1–55 and 61–65

Status: `LEGACY_MIXED_EXTRACTION_REQUIRES_CLEANUP`.

These rows are often useful for locating pages, routes, firms, technical topics, diagrams, dates and numerical values. They are not safe for exact quotation, terminology history, linguistic analysis or wording-sensitive arguments without returning to the manuscript image.

### Mss 24 PDFs 56–60

Status: `CALIBRATED_LAYERED_SELECTIVE_TRANSCRIPTION`.

These five rows separate literal manuscript wording, literal diagram labels, editorial visual description, normalized entities, uncertain readings and research summary. Their `secure_anchors` derive only from `literal_transcription` and `diagram_labels`. The calibration deliberately removes fluent reconstructions and English diagram-description terms from the source-text layer. Exact quotation still requires checking the cited phrase against the page image.

### Mss 24 PDFs 66–87

Status: `LAYERED_IMAGE_CONTROLLED_SELECTIVE_TRANSCRIPTION`.

These rows continue the calibrated field separation. Legible headings, short fragments, numbers and diagram labels are retained; unresolved Kurrent and uncertain grammatical relations remain omitted or are recorded under `uncertain_readings`. Exact quotation still requires checking the cited phrase against the page image.

### Mss 23

Generally more conservative: it more often preserves fragments, figures and uncertain bracketed readings instead of rewriting pages into fluent prose. Still selective rather than diplomatic. Exact quotation requires image control.

### Mss 25

The controlled Bessemer/Sheffield cluster (especially PDFs 295–300) is closer to the desired standard: secure headings and short literal phrases are retained while difficult continuous Kurrent is left omitted. These pages still require image control before exact quotation.

## Corrected data model

Future work and legacy cleanup must keep these evidence layers separate:

- `literal_transcription`: only source wording actually read on the manuscript page. No paraphrase, completion from context, or reconstructed sentence.
- `diagram_labels`: only literal labels written in maps, plans, tables, profiles and apparatus diagrams.
- `editorial_description`: modern description of visual form, diagram function, layout or inferred machine relation. This may be useful research data but is not transcription.
- `normalized_entities`: normalized persons, places, firms, minerals, apparatus names, etc. Search/index layer only.
- `uncertain_readings`: uncertain literal source readings.
- `research_summary`: analytical account of the page's evidential content.
- `secure_anchors`: may derive only from `literal_transcription` and `diagram_labels`. Never admit terms that exist only in `editorial_description` or `normalized_entities`.

Until the JSONL files are formally migrated to this expanded schema, apply this separation conceptually and conservatively. Do not use a complete modern explanatory sentence in the `transcription` field unless it is actually legible as Wedding's sentence.

## What counts as completed transcription from now on

A page counts as transcribed only when actual readable wording has been entered after direct image control. Generic page descriptions, OCR summaries, visual interpretation, inferred machinery/layout relations, normalized entities and topical summaries do not count.

Report **coverage** separately from **transcription quality**.

The original PaddleOCR JSON remains immutable source material. Uncertain readings stay uncertain; omitted matter remains omitted rather than being promoted from OCR or inference.

## Files

- `QUALITY_STATUS.json`: machine-readable quality override; automation should read this together with `README.json`.
- `README.json`: machine-readable historical coverage checkpoint and remaining-page lists. Important: its current `through_pdf_page` value records coverage, not citation-ready quality.
- `WEDDING_MSS23_CORRECTED_TRANSCRIPTION.jsonl`: Mss 23 ledger.
- `WEDDING_MSS24_CORRECTED_TRANSCRIPTION.jsonl`: Mss 24 ledger; PDFs 1–55 and 61–65 carry the legacy mixed-extraction warning above; PDFs 56–60 and 66–87 use the layered schema; PDFs 88–116 are blank or object-view tail pages.
- `WEDDING_MSS25_CORRECTED_TRANSCRIPTION.jsonl`: Mss 25 ledger.
- `../CURRENT_PROGRESS.md`: project-level narrative checkpoint.

## Historical/supporting material elsewhere in the project

`WEDDING_FULL_OCR_READING_LOG_*`, `WEDDING_OCR_FIRST_PASS_*`, `WEDDING_BESSEMER_TARGETED_OCR_*`, `WEDDING_MSS25_VISUAL_CONTROL_PASS*`, itinerary indexes and related research notes remain supporting material. They may contain verified anchors or useful routing information, but they are not progress or quotation authorities.

## Checkpoint provenance

Historical coverage checkpoint: commit `afe48813a03e1ff54d154761d17a25820d094b0c` (`Record substantive Mss24 progress through PDF 65`). Substantive edits include `8d159cbf19672bc500c9b52b3c7fa12b9f0677f6`; machine checkpoint update `83007e382b767e8c24e4f1f70438153391fab367`.

Quality audit supersedes the earlier assumption that all material counted as `substantive transcription` in those commits is equivalent to scholarly transcription.
