# WMC periodical title ledger v1

**Date:** 2026-09-09  
**Branch:** `research/working-mens-microscopy-19c`  
**Purpose:** exact-title / run control for the periodical-first RSVP/WMC research line. This file complements `WMC_PERIODICAL_CORPUS_INDEX_V1.md` and should be updated whenever a title, run, issue, reprint relation, or material state is closed.

## 1. London Working Men's College

### The Working Men's College Magazine

**State:** `CLOSED_BIBLIOGRAPHIC`, run boundary still requires issue-level control.

Current controls:

- Open Library records *The Working Men's College Magazine*, Working Men's College (London), published by Macmillan & Co., beginning 1859; monthly; indexed; digital reproduction from the Goldsmiths' Library copy.
- A contemporary 1861 *Atlantic Monthly* visitor explicitly reports that the College published a monthly *Working-Men's College Magazine*, describes it as devoted to College interests, and says he bought the annual volume and used it to read up on the College.
- Contemporary periodical-list evidence records no. 9 in October 1859.
- J. F. C. Harrison's history quotes the *Working Men's College Magazine* for January 1862, proving survival into 1862.

**Controlled formulation:** active from 1859 and still extant in January 1862. Do not yet hard-code a terminal month/issue without complete issue-level bibliographic inspection.

**Research value:** this is now the primary institutional serial for the RSVP project, not a generic report series.

Immediate extraction fields:

`issue/date | editor/contributor | genre | class/lecture | science/natural history | microscopy | museum | club | advertisement | notice | reprint | correspondence | wrapper/supplement | external reference`

**Physical-inspection priority:** very high. Need to determine whether bound digital copies preserve original wrappers, advertisements, supplements, issue boundaries, and inserted matter.

Sources:
- https://openlibrary.org/works/OL32291568W/The_working_men%27s_college_magazine
- https://www.gutenberg.org/cache/epub/11154/pg11154-images.html
- NCSE / contemporary periodical-list evidence for no. 9 (1859)
- J. F. C. Harrison, *A History of the Working Men's College, 1854–1954* (quotation from January 1862 issue)

### The Working Men's College Journal

**State:** `CLOSED_BIBLIOGRAPHIC` for later existence; start date/run not yet closed.

WorldCat records *The Working Men's College Journal* as a London Working Men's College periodical, publisher Working Men's College, date displayed as `189u`. Google/Play Books preserves later volumes, including vol. 10 in 1907, described as "conducted by members of the Working Men's College, London."

**Interpretive boundary:** do not assume continuity from the 1859–62 *Magazine* into the later *Journal* until title-history / restart evidence is inspected.

**RSVP relevance:** useful as a later comparison for institutional self-publication and member authorship, but secondary to the 1859–62 Magazine for the current pilot.

Sources:
- https://search.worldcat.org/title/173716279
- Google Books / Google Play Books, *The Working Men's College Journal*, vol. 10 (1907)

## 2. Sheffield People's College

### The People's College Journal

**State:** `CLOSED_BIBLIOGRAPHIC_ARCHIVE`, partial issue survival directly identified.

University of Sheffield Special Collections and Archives, collection 10, item `10/2/7`, preserves two issues:

- No. 2 — December 1846;
- No. 3 — January 1847.

The archival description identifies the title as *The People's College Journal* and describes it as a **monthly periodical chiefly devoted to the cause of popular education**, edited by Rev. R. S. Bayley, F.S.A. The collection-level description states that issues also survive in Sheffield City Library.

The *Dictionary of National Biography* entry for Robert Slater Bayley independently states that Bayley started the monthly *People's College Journal* in 1846, that it was printed at the College, intended to advance popular education, and ended in May 1847.

**Controlled run formulation:** begun 1846; monthly; still active January 1847; DNB gives termination in May 1847. Full issue census still needed.

**Research value:** strongest provincial institutional-serial control against London WMC, and chronologically earlier than the London College itself.

Immediate extraction questions:

- how much of each issue is written by teachers vs students;
- recurring genres (editorial, lecture abstract, science/natural history, correspondence, poetry, institutional news);
- whether science classes or natural-history activity become serial content;
- whether contributors recur in later Sheffield learned/microscopical networks;
- whether advertisements/wrappers survive in City Library or archive copies;
- whether the journal was exchanged with other mechanics'/people's colleges.

Sources:
- https://archives.shef.ac.uk/repositories/3/archival_objects/26999
- https://archives.shef.ac.uk/repositories/3/resources/386
- DNB, `Bayley, Robert S.`

## 3. Haley Hill Working Men's College / Literary and Scientific Society, Halifax

### Manuscript magazine -> The Circulator

**State:** `CLOSED_BIBLIOGRAPHIC_SECONDARY`, primary issue-level/content control still pending.

A Halifax bibliographical history states that Haley Hill Working Men's College fostered a scientific society c.1860, circulated a **manuscript magazine** until 1866, and then began printing **The Circulator** in 1866 at 2d. per number through R. Leyland and Son; it reportedly lasted two years.

A surviving bibliographical catalogue supplies the fuller printed identity:

> *The Circulator. A magazine of literature, Science & Art. Conducted by members of the Haley Hill Literary and Scientific Society, 1866–7. Halifax: R. Leyland & Son.*

