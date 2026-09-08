# Internal digest 02 — relocation versus reference-object repeatability

Date: 2026-09-08

Status: **INTERNAL REPOSITORY EVIDENCE ONLY**

## Why this distinction is necessary

The internal sweep shows that the repository already contains two technically adjacent but historically different solutions to repeatability:

- **relocation systems** make the *same microscopic field or object* findable again;
- **reference-object systems** make a *comparison or optical test* repeatable by stabilizing the object or difficulty presented to the microscope.

A finder belongs to the first family. Test plates, test diatoms and named commercial test preparations belong primarily to the second. They should be compared because both solve repeatability problems on glass, but they should not be merged into one technology.

## A. Relocation — returning to the same microscopic object

### Albert Grunow

Authorities:

- `data/analysis/grunow_vienna_sample_level_closure_v2.json`
- `docs/GRUNOW_SAMPLE_LEVEL_CLOSURE_2026-08-11.md`

The repository has S-level evidence for a working coordinate system. Preparation identity plus paired stage coordinates recover individual valves. The instructions distinguish older pasted scales from a later procedure in which the slide's upper-left corner was aligned against a millimetre scale whose zero coincided with microscope focus. Drawings carry the preparation number and coordinate, so a visual representation can lead back to the microscopic object.

This is currently the closest internal analogue to a strict finder mechanism.

## B. Spatial indexing — finding a named specimen within one preparation

### Charles Elcock Type Slides

Authorities:

- `data/analysis/elcock_type_slides_s_grade_closure_v1.json`
- `data/analysis/retrievability_cross_media_infrastructure_v1.json`

Elcock's Type Slides place multiple Foraminifera on black rectangular matrices. Individual grid squares carry printed numbers and species names are visible in the field. The product makes a miniature collection spatially searchable on a single slide.

This mechanism stabilizes a within-slide index. It sits between whole-slide addressing and arbitrary field relocation.

## C. Calibrated reference surfaces — returning to the same optical challenge

### Henry J. Grayson

Authority: `data/analysis/grayson_melbourne_test_ruling_object_archive_upgrade_v1.json`.

Grayson's surviving test plates carry calibrated bands labelled by line density, including a twelve-band object ranging from 10,000 to 120,000 lines per inch. The glass itself encodes the optical-reference values. Repeatability rests on returning to a known ruled band whose difficulty has been numerically stabilized.

### Nobert / Fasoldt

Authorities:

- `data/analysis/trade_catalogue_object_closure_delta_v2.json`
- `sources/source-registry-07.json#US-NMAH-TEST-PLATES`

The repository already closes an object/use chain for nineteenth-century test plates: precision-made test slide → acquisition → resolution experiment → photomicrographic derivative → publication/dispute → later museum object. NMAH preserves an 1884 Charles Fasoldt test slide and photomicrographs made from a Nobert nineteen-band test plate; the museum record also reconstructs the 1867 acquisition and 1868–1869 Army Medical Museum observations.

This is not field relocation. It is a transferable metrological reference object.

## D. Biological reference preparations — returning to a standardized specimen

### Nobert test plate and Möller diatom type slide in Francis Abbott, 1869

Authority: `bibliography/bibliography-11.csv`, record `src_abbott_nobert_moller_1869`.

The bibliography already contains Francis Abbott's 1869 paper centered on Nobert's ruled test plate and Möller's diatom type slide as physical objects for evaluating microscope objectives. The pairing is useful because it places a fabricated ruling beside a prepared biological reference object within the same optical-testing practice.

### John Thomas Norman preparations, 1875

Authority: `data/analysis/source_registry_to_uk_corpus_reverse_bridges_v1.json`, corpus record `R47680`.

A 1875 microscopist tested a foreign objective on named preparations including *Nitzschia sigmoidea* and *Navicula rhomboides* mounted dry by Norman, alongside Topping slides. Commercial maker attribution and preparation identity stabilized the test object sufficiently for reuse in optical comparison after purchase.

Again, the repeatable unit is the named preparation or specimen, not a coordinate within it.

## Comparative model emerging internally

| Mechanism | What is stabilized? | What can be repeated? | Strong internal case |
| --- | --- | --- | --- |
| collection address | identity/location of a slide among slides | retrieval of the preparation | Cole / Cajal / Oxford RMS |
| within-slide index | named position among several mounted specimens | retrieval of a specimen position | Elcock |
| field/object relocation | spatial reference to an exact microscopic object | return to the same valve/field | Grunow |
| calibrated reference surface | known spatial band / numerical difficulty | optical test under a fixed challenge | Grayson / Nobert / Fasoldt |
| biological reference preparation | stable named difficult specimen/preparation | comparative objective test | Möller / Norman / Topping |

## Consequence for the finder project

The internal repository suggests that the historical question should be wider than an accessory genealogy but narrower than `addressability` in general. The promising common problem is **repeatable return**. Historical techniques divide according to what has to be made repeatable:

1. return to the same slide;
2. return to the same specimen-position within a slide;
3. return to the same microscopic field or individual object;
4. return to the same calibrated optical challenge;
5. return to a standardized biological reference object.

Finder technology becomes especially interesting at step 3 because it tries to turn a fleeting field of view into a transferable address. The neighbouring systems show other ways nineteenth-century microscopy stabilized comparison without doing that exact operation.

## Remaining internal limit

The checked internal corpus and indexed default-branch files still do not provide a named historical finder-device genealogy or a source-level vocabulary history of `finder`, `indicator`, `locator`, and related terms. The next phase should first finish the internal vocabulary sweep; only then should external research open against the specific missing mechanisms.
