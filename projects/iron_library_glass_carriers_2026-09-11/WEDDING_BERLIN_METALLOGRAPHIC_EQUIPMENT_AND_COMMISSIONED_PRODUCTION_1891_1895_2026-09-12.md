# Berlin metallography — imaging equipment and commissioned production, 1888–1895

Date: 2026-09-12

Status: PRIMARY / NEAR-CONTEMPORARY CONTROL. Legacy filename begins `1891_1895`, but the evidence chain is now securely pushed back to **1888**. This file separates: (1) early institutional microphotography, (2) later explicit equipment codification, (3) dedicated specimen-production/imaging equipment, (4) commissioned/internal production, and (5) later external circulation.

## 1. 1888 — Wedding is already producing institutional microphotographic evidence

The 1904 official index to the `Mittheilungen aus den technischen Versuchsanstalten` explicitly lists, under **Wedding / Abteilung 4 / Jahrgang 1888**:

- **`Mikrophotographien von Drähten`** — plates I and II–VIII;
- **`desgl. von Stahl`** — plate III;
- **p.84: `Anwendung des Zirkonlichtes bei der Aufnahme von Negativen durch das Mikroskop`.**

Primary institutional retrospective:
- Martens/Guth, official 1904 Materialprüfungsamt history/index as exposed through the Paderborn digital object.

This materially changes the equipment chronology. Berlin institutional microphotography is already a published technical practice in **1888**; 1891 is not its beginning.

Use:

**`INSTITUTIONAL_METAL_MICROPHOTOGRAPHY <= 1888`.**

Claim ceiling: the full Wedding p.84 text has not yet been directly transcribed in this workflow. The official 1904 index securely controls title, author, year, page and associated microphotographic plates.

## 2. 1888/89 — Wedding's imaging geometry is described in contemporary photographic literature

Josef Maria Eder's 1889 *Jahrbuch für Photographie und Reproduktionstechnik* discusses zircon light for microphotography and describes its application to **photographing temper / interference colours (`Anlauffarben`) of iron surfaces according to Professor Wedding in Berlin**.

The same contemporary account states that Wedding found microstructural details became much more visible when the iron surface was placed **obliquely relative to the microscope axis**.

The described reflected-light arrangement uses a plan-parallel glass plate at about **45°** between object and objective to direct the illumination toward the metal surface while permitting image formation through the objective.

A closely related contemporary technical description of work learned in Berlin from Martens describes use of **zircon light (Linnemann type)** and a **45° plan-parallel glass plate** for reflected-light photography of polished metal surfaces.

Sources:
- Eder, *Jahrbuch für Photographie und Reproduktionstechnik* 3 (1889), article on zircon light and microphotography;
- contemporary metallurgical/photographic technical report preserving the Berlin/Martens reflected-light setup.

Evidence ceiling:
- Eder directly attributes the iron-surface / inclination observation to Wedding;
- do not silently identify every component of Eder's general zircon-light apparatus as Wedding's own exact p.84 setup until Wedding's original text is recovered.

Secure method variables:

**bright stable artificial source + reflected-light geometry + specimen orientation + negative capture.**

## 3. 1891 — Martens makes the institutional equipment itself the explicit subject

A. Martens published:

**`Die mikrophotographische Ausrüstung der kön. Mechanisch-Technischen Versuchsanstalt`, Mittheilungen aus den königlichen technischen Versuchsanstalten, Heft 6 (1891), p.278.**

This bibliographic object is independently listed in Francis Scott Rice's 1897 bibliography and in later microscopy literature.

The 1904 official index adds object-level visual controls around the article:

- **`Mikrophotographien von Eisenschliffen`** — plates V–VI;
- **`Mikrophotographischer Apparat Martens–Zeiß`** — plate IV.

The 1891 volume of the *Zeitschrift für wissenschaftliche Mikroskopie* also indexes/reviews Martens' Berlin microphotographic equipment at p.504, showing that the setup was recognised in the contemporary microscopy community.

Use:

**1888 = institutional microphotographic practice already visible**

**1891 = the apparatus/system becomes an explicit publishable technical object and is externally reviewed.**

