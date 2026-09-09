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
| January 1861, no. 25, p. iii | Sutcliffe footnote 49 gives `WMCM (January, 1861), 25: iii` for Litchfield's editorial defending the `differentia of the College` against wage/utilitarian education; the passage contrasts arithmetic justified by extra wages with grammar and frames the College as a protest against popular doctrines of education. | `CLOSED_CITATION_SECONDARY_HIGH` | This is the strongest current late-run anchor. If `25` is issue number, it fits a monthly sequence beginning Jan. 1859 exactly; direct issue inspection should confirm the notation. |
| January 1862 | J. F. C. Harrison's *A History of the Working Men's College, 1854–1954* preview attributes `Think what we are, or ought to be; a body of men met together for general good ... a community associated for education in fellowship` to *The Working Men's College Magazine, January 1862*. | `RUN_CONFLICT_HIGH_VALUE` | Isolated but important counterevidence to a Jan-1861 termination. Could represent miscitation, a later issue, supplement, or another bound component. Must inspect the cited primary item. |
| 1862 external-use context | A study of Elizabeth Gaskell's Cotton Famine correspondence identifies *The Working Men's College Magazine* as a regular WMC publication in notes to 1862 correspondence. | `CONTEXT_ONLY` | Consistent with the Magazine remaining available/known in 1862 but does not prove a newly issued 1862 number. |

## Run conflict

Two incompatible secondary reconstructions are preserved deliberately, but the evidential balance is no longer even.

### Model A — January 1859 to January 1861

A Boston University dissertation states explicitly that the Magazine began in January 1859 under John Ludlow and ended in January 1861 under R. B. Litchfield, chiefly because insufficient circulation caused financial difficulty; it says no successor appeared until *The Working Men's College Journal* in February 1890.

This model now has an additional exact anchor: Sutcliffe cites a **January 1861, no. 25, p. iii** issue. A monthly no. 25 is arithmetically consistent with January 1859 as no. 1, although this sequence must still be verified against the physical issues rather than assumed.

Several later bibliographies also describe the title as three volumes, `1859–1861`.

### Model B — 1859 to at least January 1862

Counterevidence currently rests mainly on:

- Harrison's institutional history explicitly citing *Working Men's College Magazine, January 1862*;
- an independent periodical index giving the title's span as `1859–1862`;
- 1862 correspondence/context in which the Magazine is treated as a regular College publication.

The latter two are weaker than an actual issue citation; the Harrison citation therefore carries most of the weight for Model B.

### Controlled state

`RUN_START = Jan 1859 (strong)`  
`LATE_ISSUE_ANCHOR = Jan 1861 / no.25 / p.iii (strong secondary citation)`  
`RUN_END_LEADING_MODEL = Jan 1861`  
`RUN_END_COUNTEREVIDENCE = Harrison citation to Jan 1862`  
`RESOLUTION_METHOD = direct issue/bound-volume inspection`

Do not silently discard the 1862 citation, but do not treat it as equivalent to a directly closed issue either.

## Known functional genres already recoverable

1. `PROGRAMMATIC_LECTURE` — Maurice / educational purpose, opening issue.
2. `SUPPLEMENT` — Feb. 1859 physical/serial layer.
3. `GOVERNANCE` — Oct. 1859, p.162.
4. `READ_GUIDE` — Litchfield, Sep. 1860, p.135.
5. `EDUCATIONAL_POLEMIC` — Litchfield, Jan. 1861, no.25, p.iii: liberal education vs wage/utilitarian justification.
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
- whether `January 1862` exists as an actual issue, supplement, annual-volume component, or miscitation;
- whether January 1861 no.25 is in fact the terminal issue.

## Sources currently controlling this ledger

- Open Library bibliographic record: *The Working Men's College Magazine*, Macmillan & Co., monthly, 3 volumes, reproduction from Goldsmiths' Library / Senate House Library.
- *Atlantic Monthly*, July 1861, `The London Working-Men's College`.
- Marcella Pellegrino Sutcliffe, `The origins of the 'two cultures' debate in the adult education movement: the case of the Working Men's College (c.1854–1914)`, *History of Education* 43 (2014), issue/page citations above.
- NCSE / *Literary Gazette*, 8 Oct. 1859, publication list, Magazine no. 9.
- J. F. C. Harrison, *A History of the Working Men's College, 1854–1954*, preview citation to January 1862.
- Boston University dissertation giving Jan 1859–Jan 1861 run.
- later bibliographies listing three volumes, 1859–1861.

## Next pass

1. Recover table of contents / index for each bound volume if possible without relying on OCR snippets.
2. Page-close January 1861 no.25 and determine whether it is terminal.
3. Build first science/natural-history hit list with exact issue/page.
4. Preserve any discrepancy between issue-level chronology and later three-volume binding rather than normalizing it away.
