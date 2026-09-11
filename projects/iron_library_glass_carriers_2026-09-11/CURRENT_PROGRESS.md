# CURRENT PROGRESS — Iron Library / Wedding / Sheffield–Berlin

**Pinned continuation state — updated 2026-09-11 after Wedding OCR upload and first-pass indexing.**

This is the authoritative resume point for the active Iron Library project. Do not let unrelated repository activity supersede it.

## 1. Current research position

The project is no longer a generic Iron Library search and no longer a simple `Sorby → Wedding → Martens` diffusion story.

Controlled comparative sequence:

**industrial travel / works comparison → travelling sample → external test / expert judgement → numbering / provenance / collection → prepared specimen → microscopic field → microphotography → printed / institutional reference system.**

The central question is how material comparison changed scale, evidential carrier, access regime, preparation practice, institutional setting and reference structure while remaining a comparative activity.

Geographic/institutional axis: **Sheffield ↔ Berlin/Charlottenburg**, with Schaffhausen/Fischer supplying the pre-Wedding comparison baseline.

## 2. Wedding OCR dependency is now satisfied

Hermann Wedding's Iron Library manuscripts are fully digitised on e-codices and local 900 px acquisition is complete:

- `Mss 23` — 1856–1857; Freiberg/training notes;
- `Mss 24` — 1858; German industrial study tour;
- `Mss 25` — 1860–1862; Germany–Belgium–England/Britain.

The three PaddleOCR JSON files are now present in the repository root:

- `wedding_mss23.pdf_by_PaddleOCR-VL-1.6.json`
- `wedding_mss24.pdf_by_PaddleOCR-VL-1.6.json`
- `wedding_mss25.pdf_by_PaddleOCR-VL-1.6.json`

The current OCR is accepted as the speed/quality balance point for discovery and routing. It is **not** a diplomatic transcription. Important names/dates/technical terms will be corrected selectively against the manuscript images/PDFs when they become analytically consequential.

Detailed first-pass note:

`WEDDING_OCR_FIRST_PASS_2026-09-11.md`

### First OCR findings now pinned

#### Mss 23

- OCR entry 5: `über die Freiberger Hütten` / `Notizen`, with `Freiberg 1856-1857` and H. Wedding.
- OCR entry 7: `Die Mulder Hütten` (exact spelling to verify visually).
- Process headings become recoverable even when prose fails: `Die Bleiarbeit`, `Das Rösten der Bleierze`, `Das Verschmelzen der gerösteten Bleierze ...`, and `Die Concentration oder das Spuren des Kupfersteines`.
- OCR entry 57 looks like a later copied/inserted layer referring to H. Th. Richter and C. Schiffner 1935; do not merge it automatically into Wedding's 1856–57 hand.

Working use: process/training baseline — what Wedding learned to record, measure, draw and distinguish.

#### Mss 24

A skeleton itinerary is already visible:

- broad route/title through Thüringen/Bayern/Rhein/Westfalen, `Michaeli 1858`;
- Saarbrücken;
- Krupp;
- Essen / Bochum;
- Dortmund;
- Hörde;
- Berlin.

Working use: domestic cross-site comparison before the transnational Mss 25 regime.

#### Mss 25

The front matter is immediately valuable. OCR entries 15–18 are recognisably contact/address/firm/hotel lists, with London, Manchester, Liverpool, Bradford, Birmingham, Swansea, Merthyr, Leeds, Cockerill, Aachen, Bruxelles and other nodes. Treat this as an **access-network apparatus**, not incidental notes.

A provisional British chronology is already recoverable:

