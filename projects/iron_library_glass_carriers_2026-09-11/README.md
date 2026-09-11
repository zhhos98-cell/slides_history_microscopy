# Iron Library / glass carriers — project router

Started: 2026-09-11

This is a bounded satellite project inside `slides_history_microscopy`. It extends questions raised by **“Using Up Old Slides”: The Changing Affordances of Glass in British Microscopy, 1862–1883** into the Iron Library / Georg Fischer holdings without reopening the frozen 307/155 microscope-slide census.

## Governing question

The parent paper asks what used microscope-slide glass could still be made to do: clean, remount, revarnish, cut, repurpose, pack and circulate. This project follows a neighboring but distinct material problem: **what work was assigned to glass when microscopic observation became a photographic and industrial-material-testing record?**

The first secure Iron Library case is not a nineteenth-century biological specimen slide. Bernhard Droste records donating **three original glass plates carrying early microphotographic images from the Königliche mechanisch-technische Versuchsanstalt zu Berlin**. In the same discussion he connects Adolf Martens's microscopic study of metals, Martens's work with Carl Zeiss on reflected-light microscopy, microstructure images shown at Chicago in 1893, the Berlin testing institute's published results, and Emil Heyn's later metallography. The three plates therefore open a bounded comparison between a microscope preparation as a support for a specimen and a photographic glass plate as a support for a microscopic image.

The Georg Fischer corporate archive supplies a second, later control corpus. `GFA 25 :: Werk Singen, Glasplatten` contains photographs on glass plates from 1900–1960, including a laboratory class `GFA 25/LAB` (1931–1953). These are photographic negatives/plates, **not microscope specimen slides unless an item record independently says so**. Their value is comparative: they preserve a glass-carrier workflow with archival addresses, subject classes and later digitisation.

## Current state

The original glass-carrier problem has moved from broad discovery to **exact-source closure**, but the project has now reopened a second, explicitly bounded layer: **residency / digitisation triage**.

Secure at present:

- Droste states that he donated three original early microphotographic glass plates to the Iron Library.
- Droste figure 2 shows those plates and its image credit is `Foto: Eisenbibliothek, G 745,1`; this is a secure published association but not yet a secure statement that `G 745,1` is the physical accession number.
- Droste's image credits also associate Martens's 1891 article with `Per765`; the catalogue meaning of that identifier remains open.
- the 1893 source route is now exact: *Mitteilungen*, Band 11 (1893), plus SLUB's separately catalogued `Atlas: 10/11.1892/93`.
- the 1904 Materialprüfungsamt account describes characteristic polished specimens stored in zinc-sheet desiccators and, separately, cabinets holding more than 3,600 microphotographs. This is a later first-order case in which specimen and image enter different collection systems.
- the GF corporate archive has a separately catalogued Singen glass-plate fonds, `GFA 25`, and a laboratory subclass `GFA 25/LAB`.
- `GFA 1/141.37`, titled `Siegelabdrücke und Dias` (1852–1906), exists as a twelve-object archival item, but the word `Dias` is not yet enough to identify format, use or relation to microscopy.
- Hermann Wedding's Iron Library manuscripts `Mss 23`, `Mss 24` and `Mss 25` are already fully digitised on e-codices with public IIIF manifests. They are therefore pre-visit corpora, not a residency rationale by themselves.
- Johann Conrad Fischer's travel journals are already available through the Iron Library's 2023 digital edition, based on digitised e-rara reference copies. The Sheffield/British-metallurgy material is likewise a remote baseline.
- the broad Sorby–Wedding–Martens history of metallography and the 1885 specimen-preparation/illumination dispute are already historiographically visible. Novelty cannot rest on rediscovering that chain.
- a stronger question has emerged around **observational regimes across scale and media**: industrial travel/workshop comparison → prepared specimen → polished surface → reflected-light microscopy → microphotographic glass plate → printed plate → reference/archive.

Still open:

- what `G 745,1`, `Per765` and `A346` denote in the Iron Library's catalogue/image system;
- individual current signatures/accession numbers for the three Droste plates;
- dates, dimensions, photographic process, inscriptions, subjects and publication matches for each plate;
- direct inspection of Martens's 1891/1893 Tafeln, especially 1893 Tafeln VII–XIII;
- whether any `GFA 25/LAB` item is itself a micrograph or records microscopic/material-testing practice;
- what the `Dias` in `GFA 1/141.37` physically are;
- which nineteenth-century GFA working-paper/correspondence series remain genuinely undigitised after item-level ANTON checking;
- whether the unresolved onsite corpus is thick enough to require a residency rather than a small reproduction request;
- any direct historical transfer, formal continuity or reuse relation between British specimen-slide glass and these metallographic / photographic glass plates.

Do **not** infer such continuity from a shared glass substrate alone.

## Project files

- `SOURCE_MAP.md` — controlled external sources, locators, evidence level and claim ceilings for the original glass-carrier problem.
- `RESEARCH_STATE.md` — current interpretation, relation to the parent slide project, bounded search queue and stop condition.
- `EXACT_SOURCE_REQUEST.md` — ready-to-use staff-enquiry control for `G 745,1`, `Per765`, `A346` and the three original microphotographic plates; not yet sent.
- `RESIDENCY_TRIAGE_2026-09-11.md` — digitised-versus-onsite triage, historiographical ceiling, Sheffield/person-network hypotheses, Story-Maskelyne/Percy/Tutton leads, and the revised observational-regime question.
- `PUBLIC_DIGITAL_CORPUS.md` — acquisition map for Wedding, Fischer, Droste/Martens, Sorby and Royal Society controls.
- `public_corpus/manifest.tsv` — machine-readable source/access policy table.
- `public_corpus/fetch_public_corpus.py` — conservative local fetch helper for IIIF manifests and optional raw research files; raw downloads are git-ignored.

These files are project-local authorities only. They do not alter `REPOSITORY_STATE.json`, `CURRENT_DIRECTION.md`, the frozen 155-node survey, or the core bibliography.

## Resume condition

Two tracks now coexist:

1. **glass-carrier exact-source closure** remains parked until a staff reply resolves local identifiers, the Martens plate sequences become inspectable, an item-level `GFA 25/LAB` microscopy record appears, or `GFA 1/141.37` is physically resolved;
2. **residency/digitisation triage** is active and should proceed by exhausting remote Wedding/Fischer material first, then identifying a demonstrably undigitised, physically specific onsite corpus.

A residency application is warranted only when the remaining material is both holdings-specific and too thick/materially dependent to replace with a few digital reproductions.

## External research rule

New external claims should enter a controlled project note with a stable source, explicit evidence level and claim ceiling before they are promoted into article argument. A catalogue keyword, OCR hit, shared material term or mere co-presence is a routing signal, not a historical relation.
