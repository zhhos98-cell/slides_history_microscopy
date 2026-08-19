# Backup state

Snapshot date: 2026-08-18
Target repository: `zhhos98-cell/slides_history_microscopy`
Project directory: `projects/gusu_vonderburg_2026-08-18/`

## Embedded directly in Git

The repository contains the complete **current logical research state** needed to continue the project:

- user dialogue / working-session transcript;
- research decision and correction log;
- full artifact inventory with original byte sizes and SHA256 hashes;
- current v1.3 canonical concordance (all rows and key machine fields), stored as nine deterministic parts under `latest/canonical_parts/`;
- `latest/REASSEMBLE_CANONICAL.sh`, which reconstructs and verifies the LF-normalized canonical CSV (`120072` bytes; SHA256 `5d0e4406efce9c90d32248a3f6285596e49299d31023c4e7cafadfa492d0b7eb`);
- CMA boundary audit and current v1.3 summary;
- Met 69-row exact-IIIF download manifest, exception log, and audit summary;
- CMA 11-row verified batch-download command table and downloader;
- current strict CMA resolver (`resolve_cma_gusu_v11.py`);
- legacy generic resolver, explicitly placed under `legacy/` because its provenance-only append behavior was superseded;
- page-image/book-ingest fetch, crop, template, and publisher-sample files.

## Full historical artifact inventory

`conversation/FILE_INVENTORY_2026-08-18.tsv` lists every session artifact generated in the working container, including seed/v0.3–v1.3 machine and Excel tables, NDJSON, intermediate audit tables, bundle ZIPs, scripts, and the user-supplied layout screenshot. Each entry records its original byte size and SHA256.

The original current full machine table had:

- `gusu_vonderburg_manifest_v13_machine.csv`: 406753 bytes; SHA256 `27631275477db2496087b985d1f66958b55aec41d0b70e7ef64ad27353698faa`.

The GitHub canonical compact table preserves every row and the key continuation fields, while dropping redundant historical/debug columns. Its pre-GitHub local CRLF form had SHA256 `ccbf765f6d74766321442512f6b53eee043d5888d0a5a94715cd128ae5a30fdf`; GitHub stores the deterministic LF-normalized representation described above.

## Binary / redundant wrapper caveat

The GitHub connector available in this session exposes normal repository writes as UTF-8 text writes. Therefore **historical duplicate ZIP wrapper files and the PNG screenshot bytes are not embedded byte-for-byte in this directory**. Their exact original filenames, byte sizes, and SHA256 hashes are preserved in the inventory. The screenshot used to infer the two-page / ~three-entry-per-page layout is recorded there as:

`a5f0c96d-3a09-4ed1-8e83-afd2865aa097.png` — 908928 bytes — SHA256 `b3ec271a424e6eb0a557a8e66147c9a93e85d362b2911268b4e88c13dd57b0d6`.

The historical bundle ZIPs were convenience wrappers around data/scripts already represented by the current canonical state, version/decision log, and artifact inventory; their hashes remain available for provenance checking.

## Continuation rule

Start future work from:

1. `conversation/DECISION_LOG_2026-08-18.md` for epistemic state and corrections;
2. reconstructed `latest/gusu_vonderburg_canonical_v13.csv` for the museum concordance;
3. `latest/resolve_cma_gusu_v11.py` for the next Cleveland API pass;
4. `latest/gusu_vonderburg_met_v10_download_manifest.csv` and `latest/gusu_vonderburg_cma_v12_batch_commands.csv` for already-verified image operations.

Do not reinstate the old contiguous-CMA-accession assumption, do not substitute accession order for book order, and do not promote search-index absence to evidence of nonexistence.
