# GitHub Pages site

Live site: https://zhhos98-cell.github.io/slides_history_microscopy/

Launched: 2026-08-09  
Source: `main:/`

## Design and role

The site reuses the visual grammar of the Blaschka corpus site while remaining a separate microscopy project. It is a presentation and navigation layer over the research backend, not a second authoritative database.

`REPOSITORY_STATE.json` is the top-level repository authority map. Pages must follow that map rather than infer current state from the newest-looking versioned filename.

The frozen surviving-object catalogue remains independently reconstructed in the browser from `07K`–`07AQ`, the 07AR superseded-alias map, scope overrides, and final QC. The browser asserts exactly 155 entries before rendering the object explorer.

## Backend corpus publication layer

`data/corpus/CORPUS_MANIFEST_V6.json` is the current compact site-facing contract over the seven canonical microscopy masters. It preserves the V5 corpus payload counts and source-master fingerprints while refreshing the published research-output index.

The compact layer publishes every document-level entry from the six textual masters: 142 core bibliographic/document entries, 60 extension document entries, and 2 structured-OCR source entries. It also publishes all current compact BNA derived results: all 43 query-yield rows, all 71 year-yield rows, all 930 event clusters, and all 995 newspaper-yield rows. `data/corpus/BNA_DERIVED_INDEX_V5.json` maps the complete event-cluster and newspaper tables.

The event-cluster export preserves cluster ID, type, record count, representative BNA record ID, and exceptional clustering basis; repeated standard clustering/review prose is stored once per chunk. Newspaper-yield rows preserve newspaper title and A/B/C/X grade counts.

The following high-volume layers remain in the canonical masters rather than being duplicated into Pages: 49,277 core page-text records / 50,744 occurrences; 73,073,904 extension full-text characters; structured-OCR page arrays; and 9,365 article-level BNA record payloads/raw OCR. The manifest preserves their counts together with byte sizes and SHA-256 hashes for all seven masters.

## Research outputs

`data/corpus/RESEARCH_OUTPUTS_V6.json` is the current curated public research-output index and contains 41 current/foundational outputs. It covers repository/analysis authority, frozen closure files, derived 155 documentation, object-to-text bridges, Cole/material-publication analysis, Balfour, Challenger, Elcock, Naples, trade/addressing infrastructure, reverse-index bridges, harvest evidence, bibliography/source manifests and site architecture.

Older `RESEARCH_OUTPUTS_V4.json`, `RESEARCH_OUTPUTS_V5.json`, `CORPUS_MANIFEST_V4.json` and `CORPUS_MANIFEST_V5.json` remain predecessor snapshots and should not be used for current public counts.

## Bibliography and source pages

The bibliography page loads `bibliography/bibliography-manifest.json` and all 22 current row chunks, then generates complete CSV/TSV/JSON/CSL JSON/BibTeX/RIS exports. The legacy `bibliography/bibliography.csv` is not a complete current export and should not be linked as the authoritative bibliography.

The sources page loads `sources/source-registry-manifest.json`; registry chunks are additive research routes and do not alter frozen object membership.

## Editing rule

Pages can grow as the research backend grows, but the closed 307/155 census is versioned separately. New research results should enter a versioned analytical/provenance file first and then be surfaced by the site. Bulk primary/OCR text should remain in archival masters unless moving it improves verification or reuse.

Cross-layer integrity is checked by `scripts/validate_repository_state.py` and the `repository-integrity` GitHub Actions workflow.
