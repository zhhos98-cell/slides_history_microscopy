# External link / dead-pointer audit — 2026-08-10

Status: **AUTOMATED PASS COMPLETE / MANUAL DEAD-CANDIDATE CHECK COMPLETE**

This audit checks current public bibliography and canonical source-registry routes only. It does not scan historical snapshots, superseded source rows, excluded cross-project rows, or the frozen survey as if those were live public links.

## 1. Method

`scripts/audit_external_links.py` performs concurrent HTTP GET checks against unique bibliography and canonical source-registry URLs. The current version follows redirects and treats common anti-bot responses such as 401/403/429 as reachable-but-restricted rather than dead.

A first pass exposed two methodological false-positive classes: institutional servers rejecting ranged requests, and live sites returning different responses to automated clients. The checker was therefore revised so that 404, 410 and 416 responses are retried without the Range header using a browser-style user agent. Even after retry, 404/410 is classified only as `dead_candidate`; deletion still requires manual confirmation.

## 2. Refined automated result

GitHub Actions run `31364908904` checked **384 unique URLs**:

- bibliography unique URLs: **269**;
- canonical source-registry unique URLs: **122**;
- `ok`: **263**;
- `reachable_but_restricted`: **75**;
- `dead_candidate`: **1**;
- network/TLS/timeout/server review states: **45**;
- total manual-review queue including the dead candidate: **46**;
- redirects followed: **49**.

The integrity job and link-audit job both passed. The generated machine-readable and Markdown reports are retained as the workflow artifact `external-link-audit` for the run.

## 3. The only 404/410 candidate is not dead

The automated checker returned 404 twice for:

`https://repertorium.library.uu.nl/collectie/zoologisch-museum/`

This route belongs to `NL-UTRECHT-ZOOLOGICAL-MUSEUM`.

Manual browser/search verification on the same date recovered the page as the live Utrecht University Repertorium record **Collectie Zoölogisch Museum**, including the collection history from the Bleuland material through Hubrecht-era museum development.

**Disposition:** keep the existing URL. The automated 404 is a client/server behaviour mismatch, not confirmed link death.

Result: **zero confirmed dead pointers among the 404/410 candidates in the current public layers**.

## 4. Stale routes actually corrected

### Croatian National Collection of Diatoms

The bibliography row `src_croatia_national_diatoms_2019` used an older `camen.pmf.unizg.hr` history URL that failed TLS validation. The Faculty of Science now exposes the same Department of Biology history page at:

`https://www.pmf.unizg.hr/biol/en/about_us/history`

The current page still identifies the Croatian National Collection of Diatoms as a collection of permanent microscopic preparations established in 2018 and states a current total of more than 4,000 preparations. The bibliography row already preserves the dated 2019 >6,000 statement separately, so only the current verification route was changed; the two count states were not normalized.

### Cajal / Simurg

The source-registry record `ES-MNCN-CAJAL-LEGACY` used the older Simurg item-style route `https://simurg.csic.es/view/2071353`. MNCN's current Cajal page now points to the collection-level Simurg route:

`https://simurg.csic.es/collection/1868040/espacio-cajal`

The current Simurg collection is indexed as **Espacio Cajal** and exposes a dedicated microscopic-preparation category. The source-registry secondary URL was therefore updated to the collection route. Automated TLS validation remains problematic for Simurg, so the link is retained as a manually verified current route rather than marked `ok` by the crawler.

## 5. Scope contamination caught by the link pass

The link review also surfaced `GB-SHEFFIELD-SORBY`. This is not a dead-link problem and not a duplicate-route problem. It is a cross-project residue.

The raw source row remains in its historical chunk, but `source-registry-manifest.json` now lists it under `excluded_ids`. Current/public routing suppresses it along with the three superseded duplicate routes.

Current source-registry arithmetic is therefore:

- raw rows: **87**;
- superseded duplicate routes: **3**;
- excluded out-of-scope routes: **1**;
- canonical/public routes: **83**.

## 6. Remaining review states

The remaining 45 non-404 review URLs are not treated as dead. They cluster into recognizable infrastructure/client failures:

- `microscopist.net` pages repeatedly reset automated connections;
- Simurg and several institutional sites expose TLS/certificate problems to the GitHub runner;
- some Fiocruz, UCM, repository and museum pages time out;
- a small number of sites return 5xx or network-unreachable states;
- many otherwise usable institutional/publisher routes return 403 or 429 and are already classified separately as reachable-but-restricted.

Representative manual checks showed why these statuses must not trigger deletion: the Whipple collection object page was live despite the automated timeout; the MNCN Cajal page was live despite the initial range-related failure; and the Utrecht page was live despite the repeated automated 404.

The old `mncn.bmtest.es` Caballero article route remains in the review queue. The current MNCN blog index still exposes the 2015 article title, but an exact stable replacement article URL has not yet been established. It should therefore remain flagged rather than be replaced with a guessed slug.

## 7. Redirect policy

The run followed 49 redirects. Most are normal DOI resolution or harmless institutional canonicalization. They are not automatically rewritten because the original route may be the more durable identifier (especially DOI/handle links).

Non-identifier redirect targets should be normalized only when the institution has clearly moved to a new canonical hostname or path and the replacement is independently verified. The Croatian Faculty of Science correction above meets that threshold; ordinary DOI resolution does not require rewriting.

## 8. Current policy

1. Automated 404/410 is a **candidate**, not a deletion decision.
2. 401/403/429 is treated as restricted/reachable, not dead.
3. TLS, timeout, DNS, connection reset and 5xx results remain manual-review states.
4. Stable identifiers such as DOI/handle URLs are generally retained even when they redirect.
5. Institutional URL replacement requires a verified current route; no guessed slug/path normalization.
6. Link auditing may expose duplicate or scope problems, but those are resolved in the appropriate manifest rather than by deleting raw audit evidence.

This pass therefore closes the immediate dead-pointer cleanup with **zero confirmed dead current pointers**, two verified route refreshes, one cross-project source exclusion, and a bounded host/network review queue that does not justify further destructive cleanup.