The full Martens p.278 article still needs direct transcription.

## 4. 1892 — microscopic failure/structure cases become an explicit publication series

Martens published:

**`Über einige in der Mechanisch-Technischen Versuchsanstalt ausgeführte mikroskopische Eisenuntersuchungen`, Mittheilungen, vol. X (1892), p.57.**

The 1904 official index summarises the cases as including:

- brittle scratching wire (`brüchiger Kratzendraht`);
- bending tests;
- brittle wire-rope wire (`brüchiger Seildraht`);
- defects in tensile-test specimens;
- chemical + microscopic testing;
- block and girder cross-sections.

The same index associates **fracture surfaces and microphotographs of iron** with the 1892 material.

This establishes that by 1892 microphotography/microscopy was not merely apparatus experimentation: it was being applied to concrete failure, defect and section-analysis problems.

## 5. Rechnungsjahr 1892/93 — dedicated specimen-production/imaging hardware is expanded

The contemporary annual-report summary in *Stahl und Eisen*, 1 February 1894, is exceptionally explicit.

The mechanical-technical department acquired:

- a **grinding machine (`Schleifmaschine`) for producing polished sections for microscopic investigation of metals**;
- the acquisitions were supported by a **special ministerial appropriation/decree**.

The institute's own precision mechanic additionally made:

- a **lighting device for reflected light (`auffallendes Licht`) for microphotographic purposes**.

Primary source:
- *Stahl und Eisen*, 1 Feb. 1894, `Die Thätigkeit ... im Jahre 1892/93`, printed p.144.

Evidence status:

`CONTEMPORARY_PRIMARY_TEXT_LAYER = SECURE`

`PDF_SCREENSHOT = PENDING (mirror cache miss after attempted screenshot)`

This is not the beginning of Berlin microphotography. It is a threshold in **dedicated production capacity and equipment expansion**:

**specialised metal-section machine + dedicated reflected-light imaging device + ministerial funding.**

## 6. 1892/93 — commissioned/application-based Schliff + photograph pair

The same annual-report summary states that among 247 completed applications (45 from public authorities, 202 from private parties), the department performed:

**production of 2 steel polished sections for microscopic examination of structure, together with the corresponding photographic recordings.**

This establishes:

**`COMMISSIONED / APPLICATION-BASED METALLOGRAPHIC PRODUCTION <= 1892/93`.**

Claim ceiling: applicant identity and whether the sections/photos were physically delivered outward are not given in the summary. Do not upgrade this to a standing external circulation service.

Secure carrier pair:

**steel specimen → prepared Schliff → microscopic structure → corresponding photograph.**

## 7. 1893/94 annual-report summary: negative control only

The following *Stahl und Eisen* annual-report summary is detailed about equipment, 221 applications and 2,672 tests but contains no explicit `Schliff`, `mikroskop` or `Photograph` line.

Use only:

`1893/94 St&E summary = no explicit metallographic-production line found`.

Do not infer that metallography stopped or was absent; the full `Mittheilungen` report may include omitted detail.

## 8. Rechnungsjahr 1894/95 — metallographic production becomes quantitatively visible

The contemporary annual-report summary published 15 February 1896 records:

- **36 photographic recordings (`Photographische Aufnahmen`)**;
- **115 qcm of polished sections for microscopic investigations**;
- colour investigations and annealing experiments alongside mechanical/technological testing.

Primary source:
- *Stahl und Eisen*, 15 Feb. 1896, printed p.175.

Evidence status:

`CONTEMPORARY_PRIMARY_TEXT_LAYER = SECURE`

`PDF_SCREENSHOT = PENDING (cache miss)`

The scale is now annual and measurable, rather than a single two-section application.

## 9. 1894/95 — microscopy enters accident diagnosis and procurement governance

The same report describes gas cylinders involved in an explosion at the Royal Ballooning Department's Schöneberg exercise ground.

The investigation combined:

- extensive strength tests;
- **microscopic examination of material microstructure**.

The report states that the investigation led to **new conditions governing future supply of such cylinders**.

Controlled chain:

**accident / failure → mechanical testing + microstructure → institutional judgement → revised procurement specification.**

