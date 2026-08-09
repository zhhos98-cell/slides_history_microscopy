# Microscope Slides and the Social Life of Microscopy

**Live site:** https://zhhos98-cell.github.io/slides_history_microscopy/

This repository supports a public research site on nineteenth-century microscope slides, their circulation, surviving collections, and the textual worlds around them.

The project connects surviving slides and provenance records with periodicals, newspapers, catalogues, society reports, dealers, collectors, institutions, and other historical evidence. The public site is intended as a research atlas and dataset rather than a complete archive of the working corpus.

## Public site

The GitHub Pages site is the primary public interface:

https://zhhos98-cell.github.io/slides_history_microscopy/

It currently provides access to the frozen nineteenth-century object/provenance census, source-level microscopy metadata, selected British Newspaper Archive-derived tables, and research connections built from the underlying corpus.

## Data status

The nineteenth-century object/provenance census is frozen at **155 records** under status `CLOSED_2026-08-09`.

The microscopy source layer currently represents:

- 142 core documents
- 60 extension documents
- 2 structured OCR sources
- 9,365 BNA article records in the canonical master
- 930 published BNA event clusters
- 995 published BNA newspaper-yield rows
- 43 BNA query-yield rows
- 71 BNA year-yield rows

The repository publishes compact metadata and derived research data. Bulk OCR, page-level text, and article-level payloads remain in the canonical research masters and are intentionally excluded from the public repository.

## Repository structure

- `index.html`, `styles.css`, `site.js` — GitHub Pages frontend
- `data/survey/` — frozen object/provenance census and closure metadata
- `data/corpus/` — compact publication layer derived from the microscopy masters
- `data/analysis/` — selected derived research outputs
- `data/evidence/` — normalized evidence used for cross-source connections
- `scripts/` — reproducibility and dataset-building utilities
- `docs/` — project and data documentation

## Data principles

The public data layer preserves provenance and evidential limits. Current custody is kept distinct from historical ownership and circulation. Object identity is asserted only when the underlying evidence supports it. Quantities are interpreted within their source-specific namespaces rather than treated as automatically commensurable.

The public site may simplify or normalize display fields, but it does not silently overwrite canonical source records or the frozen census membership.

## Version

Current public data release: **2026-08-09**

Object census: **CLOSED_2026-08-09 / 155**
