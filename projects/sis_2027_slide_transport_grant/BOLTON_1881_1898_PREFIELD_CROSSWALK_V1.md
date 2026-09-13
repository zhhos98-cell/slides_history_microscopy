# Bolton 1881 → 1898 pre-field crosswalk v2

Updated: 2026-09-13
Status: DIRECT 1881 PRIMARY-INDEX CONTROL / 1898 CATALOGUE CONTENT NOT YET DIGITALLY CONTROLLED

## 1. Problem

Bolton now has a strong institutional sequence but the crucial identity crosswalk still depends on records not yet directly inspected:

`1880–81 accessions and selection`
→ `re-arranged Society cabinet`
→ `1882–87 lending register`
→ `1898 printed catalogue`.

The archive-supplied finding aid gives the exact documents:

- `FZ/14/1/1` — General and Committee Minutes, 1 Aug 1877–29 Oct 1880;
- `FZ/14/1/2` — General and Committee Minutes, 5 Nov 1880–8 Feb 1900;
- `FZ/14/2/1` — Account and Subscription Book, 1880–94;
- `FZ/14/3/1` — **Register of Slides Lent Out, May 1882–Jul 1887**;
- `FZ/14/3/2` — *Catalogue of Slides, Journals, and Books belonging to the Society*, 1898.

The 1898 catalogue has not yet been found as a public digital full text. Do not invent numbering or classification schemes before inspection.

## 2. Direct 1881 printed control

The indexed text of *The Northern Microscopist*, vol. 1 (1881), printed p. **167**, contains a notice headed **BOLTON MICROSCOPICAL SOCIETY**.

It states, in one continuous institutional description, that:
- although the Society took a summer holiday in June–August, work continued;
- the valuable slide collection was being **re-arranged** because of recent additions;
- the most notable addition was **six dozen choice slides** given by Mrs Redmayne from the collection of the late Dr Redmayne, described as founder of the Society;
- to permit the most suitable selection, Mrs Redmayne placed the **whole collection** in the hands of the Society President and Secretary;
- **forty-eight choice slides of diatoms** had also been added;
- the Society's slides were **lent to members**, who would have material for winter-evening study.

This is now primary-period indexed control of the whole chain rather than reliance on a later biographical paraphrase.

Source:
*The Northern Microscopist* 1 (1881), p. 167, `Notices of Meetings — Bolton Microscopical Society`; Internet Archive identifier `microscopicalnew01davi` / indexed public scan.

The current web interface has not yielded a stable page-image screenshot because the full-volume PDF exceeds the fetch limit. Treat the wording as direct OCR/indexed-periodical control; inspect the page image in the archive or a lighter page-level interface before using a long quotation in publication.

## 3. Controlled 1880–81 intake anchors

### Sharpus series, 1880

Contemporary reporting records that corresponding member F. W. Sharpus, through W. R. Hughes, presented a series of twelve Echinodermata slides to the Society cabinet.

Use as a bounded series candidate because:
- quantity is explicit;
- subject family is explicit;
- donor/intermediary relation is explicit;
- it predates the lending register by only c.2 years.

Crosswalk target:
`Sharpus / Hughes / Echinodermata / 12 slides`.

### Redmayne selection, 1881 — p.167 directly controlled

The 1881 notice directly establishes:
- Mrs Redmayne placed the whole collection in the hands of the Society President and Secretary for selection;
- **six dozen = 72 choice slides** were selected/given to the Society;
- the Society collection was being **re-arranged**;
- Society slides were **lent to members**.

Crosswalk target:
`Redmayne / 72 selected slides / diagnostic maker-subject labels recovered from minutes/register/catalogue`.

Do not assume every Redmayne-labelled slide in later records belonged to the 72 selected set unless the accession/minutes establish it.

### Additional forty-eight diatom slides, 1881 — p.167 directly controlled

The same notice records **48 choice slides of diatoms** newly added.

Current donor/source: not identified by the controlled notice.

Crosswalk target:
`48 / diatom(s) / accession around summer 1881`.

Keep this separate from the 72 Redmayne slides unless internal records explicitly connect them.

## 4. Exact field sequence

### Step A — accession language in minutes

