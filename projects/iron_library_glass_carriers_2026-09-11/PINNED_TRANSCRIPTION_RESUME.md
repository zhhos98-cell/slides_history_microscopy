# PINNED TRANSCRIPTION RESUME

> **Authoritative transcription work lives on branch `ironlibrary-json-correction`.**
>
> Do **not** infer substantive transcription progress from OCR-routing logs, visual-control passes, targeted OCR notes, or research/application files on `main`.
>
> **QUALITY WARNING (2026-09-12): the existing Mss 24 ledger through PDF 65 is not a citation-ready scholarly transcription.** A quality audit found that many rows mix literal manuscript readings with editorial reconstruction, diagram interpretation, normalized technical prose, and English image-description terms. In several pages, editorial descriptions such as `cross-section`, `columnar basalt`, `country rock`, `circular plan`, `bell`, `gas outlet`, `blast-furnace section`, and `pile diagram` were incorrectly admitted into `secure_anchors`. Therefore `through_pdf_page: 65` is a workflow-progress checkpoint, **not** a claim that PDFs 1–65 are reliable verbatim transcriptions.

## Current authoritative checkpoint

- Branch: `ironlibrary-json-correction`
- Verified workflow checkpoint commit: `afe48813a03e1ff54d154761d17a25820d094b0c`
- Mss 23: textual sequence processed through PDF 210; PDFs 211–223 are object/digitisation views.
- Mss 24: image-controlled extraction/transcription workflow processed through PDF 65.
- **Next unprocessed sequential page: Mss 24 PDF 66.**
- Remaining Mss 24 text sequence: PDFs 66–87.
- Mss 25: mostly still awaiting sequential page-level work; separately verified out-of-sequence readings remain in the correction ledger.

### Important distinction

The checkpoint above records **coverage**, not uniform transcription quality. The current ledgers contain at least two different products:

1. genuine selective transcription: literal source wording, dates, names, figures, labels, with omissions left as `...` and uncertain readings bracketed;
2. image-controlled analytical extraction: modern prose summarizing diagrams, machinery, routes or page meaning, sometimes mixed into the `transcription` and `secure_anchors` fields.

The second product is useful for retrieval and research triage but must not be quoted as Wedding's wording.

## Required schema from the next quality pass onward

Do **not** continue the old mixed schema without correction. Separate these layers explicitly:

- `literal_transcription` — only words actually read on the manuscript page; no paraphrase or reconstructed sentences.
- `diagram_labels` — only labels actually written in or beside diagrams/maps/tables.
- `editorial_description` — modern description of visual structures, diagrams, machinery or page layout; never treated as source wording.
- `normalized_entities` — normalized names of places, firms, people, minerals, machines, etc.; useful for search but not quotation.
- `uncertain_readings` — uncertain source readings only.
- `research_summary` — analytical summary of what the page shows or means.
- `secure_anchors` — may derive only from literal source wording and literal diagram labels, never from editorial description or normalized entities.

Until the JSONL schema is migrated, the same separation must be enforced conceptually: bracketed editorial descriptions and modern explanatory prose are **not transcription** and must not enter `secure_anchors`.

## Legacy-data status

### Mss 24 PDFs 1–65

Status: **LEGACY_MIXED_EXTRACTION_REQUIRES_CLEANUP**.

- Useful for page routing, names, dates, locations, technical topics and many numerical anchors.
- Not safe for exact quotation, terminology history, linguistic analysis, or claims that depend on exact wording without returning to the manuscript image.
- English editorial terms inside `secure_anchors` are prima facie contamination and must be removed or moved to `editorial_description`.
- Complete fluent modern German sentences that synthesize machinery/layout relationships require rechecking; they may be analytical reconstruction rather than literal source text.

### Mss 25 controlled Bessemer pages (especially PDFs 295–300)

These are generally closer to the desired selective-transcription standard because they preserve only secure headings/phrases/figures and leave unread body text omitted. They should still be image-checked before exact quotation.

### Mss 23

Generally more conservative than Mss 24, but it is still selective rather than diplomatic transcription. Exact quotations require image control.

## Immediate resume rule

**Do not blindly continue from PDF 66 under the old field semantics.** First apply the corrected separation standard to a small calibration batch (recommended: Mss 24 PDFs 56–60, or another 5-page mixed text/diagram sample). Compare old and corrected versions, establish the migration pattern, then continue PDF 66 onward using the corrected schema. Legacy PDFs 1–65 should subsequently receive a cleanup pass rather than being treated as finished transcription.

## Canonical files on the correction branch

`projects/iron_library_glass_carriers_2026-09-11/corrected_transcription/`

- `README.md` — human-readable quality and resume guide.
- `README.json` — machine-readable historical checkpoint/status lists; **its `through_pdf_page` field currently records coverage only and must not be interpreted as citation-ready quality.**
- `WEDDING_MSS23_CORRECTED_TRANSCRIPTION.jsonl` — Mss 23 ledger.
- `WEDDING_MSS24_CORRECTED_TRANSCRIPTION.jsonl` — Mss 24 ledger; PDFs 1–65 currently carry the legacy mixed-extraction warning above.
- `WEDDING_MSS25_CORRECTED_TRANSCRIPTION.jsonl` — Mss 25 ledger.

Project-level human checkpoint on that branch:

- `projects/iron_library_glass_carriers_2026-09-11/CURRENT_PROGRESS.md`

## Counting rule going forward

A page counts as **transcribed** only when actual readable source wording has been entered after control against the manuscript image. Generic descriptions, routing labels, OCR summaries, visual reconstructions, inferred machine relations, and `IMAGE_REVIEWED_AWAITING_TRANSCRIPTION` rows do not count as transcription.

Coverage and transcription quality must be reported separately.

Last quality audit and pin update: 2026-09-12.
