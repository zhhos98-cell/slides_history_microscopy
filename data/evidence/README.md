# Evidence layers

Normalised structured evidence retained from bounded harvesting or source-specific extraction. Evidence files enrich the frozen survey and support later analysis; they do not constitute a parallel census.

## Current retained module

### `targeted_deep_4/`

Normalised output from the final bounded `targeted-deep` harvesting pass retained for the closed survey version. The directory contains:

- `manifest.json` — retained structured evidence manifest;
- `README.md` — module scope and interpretation;
- `MANUAL_RESIDUALS.md` — unresolved/manual-review cases.

The partial interrupted Sorbonne branch from the predecessor workflow is intentionally outside the retained normalised evidence layer.

## Editing discipline

1. Retain source/institution identifiers and provenance hooks needed to trace an extracted record.
2. Do not promote a harvested search result into a historical relation without contextual verification.
3. Do not use evidence-layer counts to rewrite the frozen 155 membership.
4. Keep incomplete/manual residuals explicit rather than filling gaps by inference.
5. Durable new harvesting results should be reviewed and versioned here; transient runtime outputs belong in ignored `outputs/` or `data/normalized/` directories.

See `data/README.md` for the authority order across data layers.
