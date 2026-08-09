# Analysis layers

Versioned derived research layers over the frozen surviving-object survey. Files here interpret, classify, route or crosswalk evidence; they do not rewrite frozen survey membership or source wording.

## Current modules

### `slide_155_analysis_v1/`

Derived analytical classification over all 155 frozen nineteenth-century nodes. It normalises unit level, production period, subject cluster, institutional/commercial context, circulation mode, count namespace and historical actor role. Review flags concern the derived classification, not the reliability of the frozen source row.

### `slide_155_corpus_expansion_v1/`

Object-first expansion into the nineteenth-century microscopy text corpus. It contains:

- contextual object↔text bridges;
- bounded primary-source targets;
- dated source-pass outcomes and research logs;
- the Naples 1880 423-offering catalogue manifest;
- Naples→UK circulation and RMS item crosswalks.

## Authority and editing rules

1. Preserve the frozen survey row as the underlying object/provenance evidence.
2. Store new interpretation in a new or explicitly revised analytical file rather than rewriting the source census.
3. Keep exact identity, bounded correspondence and unresolved identity distinct.
4. Positive OCR/name/taxon matches are routing signals until source context closes the relation.
5. Keep event, catalogue, shipment, exhibition and surviving-object identities separate unless explicit evidence connects them.
6. Record negative bounded checks when they materially constrain later searching.

The root `data/README.md` defines authority order across survey, evidence, analysis and compact corpus layers.
