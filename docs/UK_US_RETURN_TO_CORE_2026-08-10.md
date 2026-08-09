# UK/US return to core — research pause note

Date: 2026-08-10

Status: **PARKED FOR LATER READING**

## Decision

The global slide bibliography stops at **pass 17** for now: **197 verified entries, 86 research and 111 primary/object records, 19 publication languages**. The frozen surviving-object survey remains **307 discovery nodes / 155 strict nineteenth-century nodes, CLOSED_2026-08-09**.

No further global bibliography expansion is currently justified. The project’s research core is nineteenth-century British microscopy, with the United States used only as a bounded comparator where British journals, societies, commercial networks or surviving objects already create a direct connection.

A partially started South Asia / southern Africa pass exists on an unmerged branch but is **not part of `main` and should not be merged as the next step**. If the project is resumed, begin from the UK/US priorities below rather than continuing that geographic sweep.

## What the GitHub layer adds to the existing corpus

The main historical corpus is already strong on discourse and events: journals, advertisements, society proceedings, catalogues, correspondence, technical instructions and exchange notices. The GitHub work adds a different class of evidence: surviving labels, series numbers, cabinet positions, accession histories, cards, object catalogues and present custody.

The productive relationship is therefore:

**historical corpus = what actors said/did**

**GitHub object layer = what survived and how it is now addressable**

GitHub should function as a reverse index into the historical corpus. Modern museum prose is evidence about surviving objects, not nineteenth-century corpus text.

## Five gains from the crosswalk

### 1. Addressability

A microscope slide can accumulate successive addresses: standardized glass geometry and finder coordinates, maker labels, catalogue/series numbers, cabinet positions, society inventories, later institutional accessions and modern database identifiers. The research problem is therefore not only standardization but **re-addressing and retrieval across time**.

### 2. The circulating object was often larger than the slide

Postal Microscopical Society circuits linked physical slides to manuscript books, notes, drawings, packing rules, postage, damage liability and valuation. A useful unit of analysis is therefore the **slide-plus-documentation-plus-logistics system**, not the slide in isolation.

### 3. Commercial preparations could be reused epistemically

Named preparations by makers such as John Thomas Norman were later used as test/reference objects for judging optical performance. Commercial identity and preparation quality could stabilize a specimen sufficiently for reuse in instrument comparison.

### 4. Elcock now has an unusually complete production-to-survival chain

The combined corpus/object evidence can connect Charles Elcock to field collection, washing and separation, mounting media, Postal Microscopical Society circulation and note-making, advertised Foraminifera Type Slides, prices, retailers and the surviving Whipple workshop archive. This is substantially stronger than a maker biography or trade list alone.

### 5. “Material publication” can now be defined narrowly

Cole’s synchronized preparation + text + plate issue system, Elcock’s commercial comparative Type Slide, replicated published sets, ordinary catalogue offerings and anatomical serial sections are different forms. Numbering, circulation or seriality alone does not make a physical preparation a publication.

See `data/analysis/material_slide_publication_forms_v2.json` for the stricter taxonomy.

## Future corpus expansion — ranked

1. **Arthur C. Cole, _Studies in Microscopical Science_, vols. I–II.** This is the clearest next corpus task because the local source already exists (`studiesinmicrosc01cole_djvu.zip`). Ingest the full preparation-by-preparation text, issue order, methods, materials and preparation/text/plate synchronization. Preserve the different source-level attributions to A. C. Cole and Martin J. Cole instead of reconciling them in advance.

2. **_Microscopical News and Northern Microscopist_ IV (1884).** Recover and ingest the whole volume, not only the known Charles Collins Jr. “Fish Scales” notice at p. 109. The surrounding trade and regional material may matter more than a single targeted extract.

3. **H. L. Smith, _Diatomacearum Species Typicae_, Century III.** Recover only the located 1878 _American Journal of Microscopy and Popular Science_ article/pages. Do not use this as a reason to build a broad American microscopy corpus.

4. **Frederic Kitton, Norfolk Diatoms Series III–IV.** Series I–II are already textually grounded while surviving set evidence indicates I–IV / nos. 1–100. Contemporary prospectuses/notices for III–IV would efficiently complete the series architecture.

5. **John Thomas Norman 1872 catalogue + St Andrews labels.** Crosswalk catalogue wording to surviving labels and then to UK corpus reuse, including the use of Norman preparations as objective-test objects.

6. **Andrew Pritchard 1837 catalogue + Whipple cabinet.** Locate the original catalogue and compare advertised categories/prices to surviving Pritchard-labelled commercial mounts, homemade preparations, broken slides and cabinet structure.

Machine-readable priorities are in `data/analysis/uk_us_object_to_corpus_expansion_v1.json`.

## Keep as object metadata rather than corpus text

Whipple Elcock labels/raw packets/tools; Oxford RMS cabinet indexes; Quekett cabinet records; Farlow set-level records; Harvard Embryological Collection cards; Bailey/Boston accession evidence; and the Oscar W. Richards Smithsonian archive should be used as reverse-index evidence. They should not be bulk-ingested into the nineteenth-century historical text corpus.

For the US, the working rule is **British connection first**. H. L. Smith/Farlow, Minot/Harvard and Bailey/Boston are useful because British sources already connect to them. Oscar Richards is best treated as a retrospective bibliography/trade-literature finding aid.

## Stop rules while parked

- no further geographic bibliography expansion for completeness;
- no general-purpose global crawling;
- no broad US microscopy harvest;
- no bulk ingestion of modern museum prose into the nineteenth-century corpus;
- no new medium domain such as geological thin sections without a separate scope decision;
- no substantial source-acquisition time until microscopy becomes an active reading/writing project.

## Resume point

When the project is actively resumed, **start by reading and structuring Cole**, not by discovering more collections.
