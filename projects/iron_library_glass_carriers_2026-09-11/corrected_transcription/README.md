# Corrected transcription workspace

This directory is the **authoritative substantive-transcription workspace** for Wedding Mss 23–25 on branch `ironlibrary-json-correction`.

## Resume here

Current verified sequential checkpoint: **Mss 24 through PDF 65; resume at PDF 66**.

Mss 23 textual sequence is complete through PDF 210; PDFs 211–223 are object/digitisation views. Mss 24 PDFs 6–65 contain substantive image-controlled transcription. Mss 24 PDFs 66–87 remain the next sequential text block.

## Files

- `README.json`: machine-readable checkpoint, status taxonomy and remaining-page lists. **Read this first for automation/resume.**
- `WEDDING_MSS23_CORRECTED_TRANSCRIPTION.jsonl`: page ledger for Mss 23.
- `WEDDING_MSS24_CORRECTED_TRANSCRIPTION.jsonl`: page ledger for Mss 24.
- `WEDDING_MSS25_CORRECTED_TRANSCRIPTION.jsonl`: page ledger for Mss 25.
- `../CURRENT_PROGRESS.md`: project-level narrative checkpoint.

## What counts as completed transcription

Only rows containing actual readable wording entered after control against the manuscript PDF count as substantively transcribed. `IMAGE_REVIEWED_AWAITING_TRANSCRIPTION`, generic page descriptions, OCR routing, visual-control passes and topical research notes do **not** count.

The original PaddleOCR JSON is treated as immutable source material. Uncertain readings stay bracketed; omitted or still-untranscribed matter is not silently promoted into secure text.

## Historical/supporting material elsewhere in the project

Files such as `WEDDING_FULL_OCR_READING_LOG_*`, `WEDDING_OCR_FIRST_PASS_*`, `WEDDING_BESSEMER_TARGETED_OCR_*`, and `WEDDING_MSS25_VISUAL_CONTROL_PASS*` are supporting logs. They can contain verified anchors and useful page routing, but they are not progress authorities for sequential transcription.

## Verified checkpoint provenance

The current checkpoint was recorded by commit `afe48813a03e1ff54d154761d17a25820d094b0c` (`Record substantive Mss24 progress through PDF 65`). The corresponding substantive page edits include commit `8d159cbf19672bc500c9b52b3c7fa12b9f0677f6`, and the machine-readable checkpoint update is in `83007e382b767e8c24e4f1f70438153391fab367`.
