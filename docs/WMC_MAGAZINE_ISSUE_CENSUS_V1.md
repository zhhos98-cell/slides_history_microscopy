# Working Men's College Magazine — issue census v1

**Date:** 2026-09-09  
**Branch:** `research/working-mens-microscopy-19c`  
**Purpose:** issue-level control surface for *The Working Men's College Magazine*. This file separates direct contemporary evidence, scholarly exact citations, bibliographic run claims, and material-state questions.

## Governing correction

The earlier provisional endpoint `January 1861` is withdrawn.

Current evidence:

- Boston University research text says Jan 1859–Jan 1861;
- July 1861 *Atlantic Monthly* contemporaneously describes WMC as publishing a **monthly** Magazine and describes a reader buying/using the volume for the year;
- N. E. C. Smith gives an exact citation to *Working Men's College Magazine* **3 (1861), p.173**;
- modern scholarship cites multiple additional 1861 pages;
- Open Library describes a monthly **3-volume** Goldsmiths' Library reproduction;
- later bibliography lists 3 vols., 1859–1861;
- Harrison explicitly cites **January 1862**;
- another periodical index lists the title as 1859–1862.

Therefore:

`RUN_STATE = CONFLICTED_BUT_DEFINITELY_ACTIVE_AFTER_JAN_1861`

`JAN_1861_END = CONTRADICTED`

`JAN_1862 = LIVE_CANDIDATE / PRIMARY_ISSUE_PENDING`

Do not normalize the terminal date until a direct issue/volume census resolves it.

## Exact / near-exact issue evidence currently recovered

| date | issue/volume state | page / locus | content / function | evidence state | next action |
|---|---|---|---|---|---|
| Jan 1859 | issue 1 implied by secondary citation | pp.2–3 cited | governance / educational-order discussion | `SECONDARY_ISSUE_CITATION` | inspect issue image/contents |
| Feb 1859 | no.ii explicitly cited | Supplement pp.32–33 | citizenship / governance / educational argument | `SECONDARY_ISSUE_CITATION` | inspect supplement material state |
| Mar 1859 | issue expected; editorship context | — | Ludlow resignation dated 7 Mar 1859, not issue evidence | `RUN_CONTEXT_ONLY` | locate issue/masthead |
| Oct 1859 | contemporary publication-list evidence | secondary p.162 citation | drawing / liberal-vs-technical education | `TRADE_LIST_PLUS_SECONDARY_PAGE_CITATION` | inspect issue; resolve number OCR |
| 1860 | volume/year securely cited in later histories | multiple loci pending | institutional/social content | `YEAR_VOLUME_CONTEXT` | build issue census |
| Sep 1860 | issue cited | p.135 | R. B. Litchfield, `What shall I read?` | `SECONDARY_ISSUE_CITATION` | inspect article and surrounding contents |
| Jan 1861 | issue cited | p.25 / preliminary iii | liberal-education self-definition | `SECONDARY_ISSUE_CITATION` | inspect full issue |
| 1861, vol.3 | exact scholarly citation | **p.173** | `Report of General Meeting`; Cooke Physiological Botany class / microscope teaching plan | `SECONDARY_EXACT_CITATION_HIGH_VALUE` | inspect p.173 primary page |
| Jul 1861 external testimony | Magazine described as current monthly | user-level locus | annual volume purchased/read in WMC reading room | `CONTEMPORARY_EXTERNAL_PRIMARY` | use as run/function control |
| Jan 1862 | date explicitly cited by Harrison | quotation locus | College fellowship/self-definition | `RUN_CONFLICT_HISTORY_CITATION` | locate issue / verify date |

## Science / natural-history content state — upgraded

### 1. Cooke class report is inside the Magazine

N. E. C. Smith's exact citation:

> `Report of General Meeting`, *Working Men's College Magazine* 3 (1861), 173.

Smith reads this item as evidence for M. C. Cooke's 1861 evening class of Physiological Botany and states that Cooke emphasized microscope use in his teaching plan.

State:

`SCIENCE_IN_WMCM = POSITIVE`

`COOKE_CLASS_REPORT = CLOSED_SECONDARY_EXACT_CITATION`

`PRIMARY_WORDING = PENDING`

This supersedes the previous `NEGATIVE_BOUNDED_INDEX_SEARCH` as the governing content state.

