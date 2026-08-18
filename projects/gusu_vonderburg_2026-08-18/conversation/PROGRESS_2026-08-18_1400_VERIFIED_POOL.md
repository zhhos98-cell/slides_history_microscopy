# Progress checkpoint — verified-pool visual concordance

Date: 2026-08-18, afternoon +08:00

## Purpose of this checkpoint

This checkpoint supersedes any interpretation that treats `CMA 113 + Met 107 = 220` as independent evidence. The current visual-matching pass deliberately removes those arithmetic boundaries from the candidate pool.

## Boundary-independent visual pool v2

Workflow: `.github/workflows/gusu_sift_verified_pool.yml`
Builder: `scripts/build_verified_visual_pool.py`
Matcher: `scripts/match_public_book_samples_sift.py`
Derived result commit: `2fce5ef7b9e20a8c799f49054934f73b207e3974`
Output: `latest/public_book_sample_sift_verified_pool_v2/`

Candidate pool:
- CMA: 37 current 2025 Christer von der Burg API records exposing `image_web`.
- Met: 106 public-domain primary images from independently verified live accession range `2025.352–2025.460`.
- Total museum image candidates: 143.
- NO CMA-113, Met-107, or combined-220 count boundary was used.

Book/sample photographs:
- 15 harvested rows.
- 14 unique image URLs after exact-URL deduplication.
- 10 Wenwu publisher samples.
- 3 Guangzhou Daily samples.
- 1 unique Shuseido Japanese bookseller product image.

Strong visual rule remains conservative:
`homography_inliers >= 10 AND inlier_ratio >= 0.35`.

## Strong matches

The v2 run reproduces all earlier strong matches and adds one new independent photographic source.

### CMA 2025.84 — Gathering Osmanthus / 折桂圖

Wenwu publisher sample `175829778.jpg`:
- 1514 RANSAC inliers
- inlier ratio 0.9825
- independently agrees with confirmed book catalogue no. 52 / pp. 198–199 anchor.

### CMA 2025.108 — Bird on Pomegranate / 石榴上的鳥兒

Now independently visible in four public photographs from three source contexts:

1. Wenwu `175829776.jpg`: 251 inliers / 0.9061.
2. Wenwu `175829780.jpg`: 120 / 0.5405.
3. Guangzhou Daily image: 32 / 0.7111.
4. **NEW: Shuseido product image `192492972.png`: 16 / 0.64.**

For the Shuseido photograph, the second-ranked candidate has only 9 inliers. This new match was generated against the boundary-independent 143-image pool and therefore is not an artefact of the old 220 working manifest.

The persistent concordance table `latest/book_concordance/public_sample_visual_matches.csv` has been updated with the Shuseido row.

## Targeted audit: Met 2025.358 — May You Soon Bear Noble Sons / 早生貴子圖

Met 2025.358 is a verified public-domain Suzhou print, Qianlong period, 104 × 54 cm, and The Met describes it as one of the recently acquired trove of more than one hundred examples.

Within the **14 unique public book/sample photographs currently harvested**, it has NO strong geometric match.

Its appearances in sample top-20 lists include:
- Wenwu sample 4: rank 9, 8 inliers / 0.1013.
- Wenwu sample 8: rank 3, 10 / 0.25.
- Wenwu sample 11: rank 16, 7 / 0.1373.
- Guangzhou sample 5: rank 2, 8 / 0.1194; that photograph's actual strong identity is CMA 2025.108.

Therefore the maximum current support is 10 inliers / 0.25, below the predeclared strong threshold. This is a **negative result only for the current public sample-photo set**. It does NOT imply that 2025.358 is absent from the 220-entry book.

Persistent audit file: `latest/book_concordance/met_2025_358_public_sample_visual_audit.csv`.

## Met lower boundary correction

Met 2025.352 and 2025.353 must not be excluded merely to turn 109 live records into 107.

Independent official-object-page facts now recorded in `latest/met_v2/met_352_353_independent_audit_2026-08-18.csv`:

- `2025.352` A Scenic View of Minghuang’s Gardens / 唐明皇花園勝景: print, Qing/Qianlong, Public Domain, Download Image, credit line `Florence and Herbert Irving Acquisitions Fund for Asian Art, 2025`.
- `2025.353` New Year's Morning / 歲朝圖: explicitly `China, Suzhou`, dated 1747, woodblock print, Public Domain, Download Image, same 2025 acquisition fund.

No independent evidence has yet been recovered that assigns these two to a different acquisition. Their old exclusion was arithmetic, not documentary.

## CMA upper boundary remains unresolved

CMA 2025.129 `May You Soon Bear Noble Sons / 早生貴子圖` remains a verified March 2025 von der Burg sale/purchase record with the same accession date and J. H. Wade purchase context as the main group. It cannot be excluded merely because `2025.19–2025.128` plus record semantics reproduces the published count 113.

The current hard question remains book/acquisition-document level: whether CMA 129 is a catalogue member/impression related to Met 358, a related non-core print bought alongside the 113, or another case. The current public sample photographs do not resolve this.

## Next evidence targets

1. Recover catalogue number/page evidence for `早生貴子圖`, without assuming which museum impression is the book object.
2. Seek museum-side or catalogue-side evidence independently resolving CMA 129 and Met 352/353 boundaries.
3. Continue mining publisher/bookseller photographs for readable catalogue headers and plate numbers.
4. Promote a book concordance only when text/page evidence or strong visual identity supports it; never from accession arithmetic alone.
