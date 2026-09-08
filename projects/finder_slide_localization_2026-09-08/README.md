# Finder / microscopic relocation technologies

Date started: 2026-09-08

Branch: `research/finder-slide-localization-tech`

Status: **SYNTHESIS READY — BOUNDED EXTERNAL PASS COMPLETE — BROAD DISCOVERY CLOSED**

## Scope

This satellite project asks how nineteenth-century microscopists made a microscopic field or microscopic object **findable again**. The immediate subject is the family of techniques approached through finders, indicators, stage coordinates, slide-borne scales/grids, material marking devices, optical transfer systems and related locating technologies.

The core microscope-slide census remains frozen. This project does not extend the 307/155 survey, alter the parked bibliography, or reopen the repository-wide discovery queue.

## Governing question

**How was a microscopic field converted into an address that could be revisited across time, operators, instruments, drawings, correspondence and collections?**

The project no longer treats `finder` as a sufficient historical category. Its governing variable is **reference-frame portability**: where was spatial reference stabilised, and what happened to the address when the slide, stage, microscope, objective, observer, documentary medium or custody regime changed?

Operational chain:

`field/object -> stabilised reference frame -> recorded address or material mark -> displacement -> reconstruction of locality -> same field/object`

## Address hierarchy inherited from the Slides repository

The repository already uses `addressability` at several scales. This project isolates the finest spatial level and keeps it distinct from neighbouring address systems:

1. **collection / cabinet address** — makes a slide retrievable among other slides;
2. **slide / series address** — identifies a preparation, product, issue, or sample;
3. **within-slide spatial index** — assigns locations to several mounted specimens on one slide;
4. **microscope-field / object relocation** — permits return to a particular microscopic field or object by a reproducible spatial reference.

Only the fourth category is a finder-equivalent mechanism in the strict working sense. The third is a close comparator. The first two remain contextual infrastructure.

## Five mechanism families closed by the external pass

### 1. Instrument/stage-bound coordinate frame

Examples: Wright; Okeden; Smith; mechanical-stage verniers; partly Grunow; provisionally Klönne & Müller.

The apparatus itself supplies the reference frame. Numerical return can be precise, but the address is vulnerable to changes in stage geometry, zero, orientation, calibration or microscope.

### 2. Transferable external indicator/carrier

Central case: **Jacob Whitman Bailey's Universal Indicator (1855)**.

Bailey explicitly made portability a correspondence/collection problem: the record should remain useful beyond the original microscope and observer.

### 3. Substitution reference slide/grid

Central case: **Maltwood's Finder (1858)**; later Webb and England Finder.

The preparation is removed and a reference grid is substituted at a reproducible position. Stable slide geometry/orientation converts a microscopic locality into a portable grid address.

### 4. Direct material target marking

Examples: **Bridgman (1855)**; Francotte; Winkel; Gage.

The target locality is materially marked on the coverslip/preparation, often with a diamond-scratched ring. The spatial key travels with the preparation instead of being translated into an external coordinate.

### 5. Optical/eyepiece transfer reference

Example: Royston-Pigott General/Transfer Finder.

The reference resides in the optical system and can preserve locality through changes of objective/magnification. This is analytically distinct from cross-instrument portability.

## Strongest historical hinge: Bailey 1855 and the surviving collection

The bounded external pass substantially changes the project's centre of gravity.

Bailey is now the strongest early case because three levels of evidence converge:

- his 1855 **Universal Indicator** publication formulates the portability problem before Maltwood;
- Harvard Farlow preserves slides with characteristic Indicator reference lines/orientation marks and a historical catalogue recording marks/measurements for finding individual specimens;
- the Harvard online catalogue contains selected slides later recorded by **Loring W. Bailey with Maltwood's Finder**, including explicit dual-address entries such as `by indicator card A, by Maltwood's Finder, L.W.B.` and `by indicator, by Maltwood's Finder`.

This gives the project a rare object-level transition:

`microscopic object -> Bailey indicator address -> later Maltwood re-address -> catalogue -> surviving collection`

Finder history can therefore be treated as a history of **re-addressing and reference-frame migration**, not merely a sequence of gadget inventions.

## Repository-native anchor: Grunow

Authorities: `data/analysis/grunow_vienna_sample_level_closure_v2.json` and `docs/GRUNOW_SAMPLE_LEVEL_CLOSURE_2026-08-11.md`.

The repository already closes representative historical chains in which a sample number identifies a preparation variant and paired microscope-stage coordinates recover an exact valve. Grunow's instructions distinguish older preparations with pasted scales from later localisation by aligning the slide's upper-left corner to a millimetre scale whose zero coincided with microscope focus. Sample 1363b (`12.9/32.9`) links preparation identity, coordinate and drawing; sample 3073b records several valves by coordinate and uses circling to mark valves already drawn.

