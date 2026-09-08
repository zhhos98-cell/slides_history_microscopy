# Finder / microscopic relocation technologies

Date started: 2026-09-08

Branch: `research/finder-slide-localization-tech`

Status: **INTERNAL DIGEST FIRST — EXTERNAL DISCOVERY NOT YET OPEN**

## Scope

This satellite project asks how nineteenth-century microscopists made a microscopic field or microscopic object **findable again**. The immediate subject is the family of techniques usually approached through finders, stage coordinates, slide-borne scales or grids, and related locating devices. The project begins from mechanisms already controlled in this repository rather than from a new general web survey.

The core microscope-slide census remains frozen. This project does not extend the 307/155 survey, alter the parked bibliography, or reopen the repository-wide discovery queue.

## Governing distinction

The repository already uses `addressability` at several scales. This project isolates the finest spatial level and keeps it distinct from neighbouring address systems:

1. **collection / cabinet address** — makes a slide retrievable among other slides;
2. **slide / series address** — identifies a preparation, product, issue, or sample;
3. **within-slide spatial index** — assigns locations to several mounted specimens on one slide;
4. **microscope-field / object relocation** — permits return to a particular microscopic field or object by a reproducible spatial reference.

Only the fourth category is a finder-equivalent mechanism in the strict working sense. The third is a close comparator. The first two remain contextual infrastructure.

## Internal starting points

### Grunow — strict relocation mechanism, S-level

Authority: `data/analysis/grunow_vienna_sample_level_closure_v2.json` and `docs/GRUNOW_SAMPLE_LEVEL_CLOSURE_2026-08-11.md`.

The repository already closes representative historical chains in which a sample number identifies a preparation variant and paired microscope-stage coordinates recover an exact valve. Grunow's instructions also distinguish older preparations with pasted scales from later localisation by aligning the slide's upper-left corner to a millimetre scale whose zero coincided with microscope focus. Sample 1363b (`12.9/32.9`) links preparation identity, coordinate and drawing; sample 3073b records several valves by coordinate and uses circling to mark valves already drawn.

This is the project's strongest internal anchor because location is operational: the coordinate is used to return to an exact microscopic object.

### Elcock — within-slide spatial index, S-level comparator

Authority: `data/analysis/elcock_type_slides_s_grade_closure_v1.json` and `data/analysis/retrievability_cross_media_infrastructure_v1.json`.

Elcock's Type Slides arrange many Foraminifera on black rectangular matrices; grid squares carry printed numbers, while named species are made legible within the comparative field. This is a spatial retrieval interface internal to one commercial preparation. It does not yet demonstrate arbitrary object relocation by microscope-stage coordinate and therefore should remain distinct from a strict finder.

### Grayson — calibrated reference surface, S-level comparator

Authority: `data/analysis/grayson_melbourne_test_ruling_object_archive_upgrade_v1.json`.

Grayson's surviving test plates encode calibrated line-density bands directly on glass, including a twelve-band 10,000–120,000 lines/inch scale. These objects stabilize repeatable optical-reference positions and values. They belong beside finder history as a comparator for spatial calibration and reference, not as evidence of a field-locating device.

### Existing addressability synthesis — context, not finder evidence

Authorities: `data/analysis/address_systems_argument_matrix_v1.json`, `data/analysis/slide_archive_addressing_systems_v1.json`, `data/analysis/retrievability_cross_media_infrastructure_v1.json`, and `data/analysis/GRAND_SYNTHESIS_2026-08-14_v1.json`.

The current repository argument already treats microscope coordinates as one address mechanism among labels, catalogue numbers, cabinet positions, registers, publication references and museum identifiers. A superseded UK/US return note also explicitly names `finder coordinates` alongside standardized glass geometry. These syntheses establish why microscopic relocation matters to the larger project, but they do not yet supply a named historical finder-device genealogy.

## Internal research question

**How was a microscopic field converted into an address that could be revisited across time, operators, instruments, drawings, and circulation?**

This formulation keeps the historical operation visible before deciding whether the relevant device should be called a finder, indicator, locator, coordinate system, scale, grid, or something else in a particular source.

## Analytical axes for the next pass

- **reference frame**: microscope/stage-bound; slide-bound; embedded/printed on the preparation;
- **resolution**: slide; region; field; individual microscopic object;
- **portability**: same setup only; same mechanical geometry; transferable with slide; readable on another instrument;
- **address form**: paired coordinate; ruled scale; grid cell; printed number; graphical mark; drawing cross-reference;
- **operation**: relocate; compare; draw; classify; test optics; teach;
- **cross-media relation**: coordinate ↔ catalogue; coordinate ↔ drawing; grid ↔ species name; ruling ↔ optical value;
- **failure mode**: reference frame lost; orientation changed; slide remounted; instrument/stage changed; key detached; coordinate convention undocumented.

## Internal gap map before external research

The checked default-branch material does **not yet close**:

- a named finder/indicator/locator device genealogy;
- Maltwood or a named Maltwood-type finder chain;
- a historical vocabulary map for `finder`, `indicator`, `locator`, and cognate terms;
- the portability problem across different microscopes or mechanical stages;
- a sourced chronology connecting stage-bound coordinates, slide-borne scales/grids, and portable finder systems;
- manufacture, trade, patent, society, or instructional circulation of finder devices;
- the relation between finder design and standardized slide geometry at source level.

These are bounded gaps for a later external pass. They are not permission for generic discovery yet.

## Stop rule for the internal phase

Do not begin broad web discovery until the controlled repository evidence has been concordanced by mechanism and the existing historical corpus/source registry has been checked for locating vocabulary. External work should then answer only the gaps that remain.
