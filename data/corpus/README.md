# Microscopy backend metadata layer

Site-facing compact export, 2026-08-09.

The compact Pages/repository layer carries every document-level entry from the three core masters and the three extension masters, all 43 BNA query-yield rows, all 71 BNA year-yield rows, all 930 derived BNA event clusters, all 995 newspaper-yield rows, and the current research-output ledger. The event and newspaper tables are compacted structurally, with repeated clustering notes stored once per chunk rather than copied into every row.

Large text bodies remain in the canonical masters: 49,277 core page records (50,744 occurrences), 73,073,904 extension full-text characters, structured-OCR page arrays, and the 9,365 BNA article-level payloads/raw OCR. `CORPUS_MANIFEST_V5.json` records counts and the byte size/SHA-256 of each of the seven source masters; `BNA_DERIVED_INDEX_V5.json` maps the complete compact derived tables.
