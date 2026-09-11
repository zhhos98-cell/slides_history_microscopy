# Iron Library / glass carriers — project router

> **PINNED RESUME POINT:** read `CURRENT_PROGRESS.md` first. It is the authoritative continuation state for the active Sheffield–Berlin / Wedding / Fischer line. Do not let unrelated repository work supersede it.

Started: 2026-09-11

This is a bounded satellite project inside `slides_history_microscopy`. It extends questions raised by **“Using Up Old Slides”: The Changing Affordances of Glass in British Microscopy, 1862–1883** into the Iron Library / Georg Fischer holdings without reopening the frozen 307/155 microscope-slide census.

## Governing question

The active problem is no longer simply a history of metallography or a search for a direct Britain → Germany transfer chain.

The controlled comparative sequence is:

**industrial travel / works comparison → travelling sample → external test / expert judgement → numbering / provenance / collection → prepared specimen → microscopic field → microphotography → printed / institutional reference system.**

The project asks how material comparison changed scale, evidential carrier, access regime, preparation practice and institutional setting while remaining a comparative activity.

## Current state

### Wedding

Hermann Wedding `Mss 23`, `Mss 24` and `Mss 25` are fully digitised on e-codices and have been downloaded locally at 900 px for rapid reading/indexing. `Mss 25` exposes 402 IIIF canvases.

A local OCR workflow has been specified to merge reading PDFs and OCR original JPGs with Tesseract-first / PaddleOCR-fallback, producing one provenance-rich JSON per manuscript. The JSON outputs are **not yet visible in this repository**, so completion must not be assumed.

A new historiographical hypothesis is being tested: Wedding's career and British travel are known, but the three handwritten notebooks may be substantially under-exploited at page level. This remains a hypothesis pending formal citation audit.

### Fischer

Three supplied machine-readable Fischer files represent two historical texts: duplicate/OCR witnesses of the 1845 journey plus the 1846 journey.

The corpus now supports controlled analysis of:

- comparison / `Autopsie`;
- quantitative works observation;
- access and technical credibility;
- travelling samples;
- Low Moor tapping samples + batch numbering;
- staged process series;
- Royal Mint external testing and reference-quality supply;
- provenance preservation/loss;
- skilled grinding/polishing as preparation for expert judgement;
- photography and negative-positive reproducibility;
- catalogue-numbered collection display at the Royal Polytechnic Institution;
- iterative travel/test/document/return circuits.

A dedicated negative-control search found **no positive textual evidence of microscopy in Fischer 1845–46**. Optical/photographic and industrial-finishing episodes are retained as pre-metallographic controls, not relabelled as microscopy.

### Sorby / Story-Maskelyne

The current comparison treats them as parallel material-to-microscopic-object regimes, not as an assumed direct transmission chain:

- **Sorby / Sheffield:** industrial material → preparation → polished/etched surface → reflected/direct illumination → microscopic field → photomicrograph;
- **Story-Maskelyne / British Museum mineralogy:** museum specimen / meteorite → prepared thin section → glass carrier → transmitted/polarised comparison → collection/classification.

Maskelyne's 1894 Royal Society referee report on Tutton's cutting/grinding/polishing instrument remains a strong preparation control.

### Berlin / Martens

The post-Wedding institutional comparison remains centred on the Königliche mechanisch-technische Versuchsanstalt / later Materialprüfungsamt, including specimen preparation, reflected-light microscopy, microphotography and separate specimen/image reference collections.

The three original Droste/Martens microphotographic glass plates remain the strongest object-dependent onsite lead.

## Project files

- `CURRENT_PROGRESS.md` — **authoritative current resume point**.
- `WEDDING_NOTEBOOK_CITATION_AUDIT.md` — controls the hypothesis that Mss 23–25 may be under-exploited at page level; includes citation-audit protocol and claim ceiling.
- `EXTERNAL_SOURCE_EXPANSION_2026-09-11.md` — controlled outward search/download queue generated from the Fischer texts: Faraday, Low Moor, Polytechnic, Croucher/Willats, Fischer 1851, Sorby, Maskelyne, Wedding and Martens.
- `FISCHER_1845_1846_EVENT_INDEX.tsv` — date-ordered event table.
- `FISCHER_KNOWLEDGE_BOUNDARY_MATRIX_1845_1846.tsv` — knowledge/access/boundary modes.
- `FISCHER_SAMPLE_AND_REFERENCE_REGIMES_1845_1846.md` — distinct sample/reference regimes.
- `FISCHER_ITERATIVE_TESTING_CIRCUIT_1845_1846.md` — repeated sample/test/document/return circuit.
- `FISCHER_TESTING_REGIME_1845_1846.md` — testing, batch sampling and provenance.
- `FISCHER_MEASUREMENT_AND_OBSERVATION_1845_1846.md` — autopsy, measurement and reliability.
- `FISCHER_KNOWLEDGE_EXCHANGE_AND_SECRECY_1845_1846.md` — publication, secrecy, patents, disclosure and reciprocal questioning.
- `FISCHER_ACCESS_NETWORK_1845_1846.md` — recommendation, credibility and tiered access.
- `FISCHER_1845_1846_NODE_INDEX.md` — broader synthesis.
- `SOURCE_MAP.md` — controlled external sources and claim ceilings for the original glass-carrier problem.
- `RESEARCH_STATE.md` — interpretation and bounded research queue.
- `EXACT_SOURCE_REQUEST.md` — staff-enquiry control for `G 745,1`, `Per765`, `A346` and the three original microphotographic plates.
- `RESIDENCY_TRIAGE_2026-09-11.md` — digitised-versus-onsite triage and historiographical ceiling.
- `PUBLIC_DIGITAL_CORPUS.md` — acquisition map for Wedding, Fischer, Droste/Martens, Sorby and Royal Society controls.
- `public_corpus/manifest.tsv` — machine-readable source/access policy table.
- `public_corpus/fetch_public_corpus.py` / `.ps1` — conservative local fetch helpers; raw downloads remain git-ignored.

## Immediate resume condition

If the three Wedding OCR JSON files are present, stop broad searching and index them first.

If they are absent, continue only the controlled source-acquisition/citation-audit queue in `EXTERNAL_SOURCE_EXPANSION_2026-09-11.md` and `WEDDING_NOTEBOOK_CITATION_AUDIT.md`.

Do not reopen generic Iron Library searching before the Wedding British itinerary/person/comparison index has been completed.

## Claim ceilings

Do not currently claim:

- Fischer 1845–46 practised microscopy;
- Sorby and Maskelyne formed a direct transmission chain;
- Wedding met Sorby in 1860/62;
- Mss 23–25 have never been read;
- shared glass substrate proves continuity;
- Low Moor batch samples are modern reference materials;
- analytical similarity establishes genealogy.

New external claims should enter a controlled project note with a stable source, explicit evidence level and claim ceiling before promotion into the article argument.
