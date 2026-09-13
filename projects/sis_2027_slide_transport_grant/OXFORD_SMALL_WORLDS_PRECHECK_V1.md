# Oxford Small Worlds pre-crosswalk v1

Updated: 2026-09-13
Status: PUBLIC-DATABASE PRECHECK / ITEM CROSSWALK REMAINS OPEN

## 1. What is publicly closed

The History of Science Museum's legacy `Small Worlds` microscopical-specimen database remains accessible.

Official database introduction states:
- 10,084 catalogue records;
- 1,955 images;
- hierarchy of 227 containers → 513 drawers → 4,293 slides → 5,051 specimens;
- text-based search can be run against Containers, Drawers, Slides, Specimens, or all levels;
- substring search is supported and `%` acts as a wildcard.

Official routes:
- `https://www.mhs.ox.ac.uk/smallworlds/database/index.html`
- `https://www.mhs.ox.ac.uk/smallworlds/database/search.html`

The main repository already establishes at collection level that Oxford preserves about ten thousand microscope slides and that more than three-quarters are in one cabinet on permanent loan from the Royal Microscopical Society, with RMS-related manuscript/archive material held in the same museum.

## 2. Historical event selected for pre-crosswalk

9 June 1880, Royal Microscopical Society:
- twelve slides from the Zoological Station at Naples;
- donated/sent through A. W. Waters;
- received by RMS;
- Mr Crisp called attention to them and they were exhibited under microscopes;
- JRMS names all twelve physical slides.

Repository authority:
`data/analysis/slide_155_corpus_expansion_v1/NAPLES_1880_RMS_12_SLIDES_ITEM_CROSSWALK_V1.csv`.

Diagnostic labels include:
- *Amphioxus lanceolatus*;
- *Ascetta bianca*;
- *Asterias/Asteracanthion glacialis* — gastrula / larva / mesoderm formation;
- *Echinocardium cordatum* — larva;
- *Pyrosoma elegans* — young colony;
- *Pseudodidemnum listerianum* — ova with embryo;
- *Toxopneustes brevispinosus* — larvae, 3rd / 5th / 15th day;
- *Stichopus regalis* — ovary.

The Naples commercial catalogue crosswalk has nine exact/strong catalogue-offering matches and three bounded matches. This closes the shipment against the Naples offering catalogue, not against surviving Oxford objects.

## 3. Public web precheck result

Targeted public/search-engine queries for the distinctive Naples taxa and the Small Worlds domain did not recover a diagnostic surviving object page.

This result is **not** evidence of non-survival.

Reasons the negative result cannot be promoted:
- search-engine indexing of the legacy database is incomplete;
- the database may preserve historical labels using different spelling, synonymy or abbreviated text;
- catalogue records may sit at specimen rather than slide level;
- the twelve RMS preparations may have changed cabinet/catalogue addresses;
- not every Small Worlds record is necessarily part of the RMS cabinet.

## 4. Research consequence

The historical-event → surviving-object crosswalk remains a genuine archival task.

Priority sequence at Oxford:
1. use Box 31 / Box 38 around 9 June 1880 to confirm internal custody/status of the Naples twelve;
2. test Box 49 (1897 slide register) for Naples / Waters / Crisp / diagnostic taxa / older slide numbers;
3. test Box 103 Donations catalogue if the event is classified as a permanent gift;
4. use historical catalogues MS 5 / MS 13 / MS 18 only where subject scope is compatible;
5. record historical numbers/labels/subjects;
6. then search/ask HSM staff to map diagnostic historical entries into the cabinet / Small Worlds or successor catalogue.

## 5. Other event hooks

If the Naples series does not crosswalk, use lower-complexity diagnostic gifts:
- 13 June 1883 — Charles Coppock, five donated slides including an Eozoon section and pathological lung preparations;
- March 1884 — J. Norman jun., two slides of sticklebacks;
- 12 January 1870 — Rev. T. H. Browne, box of twelve sections of bone.

These may offer stronger maker/donor labels than the Naples taxonomic series.

## 6. Capture fields for any successful crosswalk

Historical side:
- public event date;
- donor/sender/intermediary;
- exact historical wording (`presented`, `received`, `exhibited`, `donated`);
- historical subject/taxon;
- historical number/catalogue address;
- internal minute/council status;
- register/catalogue entry.

Modern/object side:
- HSM inventory/container number;
- drawer ID;
- slide ID;
- specimen ID;
- full label transcription;
- image availability;
- maker/preparer attribution;
- current classification;
- evidence supporting or rejecting same-object identity.

## 7. Claim ceiling

Until a diagnostic historical entry and a surviving object converge independently, state only:

`Oxford preserves the RMS collection architecture and the archival/catalogue layers needed to test item continuity.`

Do not state:
`the 1880 Naples slides survive at Oxford`.

A failed crosswalk remains informative about collection transformation, but it is not evidence that the objects were lost without additional archival support.