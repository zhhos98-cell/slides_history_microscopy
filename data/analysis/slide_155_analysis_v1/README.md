# Frozen 155 analytical layer — v1

This directory is a **derived analysis layer** over the sealed `CLOSED_2026-08-09` microscope-slide catalogue. It does **not** alter the frozen 155-entry membership, source wording, provenance claims, quantity namespaces, or raw modular audit trail.

Source: final 155-row backend export, artifact `9030906012`.

## Fields

- `unit_level`: `single_slide`; `bounded_set`; `container_assemblage`; `named_collection`; `institutional_layer`; `mixed_parent_collection`.
- `production_period`: `early_19c_1800_1839`; `mid_19c_1840_1869`; `late_19c_1870_1899`; `spans_19c_periods`; `mixed_19c_plus_20c`; `19c_unspecified`.
- `subject_cluster`: a single primary analytical subject cluster derived from explicit `subject_scope` wording. This is for aggregation only; the original multi-domain field remains authoritative.
- `commercial_or_institutional`: `published_distributed_set`; `commercial_trade`; `institutional_teaching_research`; `personal_research_collection`; `hybrid`; `unclear`.
- `circulation_mode`: semicolon-separated normalized movement modes from explicit relationship verbs: sale/purchase; gift/donation/presentation; exchange/distribution; institutional transfer/deposit; research correspondence/sending; family descent; loan/borrowing; retained without an explicit transfer; or no circulation event stated.
- `count_namespace`: semicolon-separated classification of `stated_count` only. It deliberately ignores `harvestable_item_count`, so catalogue/database record counts are not silently converted into historical object quantities.
- `historical_actor_role`: semicolon-separated normalized roles from explicit `relationship_phrase` wording. A named user is never silently promoted to preparer.
- `analysis_review`: blank, `CHECK`, or `REVIEW`. `REVIEW` means at least one normalized field is low-confidence; `CHECK` means no low-confidence field but four or more fields are medium-confidence. These flags concern the **derived categorisation**, not the reliability of the frozen source row.

## Use rules

1. The frozen catalogue remains read-only. Corrections to this analytical layer do not rewrite the 155 source rows.
2. For first-pass quantitative work, use blank `analysis_review` rows first. Read `CHECK` and `REVIEW` rows against the retained source wording before publication-level claims.
3. `count_namespace` values are non-additive unless the same namespace and historical state are explicitly selected.
4. `mixed_parent_collection` is a warning against projecting current or mixed-period totals backward into the nineteenth century.
5. The subject cluster is intentionally reductive. Use `subject_scope` for historical interpretation.

## v1 distribution

- 155 rows total.
- 97 rows have no review flag.
- 20 rows are `CHECK`.
- 38 rows are `REVIEW`.
- Unit level: 65 named collections; 43 mixed parent collections; 22 institutional layers; 11 container assemblages; 9 bounded sets; 5 single slides.
- Production period: 62 late nineteenth century; 35 span analytical nineteenth-century periods; 28 mixed nineteenth/twentieth century; 20 mid nineteenth century; 5 early nineteenth century; 5 nineteenth century unspecified.
- Largest primary subject clusters: medical/histology/pathology 41; diatoms/phycology 37; geology/petrography/palaeobotany 20; foraminifera/protists 16.

This is an analytical convenience layer, not a replacement for the source catalogue.