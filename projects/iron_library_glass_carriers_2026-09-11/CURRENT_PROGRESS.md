# CURRENT PROGRESS — Iron Library / Wedding / Sheffield–Berlin

**Pinned continuation state — 2026-09-11.**

This is the authoritative first resume point for the active Iron Library project. Do not let unrelated repository activity supersede it.

## 1. Current research position

The project has moved beyond generic Iron Library discovery and beyond a simple `Sorby → Wedding → Martens` diffusion story.

The controlled comparative problem is now:

**industrial travel / works comparison → travelling sample → external test / expert judgement → numbering / provenance / collection → prepared specimen → microscopic field → microphotography → printed / institutional reference system.**

The central question is not who invented metallography. It is how **material comparison changed scale, evidential carrier, access regime, preparation practice, institutional setting and reference structure** while remaining a comparative activity.

Two linked questions currently govern the work:

> How did the comparison of iron and steel move from industrial works visited by travelling metallurgists to prepared surfaces, microscopic fields and photographic reference collections?

> What happened when knowledge that depended on recommendation, privileged factory access, practical competence, selective disclosure, travelling samples and cross-site testing was reorganised into institutional specimen/testing/image systems?

The main geographic/institutional comparison remains **Sheffield ↔ Berlin/Charlottenburg**, with Schaffhausen/Fischer supplying a pre-Wedding comparison baseline.

## 2. Wedding corpus status

Hermann Wedding's Iron Library manuscripts are fully digitised on e-codices:

- `Mss 23` — 1856–1857; Freiberg/training notes;
- `Mss 24` — 1858; German industrial study tour;
- `Mss 25` — 1860–1862; Germany–Belgium–England, including British industrial/Bessemer material.

The user reports that local 900 px IIIF acquisition of **Mss 23, Mss 24 and Mss 25 is complete**. `Mss 25` exposes **402 IIIF canvases**.

Local working directories:

- `C:\Users\13563\Desktop\wedding_mss23`
- `C:\Users\13563\Desktop\wedding_mss24`
- `C:\Users\13563\Desktop\wedding_mss25`

A local-computer/Codex workflow has been specified to:

1. merge each image sequence into a reading PDF;
2. OCR the original JPG pages locally, not a PDF re-render;
3. use Tesseract first for simple pages;
4. use PaddleOCR as fallback for complex / low-confidence pages;
5. emit one provenance-rich JSON per manuscript.

**The three Wedding OCR JSON files are not yet visible in this repository. Do not assume that OCR/upload is complete until the files actually appear.**

When the JSONs arrive, the first analytical operation is a page-level itinerary/person/comparison index, not more generic web searching.

## 3. Fischer 1845–1846 corpus: controlled baseline

Three Fischer machine-readable text files were supplied in chat. Two are duplicate/OCR witnesses of the 1845 journey; the cleaner `...Low-Moor, Sheffield, und zurück im Sommer 1845.txt` is the canonical working text. The third is the 1846 journey through London, Derby/Butterley, Sheffield and Liverpool.

Existing detailed project files:

1. `FISCHER_1845_1846_EVENT_INDEX.tsv`
2. `FISCHER_KNOWLEDGE_BOUNDARY_MATRIX_1845_1846.tsv`
3. `FISCHER_SAMPLE_AND_REFERENCE_REGIMES_1845_1846.md`
4. `FISCHER_ITERATIVE_TESTING_CIRCUIT_1845_1846.md`
5. `FISCHER_TESTING_REGIME_1845_1846.md`
6. `FISCHER_MEASUREMENT_AND_OBSERVATION_1845_1846.md`
7. `FISCHER_KNOWLEDGE_EXCHANGE_AND_SECRECY_1845_1846.md`
8. `FISCHER_ACCESS_NETWORK_1845_1846.md`
9. `FISCHER_1845_1846_NODE_INDEX.md`

These OCR texts are research aids, not diplomatic transcriptions.

### Controlled Fischer findings

