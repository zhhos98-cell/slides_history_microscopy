# Data cleanup — 2026-08-09

This pass cleans the repository tree without altering the frozen microscope-slide census or deleting substantive research evidence.

## Principles

1. Preserve canonical survey batches and closure metadata because they are the executable audit trail.
2. Preserve versioned analytical/evidence outputs even when later work supersedes an interpretation; Git history alone is not used as a substitute for a research audit trail.
3. Remove transient marker files, duplicated micro-documentation and ambiguous stale summaries when their useful content has been consolidated into a current README or manifest.
4. Keep bulk OCR/full-text/article payloads outside the compact Pages layer; retain hashes and counts in the current corpus manifest.
5. Prevent runtime/build outputs from being committed accidentally.

## Corpus layer after cleanup

Current publication contract: `data/corpus/CORPUS_MANIFEST_V5.json`.

Retained data families:

- V4 core document chunks, because their contents did not change when the publication contract advanced to V5;
- V4 extension document chunks for the same reason;
- V4 BNA metadata/query/year tables reused by V5;
- V5 complete compact BNA event-cluster and newspaper-yield tables;
- V4 research-output ledger reused by V5;
- V5 publication check;
- V4 predecessor manifest as explicit provenance.

The mixed V4/V5 suffixes therefore encode derivation history. They are not competing current layers.

## Removed as repository clutter

The following files were transient, redundant, stale or fully folded into `data/corpus/README.md`:

- `data/corpus/README_POINTER.txt`;
- `data/corpus/OMISSION_POLICY.md`;
- `data/corpus/SITE_LAYER_STATUS.md`;
- `data/corpus/VERSION`;
- `data/corpus/LAYER_COUNTS.json`;
- `data/corpus/LAST_UPDATED`;
- `data/corpus/NOTE`;
- `data/corpus/_PUBLIC_SITE_LAYER`;
- `data/corpus/CANONICAL_MASTER_SCOPE.md`;
- `data/corpus/SCHEMA_NOTES.md`;
- `data/corpus/BNA_YIELD_README.md`;
- `data/corpus/INDEX.md`;
- ambiguous superseded `data/corpus/PUBLICATION_CHECK_2026-08-09.json`.

Their substantive current information is retained in `data/corpus/README.md`, `CORPUS_MANIFEST_V5.json` and `PUBLICATION_CHECK_V5_2026-08-09.json`. Their exact previous states remain recoverable from Git history.

## New hygiene and navigation files

- `.gitignore` excludes runtime `outputs/`, `data/normalized/`, local artifacts, Python caches and editor/OS noise.
- `data/README.md` defines the authority and relationship of `survey/`, `analysis/`, `evidence/` and `corpus/`.
- `data/survey/README.md` documents the frozen survey/audit-trail structure.
- `data/analysis/README.md` documents derived-analysis authority.
- `data/evidence/README.md` documents retained harvesting evidence.

## Pages alignment

The website loader and data ledger now point to `CORPUS_MANIFEST_V5.json`. The interactive BNA panel remains a query-yield browser, while the site explicitly links the complete compact V5 event-cluster and newspaper-yield tables.

## Explicit non-changes

This cleanup does not change:

- any `07K`–`07AQ` strict survey batch;
- the 07AR alias map, closure manifest, final QC or scope overrides;
- the frozen count of 155 strict nineteenth-century nodes;
- any object-to-text or Naples research output;
- any targeted-harvest evidence record;
- any source-master fingerprint in the V5 corpus manifest.
