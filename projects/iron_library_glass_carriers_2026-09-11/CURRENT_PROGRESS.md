# CURRENT PROGRESS — Iron Library / Wedding / Sheffield–Berlin

**Pinned continuation state — 2026-09-11.**

This file is the first resume point for the Iron Library project. Do not replace or supersede it with unrelated project activity. Update it only when this project itself advances.

## Current research position

The project has moved beyond generic Iron Library discovery. The working comparative frame is:

**Sheffield / British industrial observation and testing → return/circulation to Berlin/Charlottenburg → prepared specimen → reflected-light microscopy → microphotography → printed/reference collections.**

The stronger question is not who invented metallography or whether knowledge simply diffused from Britain to Germany. The working problem is how **material comparison changed scale, institutional setting, evidential carrier, access regime and reference structure** while remaining a comparative practice.

Two linked questions are now controlled:

> How did the comparison of iron and steel move from industrial works visited by travelling metallurgists to prepared surfaces, microscopic fields and photographic reference collections?

> What happened when knowledge that had depended on personal recommendation, privileged factory access, practical competence, selective disclosure, travelling samples and repeated cross-site testing was reorganised into institutional specimen/testing/image systems?

The useful geographic comparison is **Sheffield + Berlin/Charlottenburg**. Iron Library material supplies the travel/industrial/object-history side; Berlin material-testing history supplies the post-return institutional reorganisation.

## Wedding digital corpus status

1. Hermann Wedding's Iron Library manuscripts `Mss 23`, `Mss 24`, `Mss 25` are fully digitised on e-codices.
2. `Mss 25` (1860–1862; Germany–Belgium–England) remains the priority remote corpus for British travel, Sheffield, Bessemer, named works, introductions and technical contacts.
3. `Mss 25` contains **402 IIIF canvases**.
4. A Windows PowerShell IIIF workflow was tested successfully; **900 px** was selected for whole-volume rapid reading/indexing, with later reacquisition of important pages at 2000 px or full resolution.
5. The user reports that local 900 px image acquisition for **Mss 23, Mss 24 and Mss 25 has completed**.
6. `Mss 25` working directory was established as `C:\Users\13563\Desktop\wedding_mss25`, with analogous Mss 23/24 folders.
7. A separate local-computer/Codex task was specified to merge each volume to PDF, run local OCR and upload provenance-rich JSON files. **No Wedding OCR JSON is currently visible in the GitHub project; do not assume that task is complete.**

## Fischer 1845–1846 corpus: controlled baseline

Three machine-readable Fischer text files were supplied. Two are duplicate/OCR witnesses of the 1845 account; the cleaner `...Low-Moor, Sheffield, und zurück im Sommer 1845.txt` is the canonical working text. The third is the 1846 journey through London, Derby/Butterley, Sheffield and Liverpool.

Current Fischer project files:

1. `FISCHER_1845_1846_EVENT_INDEX.tsv` — date-ordered machine-readable event table;
2. `FISCHER_KNOWLEDGE_BOUNDARY_MATRIX_1845_1846.tsv` — publication/practical competence/access/patent/secrecy/sample/image/testing matrix;
3. `FISCHER_SAMPLE_AND_REFERENCE_REGIMES_1845_1846.md` — demonstration, trace, staged-series, reference-quality and prepared-test-object distinctions;
4. `FISCHER_ITERATIVE_TESTING_CIRCUIT_1845_1846.md` — 1845–46 as one repeated sample/test/document/return circuit rather than two isolated journeys;
5. `FISCHER_TESTING_REGIME_1845_1846.md` — batch sampling, external trials, mechanical testing, hardening and provenance;
6. `FISCHER_MEASUREMENT_AND_OBSERVATION_1845_1846.md` — autopsy, counting/measurement/weighing/calculation, sensory judgement and reliability;
7. `FISCHER_KNOWLEDGE_EXCHANGE_AND_SECRECY_1845_1846.md` — practical knowledge, patents, strategic non-disclosure, selective disclosure and reciprocal questioning;
8. `FISCHER_ACCESS_NETWORK_1845_1846.md` — functional network, technical credibility and tiered visibility;
9. `FISCHER_1845_1846_NODE_INDEX.md` — broader synthesis.