- `Vergleichungspunkte` and `Autopsie` make comparison/direct presence actor categories, but Fischer's practice is broader than sight alone: **see → count → measure → ask → weigh → calculate → compare → sample → record**.
- Low Moor takes a **sample from each tapping and numbers the output**, linking production event, material identity and specified quality.
- The same Low Moor visit yields a staged travelling series of ore, limestone, coal, coke and iron through successive production stages.
- Royal Mint testing turns Fischer's steel `Musterstange` into a practical normative reference for future supply of the same quality. Do not call this a modern certified reference material.
- Provenance can be preserved (sample + batch number) or destroyed (heterogeneous remelting of old material of unknown quality).
- Industrial testing already combines dedicated apparatus with embodied sensory expertise.
- Recommendation, prior relation, performed technical competence and named guides condition what becomes visible. Butterley provides a negative control: formal access with a technically weak guide produces data Fischer himself marks as unreliable.
- Patent priority, secrecy, selective disclosure, reciprocal questioning, demonstration and publication are distinct boundary regimes; do not collapse them into generic `tacit knowledge`.
- 1845–46 is one iterative circuit: **journey → sample/order → shipment → external test → written judgement → repeat supply → return journey → reuse of test authority**.
- Beck's works drawing becomes a photographic negative and attempted positive copies: **industrial operation → drawing → photographic negative → reproducible positive image**.
- Numbering has different functions: Low Moor batch identity, Polytechnic catalogue addressability and later metallographic specimen/image numbering must not be collapsed into one regime.

## 4. Fischer negative-control result: no positive microscopy in 1845–46

The supplied Fischer OCR corpus has now been searched directly for `Mikro-`, `Mikroskop-`, `micros-` and related forms: **no positive hit**.

Broader searches for magnification, lenses, polarisation, mineral/crystal sections and similar microscopic-preparation language also produced no positive microscopic episode.

Relevant near-neighbours exist but must remain distinct:

- 1845 Sheffield needle manufacture includes grinding and polishing — industrial finishing, not microscopic specimen preparation;
- 1846 Rodgers & Son grind/polish Fischer's steel razor blanks for expert quality judgement — prepared test object, not metallography;
- 1846 Willat/Croucher material includes photographic paper, Camera Obscura, daguerreotype, negative/positive reproduction and optical display — photography/optics, not microscopy;
- dissolving views / magic-lantern illumination are optical display, not microscopic observation.

Controlled statement:

> **No positive textual evidence currently supports making Fischer 1845–1846 a microscopy story.**

This is analytically useful because it establishes a pre-metallographic baseline rather than an artificially continuous genealogy.

## 5. External source expansion generated from the Fischer texts

A dedicated acquisition note now exists:

`EXTERNAL_SOURCE_EXPANSION_2026-09-11.md`

The highest-value outward nodes are:

### Faraday / Royal Institution

Fischer records visiting Michael Faraday at the Royal Institution on 4 August 1845. Faraday inspects cast-wrought-iron objects, horseshoes, percussion-lock parts and platinum; Fischer leaves an experimental crucible for Faraday's use.

This should be pursued through:

- Faraday & Stodart, `On the Alloys of Steel` (1822);
- Fischer's earlier journals, especially 1825–27;
- the earlier recommendation/correspondence network, including the 1825 de la Rive → Faraday recommendation letter if a digital surrogate can be obtained.

### Low Moor

Treat as a traceability / staged-series node, not generic factory context.

### Royal Polytechnic Institution

Fischer's 1846 account describes >2,000 catalogue-numbered objects, staff explanation, lectures, experiments and working models.

Analytical distinction:

- Low Moor number = batch / production identity;
- Polytechnic number = collection addressability.

The 1843 Polytechnic catalogue is a priority downloadable control source.

### Croucher / Willats

Fischer's photographic vocabulary and named commercial network can be checked against J. H. Croucher's 1845 `Plain Directions for Obtaining Photographic Pictures...`, published by T. & R. Willats, 98 Cheapside.

This is a direct travel-text ↔ contemporary technical-manual bridge.

### Fischer 1851

Fischer's 1851 Great Exhibition journey is the next travel-journal priority.

Question:

