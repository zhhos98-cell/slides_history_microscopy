# Working Men's College Magazine — issue census v1

**Date:** 2026-09-09  
**Branch:** `research/working-mens-microscopy-19c`  
**Purpose:** build an issue-level control surface for *The Working Men's College Magazine* without prematurely forcing a terminal date. This file separates exact issue evidence, secondary issue citations, run-level bibliography, and material-state questions.

## Governing caution

Current run evidence is genuinely conflicting.

- Boston University research text: Magazine began **January 1859** under John Ludlow and ended **January 1861** under R. B. Litchfield; no successor until *The Working Men's College Journal* in February 1890.
- Open Library: monthly, Macmillan & Co., **3 volumes**, no more published, reproduction from the Goldsmiths' Library copy.
- A later bibliography lists **3 vols., 1859–1861**.
- J. F. C. Harrison's centenary history explicitly attributes a quotation to **The Working Men's College Magazine, January 1862**.

Therefore:

`RUN_STATE = CONFLICTED`

Do not normalize the endpoint to January 1861 or January 1862 until a direct issue/volume census of the Goldsmiths' Library / BL / other physical or digitized set resolves the discrepancy.

Possible explanations to test rather than assume:

1. Harrison miscited the date;
2. BU secondary reconstruction ended the run one year too early;
3. volume-year and issue-year boundaries differ;
4. a late/supplementary issue has been treated differently by cataloguers;
5. bound 3-volume structure obscures original monthly sequence.

## Exact / near-exact issue evidence currently recovered

| date | issue/number state | page / locus | content / function | evidence state | next action |
|---|---|---|---|---|---|
| Jan 1859 | issue 1 implied by secondary citation | pp. 2–3 cited | early governance / educational-order discussion in Sutcliffe | `SECONDARY_ISSUE_CITATION` | inspect issue image and contents |
| Feb 1859 | no. ii explicitly cited | Supplement pp. 32–33 | citizenship / governance / institutional educational argument | `SECONDARY_ISSUE_CITATION` | determine whether Supplement is separately paginated / separately bound |
| Mar 1859 | issue existence expected from monthly run | — | Ludlow resignation letter dated 7 Mar 1859 relates to editorship but is not itself issue evidence | `RUN_CONTEXT_ONLY` | locate issue and masthead/editorial state |
| Oct 1859 | monthly issue; contemporary trade-list notice recovered | p. 162 cited by Sutcliffe | WMC drawing / liberal-vs-technical education context | `TRADE_LIST_PLUS_SECONDARY_PAGE_CITATION` | inspect issue; resolve printed issue number OCR |
| Sep 1860 | issue cited | p. 135 | R. B. Litchfield, `What shall I read?`; reading guidance / knowledge classification | `SECONDARY_ISSUE_CITATION` | recover exact article opening, authorship signature, surrounding contents |
| Jan 1861 | issue cited | p. 25 / iii citation in Sutcliffe | Litchfield defence of WMC liberal-education `differentia`; anti-utilitarian institutional self-definition | `SECONDARY_ISSUE_CITATION` | inspect full issue and establish whether terminal issue |
| Jan 1862 | date explicitly cited by Harrison | quotation: `Think what we are, or ought to be...` | fellowship / College self-definition | `RUN_CONFLICT_PRIMARY_HISTORY_CITATION` | inspect Harrison footnote/source and locate physical/digital issue |

## Contemporary external evidence about issue use

### Atlantic Monthly, July 1861

A visitor describes:

- College office / reading room with catalogues, circulars and Working-Men's College Magazines present;
- the title as a **monthly magazine** devoted to College interests;
- purchase of `the volume for the year`;
- reading the Magazine in the College reading room in order to understand the institution;
- becoming a member and choosing a class after this orientation.

Functional closure:

`College office / reading room -> annual bound volume of monthly serial -> reader learns institutional structure -> membership / class choice`

This is direct evidence that annual binding and monthly publication coexisted as user-facing forms.

## Run-level bibliography

### Open Library / Goldsmiths' Library reproduction

- title: *The working men's college magazine*;
- publisher: Macmillan & Co.;
- publication start displayed as 1859;
- monthly;
- includes index;
- `no more published`;
- online object described as **3 volumes**;
- reproduction of Goldsmiths' Library of Economic Literature copy.

