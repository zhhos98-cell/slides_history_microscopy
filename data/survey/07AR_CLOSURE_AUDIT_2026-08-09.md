# Nineteenth-century microscope-slide survey: 07AR closure audit

Date: 2026-08-09  
Branch: `slide-survey-actions-pilot`  
Status: **CLOSED_2026-08-09**

07AR is an audit-and-freeze pass. It adds **no new survey rows** and ends the 2026-08-09 discovery run.

## Final canonical counts

- Raw modular ledger before 07AR cross-batch canonicalisation: **328 rows**.
- Cross-batch duplicate aliases superseded in 07AR: **20 rows with distinct alias entry IDs**.
- Additional duplicate occurrence with the same `entry_id`: **1** (`DE-MFN-HUBRECHT-EMBRYOLOGY-LATE19C`, present in both 07S and 07AN and already collapsed by `prepare_survey_inputs.py`).
- Frozen canonical discovery layer: **307 unique collection/subcollection/batch/database entries**.
- Provisional strict post-lock total before closure audit: **177**.
- Strict duplicate occurrences removed/collapsed: **21**.
- Pieter Harting row moved from strict to `POSSIBLE_19C`: **1**.
- Frozen strict nineteenth-century layer: **155 entries**.
- Strict data batches remain `07K`-`07AQ`; `07AR` contains closure metadata only.

The raw batch CSVs remain untouched as the audit trail. Canonical runtime preparation now reads `07AR_SUPERSEDED_ALIASES_2026-08-09.json` and skips the 20 superseded alias IDs; identical `entry_id` duplicates continue to collapse through the existing `seen` check.

## Duplicate and hierarchy audit

The closure review found that several late expansion passes rediscovered physical nodes already present in earlier strict batches. These are now aliases, not additional catalogue entries. The supersession map records all twenty distinct-ID aliases and their canonical IDs. Examples include the Powerhouse 19-slide H9118 box, Kitton's Farlow 100-slide set, the Walker Arnott and Grunow collections, SMG Y2001.223, Chaffers's six cabinets, Whipple 2385B, the QMC collection, OHSU Box 42, the Pritchard 1835 case, Van Tieghem's Histothèque core, Harvard HEC, the Bourgogne set, Fasoldt 1884, Dejerine, Yale Lentz, MNHN Comparative Anatomy, SMG A651330, and the Ferdinand I preparation corpus.

The Hubrecht collection appears twice under the identical entry ID in 07S and 07AN. This is not assigned a second alias ID because the canonical merge already collapses duplicate entry IDs.

The following apparent overlaps are intentionally retained because they are not duplicate physical nodes:

- John Tomes's personally prepared dental slides versus the combined Tomes father-son collection.
- MNHN Comparative Anatomy parent collection versus the bounded Gervais and Oscar Schmidt subcollections.
- RAMM's Sladen/Carpenter aggregate versus the W. B. Carpenter foraminifera subcorpus.
- Freiberg's parent thin-section collection versus the bounded 30-section Fuess set.
- Bell-Pettigrew parent collection versus named maker/contributor groups.
- Heddle collection versus the single Blarney slide.
- NHM parent/Data-Portal collections versus named historical acquisitions with independent physical/provenance identity.
- Copies of published diatom sets held by different institutions. Shared serial numbers identify corresponding positions in replicated sets; they do not make the physical copies duplicates.
- NMS Nicol/Forbes thin sections versus BGS Hooker/Nicol fossil-wood thin sections: separate surviving institutional holdings.

## Held-out and excluded leads

### Pieter Harting / Utrecht — retain as discovery, exclude from strict

UMU explicitly states that a few preparations of Pieter Harting survive and separately documents his nineteenth-century microscopy teaching and collecting. The current public wording does not close those surviving preparations specifically as glass microscope slides. `NL-UMU-PIETER-HARTING-PREPARATIONS-19C` is therefore overridden to `POSSIBLE_19C` rather than deleted.

Source: https://umu.nl/pieter-harting/

