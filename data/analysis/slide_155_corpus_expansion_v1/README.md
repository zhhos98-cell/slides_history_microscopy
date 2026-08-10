# Frozen 155 → UK microscopy corpus expansion — current status

This directory is a **derived object↔text routing and evidence layer** over the sealed `CLOSED_2026-08-09` 155-node surviving-object catalogue. It does not alter frozen membership, source wording or object provenance claims.

Before using any queue/status file here, consult:

1. `../CURRENT_STATE.json` — canonical current analysis state;
2. `../global_archive_research_priority_CURRENT.json` — live request-only router;
3. this directory for the underlying object↔text evidence and historical routing snapshots.

The current state is **public-web closure exhausted**. General periodical/source discovery is parked. Four exact-source requests remain elsewhere in the analysis layer: the two Elcock letters, the NHM Challenger binary, ZEISS archive/accessory evidence for Balfour, and the St Andrews Norman item/export layer.

## Historical corpus basis

The routing work was built against seven UK microscopy masters:

- `01A_UK_Microscopy_Core_Early_Central_1844-1877`
- `01B_UK_Microscopy_Core_Professional_1869-1886`
- `01C_UK_Microscopy_Core_Clubs_Popular_Local_1865-1886`
- `02A_UK_Microscopy_Extensions_1847-1867`
- `02B_UK_Microscopy_Extensions_1868-1875`
- `02C_UK_Microscopy_Extensions_1876-1883_and_Special_OCR`
- `03_UK_Microscopy_BNA_MASTER`

Literal actor/name matches in those masters were routing signals only. Contextual reading was required before a relation became evidence. The same discipline applies to object reverse matching: shared taxon, maker, number or institution is insufficient by itself to establish physical identity.

## Current closures represented in this directory

### Eulenstein

The 1867 QJMS and *Science-Gossip* records close the published-series programme, slide format, labels, five 100-species parts, ordering through R. & J. Beck and solicitation of English diatom material. The 1869 Arnott-material event remains a related later circulation event and is not silently identified with a surviving 1867 Farlow set.

### Charles Collins Jr.

The object↔text chain is closed at series/event/survival level. *Science-Gossip* identifies Charles Collins Jr. as the issuing slide maker; the 1885 advertisement gives priced `Special` series and the Great Portland Street retail route; the 1884 `Fish Scales` notice is bibliographically located at *Microscopical News and Northern Microscopist* IV, p.109. A primary scan of that single notice is now **optional context**, not an active closure requirement.

### H. L. Smith

Century I is directly closed in British reception: 100 slides, five pasteboard trays, numbered catalogue/labels and diamond-written slide numbers. Century II reception is also documented. Surviving Farlow architecture fixes Century III at nos. 201–300. The exact August 1878 Century III notice is **optional reception chronology**, not an active discovery target. The 146 slides given to the RMS in 1867 remain a separate earlier event.

### Frederic Kitton

Contemporary notices close Series I and II; surviving Farlow architecture closes the full Series I–IV / nos.1–100 structure, with III = 51–75 and IV = 76–100. A Series III–IV launch prospectus is optional chronology only.

### Naples / Stazione Zoologica

The August 1880 price catalogue is fully parsed as **423 historical catalogue offerings**. This is an offering namespace, not a surviving-slide total. The UK circulation layer distinguishes finished slides, preserved specimens, British remanufacture and method circulation.

For the 9 June 1880 Royal Microscopical Society shipment, twelve physical slides are named. Nine map exactly/strongly to catalogue offerings `42, 43, 67, 68, 71, 72, 86, 182, 186`; three remain bounded at `5|6`, `43–49`, and `231|232`. This closes a catalogue-offering → named British shipment/exhibition relation. It does **not** establish that any surviving St Andrews slide is one of those twelve June 1880 objects.

A separate surviving-object relation is now closed from the locally held primary catalogue. Printed p.253 reads:

- `382. Delphinus phocaena L. Milz`
- `383. -- Penis`
- `384. -- Hode`
- `385. -- Niere`

By ditto continuation, offering 383 is `Delphinus phocaena L., Penis`. St Andrews `BPM/1/T8/6` independently carries Stazione Zoologica Napoli labels, `Delphinus phocaena`, and the public right-label transcription `Panis 383`. This closes **catalogue offering 383 → surviving St Andrews object** at catalogue-offering identity level. It does not establish manufacture date, preparator, price or identity with a particular shipment copy. Preserve `Penis` and `Panis` as separate source readings. Current grading is in `../naples_row383_object_catalogue_closure_v4.json`.

## Files and authority

- `OBJECT_TEXT_BRIDGES_V1.csv` — verified bridge evidence and historical next-action prose. Treat status/next-action fields as dated routing metadata when they conflict with `../CURRENT_STATE.json`.
- `OPEN_PRIMARY_SOURCE_TARGETS_V1.csv` — retained v1 target table, now normalized to current CLOSED / OPTIONAL / PARKED dispositions. It is no longer an active search queue.
- `NAPLES_1880_CATALOGUE_423_PARSE_MANIFEST_V1.json` — authoritative manifest for the 423-offering parse.
- `NAPLES_1880_UK_CIRCULATION_CROSSWALK_V1.csv` — bounded UK circulation/exhibition event layer.
- `NAPLES_1880_UK_CIRCULATION_CROSSWALK_V1_README.md` — method and correction notes.
- `NAPLES_1880_RMS_12_SLIDES_ITEM_CROSSWALK_V1.csv` — twelve-slide RMS shipment crosswalk.
- `P1_TARGETS_1_2_OUTCOME_2026-08-09.md`, `P1_TARGET_3_NAPLES_1881_OUTCOME_2026-08-09.md`, `PROGRESS_LOG_2026-08-09.md` — historical dated research snapshots.

## Historical v1 routing snapshot

The original routing pass classified all 155 frozen nodes as 7 P1, 30 P2, 38 P3 and 80 P4; it generated 21 initial expansion gaps, 32 immediate bridges, 7 serial sets and 76 custody gaps. Those counts describe the **initial routing state**, not the present task queue. They are retained because they document how the object-first method was constructed.

## Working rules

- Inspect source context before promoting a name/OCR/taxon match to evidence.
- Keep exact identity, bounded programme correspondence and unresolved identity distinct.
- Keep catalogue offering, shipment object, surviving object, accession, serial position and database row in separate namespaces.
- Never infer preparation from ownership/use or `slides` from generic `objects/specimens`.
- When a chain is already sufficient for attribution, chronology, object identity or mechanism, additional prospectus/page hunting becomes optional rather than an automatic task.
- Do not use this directory to restart broad global or US corpus harvesting.
