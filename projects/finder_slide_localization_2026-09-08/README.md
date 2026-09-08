# Finder / microscopic relocation technologies

Date started: 2026-09-08

Branch: `research/finder-slide-localization-tech`

Status: **SYNTHESIS READY — EXACT-SOURCE CLOSURE COMPLETE — BROAD DISCOVERY CLOSED**

## Scope

This satellite project asks how nineteenth-century microscopists made a microscopic field or microscopic object **findable again**. The immediate subject is the family of techniques approached through finders, indicators, stage coordinates, slide-borne scales/grids, material marking devices, optical transfer systems and related locating technologies.

The core microscope-slide census remains frozen. This project does not extend the 307/155 survey, alter the parked bibliography, or reopen the repository-wide discovery queue.

## Governing question

**How was a microscopic field converted into an address that could be revisited across time, operators, instruments, drawings, correspondence and collections?**

The project no longer treats `finder` as a sufficient historical category. Its governing variable is now **calibrated reference-frame portability**: where was spatial reference stabilised, what displacement was it intended to survive, and what standards, calibration or translation were required to keep the address meaningful when the slide, stage, microscope, objective, observer, documentary medium or custody regime changed?

Operational chain:

`field/object -> stabilised reference frame -> recorded address or material mark -> displacement -> calibration/translation if needed -> reconstruction of locality -> same field/object`

## Address hierarchy inherited from the Slides repository

The repository already uses `addressability` at several scales. This project isolates the finest spatial level and keeps it distinct from neighbouring address systems:

1. **collection / cabinet address** — makes a slide retrievable among other slides;
2. **slide / series address** — identifies a preparation, product, issue, or sample;
3. **within-slide spatial index** — assigns locations to several mounted specimens on one slide;
4. **microscope-field / object relocation** — permits return to a particular microscopic field or object by a reproducible spatial reference.

Only the fourth category is a finder-equivalent mechanism in the strict working sense. The third is a close comparator. The first two remain contextual infrastructure.

## Five mechanism families

### 1. Instrument/stage-bound coordinate frame

Examples: Wright; Okeden; Smith; mechanical-stage verniers; **Klönne & Müller 1886 Bacteria Finder**; partly Grunow.

The apparatus or carrier supplies the reference frame. Numerical return can be precise, but the address is vulnerable to changes in stage geometry, zero, orientation, calibration or microscope.

Klönne & Müller is now closed at S-level: the 1886 Pendulum Object-frame/Bacteria Finder uses two graduated motions — a pendulum/swinging axis and a traversing screw — read through circular graduations and a millimetre scale with vernier.

### 2. Transferable external indicator/carrier

Central case: **Jacob Whitman Bailey's Universal Indicator (1855)**.

Bailey explicitly opposed devices useful only with one particular microscope and sought a record independent of the original instrument and observer, suitable for distant correspondence and long-term collection use. He described the indicator card as a transferable stage.

### 3. Substitution reference slide/grid

Central case: **Maltwood's Finder (1858)**; later Webb and England Finder.

The preparation is removed and a reference grid is substituted at a reproducible position. Stable slide geometry/orientation converts a microscopic locality into a nominally transferable grid address.

The Greville/Gregory afterlife shows that such portability is conditional: different finder instances and slide dimensions may require empirical correction before an old coordinate recovers the exact historical individual.

### 4. Direct material target marking

Examples: **Bridgman (1855)**; Francotte; Winkel; Fuess; surviving diamond-marked Gregory/Greville preparations.

The target locality is materially marked on the coverslip/preparation, often with a diamond-scratched ring. The spatial key travels with the preparation instead of being translated into an external stage coordinate.

Fuess 1895 is now capped at A-level as a direct-marking family case through near-contemporary technical evidence; exact JRMS p.587 mechanics remain a writing-detail residual only.

### 5. Optical/eyepiece transfer reference

Example: Royston-Pigott General/Transfer Finder.

The reference resides in the optical system and can preserve locality through changes of objective/magnification. This is analytically distinct from cross-instrument portability.

## Early formation cluster, 1855–1858

Exact-source closure substantially strengthens the early history.

### Bailey 1855

Bailey makes instrument/observer independence and distant correspondence explicit design objectives. `Reference-frame portability` is therefore an actor-level problem, not only a retrospective analytical term.

### Amyot 1856

Amyot directly joins physical and epistemic transport: finder/carrier devices could also function as packing cases for slides sent through the post, while the location system was intended to let a correspondent recover the relevant object.

