# Frozen 155 → UK microscopy corpus expansion queue — v1

This is a **derived routing and evidence layer** over the sealed `CLOSED_2026-08-09` 155-entry microscope-slide catalogue. It does not alter the frozen catalogue or reopen discovery.

The purpose is to use surviving-object nodes to decide what textual material is worth adding next to the nineteenth-century microscopy corpus, and then to record object↔text closures without rewriting the source catalogue.

## Current text corpus used for routing

Literal routing checks and contextual verification use the seven current UK microscopy masters:

- `01A_UK_Microscopy_Core_Early_Central_1844-1877`
- `01B_UK_Microscopy_Core_Professional_1869-1886`
- `01C_UK_Microscopy_Core_Clubs_Popular_Local_1865-1886`
- `02A_UK_Microscopy_Extensions_1847-1867`
- `02B_UK_Microscopy_Extensions_1868-1875`
- `02C_UK_Microscopy_Extensions_1876-1883_and_Special_OCR`
- `03_UK_Microscopy_BNA_MASTER`

The practical corpus window is therefore treated as approximately **1844-1886**. A node wholly after 1886 or before 1844 receives a priority penalty unless its historical chain crosses into the current corpus window.

## Important limitation

`exact actor` and `distinctive surname` signals are routing evidence only. They are fixed-string/OCR presence tests, not verified historical hits. Counts can be inflated by repeated metadata, indexes, OCR duplicates, or repeated source units. Every positive signal still requires inspection of the actual text context before it becomes evidence.

The same rule applies to catalogue reverse matching: taxon, stage and preparation-language matches are candidates until a contextual source record establishes Naples provenance or another explicit relation. Shared taxonomy alone never establishes physical-object identity.

## Queue structure

The external planning workbook/CSV separates four tracks:

1. **Expansion gaps** — event-rich, trade-rich, or serial-set object nodes with no or weak reliable actor signal in the present textual corpus.
2. **Immediate bridges** — object nodes whose named actors already have exact literal signals in the current corpus, making them strong candidates for rapid object↔text closure.
3. **Serial sets** — published/distributed numbered preparations, kept separate because serial endpoints are not surviving-slide totals.
4. **Custody gaps** — surviving nodes for which the museum-facing object source gives present custody but no explicit historical acquisition/transfer route.

The queue also stores suggested source families, bounded search strings, event hooks, corpus-window fit, and manual status fields.

## v1 routing counts

- 155 frozen object nodes routed.
- Priority: **7 P1**, **30 P2**, **38 P3**, **80 P4**.
- Actor-routing signal: **25 strong exact**, **14 moderate exact**, **12 weak exact**, **30 multi-corpus surname-only**, **6 surname-only**, **68 no reliable actor signal**.
- 21 nodes form the first `Expansion_Gaps` sheet after current-window and canonical-saturation adjustments.
- 32 nodes form the first `Immediate_Bridges` sheet.
- 7 nodes are isolated as published/distributed `Serial_Sets`.
- 76 nodes are marked as `Custody_Gaps`.

## First contextual verification pass

The literal-routing layer understated several actors because initials, OCR variants and name forms disrupted exact matching. Contextual reading validated the object-first method quickly.

### Eulenstein

QJMS 1867 pp. 64-65 describes two series, slide format, labelling, five 100-species parts and ordering through R. & J. Beck. *Science-Gossip* 1867 p. 188 describes five sections of 100 mounted slides and solicits English diatom gatherings. QJMS 1869 pp. 325-326 records Eulenstein's purchase of the late Dr Arnott's diatom material and his readiness to issue series from it. The 1869 Arnott event is retained as related circulation evidence, not silently equated with the surviving 1867 Farlow set.

### Charles Collins

*Science-Gossip* 1884 p. 87 identifies the issuing slide maker as Charles Collins Jr., nephew of the microscope maker. An 1885 advertisement in the *Journal of Microscopy and Natural Science* lists three priced `Special` Micro Slide series and states that Collins Jr.'s slides were stocked at the senior Collins shop. *Microscopical News and Northern Microscopist* IV (1884), p. 109, `Fish Scales`, is bibliographically located through a source-specific transcription; the primary scan remains optional.

### H. L. Smith

The RMS cabinet report records 146 diatom slides presented by Smith in 1867; these predate the 1876-1888 published set and remain separate. Quekett 1876 p. 177 contains Smith's mounting method. The *Monthly Microscopical Journal* XVII (1877), pp. 100-101, directly describes Century I: 100 slides, five pasteboard trays, numbered catalogue/labels, diamond-written slide numbers, and material obtained from Smith's own gatherings, the de Brébisson collection, and exchange or otherwise. The August 1878 Century III item is bibliographically located in the *American Journal of Microscopy and Popular Science*, vol. 3; its primary page text remains unparsed.

### Kitton

*Science-Gossip* 1884 p. 260 reports the first Norfolk Diatomaceae series issued in a case, with named slides and catalogue; the 1885 volume p. 18 reports the second series of the `Century`. Quekett 1885 p. 178 links the set to Kitton's broader Norfolk diatom work. A direct contemporary source for Series III-IV remains optional rather than urgent.

## Naples / Fritz Meyer P1 sequence

The Naples target has moved from discovery to a product-level historical corpus.