### Walther Flemming — exclude from surviving-slide catalogue

The closure-stage shorthand `Flemming/Lund` was a conflation. The relevant institutional history is Kiel. Christian-Albrechts-Universität zu Kiel states that Flemming's anatomical writings and preparations were lost with the destruction of the institute in 1944; his microscope and butterfly collection survived. There is therefore no surviving Flemming slide node to promote in this version.

Source: https://www.uni-kiel.de/ps/cgi-bin/unizeit/data/uz-46/pdf/uz-46.pdf

### King's College London Museum of Life Sciences — retain generic lead; Dawes excluded from nineteenth century

KCL states that the Museum of Life Sciences holds microscope slides within collections whose specimens span the early nineteenth century to the present, but the public overview does not identify which slide objects themselves are nineteenth-century. The named Dawes Collection consists of two microscope-slide cabinets assembled by Ben Dawes, who was professor in the middle of the twentieth century. The generic historical-slide lead therefore remains held out, while the Dawes cabinets are an out-of-period comparator rather than a strict nineteenth-century node.

Sources: https://www.kcl.ac.uk/lsm/centre-for-education/museums/museum-of-life-sciences and https://www.kcl.ac.uk/its-no-fluke

### Perroncito — retain held out

The earlier audit remains in force: current evidence closes a nineteenth-century parasite collection and the presence of histological preparations in the same museum context, but does not close those two claims onto the same surviving slide objects. No strict row is restored in 07AR.

## Quantity-namespace audit

The frozen directory keeps the following quantity types separate. No arithmetic conversion between them is permitted without an explicit source bridge:

- individual glass slides or microscopic preparations;
- current surviving slide totals;
- historical dated inventory/acquisition states;
- serial-set positions and published set numbers;
- embryo or specimen series;
- catalogue/sample/accession/register identifiers;
- boxes, trays, drawers and cabinets;
- cabinet capacity or slot count;
- specimens, taxa, localities, drawings, photographs, negatives and raw samples;
- digital images or database rows;
- mixed-period parent-collection totals.

In particular, register-number ranges are never subtracted to create a slide count; cabinet capacity is never treated as survival; a present aggregate is never projected backward; a collection proportion is not converted into a pre-1900 subtotal; and distributed-set serial numbers are not summed across institutions as though they were one physical copy.

## Relationship audit

The final directory preserves relationship phrases as evidence rather than flattening them into ownership. `prepared by`, `mounted by`, `collected by`, `assembled by`, `used by`, `sent to`, `received by`, `exchanged by`, `presented to`, `donated by`, `purchased by`, `sold by`, `distributed by`, `lent by`, `transferred from`, `from the collection of`, `belonging to`, `held by`, `catalogued by`, `digitised by`, `inscribed`, `labelled by`, `part of`, and `from the period of` remain distinct relations when the source distinguishes them.

Consequently:

- donor does not automatically mean preparer or original collector;
- sender does not automatically mean preparer;
- a named collection does not automatically mean every slide was made by the namesake;
- `probably by` remains probabilistic;
- a lifetime or tenure supplies only a chronological bound unless an object/date relation is explicit;
- current custody is not historical ownership or original provenance.

## Validation and freeze status

Repository-side preparation and validation scripts remain the operational route: `prepare_survey_inputs.py` merges modular rows, applies the 07AR alias-supersession map, and collapses duplicate entry IDs before `audit_19c_scope.py`, `apply_19c_scope.py`, `validate_survey.py`, batch planning and harvesting.

07AR is a **data-audit freeze, not a CI-pass claim**. At closure time no fresh GitHub check run had yet been observed for the latest branch head. The final head is checked separately after the closure files and README are committed; if GitHub still reports no fresh check, the manifest records that fact explicitly.

## Reopening policy

This directory is frozen at `CLOSED_2026-08-09`. Any later discovery, newly digitised register, institutional reply, corrected attribution, or item-level count should enter a new reopening/version rather than silently extending `07K`-`07AQ` or altering the 07AR closure counts without a versioned audit record.