Use `FZ/14/1/1` and early `FZ/14/1/2` to extract:
- exact meeting dates;
- donor/source names;
- wording: presented / selected / accepted / purchased / added / arranged;
- any assigned slide/cabinet numbers;
- names of President and Secretary acting on the Redmayne collection;
- whether unselected material was returned;
- whether the 48 diatom slides have a separate donor/source;
- cabinet/tray/box references;
- resolutions about lending.

Contemporary 1880 reporting identifies C. L. Jackson, F.R.M.S. as President and William/W. Rideout as Honorary Secretary at the November Conversazione. Do not automatically project those office-holders onto the summer 1881 selection without checking the minutes/election cycle.

### Step B — financial layer

Use `FZ/14/2/1` around 1880–82 for:
- cabinet/tray/box expenditure;
- labels/index/catalogue work;
- slide purchases;
- carriage/postage;
- repair/remounting/replacement if present;
- membership names useful for lending-register identity resolution.

Absence of expenditure is informative but not evidence that re-arrangement required no labour/material intervention.

### Step C — photograph `FZ/14/3/1` in full

The complete 1882–87 lending register is the core capture target.

Record for every legible transaction:
- date out;
- borrower;
- slide number / series / maker / subject;
- quantity;
- unit of issue: individual slide / numbered group / series / box / tray if recorded;
- date returned;
- duration;
- repeat borrowing;
- annotations, cancellations, missing/damaged entries;
- custodian/secretary initials;
- page/register numbering.

Priority diagnostic strings:
- Redmayne;
- Sharpus;
- Hughes;
- diatom / diatoms;
- Echinodermata;
- pathological / histological terms;
- any accession/cabinet numbers recovered from the minutes.

### Step D — crosswalk into `FZ/14/3/2` (1898)

First determine the catalogue's ontology before matching:
- sequential slide number?
- drawer/cabinet number?
- maker → subject ordering?
- taxonomic ordering?
- donor/provenance fields?
- series-level versus individual-slide entries?

Then match only with explicit or compound anchors:
- exact number;
- maker + subject;
- series + quantity;
- donor + subject;
- distinctive label wording.

Do not treat same taxon alone as object identity.

## 5. Crosswalk matrix to fill on site

| intake/event | date | donor/source | quantity | subject/series | internal number/address | loan register hit | borrower(s) | return/repeat | 1898 catalogue hit | confidence |
|---|---|---|---:|---|---|---|---|---|---|---|
| Sharpus via Hughes | 1880 | F. W. Sharpus / W. R. Hughes | 12 | Echinodermata | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN |
| Redmayne selection | summer 1881 | Mrs Redmayne / J. T. Redmayne collection | 72 | mixed | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN |
| additional diatoms | summer 1881 | OPEN | 48 | diatoms | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN |

## 6. Evidence grades

### Grade S candidate
Exact internal number or maker/subject combination appears in:
- 1880–81 accession/selection record;
- 1882–87 lending register;
- 1898 catalogue.

This would close:
`collection intake → temporary custody → return/repeated use → later catalogue persistence`.

### Grade A candidate
A slide/series appears in lending register + 1898 catalogue, but accession origin remains unresolved.

Useful for custody system, not for donor/provenance continuity.

### Grade B/context
Only subject family or maker recurs without stable number/compound identifier.

Do not claim same object.

## 7. What counts as success

Minimum publishable Bolton result:
The lending register demonstrates actual named borrower–preparation–return cycles from a Society collection already directly documented in 1881 as re-arranged and lent to members.

Strong result:
At least one diagnostic object/series can be traced from accession or selection through lending and into the 1898 catalogue.

Very strong result:
A transaction records non-return, damage, substitution, remounting, revised numbering or another intervention followed by continued catalogue identity.

The very strong result is not required for the project to work.

## 8. Consequence for the article

Bolton can now support an argument about **re-entry into collection order** rather than merely circulation outward.

The analytical sequence is:

`private/external material`
→ `institutional selection`
→ `cabinet re-arrangement`
→ `temporary member custody`
→ `return`
→ `catalogued persistence`.

The key question is not simply whether slides travelled. It is how a Society made them leave, return, and remain retrievable as collective scientific property.

## 9. Stop rule

Do not spend further web-search time looking for a hypothetical digitized 1898 catalogue unless a new exact identifier or scan appears.

The next major evidential upgrade requires the actual Bolton records. Prefield work is now sufficient to justify and structure the visit.