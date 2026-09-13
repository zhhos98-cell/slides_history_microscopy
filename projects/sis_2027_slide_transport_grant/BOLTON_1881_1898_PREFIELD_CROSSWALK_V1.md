# Bolton 1881 → 1898 pre-field crosswalk v3

Updated: 2026-09-13
Status: DIRECT 1881 PRIMARY-INDEX CONTROL / SHARPUS-BIRMINGHAM CONFLATION CORRECTED / 1898 CONTENT NOT YET DIGITALLY CONTROLLED

## 1. Problem

Bolton has a strong institutional sequence but the crucial identity crosswalk depends on records not yet directly inspected:

`1880–81 Redmayne display / 1881 collection transformation`
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

This is primary-period indexed control of the whole chain rather than reliance on a later biographical paraphrase.

Source:
*The Northern Microscopist* 1 (1881), p. 167, `Notices of Meetings — Bolton Microscopical Society`; Internet Archive identifier `microscopicalnew01davi` / indexed public scan.

The current web interface has not yielded a stable page-image screenshot because the full-volume PDF exceeds the fetch limit. Treat the wording as direct OCR/indexed-periodical control; inspect the page image before using a long quotation in publication.

## 3. Correction: remove Sharpus from Bolton

An earlier version used an 1880 F. W. Sharpus / W. R. Hughes Echinodermata donation as a Bolton intake anchor.

That was a source conflation. Contemporary reports and the Sharpus source history place these donations in the **Birmingham Natural History and Microscopical Society**, where Sharpus was a corresponding member and Hughes acted as presenter/intermediary.

Therefore:
- `Sharpus / Hughes / Echinodermata` is deleted from the Bolton crosswalk;
- it must not be searched as a Bolton accession series unless a separate Bolton-specific source emerges;
- the Bolton pre-field sequence begins with Redmayne's death/display in 1880 and the directly controlled 1881 cabinet transformation.

## 4. Controlled 1880–81 Bolton anchors

### Redmayne posthumous display, Nov 1880

Contemporary reporting of the Society's 19 Nov 1880 Conversazione describes Redmayne's microscopes, photomicrographs, pathological preparations and rare diatoms on display after his death.

Crosswalk question:
Were these objects temporarily held for display, and when did any part of the estate move into Society custody?

### Forty-eight diatom slides, Mar/summer 1881

The 11 Mar 1881 meeting report records the Society's decision to augment the Cabinet with **48 choice diatom slides**. The summer notice confirms forty-eight choice diatom slides had been added while the collection was being re-arranged.

Current donor/source: OPEN.

Crosswalk target:
`48 / diatom(s) / March–summer 1881 / cabinet addition`.

Keep this separate from the 72 Redmayne slides unless internal records explicitly connect them.

### Redmayne selection, summer 1881

The summer notice directly establishes:
- Mrs Redmayne placed the whole collection in the hands of the Society President and Secretary for selection;
- **six dozen = 72 choice slides** were selected/given to the Society;
- the Society collection was being **re-arranged**;
- Society slides were **lent to members**.

Crosswalk target:
`Redmayne / 72 selected slides / diagnostic maker-subject labels recovered from minutes/register/catalogue`.

Do not assume every Redmayne-labelled slide in later records belonged to the selected 72 unless the accession/minutes establish it.

## 5. Exact field sequence

### Step A — accession and custody language in minutes

Use late `FZ/14/1/1` and early `FZ/14/1/2` to extract:
- exact dates;
- Redmayne estate/display/custody language;
- donor/source of the 48 diatom slides;
- wording: presented / selected / accepted / purchased / added / arranged;
- any assigned slide/cabinet numbers;
- names of President and Secretary acting on the Redmayne collection;
- whether unselected material was returned;
- cabinet/tray/box references;
- resolutions about lending.

Do not automatically project the Nov 1880 President/Secretary onto summer 1881 without checking the election cycle.

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
- diatom / diatoms;
- pathological / histological terms;
- any accession/cabinet numbers recovered from minutes.

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

## 6. Crosswalk matrix to fill on site

| intake/event | date | donor/source | quantity | subject/series | internal number/address | loan register hit | borrower(s) | return/repeat | 1898 catalogue hit | confidence |
|---|---|---|---:|---|---|---|---|---|---|---|
| Redmayne posthumous display | 19 Nov 1880 | Redmayne estate / custody OPEN | mixed | microscopes + preparations + diatoms + photomicrographs | OPEN | n/a until ownership established | n/a | n/a | OPEN | OPEN |
| additional diatoms | Mar–summer 1881 | OPEN | 48 | diatoms | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN |
| Redmayne selection | summer 1881 | Mrs Redmayne / J. T. Redmayne collection | 72 | mixed | OPEN | OPEN | OPEN | OPEN | OPEN | OPEN |

## 7. Evidence grades

### Grade S candidate
Exact internal number or maker/subject combination appears in:
- 1880–81 accession/selection record;
- 1882–87 lending register;
- 1898 catalogue.

This would close:
`collection intake → temporary custody → return/repeated use → later catalogue persistence`.

### Grade A candidate
A slide/series appears in lending register + 1898 catalogue, but accession origin remains unresolved.

Useful for custody system, not donor/provenance continuity.

### Grade B/context
Only subject family or maker recurs without stable number/compound identifier.

Do not claim same object.

## 8. What counts as success

Minimum publishable Bolton result:
The lending register demonstrates actual named borrower–preparation–return cycles from a Society collection already directly documented in 1881 as re-arranged and lent to members.

Strong result:
At least one diagnostic object/series can be traced from accession or selection through lending and into the 1898 catalogue.

Very strong result:
A transaction records non-return, damage, substitution, remounting, revised numbering or another intervention followed by continued catalogue identity.

The very strong result is not required for the project to work.

## 9. Consequence for the article

Bolton can support an argument about **re-entry into collection order** rather than merely circulation outward.

The analytical sequence is:

`private/new material`
→ `institutional selection`
→ `cabinet re-arrangement`
→ `temporary member custody`
→ `return`
→ `catalogued persistence`.

The key question is not simply whether slides travelled. It is how a Society made them leave, return, and remain retrievable as collective scientific property.

## 10. Stop rule

Do not spend further web-search time looking for a hypothetical digitized 1898 catalogue unless a new exact identifier or scan appears.

The next major evidential upgrade requires the actual Bolton records. Prefield work is now sufficient to justify and structure the visit.