These Fischer texts are OCR/research aids, not manually verified diplomatic transcriptions.

## Fischer: strongest controlled findings

### 1. Comparison is an actor category, but `Autopsie` is not simply eyesight

Fischer explicitly uses `Vergleichungspunkte` and says British industrial scale/perfection cannot be grasped without `Autopsie`. In practice he combines direct seeing with counting, measuring, weighing, calculation, questioning, sampling and comparison.

Working shorthand:

**see → count → measure → ask → weigh → calculate → compare → sample → record**

### 2. Sample is not one category

The corpus now supports at least five distinct sample regimes:

- **demonstration sample** — portable object shown to solicit recognition, judgement or business;
- **trace sample** — sample taken from a specific production event and linked to batch identity;
- **staged process series** — material assembled across successive production stages;
- **reference-quality sample** — a tested sample becomes the benchmark for future deliveries;
- **prepared test object** — material is transformed/finished before expert judgement.

Low Moor provides the clearest traceability example: a sample is taken from every tapping and the output is numbered for supply by specified quality. The same visit produces a portable staged series of ore, limestone, coal, coke and iron through successive production stages.

### 3. The Royal Mint `Musterstange` becomes a normative reference

Brande's 1 January 1846 letter reports successful trials of Fischer's steel and requests future bars **of the same quality as the sample bar**. The object therefore moves from `tested sample` to a practical reference against which future production is specified.

Do not call this a modern certified reference material or formal metrological standard. The source supports a practical normative reference relation.

### 4. Provenance can be preserved or destroyed

Low Moor preserves identity through sample + number. Fenn later complains that English cast-steel quality has declined partly because manufacturers remelt old railway springs and other material whose prior quality they do not know.

Controlled contrast:

**known production event → sample → number → quality identity**

versus

**unknown prior material → heterogeneous remelting → provenance loss → quality uncertainty**.

### 5. Industrial testing already includes dedicated apparatus

Fischer describes a Sheffield locomotive-spring `Probemaschine`: a hardened curved spring is pressed flat, released and checked against reference points to determine whether it has permanently yielded or broken.

But apparatus does not simply replace the senses. In the file-hardening shop Fischer estimates hardening-water temperature by feel and tastes it to identify the additive. Machine, reference geometry, eye/hand/taste and craft expertise coexist.

### 6. Access is an epistemic variable and visibility is tiered

Recommendation letters, old relations, named institutional contacts and the visitor's technical reputation determine what becomes visible. Fischer says useful recommendations require being `gut angeschrieben`; a Sheffield contact explicitly offers access not given to everyone; at another works Fischer deliberately demonstrates technical competence before receiving deeper access and material samples. Butterley supplies the negative control: formal entry with a technically weak guide yields information Fischer himself marks as unreliable.

### 7. Knowledge exchange has explicit boundary rules

Fischer quotes Swedenstierna on not publishing a detailed Sheffield cast-steel process even after close observation: writing plus practical competence may guide a practitioner, while strategic withholding can remain advantageous. Fischer then states that he answered Sheffield questions about wages/production **in detail in order to become entitled to ask counter-questions**.

Controlled boundary modes now include:

`PUBLICATION | PRACTICAL_COMPETENCE | PATENT_PRIORITY | SECRET | SELECTIVE_DISCLOSURE | RECOMMENDATION | PRIVILEGED_ACCESS | RECIPROCAL_EXCHANGE | DEMONSTRATION | DOCUMENT_COPY | WITHHOLDING`.

Patent priority, strategic secrecy and selective disclosure coexist; do not flatten the domain into a single category of `tacit knowledge`.

