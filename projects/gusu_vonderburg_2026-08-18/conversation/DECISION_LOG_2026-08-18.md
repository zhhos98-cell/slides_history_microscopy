# Gusu / von der Burg project decision log

Date: 2026-08-18

## Scope

Working corpus: *Chinese Gusu Prints in the Christer von der Burg Collection* and the corresponding 2025 Cleveland Museum of Art / Metropolitan Museum of Art acquisition records. The working goal is a machine-operable concordance from book/catalogue entries to museum accessions, object pages, image assets, and batch-download endpoints.

## Canonical count and count conflict

- Canonical working count: **220 prints / 220 plates**, based on Christer von der Burg's own publication statement and Muban Educational Trust publication material.
- Some later publicity/secondary sources report **221**. This is preserved explicitly as a conflict field rather than silently normalized.
- Museum object-record count is not treated as equivalent to physical print count. Multipart works may have cover/component structures.

## Met state

- 75 verified Met accessions in the current acquisition/gift set.
- 73 independent object pages verified in the web audit.
- 69 exact direct IIIF `main-image` URLs are currently batch-ready and preserved in `gusu_vonderburg_met_v10_download_manifest.csv`.
- `2025.421`: Public Domain + Download verified, exact direct link still pending.
- `2025.424`, `.425`, `.426`: current Met UI restricts enlargement/fullscreen/download; kept out of download manifest.
- `2025.379`, `.381`: official four-print set members, no independent indexed page found in the audit.
- Sequence gaps are kept as audit gaps only and excluded from batch use.

## Cleveland state

- CMA official physical-print count: **113**.
- Early assumption that the relevant acquisition begins at `2025.23` was corrected. `2025.21`, *Part of Story of The Western Chamber / 一部西廂總*, is a verified Chinese Qing polychrome woodblock-print record.
- Current verified boundary controls: `2025.18` = non-corpus (Giambologna marble); `2025.21` = corpus; `2025.127` = corpus; `2025.130` = non-corpus (German drawing). `2025.19/.20/.22/.128/.129` remain unresolved, not inferred either way.
- Known multipart structure: `2025.82` is a cover/set record and `.1–.4` are four physical components; cover does not contribute to physical-print count.
- Hard-verified CMA Open Access/download physical rows carried forward: 11 (`2025.21`, `.32`, `.60`, `.82.1–.4`, `.83`, `.84`, `.113`, `.118`).
- Hard negative current web-image states include `2025.39`, `.100`, `.103`, `.122`.
- Preferred CMA machine interfaces are official accession-addressable endpoints: specific-artwork API, JPEG+caption ZIP, TIFF endpoint. Piction/Next-image URLs are retained only as observed web-rendition evidence, not promoted to archival full-size URLs.

## Data-model rules

- Stable machine key uses museum + accession; title is never the primary key.
- `record_kind`, `component_suffix`, `set_id`, `set_size`, cover/component fields distinguish museum records from physical prints.
- Human-readable book fields remain separate from machine/API/download fields.
- `book_catalogue_no`, `book_plate_no`, `book_page`, and book-order fields remain unresolved until catalogue pages are recovered; museum accession order is never substituted for book order.
- Candidate rows are explicitly marked and excluded from batch download unless independently verified.
- Search-index absence is only an indexing observation, not proof that a museum record is absent.
- Museum download restrictions are recorded and are not bypassed.

## Version history

- Seed: initial museum concordance / object-page candidates.
- v0.3: machine-first schema, UTF-8 machine CSV, Excel CSV, NDJSON, count-conflict fields.
- v0.4: strict provenance guard against older unrelated von der Burg CMA records; publisher sample-image log.
- v0.5: page-image ingest/crop workflow based on observed book layout.
- v0.6–0.10: hard Met audit, direct-IIIF recovery, exception manifest.
- v0.7–0.8: CMA hard image audit and exact site-index sweep; explicit cover/component handling.
- v1.1–1.2: CMA accession-addressable API/ZIP/TIFF endpoints and verified download rows; corrected lower accession assumption.
- v1.3: explicit CMA boundary controls and unresolved neighbors.

## Next hard step

Filter the official CMA Open Access API/bulk dataset by 2025 accession year + von der Burg provenance + Chinese/Suzhou print signals, preserve `record_type` and `cover_accession_number`, and reconcile those records to the official 113 physical prints. Then merge book-order fields once catalogue pages are recovered.