> Does the earlier travelling-sample / personal-judgement regime become reorganised through exhibition classification, catalogue addressability and public display?

## 6. Sorby and Story-Maskelyne: parallel regimes, not yet a transmission chain

Current functional comparison:

### Sorby / Sheffield

Working regime:

**industrial material → skilled preparation → polished/etched surface → reflected/direct illumination → microscopic field → photomicrograph / printed image**.

The key issue is not simply microscope use. Sorby's later criticism of Wedding makes specimen preparation and illumination conditions of valid microstructure.

Priority controls:

- Sorby's 1863/64 meteorite microscopy;
- surviving metallurgical specimen / photomicrograph catalogue-history;
- JRMS 1886 discussion of Wedding.

### Story-Maskelyne / British Museum mineralogy

Working regime to test:

**museum specimen / meteorite aggregate → cut/thin prepared section → glass carrier → transmitted/polarised-light comparison → collection/classification**.

A strong later preparation control is Royal Society `RR/12/397` (1894), Maskelyne's referee report on Tutton's instrument for cutting, grinding and polishing section-plates/prisms.

Do not claim a direct Sorby ↔ Maskelyne transmission without evidence. Their present value is as parallel material-to-microscopic-object regimes.

## 7. Wedding notebooks may be historiographically under-exploited — hypothesis only

A dedicated control note now exists:

`WEDDING_NOTEBOOK_CITATION_AUDIT.md`

Current suspicion:

> Wedding as a person and the broad events of his British travel are well known, but `Mss 23–25` may not have been systematically exploited page-by-page as a primary-source corpus.

This is **not yet a novelty claim**.

Preliminary searching has not yet revealed substantial page-level scholarly use, but absence from indexed web search does not prove absence. A formal citation audit is required.

Use the distinction:

`open access ≠ searchable corpus ≠ systematically exploited source`.

Potential longitudinal value of the three manuscripts:

- `Mss 23`: training — what counts as recordable metallurgical knowledge;
- `Mss 24`: domestic industrial tour — cross-site works comparison;
- `Mss 25`: transnational comparison — foreign access regimes, specialist networks, Bessemer/British sites.

Potential larger question:

> **How did a metallurgist learn to compare?**

Only after page-level extraction should this be compared with Wedding's later microscopic comparison regime.

## 8. Wedding extraction schema

When OCR/pages become available, extract the same analytical units used for Fischer.

Core fields:

- date / itinerary;
- person + functional role;
- works / institution;
- source of datum: direct observation / oral report / copied document/drawing / inference.

Observation/testing operations:

`SEE | COUNT | MEASURE | WEIGH | CALCULATE | APPARATUS_TEST | EXPERT_JUDGEMENT | SENSORY_JUDGEMENT | IMAGE | RELIABILITY_WARNING`

Access modes:

`RECOMMENDATION | PRIOR_RELATION | SPONTANEOUS_ACCESS | PRIVILEGED_ACCESS | TECHNICAL_CREDIBILITY | CREDIBILITY_PERFORMANCE | ACCESS_DENIAL_OR_LIMIT | WEAK_GUIDE`

Knowledge-boundary modes:

`PUBLICATION | PRACTICAL_COMPETENCE | PATENT_PRIORITY | SECRET | SELECTIVE_DISCLOSURE | RECIPROCAL_EXCHANGE | DEMONSTRATION | DOCUMENT_COPY | WITHHOLDING`

Sample/reference modes:

`DEMONSTRATION_SAMPLE | TRACE_SAMPLE | BATCH_IDENTITY | STAGED_SERIES | REFERENCE_QUALITY_SAMPLE | PREPARED_TEST_OBJECT | SAMPLE_DONOR | SAMPLE_RECIPIENT | PROVENANCE_LOSS | CATALOG_NUMBERING`

For every major episode ask:

- what did Wedding know before arrival?
- what produced access?
- who mediated the visit?
- what did he see / count / measure / copy / draw / receive?
- what did he regard as reliable or unreliable?
- what did he disclose in return?
- what continued moving after he left?
- what later appears in Berlin?

## 9. Immediate research order

### First dependency