### Microscopical Society Committee on Finders, 1856; Edwards 1857

By June 1856 relocation had become a society-level engineering problem. The committee required a finder to work with different microscopes, avoid cumbersome or destructive registration, remain legible in ordinary use, and be cheap/simple. Edwards tied his indicator geometry directly to the Society-recommended **3 × 1 inch slide**.

This closes a source-level relation:

`standard slide geometry -> finder geometry -> interoperability`.

### Maltwood 1858

The original Transactions paper is securely anchored at **1858**, not 1859. Maltwood's substitute-grid architecture is important as one solution within an already active portability debate, not as the origin of the problem.

## Strongest historical hinge: Bailey collection re-addressing

Three evidence levels converge:

- Bailey's 1855 publication formulates portability before Maltwood;
- Harvard Farlow preserves slides with Universal Indicator reference lines/orientation marks and a historical catalogue recording marks/measurements for finding individual specimens;
- selected catalogue entries later add **Maltwood Finder** references by Loring W. Bailey.

This gives the project a rare object-level transition:

`microscopic object -> Bailey indicator address -> later Maltwood re-address -> catalogue -> surviving collection`

Finder history can therefore be studied as **re-addressing and reference-frame migration**, not merely a sequence of gadget inventions.

## Second object-level hinge: Greville/Gregory calibrated recovery

Danielidis and Mann's 2002 re-study of Greville/Gregory material recovered exact historical individuals through old Maltwood references, but only after empirically translating those references to the available finder. They report systematic finder-to-finder differences and effects from physical slide dimensions.

The chain is:

`historical Maltwood frame -> systematic discrepancy -> calibration/translation -> recovered exact individual -> drawing/taxonomic identity`.

This is the strongest evidence for the revised governing concept **calibrated portability**.

Modern studies of the same historical collections continue to use finder coordinates, labels, drawings and exact specimens in nomenclatural work. Historical spatial addresses remain active scientific infrastructure rather than antiquarian metadata.

## Repository-native anchor: Grunow

Authorities: `data/analysis/grunow_vienna_sample_level_closure_v2.json` and `docs/GRUNOW_SAMPLE_LEVEL_CLOSURE_2026-08-11.md`.

The repository closes representative chains in which a sample number identifies a preparation variant and paired microscope-stage coordinates recover an exact valve. Older preparations could carry pasted scales; later localisation aligned the slide's upper-left corner to a millimetre scale whose zero coincided with microscope focus. Sample 1363b (`12.9/32.9`) links preparation identity, coordinate and drawing; sample 3073b records several valves by coordinate and uses circling to mark valves already drawn.

This is the strongest repository-native example of **cross-media relocation**:

`sample -> preparation -> coordinate -> exact valve -> drawing -> work-status record`

## Klein/Winkel: closed at the correct evidence ceiling

Ludwig Klein's 1888 II article identity is secure. A contemporary 1889 *Hedwigia* review says the paper recommends **Winkel's Markirapparat** and gives instructions for selecting individual forms from mixtures. Later Winkel/Zeiss catalogue evidence closes the apparatus-family principle: a diamond scratches a circle on the coverslip around a selected locality so it can later be found again.

Analytical chain:

`mixed material -> selected individual form -> material marking -> later relocation`

Guard: Klein II full primary prose was not successfully recovered in this pass. Do not assert that every later mechanical detail was already present in 1888. The residual is now exact wording/mechanical detail only.

## Late-century coexistence, not linear succession

The exact-source pass rejects a simple story in which mechanical-stage finders are replaced by Maltwood and then by a universally superior system.

Late nineteenth-century practice continued to support:

- precision within a controlled mechanical coordinate frame;
- transferable indicators;
- substitution-grid addresses;
- direct material circles/marks;
- optical transfer systems.

A late-century German technical comparison explicitly criticizes arbitrary instrument-attached scales as non-transferable across changed geometries and contrasts them with coverslip marking systems. Conversely, the exact 1886 Klönne & Müller Bacteria Finder shows that highly developed mechanical coordinate systems continued to be designed because they solved exhaustive search and precision tasks especially well.

The historical question is therefore: **which relations did each reference architecture make durable, and which displacements could it survive?**

## Controlled comparators

### Elcock — within-slide spatial index

Authority: `data/analysis/elcock_type_slides_s_grade_closure_v1.json`.

Elcock's Type Slides arrange named Foraminifera in numbered/printed positions. This is an L3 spatial retrieval interface, not strict arbitrary-field relocation.

