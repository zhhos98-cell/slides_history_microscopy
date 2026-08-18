# Gusu book-concordance checkpoint — 2026-08-18

## Hard / high-confidence results

1. **Book catalogue no. 52 / pp. 198–199 → 折桂圖 / Gathering Osmanthus → CMA 2025.84, API id 679112.**
   - Book header visibly gives `52`, `折桂圖`, `ZHE GUI TU`, `GATHERING OSMANTHUS`.
   - The photographed plate composition agrees with the official CMA work.
   - Publisher sample `175829778.jpg` independently matches CMA 2025.84 by SIFT + RANSAC with **1514 homography inliers, inlier ratio 0.9825**.
   - Page reading `198–199` is retained at medium confidence because numerals are soft.

2. **Book pp. 158–159 → 水滸繡像全圖 → CMA 2025.26, API id 678657.**
   - Horizontal right-to-left title on the photographed spread is read as `水滸繡像全圖`.
   - CMA English title is *Portraits of the Outlaws of the Marsh*; raw Chinese field `⽩滸綉像全圖` is preserved unchanged and separately normalized editorially.
   - This is a page anchor, not yet a catalogue-number anchor.

3. **Bird on Pomegranate / 石榴上的鳥兒 → CMA 2025.108, API id 679347** is visually identified in three independent public sample photographs:
   - Wenwu `175829776.jpg`: 251 homography inliers, ratio 0.9061.
   - Wenwu `175829780.jpg`: 120 inliers, ratio 0.5405.
   - Guangzhou Daily image 3: 32 inliers, ratio 0.7111.
   - Catalogue number/page remain unresolved.

4. Calibrated Latin/digit OCR passed its control:
   - Wenwu `175829778.jpg` recovered known catalogue number **52**.
   - It also recovered `Gathering` / `Osmanthus` signal.
   - Therefore OCR can be used as candidate evidence, but only under the explicit calibration rule below.

## OCR numbers that are NOT yet book numbers

For Bird-on-Pomegranate samples, broad OCR produced inconsistent candidates:
- Wenwu 776 included `36`, `58`, and other numbers in different ROIs/PSMs.
- Wenwu 780 included `33`, `44`, etc.
- Guangzhou image 3 included `47`, `73`, etc.

**None of these is promoted.** The next planned plate-aware pass first locates the plate by SIFT/homography and OCRs only metadata outside that polygon. A Bird number requires recurrence in control-calibrated ROIs and page-layout plausibility.

## Current visual coverage distinction

Working museum-unit 220:
- CMA-v1.5: 113 units, 36 official full/open-access images.
- MET-v2: 107 units, 104 public-domain original images.
- Combined official-original lower bound: **140/220 = 63.64%**.

This remains museum-unit coverage, not a verified 140-of-220 book-entry concordance.

A separate von der Burg blog index is being built to measure `online viewable` coverage outside museum OA. Blog images must remain link-only unless rights are independently confirmed and must never be counted as museum OA downloads.

## Public sample-source expansion

Cloud HTML harvesting has already recovered:
- 10 Wenwu publisher sample-image URLs (`175829776.jpg`–`175829785.jpg`).
- 3 Guangzhou Daily original OSS sample-image URLs.

The harvester has now been expanded to include the Japanese bookseller Shuseido product page (`pid=192492972`), but its expanded output is not yet considered available until a bot result commit appears.

## Explicit non-results / deprecations

- Whole-image dHash/aHash ranking is deprecated for identification: known true #52 did not rank reliably because photographed book pages differ too strongly from museum scans in crop/perspective/colour.
- Met bulk CSV is stale for this acquisition (data stops before 2025); live Collection API is authoritative for the 2025 Met records in this project.
- Search-index absence is never treated as proof of museum-record absence.

## Active but not yet harvested output

At the time of this checkpoint, no result file has yet appeared for:
- `plate_aware_ocr/summary.json`
- expanded Shuseido link-harvest output
- `vonderburg_blog_visuals/summary.json`

Do not infer failure or result from workflow trigger commits alone. Only bot-produced result files/commits count as completed outputs.
