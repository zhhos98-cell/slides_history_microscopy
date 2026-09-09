# Alfred Grugeon — Ramsbottom 1917 direct source control

**Date:** 2026-09-09  
**Branch:** `research/working-mens-microscopy-19c`  
**Source:** John Ramsbottom, `Alfred Grugeon (1826–1913)`, *Journal of Botany, British and Foreign* 55 (1917): 193–194. Directly read from the Internet Archive full-text transcription of the 1917 volume.

## Status

This note supersedes weaker authority-summary statements where Ramsbottom's article itself can be read directly. Ramsbottom is a retrospective biographical source written four years after Grugeon's death, but he explicitly states that much of his information came from Grugeon's own unpublished 1896 `Botanical Reminiscences` paper and from the *Working Men's College Journal* for 1913.

## 1. Entry into WMC botany through M. C. Cooke

Ramsbottom says Grugeon had pursued botany independently before 1860 and then, **hearing that M. C. Cooke was giving botany lessons at the Working Men's College**, joined the institution.

He soon took the South Kensington botany examination and won a prize. Ramsbottom then says Cooke resigned the following session, no replacement teacher was available, and Grugeon was persuaded to continue the class; with Cooke's help he qualified as a certificated teacher.

Controlled chain:

`independent Sunday collecting / plant identification -> hears of Cooke WMC lessons -> joins WMC -> examination -> teaching succession`

Evidence state:

`CLOSED_1917_RETROSPECTIVE_FROM_ACTOR_NEAR_SOURCE`

Do not normalize Ramsbottom's later teaching-date chronology where the OCR is internally inconsistent; use separate WMC institutional controls for exact teaching periods.

## 2. Society of Amateur Botanists membership is explicit

Ramsbottom states that Grugeon was **one of the original members of the Society of Amateur Botanists**, which Cooke formed from old students.

This upgrades the previous state from participation/paper-giver only:

`GRUGEON_SAB_ORIGINAL_MEMBER = CLOSED_1917_RETROSPECTIVE`

It is independently consistent with the contemporary 2 May 1866 report in *The Naturalist*, where Grugeon read a paper on the morphology of the foliar and floral organs of Fabaceae.

Ramsbottom also preserves Grugeon's retrospective recollection of internal tension in the Society and Cooke's later transfer of energy toward the Quekett Microscopical Club. Treat this as **Grugeon's attributed retrospective account**, not an independently verified statement of motive.

## 3. Grugeon and Cooke in the field, 1865

Ramsbottom records that Grugeon accompanied Cooke on a week-long North Wales tour in 1865 and describes Cooke collecting microfungi for fascicles.

This adds a field-practice edge:

`Cooke + Grugeon -> field collecting -> microfungi / publication-preparation context`

Do not infer that this trip generated a specific WMC Magazine or *Science-Gossip* item without a direct textual bridge.

## 4. Material/manual skill

Ramsbottom identifies Grugeon as a wood-turner by trade and notes that his lathe skill enabled him to construct ingenious models for botanical classes. He also records a special chuck for turning spirals in hard wood that was shown at the Great Exhibition of 1851 and received recognition.

This is relevant to the broader `material competence` model:

`occupational manual skill -> botanical teaching models / classroom material competence`

It should remain distinct from microscopy unless an object-specific relation is closed.

## 5. College magazine papers — direct biographical statement

Ramsbottom explicitly states that Grugeon:

> contributed several papers on **botany and natural history** to the College magazine.

This upgrades the corpus state to:

`GRUGEON_COLLEGE_MAGAZINE_SCIENCE_PAPERS_EXISTENCE = CLOSED_1917_RETROSPECTIVE`

The exact article titles, issue dates, pages, signatures/pseudonyms, and genres remain unresolved.

This is stronger than the Darwin Correspondence Project authority summary because Ramsbottom is now directly read.

### RSVP implication

