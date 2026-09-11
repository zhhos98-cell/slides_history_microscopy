# CURRENT PROGRESS — Iron Library / Wedding / Sheffield–Berlin

**Pinned continuation state — 2026-09-11.**

This file is the first resume point for the Iron Library project. Do not replace or supersede it with unrelated project activity. Update it only when this project itself advances.

## Current research position

The project has moved beyond generic Iron Library discovery. The working comparative frame is now:

**Sheffield / British industrial observation → return to Berlin/Charlottenburg → prepared specimen → reflected-light microscopy → microphotography → printed/reference collections.**

The stronger question is not who invented metallography or whether knowledge simply diffused from Britain to Germany. The working problem is how **material comparison changed scale, institutional setting and evidential carrier** while remaining a comparative practice.

A provisional formulation is:

> How did the comparison of iron and steel move from industrial works visited by travelling metallurgists to prepared surfaces, microscopic fields and photographic reference collections?

The useful geographic comparison is therefore **Sheffield + Berlin/Charlottenburg**, with Iron Library holdings supplying the travel/industrial and object-history side and Berlin material-testing history supplying the post-return institutional reorganisation.

## Wedding digital corpus status

1. Hermann Wedding's Iron Library manuscripts `Mss 23`, `Mss 24`, `Mss 25` are fully digitised on e-codices.
2. `Mss 25` (1860–1862; Germany–Belgium–England) is the priority remote corpus for British travel, Sheffield, Bessemer, named works, introductions and technical contacts.
3. `Mss 25` contains **402 IIIF canvases**.
4. A Windows PowerShell IIIF workflow was tested successfully; 2000 px was much sharper than necessary and **900 px** was selected for whole-volume rapid reading/indexing.
5. The user reports that local 900 px image acquisition for **Mss 23, Mss 24 and Mss 25 has completed**. Important pages can later be reacquired at 2000 px or full resolution.
6. `Mss 25` working directory was established as `C:\Users\13563\Desktop\wedding_mss25`, with analogous Mss 23/24 folders.
7. A separate local-computer/Codex task has been specified to merge each volume to PDF, run local Tesseract-first/PaddleOCR-fallback OCR, emit three provenance-rich JSON files and upload only those JSONs to this project. **Completion of that PDF/OCR/upload task has not yet been confirmed in this chat; do not assume it is finished.**

## Fischer 1845–1846 corpus: active controlled baseline

Three machine-readable Fischer text files were supplied. Two are duplicate/OCR witnesses of the 1845 travel account; the cleaner `...Low-Moor, Sheffield, und zurück im Sommer 1845.txt` is the canonical working text. The third is the 1846 journey through London, Derby/Butterley, Sheffield and Liverpool.

Current Fischer project files:

1. `FISCHER_1845_1846_NODE_INDEX.md` — comparison/material/image synthesis;
2. `FISCHER_TESTING_REGIME_1845_1846.md` — batch sampling, external trials, mechanical testing, hardening and provenance;
3. `FISCHER_ACCESS_NETWORK_1845_1846.md` — people coded by what access/testing/judgement they make possible;
4. `FISCHER_MEASUREMENT_AND_OBSERVATION_1845_1846.md` — autopsy, ruler/counting/weighing/calculation, sensory judgement and reliability;
5. `FISCHER_1845_1846_EVENT_INDEX.tsv` — date-ordered machine-readable event table using common analytical operation codes.

These Fischer texts are research OCR/transcription aids, not manually verified diplomatic transcriptions.

## Fischer: strongest current findings

### Comparison is an actor category

Fischer explicitly describes early British experience as supplying `Vergleichungspunkte` and states that British industrial scale/perfection cannot be grasped without `Autopsie`.

But `Autopsie` is not simply eyesight. Fischer repeatedly combines seeing with counting, measuring, weighing, calculation, questioning, sampling and comparison.

Working shorthand:

**see → count → measure → ask → weigh → calculate → compare → sample → record**

### Low Moor: sampling, numbering and traceability

At Low Moor in 1845 Fischer states that **a sample is taken from every tapping and the output/batch is numbered**, explicitly in connection with supplying iron of specified quality. He also leaves with a staged portable series of ore, limestone, coal, coke and iron through multiple production stages.

This gives a strong pre-laboratory industrial sequence:

**production event → sample → number → quality distinction → customer delivery**

Do not call this metallography or a laboratory genealogy.

### Provenance loss as the inverse problem

In 1846 Fenn tells Fischer that English cast steel quality has declined partly because competitive manufacturers buy old railway springs and similar material whose quality they do not know, then remelt the heterogeneous material together cheaply.

This creates a useful contrast:

- **Low Moor:** sample + number preserve production identity;
- **mixed old railway material:** unknown prior quality + remelting destroy provenance and make final quality less reliable.

Material provenance is therefore now a controlled research variable.

### Sheffield testing apparatus

In 1846 Fischer describes a dedicated locomotive-spring `Probemaschine`: a hardened curved spring is mechanically pressed flat, released and checked against reference points to determine whether it has permanently yielded or broken.

This is a repeatable industrial mechanical test with controlled deformation, reference geometry and a quality judgement.

### Apparatus and body coexist

In the same Sheffield file-hardening context Fischer estimates hardening-water temperature by feel and then tastes the water to identify the additive. Controlled apparatus therefore coexists with skilled eye/hand/taste judgement.

This warns against a simple story in which laboratory instruments merely replace the senses.

### External distributed testing

Brande's Royal Mint letter reports trials of Fischer's steel, satisfaction with the result, requests further bars of specified dimensions and proposes continued supply if the sample quality is maintained.

Fischer also takes his own hardened razor-blade blanks to Rodgers & Son in Sheffield for grinding, polishing, fitting and judgement of steel quality.

