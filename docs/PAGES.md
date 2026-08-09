# GitHub Pages site

Live site: https://zhhos98-cell.github.io/slides_history_microscopy/

Launched: 2026-08-09
Source: `main:/`

## Design and role

The site reuses the visual grammar of the Blaschka corpus site while remaining a separate microscopy project. It is a presentation and navigation layer over the research backend, not a second authoritative database.

The frozen surviving-object catalogue remains independently reconstructed in the browser from `07K`–`07AQ`, the 07AR superseded-alias map, scope overrides, and final QC. The browser asserts exactly 155 entries before rendering the object explorer.

## Backend corpus publication layer

`data/corpus/CORPUS_MANIFEST_V4.json` describes a compact site-facing index over the seven canonical microscopy masters. It publishes every document-level entry from the six textual masters: 142 core bibliographic/document entries, 60 extension document entries, and 2 structured-OCR source entries. It also publishes all 43 BNA query-yield rows, all 71 BNA year-yield rows, and the current research-output ledger.

The following high-volume layers remain in the canonical masters and are not duplicated into Pages: 49,277 core page-text records / 50,744 occurrences; 73,073,904 extension full-text characters; structured-OCR data arrays; and 9,365 article-level BNA record payloads/raw OCR. The manifest records counts for the BNA article layer, 930 event clusters, and 995 newspaper-yield rows, together with byte sizes and SHA-256 hashes for all seven masters.

## Research outputs

The site indexes closure/audit materials, the derived 155 analytical layer, object-to-text bridge tables, open source targets, Naples catalogue/circulation crosswalks, targeted-harvest evidence, and dated progress logs. These outputs are linked to their repository files rather than copied into prose-only web summaries.

## Editing rule

Pages can grow as the research backend grows, but the closed 307/155 census is versioned separately. New research results should enter a versioned analytical/provenance file first and then be surfaced by the site. Bulk primary/OCR text should remain in archival masters unless moving it improves verification or reuse.