By 1894/95 metallographic evidence is participating in state technical governance.

## 10. Revised clocks of institutional metallography

At least six separate dates must now be kept distinct.

### A. Microphotographic practice

**1888** — Wedding's wire/steel microphotographs + zircon-light negative-capture article are institutionally indexed.

### B. Explicit apparatus publication / external visibility

**1891** — Martens publishes the institute's microphotographic equipment; apparatus and iron-section microphotographs are separately indexed/illustrated and the setup is reviewed by the microscopy community.

### C. Applied microscopic casework

**1892** — published microscopic iron investigations address brittle wires, tensile-specimen defects, block/girder sections and chemical/microscopic comparison.

### D. Dedicated production hardware + commissioned output

**1892/93** — dedicated metal-Schliff grinder + reflected-light microphotographic illumination; two steel sections + corresponding photographs among completed applications.

### E. Quantified operational production / governance

**1894/95** — 115 qcm microscopic sections + 36 photographs; microstructure contributes to accident diagnosis and revised delivery conditions.

### F. Standing external circulation/reference service

**1899** — current earliest hard anchor for sections + associated microphotographs + negative-based study prints supplied against cost.

**1900–01** — explicit standing service; 1901 archive reaches 3,500 negatives and configurable teaching/study collections.

These clocks must not be collapsed into one `birth of metallography` date.

## 11. Analytical consequence

The Berlin infrastructure develops through multiple transformations:

**optical experiment / photographic practice → apparatus publication → applied casework → dedicated specimen/image production equipment → commissioned paired objects/images → routine quantified production → diagnostic authority → archival storage → external reproduction/circulation.**

The 1888 Wedding evidence is especially important for the Sheffield–Berlin project because the same person who had carried hand-inscribed process evidence away from Sheffield in 1860 is, by 1888, working on **how a prepared iron surface can be optically illuminated and captured as a negative**.

Long carrier shift:

**notebook sketch / timed visual process signal → reflected-light prepared surface → photographic negative.**

## 12. Claim ceilings

Secure:

- the official 1904 index records Wedding's 1888 microphotographs of wires/steel and his p.84 zircon-light negative-capture item;
- near-contemporary photographic literature attributes an oblique specimen-orientation imaging observation to Wedding;
- Martens published a dedicated account of the institute's microphotographic equipment in 1891, with institutional apparatus / iron-section microphotographs separately indexed;
- Martens' 1892 microscopic iron investigations covered concrete defect/failure/section problems;
- in 1892/93 a dedicated metal-section grinder was purchased with special ministerial funding and an in-house reflected-light microphotographic illuminator was made;
- two steel sections + matching photographic recordings were produced among that year's applications;
- 1894/95 counted 36 photographs and 115 qcm microscopic sections;
- microscopy of failed gas-cylinder material contributed to revised delivery conditions.

Strong inference:

- Berlin institutional metal microphotography was active no later than 1888;
- 1891 represents codification/public visibility of an existing imaging practice rather than its origin;
- 1892/93 marks a threshold in dedicated specimen-production/imaging capacity and application-based production;
- by 1894/95 metallography is part of operational material diagnosis/governance.

Open:

- Wedding's exact 1888 p.84 apparatus/procedure in his own wording;
- exact apparatus described by Martens in 1891 and its relation to Wedding's 1888 method;
- detailed 1891/92 annual-report activity;
- identity of 1892/93 applicants and ownership/delivery of sections/photos;
- detailed 1893/94 activity omitted from St&E summary;
- survival/numbering of early negatives/specimens.

## 13. Immediate next targets

1. Recover Wedding's **1888 p.84 `Anwendung des Zirkonlichtes...`** original text and plates I–VIII if possible.
2. Recover/transcribe Martens' **1891 p.278ff** apparatus article and contemporary 1891 microscopy review p.504.
3. Recover the **1891/92 annual report** (St&E cross-reference: 1893 p.347) to test what changed before the 1892/93 equipment acquisition.
4. Recover Martens' **1892 p.57ff** microscopic iron case studies.
5. Keep external-circulation chronology separate: earliest hard standing service remains 1899.
