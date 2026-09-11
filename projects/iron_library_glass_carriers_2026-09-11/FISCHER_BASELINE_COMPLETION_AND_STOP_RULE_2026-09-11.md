# Fischer 1845–1846 baseline — completion audit and stop rule

Status: **baseline extraction complete for current supplied OCR texts**, 2026-09-11.

This does not mean every sentence has been exhaustively indexed. It means the current Fischer corpus has been saturated for the analytical categories needed to compare against Wedding/Martens. Further Fischer work should be triggered by a genuinely new mechanism or by a Wedding comparison problem, not by accumulation of redundant examples.

## Source control

Canonical working sources:

- 1845: `Notizen auf der Reise über Paris nach London, Leeds, Low-Moor, Sheffield, und zurück im Sommer 1845.txt`;
- 1846: `Notizen auf meiner Reise über Carlsruhe, Mannheim, Cöln, und Ostende nach London, Derby, Wingfield, Alfredton und Butterly Ironworks nach Sheffield, Liverpool, und zurück über Sheffield und London nach Schaffhausen...txt`.

A second 1845 OCR witness exists but is treated as a duplicate/noisier witness unless needed for text-critical checking.

These are research OCR/transcription aids, not diplomatic transcriptions.

## Saturated analytical layers

The current extraction now controls the following distinct mechanisms.

### Observation / measurement

`AUTOPSY | SEE | COUNT | MEASURE | WEIGH | CALCULATE | SENSORY_JUDGEMENT | RELIABILITY_WARNING`

Examples include furnace-light uncertainty, ruler use, counting, requested weighing, calculation, spring testing, and bodily temperature/taste judgement.

### Access / credibility

`RECOMMENDATION | PRIOR_RELATION | SPONTANEOUS_ACCESS | PRIVILEGED_ACCESS | TECHNICAL_CREDIBILITY | CREDIBILITY_PERFORMANCE | INSTITUTIONAL_CREDENTIAL | WEAK_GUIDE`

Factory visibility is demonstrably tiered and mediator-dependent.

### Knowledge boundaries

`PUBLICATION | PRACTICAL_COMPETENCE | PATENT_PRIORITY | SECRET | SELECTIVE_DISCLOSURE | RECIPROCAL_EXCHANGE | DEMONSTRATION | DOCUMENT_COPY | WITHHOLDING`

The corpus supports coexistence of publication, practical competence, legal priority, secrecy and selective disclosure rather than a single transition from tacit craft to open knowledge.

### Sample / identity / reference

`DEMONSTRATION_SAMPLE | TRACE_SAMPLE | BATCH_IDENTITY | STAGED_SERIES | REFERENCE_QUALITY_SAMPLE | PREPARED_TEST_OBJECT | OBJECT_INSCRIPTION | SAMPLE_DONOR | SAMPLE_RECIPIENT | PROVENANCE_LOSS | CATALOG_NUMBERING`

Important distinctions:

- Low Moor: sample from every tapping + batch numbering;
- Low Moor: staged series across production states;
- Royal Mint: tested `Musterstange` becomes reference quality for future supply;
- Fischer steel objects: repeated maker/name marking before external transformation in Sheffield (1845 Huntsman hammer work; 1846 Rodgers razor blades);
- Fenn: unknown railway-scrap quality and mixed remelting as provenance-loss inverse case;
- Polytechnic Institution: catalogue numbering as collection-ordering control.

### Testing / transformation

`INSTITUTIONAL_TEST | APPARATUS_TEST | EXPERT_JUDGEMENT | SURFACE_PROCESS_EXPERIMENT | PREPARED_TEST_OBJECT`

The corpus includes Royal Mint distributed testing, Sheffield spring `Probemaschine`, skilled grinding/polishing followed by judgement, and a proposed matrix surface-protection experiment involving galvanic gilding before hot sinking.

### Portable representations

`DRAWING | IMAGE | PHOTOGRAPHIC_REPRODUCTION | LETTER_AS_AUTHORITY`

Beck works drawings circulate technically; Croucher converts a foundry drawing into negative/positive photographic form; Brande's test letter travels back into Sheffield as portable institutional authority.

### Iterative circulation

`ITERATIVE_CIRCUIT | REPEAT_SUPPLY`

The 1845 and 1846 journeys are controlled as one repeating material/document/testing circuit:

`journey -> sample/order -> remote shipment -> external test -> written judgement -> repeat supply -> return journey -> reuse of authority in later encounters`.

## Last audit pass

A final keyword-oriented audit was run across the supplied canonical 1845/1846 texts around:

- `Versuch`;
- `Probe`;
- `Muster`;
- `untersuch...`;
- `Zeichnung`;
- `Nummer`;
- `bezeichnet / gezeichnet / meinem Namen`;
- patent/secrecy/access terms already extracted in earlier passes.

Two useful late additions resulted:

1. **surface-process experiment** — Fischer proposes galvanically gilding coin matrices before hot sinking to prevent surface scale; Brande considers the experiment worth making;
2. **repeated object inscription** — Fischer explicitly marks his own steel with his name before external Sheffield transformations in both 1845 and 1846, upgrading `OBJECT_INSCRIPTION` from an incidental detail to a repeated provenance practice.

No new high-level mechanism emerged that requires restructuring the current schema.

## Fischer stop rule

Do **not** continue broad Fischer keyword mining merely to accumulate more examples of already saturated categories.

Reopen the Fischer texts only if one of the following occurs:

1. Wedding Mss 23–25 produce a mechanism not represented in the current Fischer baseline;
2. a Wedding passage needs a direct Fischer control for a specific person, works, sample, technique or access practice;
3. a citation-ready claim requires verification against the second OCR witness or original page image;
4. a new object/document in the Iron Library archive can be linked to one of Fischer's travelling samples, drawings, letters or marked materials;
5. a post-return German source creates a concrete genealogy hypothesis that needs testing backward against Fischer.

## Immediate next step

The next substantive corpus is Wedding, especially `Mss 25`.

Apply the controlled Fischer schema to Wedding without assuming similarity. The first task is to reconstruct:

- itinerary and dates;
- Sheffield / Bessemer / named works;
- access brokers and levels of visibility;
- source of each technical datum;
- samples, labels, marks, drawings and copied information;
- testing/measurement operations;
- knowledge withheld or exchanged;
- any continuing correspondence/material circuit after Wedding leaves Britain;
- any genuine specimen-preparation, microscopic or mineralogical language.

Only after the British phase is controlled should the analysis move to Wedding's return to Berlin and then to Martens / Charlottenburg material testing and microphotographic reference collections.

## Dependency status

Local Mss 23/24/25 image acquisition has been reported complete. A separate OCR/JSON workflow was specified, but no actual Wedding OCR JSON has yet been confirmed in the GitHub project at the time of this note.

Until those files appear, do not invent Wedding page-level findings from the Fischer control case.
