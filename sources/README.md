# Source registry

The `sources/` directory is the public/documentary routing layer for archives, surviving slide collections, trade records, institutional catalogues and primary-source portals used by the project.

## Current authority

`source-registry-manifest.json` is the authority for the additive registry. The registry is split across `source-registry.json` and `source-registry-02.json` through `source-registry-12.json`; the unusual first-chunk filename is historical and intentional. The public `sources/` page loads the manifest rather than treating any one chunk as complete.

Source-registry entries are **routes to evidence**, not a second object census and not automatically nineteenth-century corpus text. Modern collection descriptions can establish present custody, labels, object groupings, archive locators and later provenance states, but they do not replace nineteenth-century sources when the historical claim concerns manufacture, sale, exchange, use or transfer.

## Identity and duplication discipline

Similar institution, maker, taxon or collection names are not silently deduplicated. A registry entry is collapsed only when the evidence establishes that it points to the same documentary/object route. Parent collection, subcollection, archive series, catalogue and individual object can remain separate when they perform different evidentiary functions.

## Current research mode

General source discovery is parked. The current research state has zero public-web discovery targets and four exact-source requests. Consult `../REPOSITORY_STATE.json`, `../data/analysis/CURRENT_STATE.json` and `../data/analysis/global_archive_research_priority_CURRENT.json` before treating a source-registry lead as active work.