This is the strongest repository-native example of **cross-media relocation**:

`sample -> preparation -> coordinate -> exact valve -> drawing -> work-status record`

## Klein/Winkel lead: upgraded

The earlier internal bibliographic lead can now be stated more securely.

A contemporary 1889 *Hedwigia* review says Ludwig Klein's 1888 second paper recommends **Winkel's Markirapparat** and gives instructions for selecting individual forms from mixtures. A later Zeiss/Winkel catalogue closes the apparatus-family mechanism: an adjustable diamond scratches a circle on the coverslip around a selected preparation locality so it can later be found again.

Analytical chain:

`mixed material -> selected individual form -> material marking -> later relocation`

Guard: the later catalogue establishes the working principle of the Winkel apparatus family but does not prove that every mechanical detail of Klein's 1888 device was identical.

## Controlled comparators

### Elcock — within-slide spatial index

Authority: `data/analysis/elcock_type_slides_s_grade_closure_v1.json`.

Elcock's Type Slides arrange named Foraminifera in numbered/printed positions. This is an L3 spatial retrieval interface, not strict arbitrary-field relocation.

### Test/reference objects — separate family

Grayson, Nobert, Möller, Norman and related preparations stabilize repeatable optical tests/comparisons rather than arbitrary microscopic localities. They remain an orthogonal comparator family, especially because Meegan Kennedy is currently developing *Test Objects in Victorian Microscopy*.

## Historiographical position after bounded contemporary scan

Already occupied:

- microscope slides as material/epistemic/symbolic objects (Löwy and HPLS special issue);
- circulation, craft knowledge, standards and interoperability (especially Lea Beiermann);
- embodied Victorian microscopy (Meegan Kennedy);
- early/antebellum American microscopy (Cassedy; Warner);
- Bailey/protistology (John R. Dolan, 2022);
- test objects (Kennedy's active project);
- museum and practitioner histories of named finder devices.

The bounded pass did **not** recover a dedicated contemporary HPS synthesis organized around exact microscopic relocation across instrument-bound coordinates, transferable indicators, substitution grids, direct material marking, optical transfer, reference-frame portability and historical re-addressing.

Use this formulation carefully: `no dedicated relocation-centered HPS synthesis was recovered in this bounded pass`. Do not claim that no one has studied finders or slides.

## Modern continuity comparator

Modern technical microscopy makes the engineering distinction unusually explicit:

`instrument-specific stage coordinate -> Maltwood/England Finder portable address -> software coordinate conversion -> whole-slide-image coordinate / digital annotation`

Use this only as an afterlife/comparator. It helps specify historical variables — orientation, slide geometry, reference-frame independence, calibration and translation — without projecting digital ontology backwards.

## Project files

- `INTERNAL_CONCORDANCE_v1.json` — initial internal mechanism concordance.
- `INTERNAL_DIGEST_02_REFERENCE_OBJECTS.md` — relocation vs reference-object repeatability.
- `INTERNAL_DIGEST_03_KLEIN_WINKEL_LEAD.md` — original partial internal Klein/Winkel lead.
- `CONTEMPORARY_LITERATURE_SCAN_01.md` — contemporary historiography + modern technical continuity.
- `TECHNICAL_CONCORDANCE_v1.json` — source-level case matrix and mechanism families after external pass.
- `EXTERNAL_TECHNICAL_GENEALOGY_01.md` — technical genealogy from early 1850s through later marking/finder regimes.
- `HISTORIOGRAPHY_GAP_ASSESSMENT_v1.md` — occupied fields, bounded gap and claim guards.
- `SYNTHESIS_AND_STOP_RULE_2026-09-08.md` — project synthesis, writing route and hard stop rule.

## Current project claim

> Nineteenth-century microscopists developed multiple reference architectures for converting a transient microscopic field into a persistent address. These systems placed spatial reference in different locations — the instrument, an external indicator, a substitute grid slide, the optical train, or the preparation itself — and therefore differed in what could survive displacement across instruments, observers, magnifications, media and collections.

Compact version:

> **The microscope slide made microscopic material transportable; finder and marking systems made microscopic locality transportable.**

## Hard stop rule

**Broad finder discovery is closed.**

Do not continue generic searches for more finder names, apparatus catalogues, museum examples or practitioner descriptions merely to enlarge the list.

Reopen only if a bounded source can materially change:

1. mechanism classification (especially exact Klönne & Müller 1886 or Fuess 1895 descriptions);
2. chronology (including a meaningful Maltwood 1858/1859 reconciliation);
3. object-level re-addressing evidence;
4. Klein/Winkel exact 1888 mechanism;
5. historiographical overlap with a modern study centered on relocation/reference-frame portability;
6. an active writing need for exact quotation, figure, patent/manufacturer detail or source image.

Otherwise the satellite is **closed for discovery and open for synthesis/writing**.