### Macmillan bibliographical catalogue

Macmillan's own historical catalogue lists:

`The Working Men's College Magazine published under the direction of the Council of the (London) Working Men's College.`

This is important because it identifies **Council direction** in the publisher's bibliographic description. The title was therefore institutionally authorized print, not merely an unofficial student magazine.

### Contemporary trade-list evidence

An October 1859 periodical/publication list carries *The Working Men's College Magazine* among current monthly/serial publications from Macmillan & Co. OCR of the number is unreliable in the available scan/snippet, so do not assign an issue number from that OCR alone.

## Editorial-state questions

Current secondary reconstruction says:

- January 1859 launch under John Ludlow;
- Ludlow resigned from the editorship, with a surviving 7 March 1859 resignation letter;
- later/end editorship under R. B. Litchfield;
- insufficient circulation / financial difficulty contributed to closure.

Issue census must therefore capture for every issue:

`date | printed editor/masthead | council statement | contributors | unsigned editorials | price | publisher | printer | pagination | supplement state | notices | ads | wrappers`

Do not assign editorial responsibility to a named individual where an issue itself is unsigned or collective.

## Known periodical functions already supported

### `ORIENT`

The Magazine could introduce a newcomer to College organization and facilitate membership/class choice.

### `READ_GUIDE`

Litchfield's `What shall I read?` serialized guidance turned the Magazine into a roadmap for self-education and the classification of worthwhile reading.

### `SELF_DEFINE`

The Magazine articulated the College's institutional identity, including the distinction between liberal education and narrowly wage-oriented/utilitarian education.

### `GOVERNANCE_ARGUMENT`

Early 1859 issue/supplement citations show the Magazine participating in disputes about worker participation, hierarchy, citizenship and College governance.

### `ANNUAL_BINDING_INTERFACE`

Contemporary testimony demonstrates that monthly issues were also encountered as a purchasable annual volume in the College reading room.

## Science / natural-history extraction queue

No dedicated microscopy article is yet closed. Issue-level inspection should search for:

- `microscope`, `microscopical`, `microscopic`;
- `botany`, `physiological botany`, `natural history`;
- `geology`, `mineralogy`, `zoology`, `physiology`;
- `museum`, `specimen`, `fossil`, `shell`, `mineral`, `collection`;
- `Cooke`, `Grugeon`, `Slade`, `Seeley`, `Maskelyne`, `Davies`;
- excursions / field walks;
- donations / identifications / object acquisition;
- library acquisitions and scientific reading recommendations;
- advertisements for instruments, books, courses or societies;
- reports of College clubs or museums.

Important boundary: later evidence that M. C. Cooke taught Physiological Botany with microscope use in 1861 does **not** establish Magazine coverage. Keep the class-to-periodical edge open until issue evidence closes it.

## RSVP physical-inspection targets

High priority because the research question concerns serial materiality, not just article text:

1. original wrappers / covers;
2. advertisements and publishers' lists;
3. supplements, especially Feb 1859;
4. indexes and tables of contents;
5. whether annual bindings preserve monthly covers and issue boundaries;
6. separately paginated notices/circulars;
7. ownership / annotations / use traces in surviving copies;
8. differences among Goldsmiths' Library, British Library and any WMC-held copies;
9. evidence for January 1862 or other terminal material;
10. price/subscription information and how annual-volume sale related to monthly subscription.

## Immediate next pass

1. recover exact full citations for the Jan/Feb/Oct 1859, Sep 1860, Jan 1861 entries;
2. test direct availability of the 3-volume Goldsmiths' reproduction at issue/page level;
3. inspect Harrison's January 1862 attribution and source note;
4. build a normalized contents ledger once at least one volume can be directly read;
5. compare Magazine genres against Sheffield *People's College Journal* and Halifax *Circulator* rather than treating London as the default institutional model.

## Stop rule

Do not infer issue sequence from month arithmetic. Do not infer a terminal date from `3 volumes`. Do not convert secondary page references into primary quotations until the issue itself is inspected. A bibliographic conflict is an object of research here because later binding/cataloguing may itself alter the perceived serial history.