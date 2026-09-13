# Bolton lending register capture schema v2

Updated: 2026-09-13
Target: `FZ/14/3/1 — Register of Slides Lent Out, May 1882–Jul 1887`
Status: FIELDWORK CAPTURE PLAN / REGISTER-ORIGIN TEST ADDED

## Purpose

The register should be photographed in full if repository rules and time permit. It is the strongest currently identified non-postal-society source for testing how a microscopical society turned a cabinet into a system of temporary custody.

The goal is not merely to count loans. The register should be captured so that individual preparations, borrowers and return cycles can be reconstructed and then cross-checked against minutes, accounts, membership lists and the 1898 catalogue.

## Chronological significance

A summer 1881 contemporary report says that:
- the Society slide collection was being re-arranged after substantial additions;
- the late John Thomas Redmayne's whole private collection had been placed in the President's and Secretary's hands for selection;
- six dozen Redmayne slides and forty-eight diatom slides were added;
- Society slides were **already being lent to members**.

The surviving dedicated lending register begins in **May 1882**.

Therefore:

**May 1882 is the start of the surviving register, not the demonstrated start of slide lending.**

Do not collapse these two chronologies.

## Session-boundary hypothesis — test, do not assert

The Society's 1880 annual report states that its year began on **1 October**; lectures and ordinary work occupied members until **May**, after which the Society `virtually closes` until September. The report describes this summer recess as a period in which members pursued microscopical research away from regular meetings.

The fact that the surviving lending register begins in **May 1882** therefore creates a bounded institutional hypothesis:

`existing lending by 1881`
→ `annual session reaches May boundary`
→ `surviving formal loan register begins May 1882`.

Possible interpretation to test:
formal recordkeeping may have become especially useful when slides entered member custody across or beyond the meeting season.

This is **not yet evidence** that the register was created for the summer recess. No public report located in the bounded search states why the register began, appoints a slide librarian/curator, or announces a new lending rule in May 1882.

The exact reason must be sought in `FZ/14/1/2` and the register's opening leaves.

## Register-origin field test

Before transcribing ordinary transactions, capture the administrative birth of the volume.

### Opening-material fields

Record separately:
- `cover_title_raw`;
- `inside_title_raw`;
- `first_written_date`;
- `first_transaction_date`;
- `opening_rule_or_instruction_raw`;
- `custodian_name_or_signature`;
- `secretary_name_or_signature`;
- `prefilled_column_headings`;
- `historical_page_or_folio_numbering`;
- `slide_numbers_prefilled_or_entered_per_transaction`;
- `evidence_of_backfill`;
- `earlier_date_than_register_start_present`;
- `opening_batch_size`;
- `multiple_loans_entered_same_day`;
- `cross-reference_to_minutes_rules_or_catalogue`;
- `later_annotation_on_opening_page`.

### First 20-entry diagnostic pass

Before coding the whole register, inspect the first c.20 entries and ask:
- do they begin as a sudden batch in May 1882 or as ordinary staggered loans?
- are loans already outstanding when the register opens?
- are old loans copied retrospectively into the new book?
- does one officer make all entries?
- are borrowers given cabinet/slide numbers rather than subjects?
- are return columns filled contemporaneously or retrospectively?
- does the register begin near the Society's May session closure?

A batch/backfill pattern would suggest formalisation of a pre-existing practice; it would still not establish the cause without minute evidence.

## Minute-book date window for register origin

Highest-priority bounded minute search:

**April–June 1882 in `FZ/14/1/2`.**

Search for:
- slides;
- cabinet;
- lending / loan / lent;
- register / book / list;
- President / Secretary;
- custodian / librarian / curator;
- rules / regulations;
- numbering / catalogue / index;
- summer / recess;
- return / overdue / detention;
- responsibility for Society property.

If no creation resolution is found, widen only to **Jan–Sep 1882**, not the whole minute book.

A negative result is meaningful: the register may have been an administrative practice adopted without a formal minuted resolution.

## Image protocol

Photograph:
1. front cover / title / archival reference slip;
2. all blank and written opening leaves that explain headings or rules;
3. every written register page in sequence;
4. any inserted slips, loose notes or retrospective annotations;
5. final written and blank closing pages if they preserve later notes.

File naming:
`BOL_FZ14_3_1_p0001.jpg`, `BOL_FZ14_3_1_p0002.jpg`, etc.

Keep image sequence tied to archive page/folio numbering where present. Do not silently renumber historical folios as modern pages.

## Row-level transcription fields

Minimum fields:

| field | description |
|---|---|
| `image_id` | photograph filename |
| `folio_or_page` | historical folio/page if present |
| `entry_order` | sequential row/entry number assigned during transcription |
| `date_out_raw` | wording exactly as written |
| `date_out_iso` | normalized date where secure |
| `borrower_raw` | name exactly as written |
| `borrower_normalized` | standardized person name only after identification |
| `slide_identifier_raw` | number/letter/cabinet address exactly as written |
| `slide_subject_raw` | subject/taxon/preparation wording |
| `maker_or_preparer_raw` | if supplied |
| `series_or_group_raw` | if supplied |
| `quantity_raw` | quantity as written |
| `date_returned_raw` | if present |
| `date_returned_iso` | normalized only where secure |
| `duration_days` | derived only from secure out/return dates |
| `condition_note_raw` | damage, missing, repair, breakage etc. exactly as written |
| `administrative_note_raw` | overdue, transferred, reissued, returned by another person, etc. |
| `custodian_initial_or_signature` | if present |
| `crossout_or_correction` | describe without guessing meaning |
| `confidence` | direct / uncertain transcription |

