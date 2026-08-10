# Analysis layers

Versioned derived research layers over the frozen surviving-object survey. Files here interpret, classify, route or crosswalk evidence; they do not rewrite frozen survey membership or source wording.

## Current authority

`CURRENT_STATE.json` is the canonical machine-readable pointer to the present analysis state. It exists because this directory preserves dated/versioned research snapshots as an audit trail, and older files can contain conclusions that were later narrowed, closed or superseded.

For operational work, read in this order:

1. `CURRENT_STATE.json` — current counts, research mode, exact-source queue and supersession map;
2. `global_archive_research_priority_CURRENT.json` — current request-only router;
3. the current target-specific file named by those manifests;
4. older dated/versioned files only as historical research snapshots.

The current state is: frozen survey **307 discovery / 155 strict nineteenth-century nodes**; bibliography **pass 19 / 206 entries**; public-web discovery queue **0**; exact-source request queue **4**. Naples catalogue offering 383 is closed to St Andrews `BPM/1/T8/6` at catalogue-offering identity level and is no longer an active residual.

`../../scripts/validate_current_analysis_state.py` provides a lightweight consistency check against the frozen survey closure manifest, bibliography manifest, live router and current Naples closure.

## Current modules

### `slide_155_analysis_v1/`

Derived analytical classification over all 155 frozen nineteenth-century nodes. It normalises unit level, production period, subject cluster, institutional/commercial context, circulation mode, count namespace and historical actor role. Review flags concern the derived classification, not the reliability of the frozen source row.

### `slide_155_corpus_expansion_v1/`

Object-first expansion into the nineteenth-century microscopy text corpus. It contains:

- contextual object↔text bridges;
- bounded primary-source targets;
- dated source-pass outcomes and research logs;
- the Naples 1880 423-offering catalogue manifest;
- Naples→UK circulation and RMS item crosswalks.

## Supersession discipline

Version suffixes are research states, not competing authorities. Preserve them, but do not treat an older unresolved state as current when a later file closes it.

Important examples:

- `naples_row383_page_verification_v3.json` is a retained negative page-retrieval check; it is superseded by `naples_row383_object_catalogue_closure_v4.json`.
- `uk_us_europe_closure_batch_2026-08-10_v1.json` and `_v2.json` are historical batch snapshots.
- `uk_us_europe_closure_residuals_2026-08-10_v3.json` is the cleaned dated residual audit recording the terminal four exact-source requests and the Naples closure; it is accurate, but the live operational router is still `global_archive_research_priority_CURRENT.json`.
- `four_target_execution_status_2026-08-10.json` is an execution snapshot, not a live task list.
- older `global_archive_research_priority_v*.json` files are historical; only the `_CURRENT.json` file is operational.

See `CURRENT_STATE.json` for the complete supersession map.

## Authority and editing rules

1. Preserve the frozen survey row as the underlying object/provenance evidence.
2. Store new interpretation in a new or explicitly revised analytical file rather than rewriting the source census.
3. Keep exact identity, bounded correspondence and unresolved identity distinct.
4. Positive OCR/name/taxon matches are routing signals until source context closes the relation.
5. Keep event, catalogue, shipment, exhibition and surviving-object identities separate unless explicit evidence connects them.
6. Record negative bounded checks when they materially constrain later searching.
7. Do not delete a superseded analytical snapshot merely because its conclusion changed; mark its authority relationship in `CURRENT_STATE.json`.
8. A current-state file may correct routing/status metadata, but it must not silently rewrite the underlying historical source claim.

The root `data/README.md` defines authority order across survey, evidence, analysis and compact corpus layers.