### 8. 1845 and 1846 form an iterative testing circuit, not two isolated journeys

The strongest temporal structure is:

**journey → sample/order → shipment → external test → written judgement → repeat supply → return journey → reuse of test authority in new encounters**.

In 1845 Brande examines Fischer's material and gives an order. A steel bar later travels from Schaffhausen to the Royal Mint and is tested. By October 1846 Fischer says he has supplied the Mint repeatedly; Brande's written judgement is then carried back into Sheffield and shown during Cammell discussions.

The circuit therefore continues while Fischer is absent and bundles multiple carriers on return: material samples, letters, recommendations, drawings and embodied experience.

### 9. Representation becomes portable and reproducible

Beck's coloured works drawing circulates in British technical encounters and is then transformed by Croucher into a photographic negative and attempted positive copies. Weather and scale affect success.

Working chain:

**industrial operation → drawing → photographic negative → reproducible positive image**.

### 10. Numbering has distinct functions

Do not collapse all numbering into one regime:

- Low Moor batch/tapping numbering preserves industrial traceability;
- the Polytechnic Institution uses catalogue-numbered objects for collection ordering/retrieval;
- later metallographic specimen/image numbering, if demonstrated, must be treated as a separate reference practice.

### 11. No positive microscopic claim in Fischer 1845–1846

Exact searches in the supplied OCR texts produced no `Mikro...` hit. This does not prove absolute absence in the originals, but there is currently **no positive textual basis for making Fischer 1845–46 a microscopy story**.

Its value is the controlled baseline for comparison, access, sampling, reference quality, testing, provenance, circulation and representation.

## Revised pre-metallographic architecture

The Fischer evidence now supports a differentiated baseline:

1. works visit / `Autopsie`;
2. quantified process comparison;
3. traveller counting, measurement, weighing and calculation;
4. demonstration samples;
5. production trace samples + batch numbering;
6. staged portable process series;
7. preservation or loss of material provenance;
8. tested sample becoming a practical reference for future quality;
9. external institutional trial;
10. skilled preparation/finishing followed by expert judgement;
11. controlled mechanical testing in dedicated apparatus;
12. embodied sensory/predictive judgement;
13. recommendation, privileged access and performed technical credibility;
14. reciprocal disclosure, demonstration and strategic non-disclosure;
15. patent/priority, secrecy and selective disclosure as alternative boundary strategies;
16. letters, drawings and photographs as portable authority/evidence;
17. iterative cross-site testing and return circulation.

The later Wedding/Martens problem may add, if sources support it:

18. deliberately prepared polished specimen;
19. microscopic field;
20. microphotographic glass plate;
21. labelled/numbered specimen-image reference series or collection.

This is an analytical comparison, **not yet a direct genealogy**.

## Wedding extraction schema — ready to apply

When Wedding OCR/pages become available, build page-level indices for Mss 23–25 using the same fields.

Core metadata:

- date / itinerary;
- person + functional role: `introducer | gatekeeper | host | technical guide | worker | tester | judge | sample donor | correspondent | image-maker | institutional credential | technical evaluator | privilege grantor`;
- works / institution;
- source of datum: direct observation / oral report / copied document or drawing / inference.

Observation/testing operations:

`SEE | COUNT | MEASURE | WEIGH | CALCULATE | APPARATUS_TEST | EXPERT_JUDGEMENT | SENSORY_JUDGEMENT | IMAGE | RELIABILITY_WARNING`.

Access modes:

`RECOMMENDATION | PRIOR_RELATION | SPONTANEOUS_ACCESS | PRIVILEGED_ACCESS | TECHNICAL_CREDIBILITY | CREDIBILITY_PERFORMANCE | ACCESS_DENIAL_OR_LIMIT | WEAK_GUIDE`.

Knowledge-boundary modes:

`PUBLICATION | PRACTICAL_COMPETENCE | PATENT_PRIORITY | SECRET | SELECTIVE_DISCLOSURE | RECIPROCAL_EXCHANGE | DEMONSTRATION | DOCUMENT_COPY | WITHHOLDING`.

Sample/reference modes:

`DEMONSTRATION_SAMPLE | TRACE_SAMPLE | BATCH_IDENTITY | STAGED_SERIES | REFERENCE_QUALITY_SAMPLE | PREPARED_TEST_OBJECT | SAMPLE_DONOR | SAMPLE_RECIPIENT | PROVENANCE_LOSS | CATALOG_NUMBERING`.

Circuit fields:

- object/result sent onward?;
- tested or transformed elsewhere?;
- written judgement returned?;
- repeat supply/correspondence?;
- later reused as authority or reference?;
- relation continued after traveller left site?;
- later British ↔ Berlin return circulation?

For every major works/person episode ask: what did Wedding already know before arrival; what produced access; what level of visibility was granted; what he measured/copied/received; what he disclosed in return; what was withheld; what continued moving after he left; and what later appears in Berlin.

## Next analytical move after Wedding British itinerary control

Compare the Wedding material against:

1. Sorby's Sheffield diaries / surviving metallurgical specimen context;
2. Wedding's post-1862 Berlin teaching and metallurgical work;
3. Martens and the Königliche mechanisch-technische Versuchsanstalt / later Materialprüfungsamt;
4. the 1885 Wedding–Sorby microscopic-structure dispute, especially specimen preparation and illumination;
5. the Iron Library's three original Droste/Martens microphotographic glass plates and their unresolved object-level identifiers.

A direct Wedding–Sorby meeting in 1860/62 remains a **hypothesis**, not a claim. Test co-presence by dates/names.

## Residency logic

Digitised Wedding/Fischer material is preliminary research, not itself a reason to travel.

A Scholar in Residence case should target the second stage:

- what happened after the British industrial journeys;
- how comparison/testing was reorganised in German institutions;
- how identity/provenance/reference were preserved or reconstructed;
- how privileged/practical knowledge became inspectable, labelled and durable institutional evidence;
- how prepared specimens, microscopic fields, photographic glass plates and printed plates/reference collections worked materially;
- which still-undigitised or object-dependent Iron Library / Georg Fischer series are necessary.

## High-value unresolved onsite layer

Priority remains:

- three original Droste/Martens early microphotographic glass plates;
- exact meaning of `G 745,1`, `Per765`, `A346`;
- physical metadata, inscriptions, backs, mounts, ordering and printed-plate matches;
- nineteenth-century GF working papers/correspondence that remain undigitised after item-level ANTON verification;
- material-testing / metallography / exhibition / photographic series whose physical ordering or object features are not captured digitally.

## Resume rule

When returning to this project, read this file first, then:

1. `FISCHER_1845_1846_EVENT_INDEX.tsv`;
2. `FISCHER_SAMPLE_AND_REFERENCE_REGIMES_1845_1846.md`;
3. `FISCHER_ITERATIVE_TESTING_CIRCUIT_1845_1846.md`;
4. `FISCHER_KNOWLEDGE_BOUNDARY_MATRIX_1845_1846.tsv`;
5. `FISCHER_TESTING_REGIME_1845_1846.md`;
6. `FISCHER_MEASUREMENT_AND_OBSERVATION_1845_1846.md`;
7. `FISCHER_KNOWLEDGE_EXCHANGE_AND_SECRECY_1845_1846.md`;
8. `FISCHER_ACCESS_NETWORK_1845_1846.md`;
9. `FISCHER_1845_1846_NODE_INDEX.md`;
10. `RESIDENCY_TRIAGE_2026-09-11.md`;
11. `PUBLIC_DIGITAL_CORPUS.md` and `SOURCE_MAP.md`.

Do not reopen generic Iron Library searching before the Wedding British itinerary/person/comparison index has been completed. Do not assume Wedding OCR exists until the actual JSON/files appear in the repository.