### Test/reference objects — separate family

Grayson, Nobert, Möller, Norman and related preparations stabilize repeatable optical tests/comparisons rather than arbitrary microscopic localities. They remain an orthogonal comparator family, especially because Meegan Kennedy is currently developing *Test Objects in Victorian Microscopy*.

## Historiographical position

Already occupied:

- microscope slides as material/epistemic/symbolic objects (Löwy and HPLS special issue);
- circulation, craft knowledge, standards and interoperability (especially Lea Beiermann);
- embodied Victorian microscopy (Meegan Kennedy);
- early/antebellum American microscopy (Cassedy; Warner);
- Bailey/protistology (John R. Dolan, 2022);
- test objects (Kennedy's active project);
- museum and practitioner histories of named finder devices.

The bounded pass did **not** recover a dedicated contemporary HPS synthesis organized around exact microscopic relocation across competing reference frames, calibration, portability and historical re-addressing.

Use this carefully: `no dedicated relocation-centered HPS synthesis was recovered in this bounded pass`. Do not claim that no one has studied finders or slides.

## Current project claim

> Nineteenth-century microscopic relocation was a problem of calibrated portability. Microscopists placed spatial reference in stages, carriers, transferable indicators, substitute finder slides, optical systems, or the preparation itself. Each architecture made some relations durable while leaving others vulnerable to changes of instrument, observer, orientation, scale and custody. The history of finders is therefore less a succession of locating gadgets than a history of constructing, maintaining and migrating portable microscopic addresses.

Compact version:

> **The microscope slide transported microscopic material; finder systems transported microscopic locality, but locality remained portable only while its reference frame could be reconstructed, calibrated or translated.**

## Project files

- `INTERNAL_CONCORDANCE_v1.json` — initial internal mechanism concordance.
- `INTERNAL_DIGEST_02_REFERENCE_OBJECTS.md` — relocation vs reference-object repeatability.
- `INTERNAL_DIGEST_03_KLEIN_WINKEL_LEAD.md` — original partial internal Klein/Winkel lead.
- `CONTEMPORARY_LITERATURE_SCAN_01.md` — contemporary historiography + modern technical continuity.
- `TECHNICAL_CONCORDANCE_v1.json` — source-level case matrix and mechanism families after external pass.
- `EXTERNAL_TECHNICAL_GENEALOGY_01.md` — technical genealogy from early 1850s through later marking/finder regimes.
- `HISTORIOGRAPHY_GAP_ASSESSMENT_v1.md` — occupied fields, bounded gap and claim guards.
- `SYNTHESIS_AND_STOP_RULE_2026-09-08.md` — first project synthesis and hard stop rule.
- `EXACT_SOURCE_CLOSURE_01_1853_1858.md` — Bailey/Amyot/Committee/Edwards/Carpenter/Maltwood exact-source formation cluster.
- `OBJECT_LEVEL_READDRESSING_02_GREVILLE_MALTWOOD.md` — Greville/Gregory finder calibration, exact-individual recovery and modern re-addressing.
- `EXACT_SOURCE_CLOSURE_02_LATE_MARKING_AND_BACTERIA_FINDER.md` — Klönne & Müller exact mechanism; Fuess and Klein evidence ceilings; late marking-vs-coordinate comparison.
- `SYNTHESIS_ADDENDUM_01_CALIBRATED_PORTABILITY.md` — revised synthesis after exact-source closure.

## Residual state

- Klönne & Müller 1886 Bacteria Finder: **closed S-level**.
- Maltwood 1858/1859 chronology: **closed at working level; original Transactions paper = 1858**.
- Fuess 1895: **capped A-level direct-marking classification**; original mechanical detail only if needed for writing.
- Klein 1888 II: **selection/marking link closed through contemporary review; exact primary mechanical wording only if needed for writing**.
- historiographical overlap: reopen only if a modern academic study directly centers microscopic relocation/reference-frame portability.

## Hard stop rule

**Broad finder discovery is closed. Technical residual discovery is also closed at the current evidence ceiling.**

Reopen only if a bounded source can materially change:

1. mechanism classification;
2. chronology;
3. object-level re-addressing or calibration;
4. Klein/Winkel exact mechanism in a way that changes the interpretation;
5. historiographical overlap with a relocation-centered modern study;
6. an active writing need for exact quotation, figure, patent/manufacturer detail or source image.

Otherwise the satellite is **closed for discovery and open for synthesis/writing**.
