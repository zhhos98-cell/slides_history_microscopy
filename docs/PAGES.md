# GitHub Pages site

Live site: https://zhhos98-cell.github.io/slides_history_microscopy/

Launched: 2026-08-09
Source: `main:/`

## Design

The site reuses the visual grammar of the Blaschka corpus site without sharing project data or code: warm paper ground, dark full-height hero, thin archival grid lines, large serif display type, mono evidence labels, compact statistics, and numbered research sections. The microscope-slide project uses a cyan/teal accent and a CSS-built three-slide hero object rather than a Blaschka image.

Files:

- `index.html` — research narrative and interface shell;
- `styles.css` — responsive visual system;
- `site.js` — frozen-catalogue reconstruction, integrity check, search and filters;
- `.nojekyll` — direct static serving;
- `pages-version.txt` — lightweight build marker.

## Frozen catalogue contract

The browser does not treat a hand-edited web table as authoritative. `site.js` rebuilds the strict catalogue directly from the committed closure inputs:

1. load all strict batch CSVs `07K`–`07AQ`;
2. remove IDs listed in `07AR_SUPERSEDED_ALIASES_2026-08-09.json`;
3. collapse repeated identical `entry_id` occurrences;
4. apply `scope_19c_overrides.json`, retaining explicit `CORE_19C` rows and excluding explicit non-core/held-out rows;
5. apply `07AR_FINAL_QC_OVERRIDES_2026-08-09.json` for display-only institution/count clarification;
6. assert exactly **155** frozen rows.

If the browser-side reconstruction does not return 155 rows, the explorer reports an integrity failure instead of silently presenting a changed catalogue.

## Research content currently surfaced

The landing page exposes the current sealed/project state rather than a generic museum showcase:

- 155-node frozen nineteenth-century object/provenance layer;
- object↔text bridge logic and verified Eulenstein, Collins Jr., H. L. Smith and Kitton cases;
- Naples 1880 catalogue module: 423 historical offerings;
- the 9 June 1880 RMS twelve-slide shipment and nine exact/strong catalogue matches;
- the explicit `NOT_ASSERTED` guard against turning catalogue correspondence into surviving-object identity.

## Editing rule

The Pages site is a presentation layer. It must not silently reopen the `CLOSED_2026-08-09` survey. New historical findings belong in versioned analytical/provenance files first. The website can then surface those results after the underlying research layer is committed.
