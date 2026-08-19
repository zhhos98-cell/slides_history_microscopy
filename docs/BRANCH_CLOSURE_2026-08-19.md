# Branch closure ledger — 2026-08-19

This ledger records the disposition of the long-lived pre-V6 site/data/bibliography branches before their refs are normalized to current `main`.

## Canonical state

Current `main` is the only canonical branch for the microscopy repository. The repository has moved well beyond the August 9 V4/V5 site prototypes: the public corpus/data architecture was subsequently consolidated into V6 and followed by hundreds of research, bibliography, source, site, and Gusu commits.

The historical branch names may remain as aliases after closure, but they must not carry a competing data/site architecture.

## `site-backend-corpus-20260809`

Pre-closure state relative to the then-current main:

- 38 commits ahead of its old merge base;
- 481 commits behind current `main`;
- V4 compact corpus metadata, site layer, and major Pages rewrite.

The branch was not an unmerged final architecture. Its work was squash-integrated onto the mainline as commit:

- `9b199dd8066df6666a42a57fdce8d6f773730cdc` — `Publish microscopy backend metadata and research ledger`

Comparing the old branch to that checkpoint shows the mainline checkpoint as one squashed commit against the branch's 38-commit development history. That checkpoint exposes the compact corpus/research ledger while retaining large OCR/full-text/article payloads in canonical masters and preserving the frozen 155-object closure contract.

The same mainline then advanced through V5 and V6. Do not resurrect the branch's old `index.html`, `site.js`, `styles.css`, V4 pointer files, or V4 corpus manifest as a competing current site.

Disposition: **squash-absorbed and superseded by V5/V6; reset ref to current main.**

## `site-bna-derived-20260809`

Pre-closure state:

- 19 commits ahead of its old merge base;
- 480 commits behind current `main`;
- compact BNA V5 event-cluster/newspaper-yield layer and V5 manifest/index documentation.

The branch was squash-integrated on main as:

- `9de38a6ded4678263821055a8aa436982a2f5fb2` — `Publish complete compact BNA derived results`

Comparing the branch to that checkpoint shows one mainline squash commit against the branch's 19-commit development history. The mainline commit explicitly publishes the complete compact BNA derived layer (930 event clusters and 995 newspaper-yield rows) while keeping OCR/payload/large-text bodies in fingerprinted canonical masters.

Current `main` is 479 commits beyond that checkpoint and has since advanced corpus authority to V6.

Disposition: **squash-absorbed and superseded; reset ref to current main.**

## `repo-data-cleanup-20260809`

Pre-closure state:

- 25 commits ahead of its old merge base;
- 473 commits behind current `main`;
- data-layer READMEs/hygiene rules, removal of stale V4/V5 scaffolding, and Pages/data alignment.

Its mainline squash checkpoint is:

- `385c1cbcf94fa8e34fd643f907e78ec08db9589f` — `Clean and document microscopy repository data layers`

Comparing the branch to that checkpoint shows one mainline squash commit against the branch's 25-commit development history. Current `main` is 473 commits beyond this checkpoint and later records additional cleanup/audit, V6 manifest/output authority, and repository-integrity validation.

The companion refs `repo-data-cleanup-20260809-work` and `repo-data-cleanup-20260809-check` had no unique commits relative to main before closure.

Disposition: **squash-absorbed; work/check refs already historical; reset all three refs to current main.**

## `bibliography-south-asia-southern-africa-pass18-20260810`

This branch requires an explicit rejection record rather than a simple "absorbed" label.

The branch's broad pass-18 proposal contained 16 additions and would have moved the bibliography from 197 to 213 records. Its admission rule allowed a wider set of bounded institutional slide collections, pathology archives, teaching systems, and physical-slide/digital-transition records.

The mainline pass-18 commit is:

- `83649a9ab63906835529671990a20e8634e6060a` — `Add pass 18 South Asia Singapore and southern Africa bibliography`

Mainline deliberately narrowed the pass to 6 additions, producing 203 records after pass 18. Its documentation explicitly states that the pass is narrower than a geographic census and holds out generic current teaching facilities and other records without sufficiently strong collection/register structure. Later pass 19 separately admitted a tightly specified Wits / Van der Horst, Carter, and Wisconsin Mossman cluster.

Therefore the additional records remaining only on the old pass-18 branch are **not a forgotten batch to merge**. They belong to a rejected broader admission regime. They may be rediscovered/reassessed later from current main under a new explicit scope decision, but the obsolete branch must not silently override the narrower mainline corpus policy.

Disposition: **broader alternative rejected/superseded; reset ref to current main.**

## Earlier bibliography branches

The earlier bibliography development branches (multilingual/web/slide-locked passes and regional passes through pass 17) had already contributed their accepted records to the mainline and had no unique commits in the prior branch audit. Current main has continued through pass 18, pass 19, bibliography 01–22, manifest normalization, and later research/site development.

Disposition: **historical aliases only; reset refs to current main.**

## `uk-us-return-to-core-20260810`

Pre-closure comparison showed no unique commits relative to current main (ahead 0; behind 288). Its accepted work is already part of the mainline research state.

Disposition: **historical alias; reset ref to current main.**

## `backup/gusu-vonderburg-2026-08-18`

Pre-closure state showed exactly one unique file:

- `projects/gusu_vonderburg_2026-08-18/BACKUP_STATE.md`

The mainline project README already referenced this file even though it was absent from main. The 50-line provenance/state document has therefore been restored to main before closing the backup ref. Current main contains roughly ninety subsequent Gusu commits beyond the backup branch's merge base, including later official API/bulk audits, verified visual pools, book reconstruction, textual ancestry, and series work.

Disposition: **unique provenance file salvaged to main; backup ref may now be reset to current main.**

## Explicitly untouched

`pages-blaschka-design-20260809` is intentionally excluded from this closure pass. Blaschka work is outside the requested closure scope and this ledger makes no disposition decision about that branch.

## Closure rule

After ref normalization, all non-excluded historical branches covered above should compare to `main` as `ahead 0 / behind 0`. Future microscopy work should start from current `main`; old branch names must not be revived as alternate V4/V5 or broad-bibliography authorities.
