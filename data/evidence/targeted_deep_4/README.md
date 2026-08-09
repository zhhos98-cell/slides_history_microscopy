# Targeted deep harvest: run 4 evidence package

Source workflow run: `31287016342` (`slide-institution-harvest` run #4).

This directory records the final targeted harvest pass without reopening the frozen 2026-08-09 survey. The closure boundary remains **307 canonical discovery entries / 155 frozen strict nineteenth-century entries**.

The workflow run itself ended `cancelled` because the Sorbonne job was interrupted, but a combined artifact was produced for the seven completed institutions. Sorbonne's partial raw-page artifact is deliberately excluded from the normalisation contract.

## Tracked files

- `manifest.json`: counts, artifact identity, scope warnings and the normalisation decisions established from run 4.
- `MANUAL_RESIDUALS.md`: the small remainder worth checking manually if a concrete research use requires it.
- `../../../scripts/normalize_targeted_deep_artifact.py`: reproducible normaliser for an extracted copy of the combined Actions artifact.

The large row-level derivatives are intentionally **not committed automatically** to the repository. Running the normaliser writes:

- `copenhagen_desmid_objects.jsonl`: 510 unique SNM slide identifiers. Multiple species labels on one slide remain a list rather than being split into fictitious extra slides.
- `farlow_cheever_B01-B10.jsonl`, `B11-B20.jsonl`, `B26-B30.jsonl`, `B31-B40.jsonl`: public Cheever index rows. These are current indexed positions in a mixed-period collection, not automatic nineteenth-century dates.
- `st_andrews_bell_pettigrew_hierarchy.jsonl`: Bell-Pettigrew child groups recovered from the St Andrews catalogue.
- `ansp_symbiota_review_pool.jsonl`: intentionally review-only Symbiota rows. The site's `pre-1900` query did not reliably enforce an object-date filter.
- `ucl_whipple_mcz_targeted_pages.jsonl`: compact page-level metadata evidence retaining identifiers, relationship candidates and quantity candidates.

Example after extracting `slide-metadata-targeted-deep-4.zip`:

```bash
python scripts/normalize_targeted_deep_artifact.py /path/to/extracted/artifact --output outputs/targeted_deep_4_normalized
```

## Evidence rules

The normaliser preserves source rows and identifiers. It does not convert catalogue numbers, sample numbers, box positions, database rows or collection totals into slide counts. It also does not infer `prepared by` from a collection name, label, user or seller. Any harvested collection not already present in the frozen catalogue remains post-closure evidence only until an explicit later reopening/version.