Finish/confirm the local Wedding OCR pipeline and bring the three JSONs into the project.

### Then

1. build Mss 23–25 page-level itinerary/person/comparison indices;
2. establish exact Mss 25 British dates, Sheffield/South Wales/Bessemer works and named contacts;
3. test direct Wedding–Sorby co-presence/contact only after dates/names are controlled;
4. run the formal Wedding notebook citation audit;
5. acquire the external source queue in `EXTERNAL_SOURCE_EXPANSION_2026-09-11.md`;
6. compare Wedding's early observational regime against later 1885 microscopy / Sorby criticism;
7. follow into Martens / Königliche mechanisch-technische Versuchsanstalt / Materialprüfungsamt specimen-image-reference systems.

Do **not** reopen generic Iron Library searching before these controlled steps are done.

## 10. Download / comparison queue

Priority order now:

1. Fischer 1851;
2. Faraday & Stodart 1822;
3. Croucher 1845;
4. Royal Polytechnic catalogue 1843;
5. Great Exhibition catalogue material relevant to mining/metallurgy;
6. Sorby 1863/64 + surviving-specimen catalogue/history;
7. Wedding 1885 + JRMS 1886;
8. Maskelyne/Tutton `RR/12/397`;
9. Martens 1891 / 1893;
10. Martens & Guth / Materialprüfungsamt 1904.

The aim is to control transitions, not accumulate PDFs:

**sample identity → collection identity → expert test → prepared object → microscopic field → reproducible image → institutional reference system**.

## 11. Residency / onsite logic

Digitised Wedding/Fischer material is pre-visit research, not itself a residency rationale.

The strongest unresolved onsite layer remains:

- three original Droste/Martens early microphotographic glass plates;
- exact meaning of `G 745,1`, `Per765`, `A346`;
- physical metadata, inscriptions, backs, mounts, ordering and printed-plate matches;
- genuinely undigitised nineteenth-century GF working papers/correspondence after item-level ANTON verification;
- material-testing / metallography / exhibition / photographic series whose physical order or object features cannot be reconstructed remotely.

The residency case should ask how comparison/testing became durable institutional evidence, not simply rediscover the known history of metallography.

## 12. Claim ceilings

Do not currently claim:

- that Fischer 1845–46 practised microscopy;
- that Sorby and Maskelyne formed a direct transmission chain;
- that Wedding met Sorby in 1860/62;
- that Mss 23–25 have never been read;
- that shared glass substrate proves historical continuity;
- that Low Moor batch samples are modern reference materials;
- that analytical similarity establishes genealogy.

Current evidence supports **comparative architecture and source-directed hypotheses**, not a single continuous lineage.

## Resume order

Read in this order when returning:

1. `CURRENT_PROGRESS.md` — this file;
2. `WEDDING_NOTEBOOK_CITATION_AUDIT.md`;
3. `EXTERNAL_SOURCE_EXPANSION_2026-09-11.md`;
4. `FISCHER_1845_1846_EVENT_INDEX.tsv`;
5. `FISCHER_SAMPLE_AND_REFERENCE_REGIMES_1845_1846.md`;
6. `FISCHER_ITERATIVE_TESTING_CIRCUIT_1845_1846.md`;
7. `FISCHER_KNOWLEDGE_BOUNDARY_MATRIX_1845_1846.tsv`;
8. `FISCHER_TESTING_REGIME_1845_1846.md`;
9. `FISCHER_MEASUREMENT_AND_OBSERVATION_1845_1846.md`;
10. `FISCHER_KNOWLEDGE_EXCHANGE_AND_SECRECY_1845_1846.md`;
11. `FISCHER_ACCESS_NETWORK_1845_1846.md`;
12. `FISCHER_1845_1846_NODE_INDEX.md`;
13. `RESIDENCY_TRIAGE_2026-09-11.md`;
14. `PUBLIC_DIGITAL_CORPUS.md` and `SOURCE_MAP.md`.

**Immediate resume condition:** if Wedding OCR JSONs are present, stop broad searching and index them first. If they are absent, continue the controlled downloadable-source queue / citation audit without assuming OCR completion.
