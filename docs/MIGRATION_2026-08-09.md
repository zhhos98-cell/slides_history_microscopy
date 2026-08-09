# Standalone repository migration — 2026-08-09

## Source

- predecessor repository: `zhhos98-cell/Blachka_corpus`
- source branch: `slide-survey-actions-pilot`
- frozen source head copied: `011f8e9bf6c46d808540ee85e202978b4ffa782c`
- source tree: `7c1b3719542575f63f8c9e2135f8dcec6c54a08d`

The source branch was already a microscope-slide-only project tree at migration time: root README, `data/`, `docs/`, `scripts/`, and slide-specific Actions infrastructure. No Blaschka research data were copied into the new repository.

## Destination

- repository: `zhhos98-cell/slides_history_microscopy`
- canonical branch after migration: `main`
- migration snapshot commit: `e7eb93540f28f7342a88f915e240120a5901abec`

The GitHub Actions transfer was performed in two stages because a repository-scoped Actions token was not permitted to push new workflow files. The project files were copied first, then the workflow files were recreated through the GitHub repository API.

## Post-migration normalization

The following repository-local changes were made without altering the frozen survey data:

1. Root `README.md` was rewritten as a standalone microscope-slide project README.
2. `data/analysis/slide_155_corpus_expansion_v1/PROGRESS_LOG_2026-08-09.md` now identifies this repository and `main` as the canonical continuation point.
3. `slide_survey.yml` and `slide_institution_harvest.yml` were recreated without the former hard-coded `slide-survey-actions-pilot` checkout ref.
4. `slide_export_frozen_catalogue.yml`, previously exposed from the predecessor repository's default branch, was added here and now runs directly against this repository's `main` checkout.

## Invariants preserved

- frozen status: `CLOSED_2026-08-09`
- discovery layer: **307** canonical nodes
- strict nineteenth-century layer: **155** nodes
- closure batches and `07AR` audit files are unchanged
- frozen membership remains reconstructed by `scripts/build_frozen_strict_membership.py`
- derived analysis remains separate from the frozen census
- Naples 423-offering parse and UK circulation/item crosswalks remain derived analytical layers

Historical Actions run IDs from the predecessor repository remain provenance references only. New workflow runs and future project work should be recorded in `zhhos98-cell/slides_history_microscopy`.
