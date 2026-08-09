# P1 source target 3 — Naples microscope-slide price catalogue

Date: 2026-08-09

Object node: `UK-STANDREWS-NAPOLI-FRITZ-MEYER-SLIDES-1881`

## Outcome

The target is now parsed at catalogue-entry level from the uploaded Internet Archive DJVU text and has produced the first item-level catalogue-to-Britain crosswalk.

Primary source:

Anton Dohrn, `Preis-Verzeichnis der durch die Zoologische Station zu beziehenden mikroskopischen Präparate`, *Mittheilungen aus der Zoologischen Station zu Neapel*, Bd. 2, pp. 238-253.

The source itself is signed **`Neapel, August 1880`**. The surrounding volume/publication context is 1880-1881; for corpus work this derived extraction is therefore labelled **Naples 1880** while retaining the published volume context.

Biodiversity Heritage Library item: `37442`

- Item: https://www.biodiversitylibrary.org/item/37442
- Internet Archive identifier: `mittheilungenaus02staz`
- BHL copyright status: `NOT_IN_COPYRIGHT`

## What the uploaded primary text closes

The catalogue is much richer than the object-side summary alone suggested.

### Catalogue structure

- introductory/programmatic section: pp. 238-241;
- numbered catalogue: **1-423** on pp. **242-253**;
- therefore `423` is exactly the historical catalogue-offering namespace;
- it is not a surviving-slide count and not a current institutional total.

The historical major-group distribution of the 423 numbered offerings is:

- Protozoa: 4;
- Coelenterata: 33;
- Echinodermata: 49;
- Vermes: 33;
- Arthropoda: 57;
- `Mollusca` in the catalogue's historical classification, including Tunicata: 54;
- Vertebrata: **193**.

The vertebrate component is therefore 45.6% of the numbered catalogue. Within it are 61 Pisces, 12 Amphibia, 4 Reptilia, 65 Aves, 33 Mammalia, and 18 Homo entries. The catalogue is consequently not simply a marine-zoology slide list: it is also a large teaching/embryology/histology offer.

### Material and commercial specification

The introductory pages state explicitly:

- slide format: the `English` format, **70 x 28 mm**;
- labels (`Etiquetten`) also function as protective strips;
- most preparations are stained with carmine or other durable stains;
- they are mounted in Canada balsam, dried, then sealed with a thin layer of masking varnish;
- prices are in **gold francs**;
- price formation is tied to material rarity and to the difficulty/labour of preparation.

These statements belong to the catalogue as a whole. They must not be silently converted into row-level claims where the numbered entry itself specifies a different treatment.

### Scientific-commercial programme

Dohrn explicitly contrasts the Station's project with ordinary slides available `für Geld`. He argues that preparations have scientific value only when technical skill is combined with understanding of scientific problems and viewpoints. The intended functions include collections, demonstrations, academic teaching, comparative-anatomical work, embryology, and the provision of comparison objects that individual investigators would otherwise find difficult to obtain.

The catalogue is explicitly called **provisional**. Dohrn says a larger and more systematically divided catalogue was intended once stocks allowed it.

Although the Station's programme was principally marine, the catalogue deliberately abandons an exclusively marine scope when useful terrestrial and especially embryological material became available. This explains the heavy vertebrate and avian-embryology sections.

## Fritz Meyer attribution rule

The introduction says that Dohrn invited **Fritz Meyer** of Leipzig, whose technical-scientific competence was highly regarded, to direct the new department for microscope preparations, and that Meyer had begun setting it up about a year and a half earlier.

This supports:

`department led/organized by Fritz Meyer`

It does **not** support:

`all 423 entries prepared by Fritz Meyer`.

Individual preparer attribution remains open unless another source closes it. The existing St Andrews statement that most surviving examples appear to have been mounted by Meyer is an object-side claim about that surviving subset and remains separate.

## Object -> text chain now closed

1. JRMS 1880 p.700 reports Naples slides sent to Britain through A. W. Waters and says a Fritz Meyer-managed department had begun large-scale preparation, with a list forthcoming.
2. The source signed August 1880 is that priced catalogue programme: 423 numbered offerings, standardized slide format, treatment/mounting conventions, gold-franc prices, and explicit teaching/research rationale.
3. Quekett proceedings 1882 p.194 record chick-embryo specimens explicitly prepared by Fritz Meyer in British club use.
4. Surviving St Andrews slides provide the present object-side endpoint.

Historical chain at programme level:

`preparation department -> standardized priced catalogue -> distribution/British use -> surviving institutional objects`.

## Extraction status

A V1 machine-readable extraction now contains **423 sequential catalogue rows** with printed page, historical group/subgroup, cleaned entry text, analytical preparation/stage/orientation fields, price status, and review flags.

The DJVU plain text reorders number/description/price columns on several pages. Therefore:

- **148** row prices are securely recoverable from row-aligned OCR;
- **275** prices are deliberately left unresolved rather than guessed;
- rows 223-230 (Cephalopoda) are reconstructed from a column-scrambled page and carry a specific alignment-review flag;
- source classification is preserved, including Tunicata under `Mollusca`;
- the extraction never converts catalogue offering numbers into surviving-object counts.

Base parse status: **`PARSED_423_OCR_TEXT_V1_PRICE_PARTIAL`**.

## Post-parse reverse match: 9 June 1880 RMS shipment

The taxon/preparation reverse pass recovered a much stronger British source than the earlier broad event summary.

- JRMS `R24204`, document `D057`, printed p. **733**, records `Zoological Station of Naples—12 slides`, donated by the Station through **A. W. Waters**. Mr Crisp called special attention to them and they were exhibited under microscopes.
- The same issue, `R24207`, printed p. **736**, names all twelve physical slides.

Comparison against the parsed catalogue gives **nine exact or strong item-level matches**:

- no. **42** — *Asterias glacialis*, gastrula;
- no. **43** — *Asterias glacialis*, mesoderm formation;
- no. **67** — *Toxopneustes brevispinosus* / *Sphaerechinus granularis*, larva 3rd day;
- no. **68** — same, 5th day;
- no. **71** — same, 15th day;
- no. **72** — *Echinocardium cordatum*, larva; catalogue specifies 3 days, RMS label omits age;
- no. **86** — *Stichopus regalis*, ovary;
- no. **182** — *Pseudodidemnum Listerianum*, ova with embryo;
- no. **186** — *Pyrosoma elegans*, young colony.

Three further physical slides are **bounded but unresolved**:

- *Amphioxus lanceolatus* → catalogue **231 or 232** (`Vorderer Körpertheil` versus `Ganzes Thier`);
- *Ascetta bianca* → **5 or 6** (unstained versus stained);
- *Asteracanthion/Asterias glacialis* `Larva` → developmental block **43-49**, because the RMS label does not state the exact developmental condition.

The row-level evidence is stored in `NAPLES_1880_RMS_12_SLIDES_ITEM_CROSSWALK_V1.csv`.

This is the first defensible `catalogue offering -> named British physical slide shipment/exhibition` closure for this source. It upgrades the analytical Naples target to **`PARSED_423_PLUS_RMS_ITEM_CROSSWALK_9_EXACT_3_BOUNDED`**.

It does **not** establish that any of these twelve RMS slides is the same physical object as a surviving St Andrews slide. A three-point `catalogue -> Britain -> surviving object` identity remains open and must not be inferred from shared taxon or programme provenance.

A page-image pass on the Naples catalogue is only necessary if complete price-level quantitative work or publication-level verification of the column-scrambled rows becomes important. No further open-ended discovery work is required for this source; future work should be bounded reverse matching against known British circulation events.
