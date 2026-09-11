# Wedding OCR first pass — recognisable structure before diplomatic correction

Date: 2026-09-11

Status: ACTIVE WORKING INDEX. This note records only what the current PaddleOCR JSON makes recognisable enough to route later page-by-page checking against the manuscript images/PDFs. It is not a transcription and should not silently normalise names, dates or technical terms.

## Method / claim ceiling

The current OCR is being treated as the speed/quality balance point for discovery and indexing. Use it to locate dates, places, people, works, headings, measurements and comparison episodes. Later, correct important rows against the page image/PDF.

Confidence classes for this stage:

- A — stable anchor: place/date/name/heading is clear enough to index now.
- B — useful probable reading, but spelling or exact wording needs page-image control.
- C — model garbage/repetition/modern hallucination; do not promote into argument.

The JSON lengths currently parsed locally are Mss 23 = 223 OCR entries, Mss 24 = 116, Mss 25 = 401. These are OCR-entry indices and should not yet be equated mechanically with printed manuscript pagination.

## Mss 23 — Freiberg / training baseline

High-confidence recognisable anchors:

- OCR entry 5: `1) über die Freiberger Hütten. 2) Notizen.` with `Freiberg 1856-1857` and H. Wedding. [A]
- OCR entry 7: `Die Mulder Hütten.` [A, spelling to verify against image]
- OCR entry 72: heading/phrase `Die Bleiarbeit.` becomes readable inside otherwise noisy text. [B]
- OCR entry 76: `Das Rösten der Bleierze` is clearly recovered; `Silber` also appears in the same block. [A/B]
- OCR entry 80: `Das Verschmelzen der gerösteten Bleierze ... oder die Bleiarbeit.` is substantially recognisable. [A/B]
- OCR entry 161: `Die Concentration oder das Spuren des Kupfersteines.` is recognisable. [A/B]

Important provenance warning:

- OCR entry 57 is a later-looking inserted/copy layer, headed approximately `Freiberger Hütten Procepe. Abschrift nach einem Heft des H. Th. Richter` and referring to C. Schiffner 1935. Do not treat that entry automatically as Wedding's 1856–57 hand without codicological/image control.

Working implication: Mss 23 can already be indexed as a process/training notebook by operation headings even where prose OCR is poor. The immediate extraction target is the sequence of metallurgical operations, apparatus/drawings, measurements and categories of recordable knowledge.

## Mss 24 — 1858 German industrial comparison

High-confidence recognisable anchors:

- OCR entry 3: route/title line `Durch Thiringen, Bayern, ... Rhein, Westfalen` (middle place names are noisy) with `Michaeli 1858` and H. Wedding. [A for broad route/date; B for exact spelling]
- OCR entry 19: `Saarbrücken` is explicit. [A]
- OCR entry 47: `Krupp` is recovered inside a noisy works description. [B]
- OCR entry 71: both `Essen` and `Bochum` are explicit. [A]
- OCR entry 81: `Dortmund` is explicit. [A]
- OCR entry 83: `Hörder-...` / Hörde is explicit enough to route. [A/B]
- OCR entry 87: `Berlin` is explicit. [A]

Working implication: Mss 24 already supports a skeleton itinerary/worksite index even before prose correction. It is therefore the cleanest place to test how Wedding learned cross-site comparison domestically before Mss 25.

## Mss 25 — transnational/British itinerary: immediately usable layer

### Front matter / network lists

OCR entries 15–18 are unusually high value despite spelling noise. They appear to be lists of contacts, addresses, firms and hotels rather than continuous travel narrative.

Recognisable examples include repeated London addresses, Manchester, Liverpool, Bradford, Birmingham, Swansea, Merthyr, Leeds, Cockerill, Aachen, Bruxelles, etc. Entry 16 is strongly hotel/route oriented; entry 17 is strongly firm/contact oriented. These pages should be treated as a pre-existing access/network apparatus, not merely incidental notes. [A for document function; B for individual names]

This is analytically important because it gives us an access-network layer before reconstructing each visit: who could be contacted, where Wedding expected to lodge, and which firms/persons were in his working address book.

### British sequence now visible from OCR

The OCR is already good enough to establish a provisional chronological spine in July–August 1860. Exact wording and some dates remain for page-image checking.

