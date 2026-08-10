# Source registry

The `sources/` directory is the public/documentary routing layer for archives, surviving slide collections, trade records, institutional catalogues and primary-source portals used by the project.

## Current authority

`source-registry-manifest.json` is the authority for the additive registry. The registry is split across `source-registry.json` and `source-registry-02.json` through `source-registry-12.json`; the unusual first-chunk filename is historical and intentional.

The chunks currently preserve **87 raw routing records**. A semantic duplicate-route audit identified **3 superseded duplicate IDs**, leaving **84 canonical source routes**. The superseded IDs remain in their original chunks for audit history and are suppressed by current/public consumers through the manifest alias map.

The public `sources/` page now reads the manifest dynamically, loads all 12 chunks, suppresses `superseded_ids`, and asserts the canonical count. It no longer relies on a hard-coded three-file list.

Source-registry entries are **routes to evidence**, not a second object census and not automatically nineteenth-century corpus text. Modern collection descriptions can establish present custody, labels, object groupings, archive locators and later provenance states, but they do not replace nineteenth-century sources when the historical claim concerns manufacture, sale, exchange, use or transfer.

## Identity and duplication discipline

A repeated URL is only a routing signal. It is not sufficient grounds for row deletion.

Three same-endpoint duplicates are currently canonicalized:

- `ZA-IZIKO-ENTOMOLOGY` → `ZA-IZIKO-ENTOMOLOGY-SLIDES`;
- `AR-LAPLATA-FYCOLOGY` → `AR-MLP-FICOLOGIA-DIATOMS`;
- `NZ-TEPAPA-COLLECTIONS-ARCHIVES` → `NZ-TEPAPA-NATURAL-HISTORY-ARCHIVES`.

In each case the later record is an enriched version of the same institutional route and same primary URL.

Other repeated URLs remain deliberately separate where the documentary function differs. Current examples include the Bell Pettigrew parent collection reused by Elcock and Naples subcollection records, the Challenger sediment dataset reused as a secondary comparator by the CT-reassessment record, and the NHM foraminifera landing page reused by the distinct Heron-Allen & Earland Type Slide system.

Similar institution, maker, taxon or collection names are therefore not silently deduplicated. Parent collection, subcollection, archive series, catalogue and individual object can remain separate when they perform different evidentiary functions.

## Current research mode

General source discovery is parked. The current research state has zero public-web discovery targets and four exact-source requests. Consult `../REPOSITORY_STATE.json`, `../data/analysis/CURRENT_STATE.json` and `../data/analysis/global_archive_research_priority_CURRENT.json` before treating a source-registry lead as active work.