- entry 294: `19 Juli: Manchesterer`; next line `William Fairbaix ...` — Manchester/date usable now; personal-name normalisation waits for image control;
- entry 295: `22 July` with probable Sheffield/works heading;
- entry 300: `26 Juli`;
- entry 301: `Friday 27th Juli Low Moor`, plus `Mr. Fenton`; 27 July 1860 was indeed Friday;
- entry 304: `28 juli`;
- entry 308: Newcastle upon Tyne; OCR reads `Thursday 31 July`, but 31 July 1860 was Tuesday, so date/weekday is flagged for image checking rather than silently corrected;
- entry 310: `Monday 6 Aug. 60 Govan Works ... Glasgow`; 6 August 1860 was Monday;
- entry 272: explicit Sheffield, date wording noisy;
- entry 316: Low Moor + Cumberland + Wolverhampton + Sheffield in a dense comparison/reference block; do not force into a single dated visit;
- entry 323: `Steffeld Brown ...`, probable Sheffield/Brown reference pending image control;
- later entries move clearly into Cornwall/Wales/mining material.

This is enough to stop thinking of Mss 25 as unreadable OCR. The British spine and network layer are already indexable.

### OCR confidence rule

Use three levels:

- **A** — stable anchor: date/place/name/heading clear enough to index;
- **B** — useful probable reading; exact spelling/wording needs page-image control;
- **C** — repetition, modern-date hallucination, generic filler or multilingual garbage; do not promote into argument.

Calendar consistency is an OCR diagnostic, not a licence to rewrite the manuscript. Store OCR reading and calendar flag separately.

## 3. Fischer 1845–1846 baseline remains controlled

Existing detailed files include the event index, knowledge-boundary matrix, sample/reference-regime analysis, iterative testing circuit, testing regime, measurement/observation note, secrecy/exchange note, access network and node index.

Controlled findings remain:

- `Vergleichungspunkte` / `Autopsie` matter, but practice is broader: **see → count → measure → ask → weigh → calculate → compare → sample → record**;
- Low Moor batch sampling/numbering links production event, material identity and quality;
- staged travelling samples preserve process sequence;
- Royal Mint testing turns Fischer's `Musterstange` into a practical reference-quality object without making it a modern certified reference material;
- provenance may be preserved or destroyed;
- access depends on recommendation, prior relation, technical credibility, named guides and selective disclosure;
- Butterley remains the negative control for weak guided access;
- patent priority, secrecy, publication, demonstration and reciprocal questioning are separate regimes;
- the 1845–46 circuit is **journey → sample/order → shipment → external test → written judgement → repeat supply → return journey → reuse of test authority**;
- no positive textual evidence currently supports making Fischer 1845–46 a microscopy story.

## 4. Parallel microscopic regimes remain controlled

### Sorby / Sheffield

Working regime:

**industrial material → skilled preparation → polished/etched surface → reflected/direct illumination → microscopic field → photomicrograph / printed image**.

### Story-Maskelyne / British Museum mineralogy

Working regime to test:

**museum specimen / meteorite → prepared thin section → glass carrier → transmitted/polarised-light comparison → collection/classification**.

Treat Sorby and Maskelyne as parallel material-to-microscopic-object regimes until direct transmission evidence exists.

### Berlin / Martens

Endpoint remains the Königliche mechanisch-technische Versuchsanstalt / Materialprüfungsamt: specimen preparation, reflected-light microscopy, microphotography and separate specimen/image reference collections. The three original Droste/Martens glass plates remain the strongest object-dependent onsite lead.

## 5. Wedding extraction schema

Core fields:

- OCR entry / manuscript page marker;
- date / itinerary;
- person + functional role;
- works / institution;
- source of datum: direct observation / oral report / copied document/drawing / inference;
- confidence A/B/C;
- image-check flag.

Observation/testing operations:

`SEE | COUNT | MEASURE | WEIGH | CALCULATE | APPARATUS_TEST | EXPERT_JUDGEMENT | SENSORY_JUDGEMENT | IMAGE | RELIABILITY_WARNING`

Access modes:

`RECOMMENDATION | PRIOR_RELATION | SPONTANEOUS_ACCESS | PRIVILEGED_ACCESS | TECHNICAL_CREDIBILITY | CREDIBILITY_PERFORMANCE | ACCESS_DENIAL_OR_LIMIT | WEAK_GUIDE`

Knowledge-boundary modes:

`PUBLICATION | PRACTICAL_COMPETENCE | PATENT_PRIORITY | SECRET | SELECTIVE_DISCLOSURE | RECIPROCAL_EXCHANGE | DEMONSTRATION | DOCUMENT_COPY | WITHHOLDING`

Sample/reference modes:

`DEMONSTRATION_SAMPLE | TRACE_SAMPLE | BATCH_IDENTITY | STAGED_SERIES | REFERENCE_QUALITY_SAMPLE | PREPARED_TEST_OBJECT | SAMPLE_DONOR | SAMPLE_RECIPIENT | PROVENANCE_LOSS | CATALOG_NUMBERING`

## 6. Immediate research order — changed after OCR upload

The OCR dependency is complete. **Do not resume broad searching.**

1. Build the provisional Mss 25 itinerary/contact table for OCR entries **15–19 and 292–320**.
2. Separate front-matter contact/address infrastructure from visited-site narrative.
3. Extend the British chronology outward into Cornwall/Wales until dates/places stabilise.
4. Build compact Mss 24 itinerary skeleton: Saarbrücken → Krupp/Essen/Bochum → Dortmund/Hörde → Berlin.
5. Build Mss 23 process-heading/apparatus index.
6. Within the controlled British range, search for Bessemer / Daelen / von Hoff / Sorby; fuzzy candidates require image control before promotion.
7. Only after dates/names are controlled, test direct Wedding–Sorby co-presence/contact.
8. Compare Mss 25 working notes with Wedding/von Dechen 1862 official exhibition catalogue as a transformation from private working record to public institutional representation.
9. Then continue into Wedding 1885 / Sorby criticism and Martens/Materialprüfungsamt specimen-image-reference systems.

## 7. External controls already queued

Keep, but subordinate to Wedding indexing:

- Fischer 1851 + Great Exhibition catalogue;
- Faraday & Stodart 1822 and earlier Fischer/Faraday relation;
- Croucher 1845;
- Royal Polytechnic catalogue 1843;
- Wedding/von Dechen 1862 exhibition catalogue;
- Sorby 1863–64 + surviving specimen catalogue/history;
- Maskelyne 1870 and Tutton/Maskelyne preparation corpus;
- Martens 1891 / 1893;
- Martens & Guth 1904.

The point is controlled transformation, not PDF accumulation:

**working record / batch / sample → travelling object → test/judgement → catalogue/public representation → prepared object → microscopic field → reproducible image → institutional reference system**.

## 8. Claim ceilings

Do not currently claim:

- Fischer 1845–46 practised microscopy;
- Sorby and Maskelyne formed a direct transmission chain;
- Wedding met Sorby in 1860/62;
- a noisy OCR reading such as `William Fairbaix` is already a securely normalised historical identity;
- the Mss 25 Sheffield rows already prove a Bessemer meeting;
- `Mr. Fenton` has been identified;
- every place in OCR entry 316 belongs to one visit/date;
- OCR-entry number equals handwritten manuscript pagination;
- calendar checking authorises silent correction of manuscript wording;
- Mss 23–25 have never been read;
- shared glass substrate proves historical continuity;
- analytical similarity establishes genealogy.

## Resume order

1. `CURRENT_PROGRESS.md` — this file.
2. `WEDDING_OCR_FIRST_PASS_2026-09-11.md` — **active next-step note**.
3. the three Wedding OCR JSONs in repository root.
4. `WEDDING_NOTEBOOK_CITATION_AUDIT.md`.
5. `EXTERNAL_SOURCE_EXPANSION_2026-09-11.md` and `EXTERNAL_SOURCE_EXPANSION_PASS2_2026-09-11.md`.
6. Fischer baseline files as needed for controlled comparison.
7. `RESIDENCY_TRIAGE_2026-09-11.md`, `PUBLIC_DIGITAL_CORPUS.md`, `SOURCE_MAP.md` for onsite/acquisition logic.

**Immediate resume condition:** continue the Mss 25 provisional itinerary/contact index. OCR rerunning and generic Iron Library searching are lower priority than extracting the currently recognisable corpus.