### Source and parse

The primary source is Anton Dohrn, `Preis-Verzeichniss der mikroskopischen Präparate, welche durch die Zoologische Station zu Neapel zu beziehen sind`, *Mittheilungen aus der Zoologischen Station zu Neapel*, Bd. II, pp. 238-253. The catalogue is signed **Neapel, August 1880**. The numbered offerings run 1-423.

The uploaded IA DJVU text was parsed into **423 sequential historical catalogue offerings**. The 423 figure is a catalogue-offering count, not a surviving-slide total. Source-group counts are Protozoa 4; Coelenterata 33; Echinodermata 49; Vermes 33; Arthropoda 57; Mollusca in the source classification 54; Vertebrata 193. Price extraction remains partial: 148 row prices are securely aligned and 275 remain unresolved because OCR detached or reordered table columns.

The parse manifest is `NAPLES_1880_CATALOGUE_423_PARSE_MANIFEST_V1.json`.

### British circulation crosswalk

The bounded UK pass now records **eleven distinct object/specimen circulation or exhibition events**, plus separate catalogue-reception and method-circulation layers. The event layer distinguishes finished slides, preserved/biological specimens, off-catalogue British remanufacture, and preparation-method circulation.

A correction is important: the *Field* notice of 24 February 1883 reports a **Zoological Society** Bell exhibition of a selection of Naples preparations. It is separate from the **14 March 1883 RMS** event in which Bell explained **nineteen slides** received from Naples. Physical overlap is possible but remains `NOT_ASSERTED`.

New bounded events include T. Bolton's **11 November 1884 Birmingham** exhibition of `preserved specimens from the zoological stations at Naples`, and C. Baker's **May 1886 RMS** `Marine Objects from Zoological Station, Naples`. Neither wording is silently converted into `slides`.

The event layer is `NAPLES_1880_UK_CIRCULATION_CROSSWALK_V1.csv` with methodological notes in `NAPLES_1880_UK_CIRCULATION_CROSSWALK_V1_README.md`.

### First item-level catalogue → Britain closure

A reverse taxon/preparation pass recovered the detailed list for the **9 June 1880 Royal Microscopical Society** shipment.

- `R24204`, JRMS printed p. 733: the Station donated **12 slides** through A. W. Waters; Mr Crisp called attention to them and they were exhibited under microscopes.
- `R24207`, printed p. 736: all twelve slides are named.

Comparison with the 423 catalogue yields **nine exact/strong item matches**:

`42, 43, 67, 68, 71, 72, 86, 182, 186`.

Three further slides are bounded but unresolved at item level:

- *Amphioxus lanceolatus* → `231|232`;
- *Ascetta bianca* → `5|6`;
- *Asteracanthion/Asterias glacialis* larva → developmental block `43-49`.

The exact row-level mapping is `NAPLES_1880_RMS_12_SLIDES_ITEM_CROSSWALK_V1.csv`.

This is the first defensible `catalogue offering → named British physical slide shipment/exhibition` closure in the Naples pass. It is **not** yet a three-point `catalogue → Britain → surviving St Andrews object` identity. `same_physical_object_as_st_andrews` remains `NOT_ASSERTED` throughout.

### Bounded negative results matter

Immediate-context checks around the 1881 Crisp RMS selection, the 1882 C. Baker RMS Conversazione display and the 14 March 1883 Bell nineteen-slide RMS event did **not** recover a detailed Naples item list. Their catalogue-item identity therefore remains unresolved. These are recorded as bounded negative checks rather than prompts for open-ended crawling.

## Working files

- `OBJECT_TEXT_BRIDGES_V1.csv` — contextually verified object↔text bridges.
- `OPEN_PRIMARY_SOURCE_TARGETS_V1.csv` — bounded source targets and resolved statuses.
- `P1_TARGETS_1_2_OUTCOME_2026-08-09.md` — Smith/Collins source pass.
- `P1_TARGET_3_NAPLES_1881_OUTCOME_2026-08-09.md` — Naples source location, parse and follow-up.
- `NAPLES_1880_CATALOGUE_423_PARSE_MANIFEST_V1.json` — 423-row parse manifest.
- `NAPLES_1880_UK_CIRCULATION_CROSSWALK_V1.csv` — UK object/specimen-circulation event layer.
- `NAPLES_1880_UK_CIRCULATION_CROSSWALK_V1_README.md` — crosswalk method, correction log and interpretation.
- `NAPLES_1880_RMS_12_SLIDES_ITEM_CROSSWALK_V1.csv` — twelve-slide RMS shipment mapped to catalogue items.
- `PROGRESS_LOG_2026-08-09.md` — compact dated research log.

## Recommended use

For each queue row:

1. run bounded actor/object/event or taxon/preparation queries;
2. inspect the actual text context;
3. record source ID, page/date, and the exact relationship asserted;
4. distinguish `EXACT`, bounded family/programme correspondence, and unresolved identity;
5. add genuinely new source units to the text corpus;
6. never infer preparation from ownership/use or slides from generic `objects/specimens`;
7. never collapse serial endpoints, cabinet capacities, current aggregates, catalogue offerings, database rows or surviving slides into one quantity namespace.

This layer is intended to replace open-ended periodical sweeping with object-generated and catalogue-generated event-specific corpus expansion.
