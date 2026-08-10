# Source registry

The `sources/` directory is the public/documentary routing layer for archives, surviving slide collections, trade records, institutional catalogues and primary-source portals used by the project.

## Current authority

`source-registry-manifest.json` is the authority for the additive registry. The registry is split across `source-registry.json` and `source-registry-02.json` through `source-registry-12.json`; the unusual first-chunk filename is historical and intentional.

The chunks currently preserve **87 raw routing records**. A semantic duplicate-route audit identified **3 superseded duplicate IDs**. A subsequent scope audit identified **1 cross-project/out-of-scope ID** (`GB-SHEFFIELD-SORBY`). Current/public consumption therefore contains **83 canonical source routes**. Superseded and excluded rows remain in their original chunks only as audit history and are suppressed through the manifest.

The public `sources/` page reads the manifest dynamically, loads all 12 chunks, suppresses both `superseded_ids` and `excluded_ids`, and asserts the canonical count. It does not treat raw chunk concatenation as the current registry.

Source-registry entries are **routes to evidence**, not a second object census and not automatically nineteenth-century corpus text. Modern collection descriptions can establish present custody, labels, object groupings, archive locators and later provenance states, but they do not replace nineteenth-century sources when the historical claim concerns manufacture, sale, exchange, use or transfer.

## Identity, duplication and scope discipline

A repeated URL is only a routing signal. It is not sufficient grounds for row deletion.

Three same-endpoint duplicates are currently canonicalized:

- `ZA-IZIKO-ENTOMOLOGY` → `ZA-IZIKO-ENTOMOLOGY-SLIDES`;
- `AR-LAPLATA-FYCOLOGY` → `AR-MLP-FICOLOGIA-DIATOMS`;
- `NZ-TEPAPA-COLLECTIONS-ARCHIVES` → `NZ-TEPAPA-NATURAL-HISTORY-ARCHIVES`.

In each case the later record is an enriched version of the same institutional route and same primary URL.

`GB-SHEFFIELD-SORBY` is handled differently: it is not a duplicate. It is retained only in the raw audit layer as a cross-project residue and is excluded from canonical/public routing because it lies outside the current project's scope.

Other repeated URLs remain deliberately separate where the documentary function differs. Current examples include the Bell Pettigrew parent collection reused by Elcock and Naples subcollection records, the Challenger sediment dataset reused as a secondary comparator by the CT-reassessment record, and the NHM foraminifera landing page reused by the distinct Heron-Allen & Earland Type Slide system.

Similar institution, maker, taxon or collection names are therefore not silently deduplicated. Parent collection, subcollection, archive series, catalogue and individual object can remain separate when they perform different evidentiary functions.

## Current research mode

General source discovery is parked. The current research state has zero public-web discovery targets and four exact-source requests. Consult `../REPOSITORY_STATE.json`, `../data/analysis/CURRENT_STATE.json` and `../data/analysis/global_archive_research_priority_CURRENT.json` before treating a source-registry lead as active work.
