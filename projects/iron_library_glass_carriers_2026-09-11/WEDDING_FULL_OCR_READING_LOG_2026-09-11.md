# Wedding full OCR reading log — 2026-09-11

Status: ACTIVE. This file is the rolling checkpoint for a full-pass read of the current PaddleOCR-VL JSON outputs for Eisenbibliothek Mss 23–25. It is deliberately an indexing/triage layer, not a diplomatic transcription.

## Pass 0 — corpus loaded

Current JSON lengths:

- Mss 23: 223 OCR entries; 135 entries contain non-empty OCR text.
- Mss 24: 116 OCR entries; 94 entries contain non-empty OCR text.
- Mss 25: 401 OCR entries; 380 entries contain non-empty OCR text.

Total: 740 OCR entries; 609 with non-empty OCR text.

The reading strategy is now fixed:

1. scan every OCR entry once;
2. preserve literal OCR anchors rather than silently correcting them;
3. separate recognisable historical content from obvious model filler/repetition/modern-date hallucination;
4. extract dates, places, people/firms, works/institutions, process/testing actions, sample/reference/image/numbering clues, and access/knowledge-boundary clues;
5. mark page-image/PDF checks only where an anchor matters analytically;
6. build the Wedding comparison architecture before attempting prose correction.

Noise flags used during the scan include repeated `The quick brown fox...`, intrusive modern years, extreme lexical repetition and non-Latin filler. A noisy page can still preserve a valid historical anchor, so noise is recorded separately rather than deleting the row.

## First full-scan checkpoint

Automated literal-anchor scan across all 740 entries is complete. It is being used only to route manual reading, not as evidence by itself.

Immediate high-yield zone remains Mss 25, especially the front-matter contact/address pages and the British sequence around OCR entries 294–370. Current stable or near-stable anchors include Manchester, Sheffield, Low Moor, Newcastle upon Tyne, Glasgow/Govan, Cornwall, Wales and multiple industrial-work references. Calendar consistency will be used as a diagnostic flag, never as silent emendation.

Next checkpoint will add the first curated chronological/site table after the full Mss 25 high-yield pass.

## Checkpoint 2 — full recognisable-content pass across Mss 23–25

The whole 740-entry corpus has now been routed once at recognisable-content level. This does **not** mean every handwritten sentence has been read correctly. It means every OCR entry has been exposed to a first-pass classification and the recoverable anchors have been separated from obvious filler.

Three machine-readable working indices now exist:

- `WEDDING_MSS25_ITINERARY_AND_DOCUMENT_MODE_INDEX.tsv`
- `WEDDING_MSS24_ITINERARY_SKELETON.tsv`
- `WEDDING_MSS23_PROCESS_HEADING_INDEX.tsv`

### Mss 25: document modes must be separated before chronology

The decisive result of the full pass is that Mss 25 cannot safely be treated as one continuous diary stream. At least four documentary modes are interleaved:

1. **ACCESS_INFRASTRUCTURE** — front-matter contacts, addresses, firms, hotels and intended route nodes;
2. **DATED_VISIT / SITE_TECHNICAL_NOTES** — visits to works/mines and measurements/process descriptions;
3. **COMPARATIVE_REFERENCE_BLOCKS** — multiple sites, ores, prices or process figures assembled together and not necessarily recording one visit;
4. **COPIED_PRINT_REFERENCE / GEOLOGICAL_REFERENCE_NOTES** — geological survey, de la Beche, map/catalogue, historical and institutional material copied or excerpted from printed/reference sources.

This distinction is now mandatory. A place name in a comparative table or copied geological note is not automatically an itinerary event.

The front matter, especially OCR entries 14–17, is itself a major source: London, Manchester, Bradford, Liverpool, Swansea, Wolverhampton, Brussels, Liège/Aachen, Cockerill, Couillet and many hotel nodes occur before the dated British narrative. It preserves an access apparatus that can later be compared to Fischer's recommendation/credibility network.

### Mss 25: provisional 1860 British spine

The OCR supports a substantially longer British chronology than the earlier Manchester–Scotland slice suggested. A provisional high-yield spine now starts in late April / early May and runs through South-West England, South Wales, northern England and Scotland before moving into Cornwall/reference geology.

Calendar checking is diagnostic only; the OCR reading is retained separately.

Strong or useful anchors:

