# Working Men's College Magazine — issue census v0.1

**Date:** 2026-09-09  
**Branch:** `research/working-mens-microscopy-19c`  
**Status:** partial issue-level reconstruction from contemporary listings and source-bearing secondary scholarship; direct bound-volume census still required.

## Governing rule

Do not infer a continuous monthly run from secondary statements alone. Record only issue/date/page relations actually supported by a source, and keep publication-date, issue-number, bound-volume, and later-citation evidence distinct.

## Current issue/page signals

| Date / issue signal | Exact evidence | State | Research significance |
|---|---|---|---|
| January 1859, opening issue | Secondary scholarship cites `WMCM (January 1859), 1:2–3`; another source cites F. D. Maurice, `Introductory Lecture on the Study of the (London) Working Men's College`, no. 1 (January 1859), p. 6. | `CLOSED_CITATION_SECONDARY` | Establishes opening month and issue no. 1; ideological/programmatic material from the start. |
| February 1859, no. ii | Marcella Pellegrino Sutcliffe cites `Working Men's College Magazine, n. ii (Feb. 1859), Supplement: 32` and separately `WMCM (February 1859), Supplement, 33`. | `CLOSED_CITATION_SECONDARY`; `MATERIAL_STATE_PENDING` | Crucial evidence that at least one issue had a **Supplement**; BL inspection should establish how supplement was physically issued/bound and whether it carries notices, governance, or curriculum material. |
| September/October 1859 issue-number signal | *Literary Gazette* / NCSE listing dated 8 Oct. 1859 advertises `The Working Men's College Magazine. No. 9. Macmillan and Co.` | `CLOSED_CONTEMPORARY_LISTING` | Confirms numbered serial circulation through no. 9 in autumn 1859; does **not** by itself prove the issue's internal printed month/date. |
| October 1859, p. 162 | Sutcliffe cites `WMCM (October 1859): 162` in discussion of College governance/student participation. | `CLOSED_CITATION_SECONDARY` | Gives an exact page/date anchor for institutional politics inside the Magazine. |
| September 1860, p. 135 | Sutcliffe cites `WMCM (September 1860): 135` for R. B. Litchfield, `What shall I read?` / reading guidance. | `CLOSED_CITATION_SECONDARY` | Strong `READ_GUIDE` function: Magazine actively directed students' reading and self-education. |
| Early 1860s, Litchfield anti-utilitarian editorial | Sutcliffe quotes Litchfield defending the `differentia of the College` against wage/utilitarian education and calling Working Men's Colleges either a `hopeless absurdity` or `Colleges militant`; exact issue/month needs footnote-level recovery. | `INDEXED_SECONDARY_NOT_ISSUE_CLOSED` | Directly relevant to how periodical print classified liberal/scientific/vocational knowledge. |
| January 1862 | J. F. C. Harrison's *A History of the Working Men's College, 1854–1954* preview attributes `Think what we are, or ought to be; a body of men met together for general good ... a community associated for education in fellowship` to *The Working Men's College Magazine, January 1862*. | `RUN_CONFLICT_HIGH_VALUE` | Strong evidence against a simple Jan-1861 termination unless Harrison's citation is erroneous or refers to another object. Must inspect cited primary issue. |
| 1862 external-use context | A study of Elizabeth Gaskell's Cotton Famine correspondence identifies *The Working Men's College Magazine* as a regular WMC publication in notes to 1862 correspondence. | `CONTEXT_ONLY` | Consistent with survival/use into 1862 but does not alone prove a newly issued 1862 number. |

## Run conflict

Two incompatible secondary reconstructions are now preserved deliberately:

### Model A — January 1859 to January 1861

A Boston University dissertation states explicitly that the Magazine began in January 1859 under John Ludlow and ended in January 1861 under R. B. Litchfield, chiefly because insufficient circulation caused financial difficulty; it says no successor appeared until *The Working Men's College Journal* in February 1890.

### Model B — 1859 to at least January 1862

Counterevidence includes:

- Harrison's institutional history explicitly citing *Working Men's College Magazine, January 1862*;
- an independent periodical index giving the title's span as `1859–1862`;
- 1862 correspondence/context in which the Magazine is treated as a regular College publication.

### Controlled state

`RUN_START = Jan 1859 (strong)`  
`RUN_END = UNRESOLVED: Jan 1861 vs >= Jan 1862`  
`RESOLUTION_METHOD = direct issue/bound-volume inspection`

Do not silently choose one endpoint.

## Known functional genres already recoverable

1. `PROGRAMMATIC_LECTURE` — Maurice / educational purpose, opening issue.
2. `SUPPLEMENT` — Feb. 1859 physical/serial layer.
3. `GOVERNANCE` — Oct. 1859, p.162.
4. `READ_GUIDE` — Litchfield, Sep. 1860, p.135.
5. `EDUCATIONAL_POLEMIC` — Litchfield on liberal vs utilitarian education, exact issue pending.
6. `ORIENT` — contemporary *Atlantic Monthly* visitor buys annual volume and uses Magazine to learn how the College works before joining/choosing a class.

## Science / natural-history extraction targets

Direct Magazine articles on microscopy are not yet closed. Issue-level inspection should search systematically for:

- `geology`, `geological`, `fossil`, `mineral`, `museum`;
- `natural history`, `botany`, `physiology`, `zoology`;
- `microscope`, `microscopic`, `microscopical`;
- `Cooke`, `Slade`, `Grugeon`, `Seeley`;
- College Museum accessions/donations;
- field excursions / country walks;
- class notices and examination results;
- scientific books and reading recommendations;
- advertisements for instruments, books, specimens, courses or lectures.

The surrounding WMC evidence establishes natural-history activity and the College Museum, but this does **not** license transferring that activity into the Magazine without an issue/page hit.

## Material inspection targets for RSVP trip

Highest priority:

- original wrapper vs later binding;
- February 1859 Supplement: bound in sequence, separately paginated, or inserted?
- whether advertisements/publishers' lists survive;
- whether monthly issue numbers/months are printed consistently;
- whether the 3-volume Goldsmiths/Senate House reproduction preserves complete issue boundaries;
- any discrepancy between contents/index and physical fascicles;
- whether `January 1862` exists as an actual issue, supplement, annual-volume component, or miscitation.

## Sources currently controlling this ledger

- Open Library bibliographic record: *The Working Men's College Magazine*, Macmillan & Co., monthly, 3 volumes, reproduction from Goldsmiths' Library / Senate House Library.
- *Atlantic Monthly*, July 1861, `The London Working-Men's College`.
- Marcella Pellegrino Sutcliffe, `The origins of the 'two cultures' debate in the adult education movement: the case of the Working Men's College (c.1854–1914)`, *History of Education* 43 (2014), issue/page citations above.
- NCSE / *Literary Gazette*, 8 Oct. 1859, publication list, Magazine no. 9.
- J. F. C. Harrison, *A History of the Working Men's College, 1854–1954*, preview citation to January 1862.
- Boston University dissertation giving Jan 1859–Jan 1861 run.

## Next pass

1. Recover table of contents / index for each bound volume if possible without relying on OCR snippets.
2. Page-close the exact issue for Litchfield's `differentia / Colleges militant` editorial.
3. Build first science/natural-history hit list with exact issue/page.
4. Preserve any discrepancy between issue-level chronology and later three-volume binding rather than normalizing it away.