### Representation becomes portable and reproducible

Fischer carries J. Beck's coloured drawings of his own steel works and uses them in technical/social encounters. In London he engages Willat and Croucher around photographic paper and arranges for a large foundry image to be converted into a photographic negative and positive copies.

Working sequence:

**industrial operation → coloured drawing → photographic negative → reproducible positive image**

Weather/scale materially affect the success of the positive reproduction.

### Access is an epistemic variable

Named contacts do different work: John Gott makes Low Moor logistically reachable; recommendations produce proprietor/works access; Faraday receives and inspects Fischer material; Brande supplies an authoritative institutional test judgement; Faraday/Brande names become credentials for access to the Croydon atmospheric-railway Engine House; a technically weak Butterley guide causes Fischer explicitly to downgrade the reliability of information.

Wedding's people therefore need to be coded by function, not merely listed as contacts.

### No microscopic claim in Fischer 1845–1846

Exact searches in the supplied 1845 and 1846 machine-readable texts did not produce a `Mikro...` hit. This does not prove absolute absence in the originals/OCR, but there is currently **no positive textual basis for making Fischer 1845–46 a microscopy story**.

Its value is instead the prehistory of comparison, sampling, testing, measurement, provenance and portable representation.

## Revised pre-metallographic sequence

The Fischer evidence now supports a differentiated baseline:

1. works visit / `Autopsie`;
2. quantified process comparison;
3. counting, measuring, weighing and calculation by the traveller;
4. production sampling and batch numbering;
5. staged portable material series;
6. preservation or loss of material provenance;
7. external institutional trial;
8. skilled preparation/finishing followed by expert judgement;
9. controlled mechanical testing in dedicated apparatus;
10. embodied sensory/predictive judgement;
11. drawings, letters and photographic reproductions that carry comparison away from the site.

The later Wedding/Martens problem may add:

12. deliberately prepared polished specimen;
13. microscopic field;
14. microphotographic glass plate;
15. printed/reference image and collection.

This is an analytical comparison and **not yet a direct historical genealogy**.

## Immediate next substantive operation

The Fischer extraction framework is now stable enough to apply to Wedding. When the Wedding images/OCR are available, build page-level indices for Mss 23–25 with common fields:

- date / itinerary;
- person and functional role: `introducer | gatekeeper | host | technical guide | worker | tester | judge | sample donor | correspondent | image-maker | institutional credential`;
- works / institution;
- technical operation;
- material sample carried, received, transformed or tested;
- `SEE | COUNT | MEASURE | WEIGH | CALCULATE | SAMPLE | NUMBER | APPARATUS_TEST | EXPERT_JUDGEMENT | SENSORY_JUDGEMENT | PROVENANCE | IMAGE | ACCESS | RELIABILITY_WARNING`;
- source of datum: direct observation / oral report / copied document or drawing / inference;
- Sheffield / Bessemer / named works;
- technical drawings;
- any genuine mineralogical, microscopic or specimen-preparation vocabulary.

The aim is to reconstruct the British observational/testing phase before asking what Wedding did after returning to Berlin.

## Next analytical move after Wedding British itinerary control

Compare the Wedding material against:

1. Sorby's Sheffield diaries / surviving metallurgical specimen context;
2. Wedding's post-1862 Berlin teaching and metallurgical work;
3. Martens and the Königliche mechanisch-technische Versuchsanstalt / later Materialprüfungsamt;
4. the 1885 Wedding–Sorby microscopic-structure dispute, especially specimen preparation and illumination;
5. the Iron Library's three original Droste/Martens microphotographic glass plates and their still-unresolved object-level identifiers.

A direct Wedding–Sorby meeting in 1860/62 remains a **hypothesis**, not a claim. Co-presence must be tested by dates and names.

## Residency logic

The already digitised Wedding/Fischer material is preliminary research, not itself a reason to travel.

A Scholar in Residence application should be built around the second stage:

- what happened after the British industrial journeys;
- how observational comparison/testing was reorganised in German institutions;
- how material identity and provenance were preserved or reconstructed;
- how prepared specimens, microscopic fields, photographic glass plates and printed plates became durable forms of evidence;
- what still-undigitised or object-dependent Iron Library / Georg Fischer material is needed to answer that question.

The onsite case becomes compelling only when the remaining corpus is demonstrably too material, distributed or extensive to replace with a small reproduction request.

## High-value unresolved onsite layer

Priority objects/series remain:

- the three original Droste/Martens early microphotographic glass plates;
- exact meaning of `G 745,1`, `Per765`, `A346`;
- physical metadata, inscriptions, backs, mounts, ordering and printed-plate matches;
- nineteenth-century GF working papers/correspondence that remain undigitised after item-level ANTON verification;
- any material-testing / metallography / exhibition / photographic series whose physical ordering or object features are not captured digitally.

## Resume rule

When returning to this project, **read this file first**, then:

1. `FISCHER_1845_1846_EVENT_INDEX.tsv` for the controlled chronology/operation codes;
2. `FISCHER_TESTING_REGIME_1845_1846.md` for testing/provenance;
3. `FISCHER_MEASUREMENT_AND_OBSERVATION_1845_1846.md` for observation/reliability;
4. `FISCHER_ACCESS_NETWORK_1845_1846.md` for functional network coding;
5. `FISCHER_1845_1846_NODE_INDEX.md` for the broader synthesis;
6. `RESIDENCY_TRIAGE_2026-09-11.md` for digitised-vs-onsite logic;
7. `PUBLIC_DIGITAL_CORPUS.md` and `SOURCE_MAP.md` for acquisition/evidence control.

Do not reopen generic Iron Library searching before the Wedding/Fischer page-level British itinerary/person/comparison index has been completed.
