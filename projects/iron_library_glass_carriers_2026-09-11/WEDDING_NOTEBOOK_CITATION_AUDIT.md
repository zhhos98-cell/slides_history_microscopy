# Wedding Mss 23–25 — historiographical / citation audit

Status: hypothesis-testing note, 2026-09-11.

## Working suspicion

Hermann Wedding is well known and his British travel, later metallurgical work and role in German metallurgy are historiographically visible. That does **not** establish that the Iron Library manuscript notebooks `Mss 23`, `Mss 24` and `Mss 25` have been systematically read page-by-page as a primary-source corpus.

The current hypothesis is therefore narrow:

> The three fully digitised notebooks may be substantially under-exploited at page level even though Wedding himself and the broad events recorded in them are not unknown.

This is a hypothesis to audit, not a novelty claim.

## Why the distinction matters

Later summaries can reconstruct a smooth career narrative from published sources, memoir, exhibition catalogues and retrospective biography:

- metallurgical training;
- study journeys;
- Britain / South Wales / Bessemer;
- 1862 London International Exhibition;
- later Berlin teaching, testing and metallography.

That narrative does not require close reading of the handwritten notebooks.

The notebooks may preserve a different evidential layer:

- exact daily itinerary;
- names of introducers, hosts, gatekeepers and technical guides;
- what Wedding knew before arrival;
- what access was granted or denied;
- what he measured, counted, copied or drew;
- what information came from direct observation versus oral report;
- reliability warnings;
- samples or drawings received/carried;
- technical judgements made in situ;
- comparative language before later retrospective smoothing.

The research value would therefore lie less in finding an unknown career event than in reconstructing a **working epistemology of industrial comparison**.

## Corpus structure

### Mss 23 — 1856–1857

Freiberg / training phase. Catalogue description indicates metallurgical notes combining personal observation with copied notebook/scientific material.

Potential analytical role:

**learning what counts as recordable metallurgical knowledge**.

### Mss 24 — 1858

German industrial study tour.

Potential analytical role:

**first sustained cross-site works comparison under German conditions**.

### Mss 25 — 1860–1862

Germany–Belgium–England, including British industrial travel / Bessemer context.

Potential analytical role:

**comparison under foreign access regimes, named specialist networks and high-value industrial sites**.

Together the three volumes potentially form a longitudinal corpus:

**training → domestic industrial tour → transnational industrial comparison**.

## Historiographical hypothesis to test

The stronger possible question is not simply `What did Wedding see in Sheffield?`

It is:

> **How did a metallurgist learn to compare?**

If the notebooks preserve the development of observation, measurement, copying, access, reliability judgement and comparison across 1856–62, they can be compared later with the microscopic comparison regime visible in Wedding's 1885 work and the Sorby response.

This would permit a controlled question:

> Which comparative habits persisted when the object of observation changed from whole works/processes to prepared microscopic surfaces, and which had to be remade?

Do not assume continuity in advance.

## Citation audit protocol

Search for actual use of the notebooks under all of the following:

- `Hermann Wedding Mss 23`
- `Hermann Wedding Mss 24`
- `Hermann Wedding Mss 25`
- `Eisenbibliothek Mss 23 Wedding`
- `Eisenbibliothek Mss 24 Wedding`
- `Eisenbibliothek Mss 25 Wedding`
- DOI `10.5076/e-codices-ebs-0023`
- DOI `10.5076/e-codices-ebs-0024`
- DOI `10.5076/e-codices-ebs-0025`
- German catalogue titles / title variants
- `Wedding 1860 England`
- `Wedding 1862 England`
- `Wedding South Wales`
- `Wedding Sheffield`
- `Wedding Bessemer`
- `Wedding Reisetagebuch`
- `Wedding Hüttenreise`

Search targets:

- Google Scholar;
- WorldCat / library catalogues;
- German and Swiss journal databases;
- dissertations / theses;
- books and book chapters;
- local / regional industrial-history publications;
- Iron Library publications;
- metallography histories;
- biographies of Wedding;
- histories of Bessemer / South Wales / Sheffield metallurgy where Wedding appears.

## Evidence classes for audit

Classify each hit as:

`A — PAGE-LEVEL USE`
: cites manuscript page/folio/image and analyses notebook content.

`B — MANUSCRIPT-LEVEL USE`
: cites Mss 23/24/25 as a source but without page-level analysis.

`C — CATALOGUE-DERIVED`
: repeats catalogue description or metadata without demonstrated manuscript reading.

`D — RETROSPECTIVE/PUBLISHED-SOURCE`
: reconstructs Wedding's travel/career from memoir, exhibition catalogue, later publication or biography rather than the notebooks.

`E — MENTION ONLY`
: names Wedding/travel/manuscript without evidential use.

## Current controlled statement

Do **not** write `nobody has read these notebooks`.

Use instead:

> Preliminary searching has not yet revealed substantial page-level scholarly use of Mss 23–25. Because absence from indexed web search is not proof of absence, a formal citation audit is required before any novelty claim is made.

## Why digitisation may still leave the corpus practically closed

The manuscripts are openly digitised, but digitisation does not equal practical textual accessibility.

Potential barriers:

- nineteenth-century German handwriting;
- hundreds of manuscript canvases;
- no reliable full-text search/transcription;
- mixed notes, copied material, drawings and observation;
- page/canvas numbering mismatches;
- requirement to distinguish direct observation from copied text.

Thus the useful distinction is:

`open access ≠ searchable corpus ≠ systematically exploited source`.

## Immediate dependency

The local acquisition of all three volumes is reported complete. A local OCR workflow has been specified:

- merge each image sequence to PDF for reading;
- OCR original JPGs locally;
- Tesseract-first for simple pages;
- PaddleOCR fallback for complex pages;
- output one provenance-rich JSON per manuscript.

Completion/upload of the three JSON files has **not yet been confirmed in the repository**.

Once they arrive, first build page-level itinerary/person/comparison indices before making any historiographical novelty claim.