- `Monday 30 Apr.` — calendar-consistent for 1860; place still uncertain.
- probable `Friday 4 May` — Plymouth / Devonport; calendar-consistent.
- `Friday 11 May` + `Mr. Garley` — calendar-consistent; place OCR poor.
- `Monday 14 May` — calendar-consistent; South-West/Redruth context probable.
- `Thursday 15 May` — calendar conflict (15 May 1860 was Tuesday); image check.
- `Friday 13 May` + Hayle — calendar conflict (13 May 1860 was Sunday); Hayle itself is strong.
- `23 May` + `South-Wales` — useful route anchor.
- `24 Mai 1860` + a works heading whose names remain noisy.
- `Friday 25 Mai 1860` + **Ebbw Vale** — calendar-consistent and one of the strongest South-Wales anchors.
- `Monday 28 Mai` — calendar-consistent and attached to ore/coal comparison material.
- probable `29 May` + Ebbw Vale.
- `2 June` + probable Abercarn.
- `Monday 3.4 June` — likely around 4 June because 4 June 1860 was Monday, but do not emend without image.
- `Thursday 5 June` — calendar conflict.
- `8 Juni. Friday` — calendar-consistent.
- a long **Abercarn/Newport** technical sequence follows, with repeated headings/markers.
- `23 Juni` + **Merthyr** + `Mr. Pierce`.
- probable `5 Juli 1860`, place OCR poor.
- `12 Juli 1860` + `Griffith & Billings` (firm/name image-check).
- possible `Friday 13 July`; OCR garbled but calendar would fit.
- `14 Juli` header.
- `19 Juli: Manchesterer` + OCR `William Fairbaix`; do not normalise to Fairbairn until image control.
- `22 July` + probable Sheffield/Turton works context.
- `26 Juli` + OCR `Peter Fairborn`; person needs image control.
- `Friday 27th Juli Low Moor` + `Mr. Fenton` — excellent internal calendar anchor.
- `28 juli` + OCR `Moroling Works`; works identity unresolved.
- `Thursday 31 July` + **Newcastle upon Tyne** — calendar conflict because 31 July 1860 was Tuesday; mandatory visual check.
- `Monday 6 Aug. 60 Govan Works ... Glasgow` — excellent calendar anchor.
- probable Gartsherrie/Gartsherrie-like works heading follows; spelling unresolved.
- later comparative pages mention Low Moor, Cumberland, Wolverhampton, Sheffield, Ulverstone, Govan/Blackburn and other sites without constituting one itinerary event.
- Cornwall follows, with Tavistock, mining technique, Stannary institutions, mine/vein notes and a large geological/reference layer.

### Mss 25: copied/reference layer is analytically important

The later Cornwall material is not merely travel description. Recognisable references include:

- `de la Beche`;
- a `Memoirs of the ... Survey of Great Britain. Vol. 1. 1846` reference with stratigraphic units including Upper/Lower Ludlow and Wenlock Limestone;
- Geological Survey publication/catalogue prose giving map scales, sheets and prices;
- `Geological Society of Cornwall`;
- lists of Cornwall localities/mineral occurrences;
- mining vocabulary such as hanging wall, underground roads/carts, gunpowder, dressing and roasting furnace.

This creates a new comparison problem: **direct works/mining observation versus copied documentary/geological knowledge inside the same notebook**. Later page-image work should tag datum source, not merely place/date.

### Mss 24: domestic comparison skeleton now controlled

Mss 24 is the cleanest middle layer between Freiberg training and the transnational notebook. Stable or near-stable anchors include:

`Thüringer-Wald? → Saarbrücken → Montigny → Krupp → Oberhausen / Concordia-Grube → Frederick-Wilhelms-Hütte? → Essen + Bochum → Niederrheinische Hütte? → Oberhausen → Elberfeld/Dortmund → Hörde → Berlin`.

Exact identities/spellings still need image control in several rows. The analytical value is already clear: the notebook repeatedly couples place/work headings with apparatus, furnace, quantities and process description, giving a domestic cross-site comparison baseline.

### Mss 23: process architecture is more useful than itinerary

Mss 23 is best indexed by operation/section, not by travel chronology. Strong headings/anchors include:

- `über die Freiberger Hütten / Notizen`, Freiberg 1856–1857;
- `Die Mulder Hütten` [spelling to control];
- `Die Bleiarbeit`;
- `Das Rösten der Bleierze`;
- `Das Verschmelzen der gerösteten Bleierze ... oder die Bleiarbeit`;
- lead-slag / silver material;
- `Das Rosten oder Liebrennen der steinigen Produkte` [exact spelling to control];
- lead/refining sections;
- `Die Concentration oder das Spuren des Kupfersteines`;
- `Das Raffinierdes Bleies` [OCR wording to control];
- multiple furnace-cycle/throughput passages;
- a numbered/weighed `Proben`-like experimental/sample series around OCR entry 197.

The later/copy layer around OCR entry 56 remains segregated because it explicitly presents itself as an `Abschrift` after H. Th. Richter and cites C. Schiffner 1935.

## Working interpretation after the complete OCR routing pass

The three manuscripts now form a stronger longitudinal sequence than a simple biographical travel narrative:

**Mss 23: process decomposition and quantitative recording → Mss 24: domestic cross-site comparison → Mss 25: transnational access network + works/mining comparison + copied/documentary reference accumulation.**

The question `How did a metallurgist learn to compare?` now has concrete documentary layers. Mss 25 additionally shows that comparison was assembled from heterogeneous sources: direct presence, named contacts, works data, cross-site tables and printed geological reference material.

This makes the later metallographic problem sharper. The move to numbered prepared sections, controlled illumination and microphotography should be compared not simply to travel, but to an earlier **composite comparison regime** that already organized people, sites, quantities, samples, documents and reference systems.

## Next PDF-control queue

Do not correct pages indiscriminately. Highest-value visual checks are now:

1. Mss 25 front-matter entries 14–17: exact names/firms/addresses that mediate access;
2. Mss 25 entries 156–221: South-West / South-Wales date-place sequence, especially Hayle, Ebbw Vale and Abercarn;
3. Mss 25 entries 258–324: Merthyr → Manchester → probable Sheffield → Low Moor → Newcastle → Govan/Glasgow and the transition into Cornwall;
4. the `William Fairbaix`, `Peter Fairborn`, `Mr. Fenton`, `Wilson & Belles`, `Richard Macagan`, `Gavsherrie` readings before person/works identification;
5. Mss 25 copied-reference pages 353, 369, 373 to identify exact printed sources;
6. Mss 24 Essen/Bochum, Hörde and Berlin transition;
7. Mss 23 section headings and the sample/experiment series around OCR entry 197.

Status after this checkpoint: **the OCR corpus has been read once as a complete routing/indexing corpus. The next phase is selective visual correction of analytically decisive rows, not another blanket OCR pass.**