- OCR entry 294: heading `19 Juli: Manchesterer`; next line begins `William Fairbaix ...`. `Manchester` + 19 July are [A]; the person reading is [B] and may be Fairbairn, but do not normalise until image control.
- OCR entry 295: OCR gives `22 July` and a probable Sheffield/works heading (`Stuffied ...`). Date [A/B], place/work name [B].
- OCR entry 300: explicit `26 Juli` in a works context. [A]
- OCR entry 301: `Friday 27th Juli Low Moor` and `Mr. Fenton` are explicit. 27 July 1860 was indeed a Friday, which gives strong internal control. [A for date/place; B for personal-name spelling]
- OCR entry 304: explicit `28 juli` and a works heading. [A/B]
- OCR entry 308: contains `Newcastle upon Tyne` and an OCR date line reading `Thursday 31 July`. The place is useful, but the weekday/date combination is impossible for 1860 (31 July was Tuesday), so this row is a mandatory image check rather than a corrected claim. [A place; C/B date wording]
- OCR entry 310: `Monday 6 Aug. 60 Govan Works ... Glasgow` is explicit, and 6 August 1860 was a Monday. [A]

Additional British anchors:

- OCR entry 272 contains an explicit `Sheffield`; the adjacent date wording is noisy and should not yet be trusted. [A place, B/C date]
- OCR entry 316 contains `Low Moor`, `Cumberland`, `Wolverhampton` and ends with `Sheffield`; it looks like a dense comparison/reference block rather than a clean single-visit diary entry. Do not force it into one itinerary date. [A places; B function]
- OCR entry 323 begins `Steffeld Brown ...`, plausibly a Sheffield/Brown works reference, but requires image checking. [B]
- later entries move into Cornwall/Wales/mining vocabulary; entries 347–348 are clearly in that zone, though proper nouns and dates are much noisier. [B]

### Date-control rule established from first pass

Calendar consistency is a useful OCR diagnostic but must not be used to silently rewrite the manuscript. Examples:

- `Friday 27th Juli` for 1860 is internally consistent.
- `Monday 6 Aug. 60` is internally consistent.
- `Thursday 31 July` is inconsistent with 1860 and therefore flags a page for visual correction.

Store the OCR reading and the calendar flag separately.

## What is already analytically visible

1. Mss 23, Mss 24 and Mss 25 have very different documentary functions: training/process notebook → domestic cross-site tour → transnational contact/works itinerary.
2. Mss 25 front matter preserves an address/contact/hotel infrastructure. Access can therefore be studied not only from successful visits but from the pre-arranged network Wedding carried with him.
3. The British section is not lost in OCR noise. A July–August 1860 spine is already recoverable, including Manchester, Low Moor, Newcastle and Govan/Glasgow, plus multiple Sheffield references.
4. Some pages contain extreme model repetition, generic English filler, modern dates or multilingual hallucination. These are useful as automatic C-class pages and should not consume interpretive time until the high-yield itinerary/contact pages are indexed.
5. The next operation should be indexing, not another OCR run. OCR correction should be selective and source-driven: fix names/dates/pages only when they matter to an analytical episode.

## Immediate next extraction order

1. Build a provisional Mss 25 table for entries 15–19 and 292–320: OCR entry, manuscript/page marker if visible, date, place, person, firm/work, operation, confidence, image-check flag.
2. Separate front-matter contact/address entries from visited-site narrative.
3. Extend the British chronology outward until the Cornwall/Wales section stabilises.
4. In parallel, make a compact Mss 24 itinerary skeleton from Saarbrücken → Krupp/Essen/Bochum → Dortmund/Hörde → Berlin.
5. Only after that, return to Mss 23 for process-heading and apparatus indexing.
6. Search for Bessemer/Daelen/von Hoff/Sorby only within the controlled British page range; fuzzy OCR candidates must be checked against the image before promotion.

## Current claim ceilings

Do not yet claim from OCR alone that:

- `William Fairbaix` is definitively William Fairbairn;
- the noisy Sheffield rows establish a Bessemer meeting;
- `Mr. Fenton` has been identified;
- every place in entry 316 belongs to one visit/date;
- the OCR-entry number equals the manuscript's handwritten page number;
- calendar checking authorises silent correction of a manuscript date/weekday.

This note is the first active resume point after OCR upload. Continue from the Mss 25 provisional itinerary/contact index, not from broad web searching.