The early *Working Men's College Magazine* is now positively known to contain not only a general-meeting report of Cooke's science class but also multiple Grugeon contributions on botany/natural history.

The grant-funded issue census should therefore explicitly search for:

- Alfred Grugeon / A. Grugeon;
- anonymous/pseudonymous botany items later attributable to him;
- morphology / variation / local floras / field observations;
- class, excursion, specimen, museum and reading contexts surrounding his papers.

## 6. Lubbock Field Club — 1893 gains much stronger support

Ramsbottom says Grugeon was **president of the Lubbock Field Club from its foundation in 1893 until his death**.

This materially changes the 1892/1893 conflict.

Current evidence weighting should now be:

- **1893:** Ramsbottom 1917 direct retrospective statement, based substantially on Grugeon's own 1896 reminiscences and WMCJ 1913; Sutcliffe independently gives 1893 with exact WMC/LMA archival reference.
- **1892:** Ayres ties presidency to Grugeon's retirement in 1892; 1904 WMC OCR contains an internally inconsistent `following year, 1892` sequence.

Controlled state:

`LUBBOCK_FOUNDING_YEAR = 1893_STRONGLY_FAVORED`

`1892_CONFLICT = RETAIN_UNTIL_1904_PAGE_IMAGE / CONTEMPORARY_1892_93_SOURCE`

Do not call the date universally closed until the malformed 1904 page and/or contemporary formation notice is resolved, but 1893 is now the strongest working date.

## 7. Ramsbottom reveals his own evidence base

At the end of the notice Ramsbottom says most of the facts came from:

1. an unpublished manuscript titled **`Botanical Reminiscences`**, a paper read before the Lubbock Field Club by Grugeon in **1896**;
2. the ***Working Men's College Journal* for 1913**;
3. additional information supplied by **C. E. Britton**.

This is a major provenance result because it identifies an actor-level ego-document behind the later biography.

### New target

`GRUGEON_BOTANICAL_REMINISCENCES_1896 = HIGH_PRIORITY_UNPUBLISHED_SOURCE_TARGET`

Potential research value:

- Grugeon's own account of learning botany before/at WMC;
- Cooke's teaching and departure;
- Society of Amateur Botanists formation and internal history;
- field collecting / specimen practice;
- WMC teaching and material methods;
- possible retrospective account of his serial publications;
- possible bridge from early WMC botany to the later Lubbock Field Club.

Do not assume the manuscript survives merely because Ramsbottom had access to it in 1917.

## 8. Source-provenance hierarchy now available

For Grugeon's early WMC/SAB history:

```text
1860s contemporary periodicals / records
    -> direct event evidence

Grugeon, `Botanical Reminiscences` (1896, unpublished)
    -> actor retrospective; currently not recovered

WMC self-history (1904)
    -> institutional retrospective

WMC Journal (1913)
    -> institutional near-obituary / retrospective source, not yet inspected

Ramsbottom (1917)
    -> biography explicitly drawing on 1896 MS + 1913 WMCJ
```

This provenance stack should be preserved rather than flattening all later accounts into one narrative.

## 9. Immediate closure queue

1. locate/search for the 1896 `Botanical Reminiscences` manuscript in WMC/LMA records, Ramsbottom/Britton papers, or later citations;
2. inspect WMCJ 1913 Grugeon material;
3. extract exact Grugeon articles from *Working Men's College Magazine*;
4. inspect Peterson 1978 attribution list for anonymous/pseudonymous items;
5. resolve 1893 vs 1892 through the 1904 page image and/or contemporary formation notice;
6. identify C. E. Britton and his relation to WMC/Grugeon sufficiently to trace possible custody of the 1896 manuscript.

## Stop rule

Treat Ramsbottom as a strong, unusually well-provenanced retrospective source, not as a contemporary 1860s witness. Attribute internal-SAB motive/conflict claims to Grugeon's reminiscence route unless independently corroborated. Do not infer survival or current location of the 1896 manuscript from Ramsbottom's access in 1917.