## Borrower/member crosswalk

`FZ/14/2/1` is not only an account book; the archive finding aid explicitly says it includes **membership lists, 1880–1894**.

For each distinct borrower where practical, create a separate person table:

| field | use |
|---|---|
| `borrower_raw` | register form |
| `member_match` | yes / probable / no / unresolved |
| `membership_name_raw` | exact form in `/2/1` |
| `membership_years` | only where explicit |
| `address_raw` | if supplied |
| `occupation_or_title_raw` | if supplied; do not infer from name alone |
| `officer_role` | if directly recorded |
| `notes` | ambiguity / same-name warning |

Purpose:
- test whether lending was limited to formal members;
- identify officers or highly active borrowers;
- distinguish one-off from recurrent users;
- provide bounded names for external directory/occupation checks only where that would change instrument-use interpretation.

Do not turn this into a social-network census unless the register itself makes borrower pattern analytically important.

## Derived analysis fields

After transcription, derive separately rather than writing inference into the raw table:
- number of distinct borrowers;
- number of lending events;
- number of identifiable individual slide addresses;
- repeat borrowing of the same slide/series;
- repeat borrowers;
- median/mean loan duration where return dates exist;
- seasonal pattern;
- **distribution around May–September recess versus Oct–May meeting season**;
- non-return/delay markers;
- condition/damage interventions;
- evidence of relay or borrower-to-borrower transfer;
- cabinet series disproportionately circulated.

Seasonality must be treated descriptively first. Do not infer that summer loans were home loans or caused the register's creation without source language.

## Identity and custody guards

- A repeated slide number is not automatically the same physical preparation if the register or later catalogue indicates replacement/remounting.
- A borrower name is not normalized to a Society member without membership evidence.
- Absence of a return date does not automatically mean loss.
- Crossed-out entries should be recorded as material marks before interpreting cancellation/return.
- Do not infer postal transport merely because the borrower lived outside Bolton; movement route requires evidence.
- Do not infer home use from the register alone unless wording or contemporary reports support it for the relevant transaction.
- Do not call May 1882 the start of lending; lending is already directly documented in 1881.
- Do not call May 1882 a recess-management reform unless minutes/register wording supports it.

## Crosswalk sequence

### 1. Minutes
Use `FZ/14/1/2` for 1882–87.

First date hook:
- **Apr–Jun 1882**, immediately before/around the May opening of the dedicated lending register.

Then follow diagnostic dates/names from the register, especially:
- unusually long or missing returns;
- explicit damaged/missing notes;
- very large multi-slide loans;
- new borrowing rules or custodian changes;
- first appearance of a numbered series.

### 2. Accounts + membership
Use `FZ/14/2/1` (1880–94) for:
- borrower/member identity where membership lists permit;
- cabinet/tray/box expenditure;
- labels/cataloguing materials;
- postage/carriage;
- purchases/replacement slides;
- repair/remounting costs if any.

### 3. 1898 catalogue
Use `FZ/14/3/2` to test whether highly circulated 1882–87 entries remain institutionally addressable in 1898.

Strong chain:
`loan-register address/subject → repeated temporary custody → 1898 catalogue address/subject`.

Stronger chain if evidence exists:
`loan → loss/damage/intervention → replacement or changed physical state → same/translated catalogue identity`.

## Fieldwork time rule

Priority order for a one-day Bolton visit:
1. photograph `FZ/14/3/1` completely, including opening/closing leaves;
2. inspect/photograph **Apr–Jun 1882** in `FZ/14/1/2` for the register's administrative origin;
3. photograph the 1880–81 Redmayne/display/selection/re-arrangement transition in `FZ/14/1/1–2`;
4. photograph diagnostic 1882–87 minute entries identified from the lending register;
5. inspect `FZ/14/2/1` for membership crosswalks and only around diagnostic financial dates/cabinet headings;
6. photograph `FZ/14/3/2` title, organization, numbering structure, and entries corresponding to diagnostic loan-register items.

Do not spend the day reading the minute books linearly if the complete lending register has not yet been captured.

## Minimum publishable result

If the register records actual named borrowing and return but no damage, the case still demonstrates that the Society cabinet was an operating custody system rather than passive storage.

If numbers/subjects can be cross-walked into the 1898 catalogue, it additionally shows continuity between repeated temporary circulation and later formal collection order.

If minutes show an 1881–82 decision to formalise lending or create the register, the case becomes stronger again: it would document the conversion of an existing lending practice into an explicit administrative recording system.

If no such minuted decision exists, do not weaken the case artificially: the register itself remains evidence of administrative formalisation no later than May 1882, while the motive/mechanism of its creation remains unresolved.

Damage/repair would strengthen the maintenance argument but is no longer required for Bolton to be central.