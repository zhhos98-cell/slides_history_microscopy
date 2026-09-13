# Bolton lending register capture schema v1

Updated: 2026-09-13
Target: `FZ/14/3/1 — Register of Slides Lent Out, May 1882–Jul 1887`
Status: FIELDWORK CAPTURE PLAN

## Purpose

The register should be photographed in full if repository rules and time permit. It is the strongest currently identified non-postal-society source for testing how a microscopical society turned a cabinet into a system of temporary custody.

The goal is not merely to count loans. The register should be captured so that individual preparations, borrowers and return cycles can be reconstructed and then cross-checked against minutes, accounts, membership lists and the 1898 catalogue.

## Chronological significance

A summer 1881 contemporary report says that:
- the Society slide collection was being re-arranged after substantial additions;
- the late John Thomas Redmayne's whole private collection had been placed in the President's and Secretary's hands for selection;
- six dozen Redmayne slides and forty-eight diatom slides were added;
- Society slides were already being lent to members.

The dedicated lending register then begins in **May 1882**, less than a year after this published description of re-arrangement and lending.

This sequence is suggestive but not self-explanatory:

`1881 documented lending/re-arrangement`
→ `May 1882 dedicated loan register begins`.

Do **not** claim that the 1881 re-arrangement caused the register to be created unless minutes or the register itself say so.

High-priority field check:
- photograph all opening leaves before the first transaction;
- look for rules, headings, resolutions, custodian names, numbering instructions, retrospective notes or a stated reason/date for beginning the register;
- check `FZ/14/1/2` around spring 1882 for a committee decision authorising or reorganising slide lending/recording.

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
- non-return/delay markers;
- condition/damage interventions;
- evidence of relay or borrower-to-borrower transfer;
- cabinet series disproportionately circulated.

## Identity and custody guards

- A repeated slide number is not automatically the same physical preparation if the register or later catalogue indicates replacement/remounting.
- A borrower name is not normalized to a Society member without membership evidence.
- Absence of a return date does not automatically mean loss.
- Crossed-out entries should be recorded as material marks before interpreting cancellation/return.
- Do not infer postal transport merely because the borrower lived outside Bolton; movement route requires evidence.
- Do not infer home use from the register alone unless wording or contemporary reports support it for the relevant transaction.

## Crosswalk sequence

### 1. Minutes
Use `FZ/14/1/2` for 1882–87.

First date hook:
- **spring 1882**, immediately before/around the May opening of the dedicated lending register.

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
2. photograph/scan the relevant 1880–82 transition in `FZ/14/1/1–2` around Redmayne display, selection/re-arrangement, lending implementation and the May 1882 register start;
3. photograph diagnostic 1882–87 minute entries identified from the lending register;
4. inspect `FZ/14/2/1` for membership crosswalks and only around diagnostic financial dates/cabinet headings;
5. photograph `FZ/14/3/2` title, organization, numbering structure, and entries corresponding to diagnostic loan-register items.

Do not spend the day reading the minute books linearly if the complete lending register has not yet been captured.

## Minimum publishable result

If the register records actual named borrowing and return but no damage, the case still demonstrates that the Society cabinet was an operating custody system rather than passive storage.

If numbers/subjects can be cross-walked into the 1898 catalogue, it additionally shows continuity between repeated temporary circulation and later formal collection order.

If minutes show an 1881–82 decision to formalise lending or create the register, the case becomes stronger again: it would document the conversion of an existing lending practice into an explicit administrative recording system.

Damage/repair would strengthen the maintenance argument but is no longer required for Bolton to be central.