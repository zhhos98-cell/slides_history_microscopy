# Thomas Davies at the Working Men's College: register control and serial archive gate

**Date:** 2026-09-08  
**Branch:** `research/working-mens-microscopy-19c`  
**Status:** WMC attendance secure at obituary level; exact enrolment years/classes remain open; archive route reduced to one-person register check; Transcriber / Junior Assistant promotion date now explicitly source-conflicted (1862/1869).

## Question

Can Thomas Davies's Working Men's College attendance be fixed to dated student-register entries and, only if the register supports it, to specific French or German classes?

This matters because the current Davies case is strongest when two training environments are kept separate:

```text
British Museum Mineralogy / Maskelyne
  -> mineral handling, registration, labelling
  -> thin-section / rock-mineral microscopy

Working Men's College
  -> evening general education
  -> French and German
```

The archival task is therefore not to prove that WMC taught Davies microscopy. It is to date and specify the **general-education component** of a composite competence trajectory.

## 1. Secure biographical baseline

L. Fletcher's obituary of Thomas Davies in *Mineralogical Magazine* 10 (1893), 161–164, gives the current near-primary biographical sequence.

It states that Davies:

- was born 29 December 1837;
- entered the British Museum in 1858 as a third-class attendant under N. S. Maskelyne;
- during the following nine years was, apart from a short interval, Maskelyne's sole helper in the arrangement and examination of the mineral collections;
- acquired practical mineral recognition through cleaning, arranging, registering and labelling specimens;
- was initiated by Maskelyne into the microscopic characters of rock-forming minerals while Maskelyne studied thin sections of meteorites;
- became highly skilled in microscopic determination of minerals in rock sections;
- attended evening classes at the Working Men's College, Great Ormond Street, in order to improve his general education;
- in the course of time acquired knowledge of French and German;
- says that his qualifications were officially recognized in **1869** by promotion from attendant to Transcriber / Junior Assistant;
- records promotion to First Class Assistant in 1880.

Source: `https://rruff.info/doclib/MinMag/Volume_10/10-46-161.pdf`, especially pp. 161–162.

**Evidence level:** `A_NEAR_PRIMARY_BIOGRAPHICAL` for the biographical sequence; the 1869 promotion date is now a `DATE_CONFLICT`, not a single controlled chronology anchor.

### Promotion-date conflict: 1862 vs 1869

A bounded chronology check produced a direct conflict that must be preserved.

- Fletcher's *Mineralogical Magazine* obituary explicitly says that Davies's promotion from attendant to Transcriber / Junior Assistant occurred in **1869**.
- A contemporary obituary in *Geological Magazine* (1893), p. 96, says instead: **“In 1862 he was promoted to the rank of Transcriber.”**
- The current Natural History Museum Archives person record `PX1373` gives the most specific administrative formulation: appointed third-class attendant **20 Feb 1858**; Transcriber or Junior Assistant (2nd Class Assistant) **25 Aug 1862**; 1st Class Assistant **10 Jul 1880**.
- Another contemporary obituary in *Natural Science* (1893) also gives **1862**, but may not represent an independent administrative source and is used only as corroborating printed reception, not as separate archival proof.

Sources:

- Fletcher, *Mineralogical Magazine* 10 (1893), 161–164: `https://rruff.info/doclib/MinMag/Volume_10/10-46-161.pdf`.
- *Geological Magazine* obituary, 1893, p. 96: `https://upload.wikimedia.org/wikipedia/commons/7/71/Geological_magazine_%28IA_geologicalmagazi3101893wood%29.pdf`.
- Natural History Museum Archives person record `PX1373`: `https://www.nhm.ac.uk/CalmView/Record.aspx?id=PX1373&src=CalmView.Persons`.

Controlled chronology:

```text
1858 third-class attendant = SECURE
Transcriber / Junior Assistant promotion = DATE_CONFLICT (1862 vs 1869)
1880 First Class Assistant = SECURE
```

Do **not** silently normalize the conflict to 1862 merely because the NHM catalogue supplies an exact day, and do **not** retain 1869 as an uncontested benchmark merely because Fletcher is the main obituary witness for the microscopy/WMC sequence. The personnel chronology should be closed, if it becomes analytically necessary, from a staff register, Trustee appointment minute, pay list, or equivalent administrative record.

For the present WMC register gate, the promotion dispute is not identity-critical. Use the uncontested identifiers (1837 birth, British Museum Mineralogy, appointment in 1858, Maskelyne relation, First Class Assistant by 1880) and interpret any WMC date without forcing it against a disputed 1862/1869 promotion point.

### Claim ceiling

The Fletcher obituary does **not** say:

- what year Davies first enrolled at WMC;
- how many years he attended;
- whether French and German were both acquired exclusively at WMC;
- which named language classes or teachers he attended;
- that Maskelyne taught him at WMC;
- that WMC taught him microscopy, mineralogy or thin-section preparation.

The sentence structure itself separates his Museum microscopic apprenticeship from his later/general educational improvement at WMC. Preserve that separation.

