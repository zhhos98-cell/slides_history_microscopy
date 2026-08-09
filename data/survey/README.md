# Survey data

This directory is the audit-preserving data layer for the global microscope-slide collection survey. The survey version is frozen as `CLOSED_2026-08-09`.

## Current frozen state

- Canonical discovery layer: 307 collection/subcollection/batch/database nodes.
- Strict nineteenth-century layer: 155 nodes.
- Strict membership is reconstructed from `07K`–`07AQ` plus the `07AR` closure metadata.
- `07AR` adds no discovery rows.

## File families

### Runtime / cumulative survey inputs

`07A_Global_Microscope_Slide_Collections_Survey.csv` is the canonical runtime survey input used by the reproducible survey scripts.

### Modular discovery and expansion batches

`07B_*` onward preserve the modular discovery/expansion history. These files remain in the repository because they are the evidentiary audit trail behind the closed census. They should not be collapsed into a single hand-edited table or deleted merely because later batches overlap earlier discovery work.

The strict nineteenth-century closure specifically reads `07K`–`07AQ`.

### Closure contract

The `07AR` family freezes and explains the closed version. Key files include:

- `07AR_CLOSURE_MANIFEST_2026-08-09.json` — closure arithmetic and counts;
- `07AR_CLOSURE_AUDIT_2026-08-09.md` — human-readable audit;
- `07AR_SUPERSEDED_ALIASES_2026-08-09.json` — distinct-ID rediscoveries collapsed at closure;
- `07AR_FINAL_QC_2026-08-09.md` — final catalogue QC;
- `07AR_FINAL_QC_OVERRIDES_2026-08-09.json` — display-only QC overrides;
- `scope_19c_overrides.json` — explicit scope decisions used by the frozen contract.

`scripts/build_frozen_strict_membership.py` is the executable membership contract. The browser-side Pages explorer independently reconstructs the same 155-node layer and fails if the count changes.

### Harvest configuration

Files such as `site_adapters*.json`, `harvest_families*.json` and `institution_harvest_profiles.json` are harvesting/extraction configuration. They are infrastructure, not survey rows.

## Editing discipline

1. Do not renumber or silently rewrite frozen `07K`–`07AQ` entry IDs.
2. Do not remove a modular batch simply because its nodes later appear in another batch; closure aliases and duplicate handling are explicit.
3. New discoveries do not extend `CLOSED_2026-08-09` in place. Reopening requires an explicit new version.
4. Historical corrections to display wording belong in versioned QC/override layers unless the original source row itself is demonstrably corrupt.
5. Keep quantity namespaces separate: slide totals, catalogue positions, cabinet capacities, database rows and mixed-period aggregates are not interchangeable.
