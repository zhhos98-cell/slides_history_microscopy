# Wedding full OCR reading log — 2026-09-11

Status: ACTIVE. This file is the rolling checkpoint for a full-pass read of the current PaddleOCR-VL JSON outputs for Eisenbibliothek Mss 23–25. It is deliberately an indexing/triage layer, not a diplomatic transcription.

## Pass 0 — corpus loaded

Current JSON lengths:

- Mss 23: 223 OCR entries; 135 entries contain non-empty OCR text.
- Mss 24: 116 OCR entries; 94 entries contain non-empty OCR text.
- Mss 25: 401 OCR entries; 380 entries contain non-empty OCR text.

Total: 740 OCR entries; 609 with non-empty OCR text.

The reading strategy is now fixed:

1. scan every OCR entry once;
2. preserve literal OCR anchors rather than silently correcting them;
3. separate recognisable historical content from obvious model filler/repetition/modern-date hallucination;
4. extract dates, places, people/firms, works/institutions, process/testing actions, sample/reference/image/numbering clues, and access/knowledge-boundary clues;
5. mark page-image/PDF checks only where an anchor matters analytically;
6. build the Wedding comparison architecture before attempting prose correction.

Noise flags used during the scan include repeated `The quick brown fox...`, intrusive modern years, extreme lexical repetition and non-Latin filler. A noisy page can still preserve a valid historical anchor, so noise is recorded separately rather than deleting the row.

## First full-scan checkpoint

Automated literal-anchor scan across all 740 entries is complete. It is being used only to route manual reading, not as evidence by itself.

Immediate high-yield zone remains Mss 25, especially the front-matter contact/address pages and the British sequence around OCR entries 294–370. Current stable or near-stable anchors include Manchester, Sheffield, Low Moor, Newcastle upon Tyne, Glasgow/Govan, Cornwall, Wales and multiple industrial-work references. Calendar consistency will be used as a diagnostic flag, never as silent emendation.

Next checkpoint will add the first curated chronological/site table after the full Mss 25 high-yield pass.