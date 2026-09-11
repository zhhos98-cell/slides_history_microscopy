# Satellite projects

This directory contains bounded projects that reuse the repository infrastructure but are **not governed by the closure state of the frozen nineteenth-century microscope-slide survey**.

Repository-level distinction:

- `REPOSITORY_STATE.json` governs the microscope-slide core: the 307-node discovery layer, 155-node strict nineteenth-century survey, bibliography, source registry, analysis layer and the four request-only residuals.
- `projects/` contains separately scoped research projects. Activity here does not reopen or extend the frozen microscope-slide census unless a project explicitly promotes evidence into a new survey version.

## Current projects

### `gusu_vonderburg_2026-08-18/`

Research/backup corpus for *Chinese Gusu Prints in the Christer von der Burg Collection* and the corresponding Cleveland Museum of Art / Metropolitan Museum of Art records.

Continuation authority:

1. `gusu_vonderburg_2026-08-18/README.md` — project router;
2. `gusu_vonderburg_2026-08-18/BACKUP_STATE.md` — recoverability and continuation rules;
3. `gusu_vonderburg_2026-08-18/conversation/DECISION_LOG_2026-08-18.md` — epistemic corrections/state;
4. `gusu_vonderburg_2026-08-18/latest/` — current operational/canonical artifacts;
5. `gusu_vonderburg_2026-08-18/conversation/PROGRESS_CONSOLIDATED_2026-08-18_TO_2026-08-19.md` — index to archived historical progress snapshots.

The Gusu project's `latest/` directory is a project-local name. It does not override microscope-slide repository authorities outside this project directory.

### `iron_library_glass_carriers_2026-09-11/`

Bounded research project connecting the parent *Using Up Old Slides* problem to Iron Library / Georg Fischer holdings on glass carriers, microphotography, metallography and industrial material testing. The project keeps biological specimen slides, microphotographic glass plates and industrial photographic glass plates analytically separate unless a source establishes a historical relation.

Continuation authority:

1. `iron_library_glass_carriers_2026-09-11/README.md` — scope, claim ceiling, current exact-source state and project router;
2. `iron_library_glass_carriers_2026-09-11/SOURCE_MAP.md` — controlled external sources, identifiers, access routes and evidence levels;
3. `iron_library_glass_carriers_2026-09-11/RESEARCH_STATE.md` — current comparison, bounded research queue and stop rules;
4. `iron_library_glass_carriers_2026-09-11/EXACT_SOURCE_REQUEST.md` — unsent, ready-to-use staff enquiry for the three Droste microphotographic glass plates and identifiers `G 745,1`, `Per765` and `A346`.

The first secure object route is Bernhard Droste's published statement that he donated three original early microphotographic glass plates associated with the Königliche mechanisch-technische Versuchsanstalt zu Berlin. Droste figure 2 associates their published image with `G 745,1`, but the catalogue meaning of that identifier and the individual plate locators remain open. The project is now in exact-source closure mode and does not reopen the frozen microscope-slide census.

## Cleanup rule

Do not infer repository-wide closure from the microscope-slide survey when a satellite project remains separately scoped. Conversely, do not let activity in a satellite project silently change the closed survey membership, bibliography counts, source-registry authority or exact-source request queue.

Historical project checkpoints belong in their project-local archive/provenance layers. Current continuation should be resolved through the project router rather than by filename recency alone.