The same catalogue notes a wide content range including local mollusks, geology, natural history, science, literature and dialect writing. A separate biographical reconstruction of geologist James Spencer states that he contributed a sequence of geological papers to the twopenny monthly, including `Popular Geology`, Halifax strata, Low Moor coal pits, and Ingleborough.

**Important transition:** handwritten serial -> printed periodical. This is not merely a title-history curiosity; it gives a direct case for asking what changed when an internal manuscript circulation system became cheap print.

**Controlled formulation:** manuscript magazine before 1866; printed *Circulator* begins 1866; secondary bibliographic evidence gives 1866–67 and a two-year life. Primary issue census remains necessary.

Research questions:
- who copied/read the manuscript magazine;
- whether the printed *Circulator* retained contributors/genres from the manuscript phase;
- how the Literary and Scientific Society related administratively to the Working Men's College;
- science / natural-history / museum content;
- distribution beyond the College;
- local press notices/reprints;
- price, wrapper, advertisement, and issue structure;
- whether geological/natural-history pieces generated excursions, specimen exchange, or later specialist publication.

Sources:
- *Halifax Books and Authors* (digitised historical bibliography), passage on Haley Hill Working Men's College and *The Circulator*;
- Jarndyce, *Periodicals* catalogue, item 220;
- https://microscopist.net/SpencerJ.html
- https://calderdalecompanion.co.uk/s70_h.html

## 4. South London Working Men's College

### Periodical interface rather than confirmed house journal

**State:** `PERIODICAL_INTERFACE_CLOSED`; internal title unresolved.

Known metropolitan print chain:

- T. H. Huxley's address to the South London Working Men's College, 4 January 1868, was subsequently published in *Macmillan's Magazine* as `A Liberal Education; and Where to Find It`.
- William Rossiter, writing as Hon. Sec. of the South London Working Men's College, published `Working Men's Colleges` in *Nature*, 13 October 1870, explicitly comparing/defending the Great Ormond Street and South London colleges.

This creates a controlled chain:

`college event / institutional position -> metropolitan periodical publication -> wider educational/scientific public`

**Open task:** determine whether South London WMC produced its own serial, newsletter, report series, or recurring printed programme before treating it as an institutional-periodical node equivalent to London/Sheffield/Halifax.

Sources:
- https://www.nature.com/articles/002475a0
- Huxley, *Lay Sermons, Addresses and Reviews* / later *Science and Education* bibliographical note on the 1868 address and *Macmillan's Magazine* publication.

## 5. Cambridge Working Men's College

### Internal serial title unresolved

**State:** `TITLE_PENDING`.

Current evidence establishes the College and its teaching network but not a confirmed house periodical title.

Search targets:
- prospectuses;
- annual reports;
- recurring printed class lists/programmes;
- Cambridge local press notices;
- Macmillan family papers;
- any member manuscript/printed magazine analogous to London or Halifax.

Do not infer a Cambridge title from the London model.

## 6. Specialist-periodical bridge cases already in scope

### Hackney Working Men's Institute -> Quarterly Journal of Microscopical Science, 1866

**State:** `INDEXED_NOT_READ` for the destination communication; upstream event `CLOSED_PRIMARY_INDEXED`.

QJMS proceedings report that the President read a communication received by the Microscopical Society committee from the Committee of Hackney Working Men's Institute and directs the reader to p.194.

**Do not infer content yet.** The communication may concern access, lecture activity, instruments, cooperation, or another matter; the p.194 text remains the closure target.

This is a high-value example of an adult-education institution entering specialist microscopical print through a society communication.

### Hardwicke's Science-Gossip

**State:** `CORE_CIRCULATION_TITLE`.

Existing repo work already demonstrates exchange notices tied to slides/specimens and later specialist-journal reuse. Keep as principal title for reconstructing reader-to-reader material circulation.

### Monthly Microscopical Journal / Journal of the Royal Microscopical Society

**State:** `CORE_SPECIALIST_RELAY`.

Use as downstream records of society meetings, objects, methods, exchanges, bibliographical recoding, and provincial-to-metropolitan transfer.

## 7. Periodical-first immediate queue

1. Build issue-level census of *The Working Men's College Magazine* from 1859 through at least January 1862.
2. Establish whether the later *Working Men's College Journal* is a revival, successor, or independent restart.
3. Reconstruct *The People's College Journal* issue sequence from 1846 to May 1847 and locate Sheffield City Library copies.
4. Find physical/digital copies of Haley Hill manuscript magazine / *The Circulator* and close exact run/content.
5. Close QJMS 1866 p.194 Hackney communication.
6. Search Cambridge and South London for institutional serial titles without assuming they existed.
7. Record every transition among `internal manuscript -> printed serial -> local newspaper -> specialist journal -> metropolitan general-science periodical`.

## 8. RSVP-funded delta marker

The grant-funded trip should prioritize evidence that cannot be safely reconstructed from bound digital text alone:

- wrappers;
- covers;
- advertisements;
- supplements;
- inserted catalogues;
- issue sequence;
- binding/rebinding;
- missing issues;
- marginal ownership/use traces;
- short-run/internal serials absent from standard catalogue title searches.

The project should therefore distinguish `bibliographic title closure` from `material serial closure` throughout.