### 2. Alfred Grugeon contributed several botany papers

Darwin Correspondence Project authority entry states that Alfred Grugeon:

- studied botany at WMC;
- became a certified instructor and taught there;
- **contributed several papers on botany to the college magazine**.

Sources given there include Ray Desmond and John Ramsbottom, *Journal of Botany* 55 (1917): 193–94.

State:

`GRUGEON_WMCM_BOTANY_PAPERS = STRONG_SECONDARY_EXISTENCE`

`EXACT_TITLES / DATES / PAGES = NOT_YET_EXTRACTED`

### 3. Attribution infrastructure already exists

William S. Peterson published:

> `The Working Men's College Magazine: A List of Attributions for Anonymous and Pseudonymous Articles, 1859–1860`, *Victorian Periodicals Newsletter* 11.2 (1978): 58–60.

This is now a high-priority control for anonymous/pseudonymous science contributions and author identification.

Meta-relevance: *Victorian Periodicals Newsletter* is the predecessor title of RSVP's *Victorian Periodicals Review*.

## Contemporary external evidence about issue use

### Atlantic Monthly, July 1861

The visitor describes:

- WMC office/reading room with catalogues, circulars and Magazine copies;
- title as a monthly Magazine devoted to College interests;
- buying/taking the volume for the year;
- reading it to understand College operations;
- joining the College and selecting a class.

Functional closure:

`College print -> institutional orientation -> membership -> class choice`

This also provides direct evidence against a simple January 1861 termination.

## Run-level bibliography

### Open Library / Goldsmiths' reproduction

- monthly;
- Macmillan & Co.;
- 3 volumes;
- includes index;
- no more published;
- reproduction from Goldsmiths' Library of Economic Literature.

### Macmillan bibliographical catalogue

Describes the Magazine as published under direction of the WMC Council.

### Later run controls

- a bibliography lists `3 vols., 1859–1861`;
- Harrison cites `January 1862`;
- a separate periodical index lists `1859–1862`.

Treat all as run evidence of differing strength; direct issue images remain decisive.

## Alfred Grugeon serial/association extraction queue

The Magazine now needs to be crosswalked against direct later traces:

- *Science-Gossip*, 1 June 1865, p.143 — Grugeon botanical observations/queries on *Paris quadrifolia* and *Valeriana dioica*;
- same issue p.144 — Society of Amateur Botanists meeting information and proposed Amateur Microscopical Society recruitment routed through 192 Piccadilly;
- Society of Amateur Botanists meeting, 2 May 1866 — Grugeon reads a morphology paper;
- *Geological Magazine* 5 (1868), p.536 — Grugeon on Hackney Downs;
- 1873 WMC Natural History Society and Field Club — Grugeon committee/papers/grass collection;
- later Lubbock Field Club / WMC Journal documentation.

Do not infer Society of Amateur Botanists membership solely from page adjacency; the 1866 meeting report directly establishes his participation as paper-giver.

## Issue census fields

For every recovered issue:

`date | vol | issue/no. | page span | editor/masthead | contributor | attribution state | genre | science/natural history | class | museum | club | object/specimen | correspondence | supplement | ads/wrappers | binding state | source confidence`

## RSVP physical-inspection targets

Priority additions after this correction:

1. Volume 3 / 1861, especially p.173;
2. Grugeon's several botany papers;
3. indexes and contributor/attribution traces;
4. short class reports / museum / excursion / donation notices;
5. Peterson-attributed anonymous/pseudonymous items;
6. original wrappers / covers / advertisements / supplements;
7. annual binding vs monthly boundaries;
8. evidence for January 1862;
9. Goldsmiths vs BL vs WMC-copy differences.

## Immediate next pass

1. recover Grugeon article titles/locations;
2. inspect Peterson 1978 list;
3. inspect Ramsbottom 1917 notice;
4. page-close WMCM vol.3 p.173;
5. resolve 1861 issue sequence and terminal date;
6. build a science-content sub-ledger by genre, not merely keyword.

## Stop rule

Do not restore the old bounded-negative science claim. Do not call the Magazine ended January 1861. Do not invent Grugeon article titles from authority summaries. Do not turn exact scholarly citations into primary quotations until the Magazine page is inspected. Preserve run conflict as a bibliographical/material problem until issue-level evidence closes it.