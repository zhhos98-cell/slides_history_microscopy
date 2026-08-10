# UK / US / Europe closure batch — 2026-08-10

Status: **ACTIVE CLOSURE ONLY**

The working rule for the next phase is now stricter than geographic bibliography building. The frozen surviving-object survey remains 307 discovery nodes / 155 strict nineteenth-century nodes and stays closed. The public bibliography has reached pass 19 / 206 verified entries; passes 18–19 remain part of the repository's audit history, but they no longer define the active search frontier. Further South Asian, African, Latin-American or East/Southeast-Asian expansion for coverage is parked. The active task is to close already-open UK, narrowly connected US, and European object↔text↔register chains.

## Batch result

### 1. Arthur C. Cole — primary-source architecture closed

The locally available full OCR of *Studies in Microscopical Science*, vols. I–II, has now been unpacked and structured directly. Volume I (1883) contains 52 numbered studies and 53 lithographed plates. Its preface explicitly gives Martin J. Cole responsibility for the microscopical preparations issued with the work. Volume II (1884) contains 36 lithographed plates and makes a more distributed workflow visible: W. Fearnley contributes Animal Histology and assists with Popular Studies and Methods; David Houston contributes Botanical Histology; Edward T. Draper supplies drawings; preparation is credited jointly to Martin J. Cole and Arthur C. Cole.

This closes the main question for the current project. Cole is a particularly strong case of **material publication** because the preparation, text and plate are coordinated parts of the issue architecture. The source also prevents a common flattening: preparator responsibility changes between the two volume-level prefaces, so Vol. I and Vol. II must not be assigned to one normalized maker field. The structured direct-primary output is `data/analysis/cole_studies_vol1_2_structured_reading_v1.json`.

### 2. Charles Collins Jr. — 1884 series closed without unnecessary volume building

The existing UK corpus already contains the decisive bibliographic event: the 1884 *Microscopical News* notice at IV, p. 109 is abstracted as Collins' **Series of 48 Fish Scales**. The 1885 journal layer records the broader “Special” Micro-Slides, including fish scales and skins, insect heads, parasites, silkworm/moth material, insect anatomy and palates. St Andrews independently preserves a Collins group and explicitly associates his own fish-skin/scales set with 1884.

The result is enough for a series-level closure: `1884 named 48-species product → 1885 expanded commercial repertoire → surviving institutional object group`. Whole-volume ingestion of *Microscopical News and Northern Microscopist* IV may still be useful for adjacent trade/local context, but it is no longer a prerequisite for the Collins chain itself. Secondary Collins labels can occur on other preparators' mounts, so retailer/label attribution and preparation authorship remain separate.

### 3. H. L. Smith — Century III set architecture closed

The surviving Farlow architecture gives *Diatomacearum Species Typicae* as Centuries I–VI, nos. 1–600, followed by supplement 601–750, with each century comprising 100 slides and the surviving system organized in labelled twenty-five-slide cards. Century III is therefore nos. **201–300**. This can be joined to the UK reception evidence for Century I, which describes 100 slides in five pasteboard trays, catalogue and numbered labels, corresponding slide numbers and diamond-written numbers; Century II is separately recorded as received.

The specific 1878 Century III notice remains useful only for reception chronology. It is now a narrow textual locator gap, not a reason to open an American microscopy corpus. Shared series numbering also does not prove that any current Farlow copy is the same physical set once received in Britain.

### 4. Frederic Kitton — Series III–IV architecture closed

The Farlow object/register layer explicitly defines *Norfolk Diatoms* as Series I–IV, nos. 1–100, with twenty-five numbers in each series. Therefore Series III = **51–75** and Series IV = **76–100**. The surviving set and handwritten Kitton catalogue close the material series architecture. A contemporary prospectus or launch notice for III–IV would enrich distribution chronology, but it is no longer necessary to know what the series was or how it was numbered. Physical-copy count remains distinct from serial position.

### 5. Andrew Pritchard — priority date corrected and object bridge closed

The old priority note contained a consequential date error: the preparation catalogue target is **1835**, not 1837. Pritchard's *A list of two thousand microscopic objects* is dated 1835; 1837 belongs to *Micrographia*. Surviving institutional material provides the other half of the bridge: an 1835 London case of eleven Pritchard microscope slides survives, and Whipple accession 2385B preserves Pritchard catalogue labels inside a later mixed cabinet of commercial and homemade slides. The 1842 second edition supplies a later catalogue state with new prepared objects.

This converts Pritchard from a loose “early catalogue” lead into `dated catalogue → surviving contemporary case → later re-cabineted catalogue-labelled objects`. The mixed Whipple case is evidence for reuse and later assembly, not proof that Pritchard made the cabinet itself.

### 6. John Thomas Norman — collection-level chain closed

The existing corpus/newspaper layer records Norman's large 1862 exhibition series of microscopic preparations. St Andrews identifies his only catalogue as the 1872 catalogue of **2,584 mounts** and preserves a dedicated Norman group within the Bell-Pettigrew collection. This is enough to close `public exhibition → catalogue scale → later institutional survival` at collection level.

The genuinely open problem is narrower: a row-by-row 2,584-entry catalogue-to-surviving-slide crosswalk. The public St Andrews group page does not expose the full Norman item list, so the item-level bridge should wait for object/export data rather than being reconstructed from labels or taxonomy. Norman labels can also enter secondary commercial circulation.

### 7. HMS Challenger — dataset/address architecture closed; binary harvest remains technical

The official NHM data resource distinguishes a **4,723-record dataset** from **4,713 physical bottles, tubes, boxes, slides and derived preparations**. Existing analysis has already structured the M/subnumber addressing system, a 105-drawer slide cabinet, Haeckel annotation, named Norman / Voigt / Hochgesang preparation evidence and the 127-preparation return event of 1920. The two totals must remain different namespaces.

The remaining full-table task is mechanical: ingest the XLSX without early exit once the binary is retrievable and subset preparation/slide terms plus named preparators. This is no longer a discovery problem and should not trigger a fresh Challenger web sweep.

### 8. Elcock — archive locator closed

The St Andrews Challenger correspondence target is now narrowed to **ms21974–ms21975**, 6–8 March 1884. Catalogue metadata explicitly connects the correspondence to Challenger expedition samples. Only those two manuscripts need transcription. Catalogue metadata cannot supply the still-open sender/sample/station/purpose details.

### 9. Naples 383 — deliberately parked

BPM/1/T8/6 remains a strong candidate because the surviving St Andrews slide is *Delphinus phocaena*, carries Stazione Zoologica Napoli provenance and the handwritten string “Panis 383”; 383 is structurally plausible inside the derived Mammalia run. The historical row itself is still missing. A single page-image check around rows 382–384 is justified when available. Further broad Naples searching is low-yield until that source page can be read.

## What changes operationally

This batch replaces “find more collections” with “reduce open edges.” Seven targets are now closed or substantially closed at the level needed for historical argument. Two remain as bounded residuals. The next useful work is therefore small and exact: Norman item exports if obtainable; Pritchard 1835/1842 category-to-object comparison; Challenger XLSX full harvest when the binary becomes retrievable; Elcock ms21974–ms21975 transcription; and one Naples rows 382–384 page check. None requires building a new geographic infrastructure.