## 2. WMC language-course context

The official WMC material for 1866 confirms that French and German were active class subjects at Great Ormond Street; the financial accounts explicitly include expenditure for `Class Teachers, French and German`.

Source: Working Men's College, *The Working Men's College, founded 1854, 45 Great Ormond Street, Bloomsbury, W.C.* (London: The College, 1866), Internet Archive identifier `workingmenscolle188work`.

**Evidence level:** `A_INSTITUTIONAL_CURRICULUM` for the existence of French/German teaching at WMC in 1866.

This is contextual only. It does **not** place Davies in those 1866 classes.

Controlled relation:

```text
Davies -> WMC evening classes / French + German = SECURE BIOGRAPHICAL
WMC -> French + German classes in 1866 = SECURE INSTITUTIONAL
Davies -> specific 1866 language class = OPEN
```

## 3. LMA archive availability

The AIM25/London Metropolitan Archives collection description for `GB 0074 LMA/4535` states that the Working Men's College archive contains **lists of students, 1854–1873**, with the earliest list recording students' occupations. The same collection includes governance minutes, College ledgers, correspondence and student-club records.

The National Archives collection summary likewise describes the WMC holdings as including a **students register** under reference `LMA/4535`.

Sources:

- AIM25/LMA collection description: `https://atom.aim25.com/index.php/working-mens-college`
- The National Archives organisation/collection summary: `https://discovery.nationalarchives.gov.uk/details/c/F157579`

**Evidence level:** `A_ARCHIVE_ROUTE` for the existence, date range and general content of the student-list/register material.

### Public-catalogue ceiling

A bounded search of AIM25/TNA and indexed web results did **not** expose a trustworthy subordinate reference for the 1854–1873 student lists. Publicly visible results repeatedly terminate at collection-level `LMA/4535`.

Therefore:

- do not invent an `E/...`, `F/...` or other child reference;
- do not treat the absence of a public child reference as evidence that the list is inaccessible or lost;
- ask the archive using the collection reference and exact date-range/content description already supplied by its catalogue.

## 4. Gate 1 — only active first request

Ask one question only:

> Do the Working Men's College student lists/registers for 1854–1873 (`LMA/4535`) contain **Thomas Davies (1837–1892), of the British Museum Department of Mineralogy / Mineral Department**?

Disambiguation fields if needed:

- born 29 December 1837;
- son of William Davies of the British Museum Geological Department;
- third-class attendant at the British Museum from 1858;
- later Transcriber / Junior Assistant, with the exact promotion year currently source-conflicted (1862/1869);
- First Class Assistant from 1880;
- associated with N. S. Maskelyne.

If the answer is **YES**, request only:

1. exact year(s) of appearance;
2. occupation, employer and/or address if recorded;
3. the exact register/list reference for that entry.

No multi-person sweep. Do not ask simultaneously for Seeley, Grugeon, Cooke's pupils or occupational categories.

## 5. Gate 2 — only after a Davies register hit

Only if Gate 1 is positive, ask whether the same registration system or an immediately linked class record identifies Davies's courses.

Minimal question:

> Does Davies's entry, or a directly linked class-enrolment record, identify French or German classes? If that information is in a different series, could you provide only the relevant reference?

If a language-class hit is found, record:

`date/term | language | class level | teacher | fee/status if present | source reference`.

Do not infer that a French/German course listed in a prospectus was attended by Davies without a name-level record.

## 6. Decision rules

### Gate 1 YES

This closes a dated WMC enrolment anchor. Compare the first/last register appearance against:

- 1858 British Museum appointment;
- early Maskelyne microscopic apprenticeship;
- the unresolved 1862/1869 Transcriber / Junior Assistant promotion chronology;
- 1880 First Class Assistant promotion.

A dated overlap would materially strengthen the **parallel/composite training** model, but the WMC date must not be used to adjudicate the 1862/1869 Museum personnel conflict without direct administrative evidence.

### Gate 1 NO

A complete negative in the relevant student-list/register sequence would **not** overturn Fletcher's obituary statement that Davies attended WMC evening classes. Possible explanations include incomplete survival, attendance not represented in the surviving list, or a different registration mechanism.

But it is sufficient as a **research-resource stop rule**: do not broaden into general WMC correspondence or staff minutes merely to prove the obituary wrong/right.

Preserve:

`WMC attendance + French/German = biographically secure; register chronology unresolved/negative in surviving checked series.`

### Archive cannot search without broad paid research

Stop the register route unless a digitized/list-level access mechanism is offered. Do not convert the request into a staff-led prosopographical search.

## 7. Effect on the material-competence argument

The Davies case does not require a WMC microscopy class.

Its analytical value is precisely that different capacities were assembled in different institutional settings:

- custodial and classificatory work at the Museum;
- microscopic mineral recognition under Maskelyne;
- language/general education at WMC;
- later promotion and scientific assistance.

A positive register hit would add chronology and institutional precision to this model. A negative register check would leave the core biographical distinction intact while setting a rational stop point for further WMC searching.
