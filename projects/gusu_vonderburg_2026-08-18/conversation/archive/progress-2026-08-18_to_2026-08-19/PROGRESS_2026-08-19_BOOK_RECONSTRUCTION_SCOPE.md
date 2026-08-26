# Gusu book reconstruction scope — 2026-08-19

## Research question

The operational target is no longer merely “how many museum images can be downloaded?” but **how much of the published two-volume catalogue can be reconstructed from public evidence**.

Book: *Chinese Gusu Prints in the Christer von der Burg Collection* / 《欧洲冯氏藏中国姑苏版画》.

## Corpus identity: now directly supported

A 22 April 2026 interview with Clarissa von Spee / Shi Mingli published by Souquee records Christer von der Burg’s own statement that the **220 prints acquired by the Cleveland Museum of Art and the Metropolitan Museum of Art are all the works included in the published book**.

Source:
https://www.souquee.com/news/interview-or-how-did-this-rare-batch-of-suzhou-woodblock-prints-end-up-in-the-ha

Relevant interview statement is near the end of the article, where von der Burg states that the 220 acquired prints are all works included in the book.

This is stronger than the earlier arithmetic hypothesis `CMA 113 + MET 107 = 220`. It establishes the museum corpus as the correct reconstruction target while **not** establishing museum accession order as book order.

Publicity still contains a 220/221 count conflict. Preserve that conflict in bibliographic notes; do not silently normalize it. For reconstruction, use the directly stated 220-object museum/book identity as the working corpus unless contrary primary evidence appears.

## Reconstruction levels

### Level A — target object corpus

Working target: **220 book prints**.

Status: corpus identity is strongly supported by the acquisition interview, but individual boundary questions inside the CMA/MET accession sets remain documentary problems. Do not resolve them by arithmetic alone.

### Level B — recoverable plate image

Current conservative official-original lower bound already recorded in the repository:

- CMA-v1.5: 113 working physical units, **36** official full/open-access images.
- MET-v2: 107 working units, **104** public-domain original images.
- Conservative official-original image lower bound: **140/220 = 63.64%**.

A later boundary-independent visual pool contains 37 CMA 2025 von der Burg API records exposing `image_web` plus 106 independently verified Met public-domain primary images, 143 museum image candidates total. This larger pool is useful for matching, but it must not be converted into a 143/220 book-reconstruction claim until boundary membership is independently resolved.

### Level C — public evidence that a specific museum object appears on a photographed book page/sample

Currently **3 unique museum objects** have such evidence:

1. CMA 2025.84 — *Gathering Osmanthus* / 折桂圖.
2. CMA 2025.26 — *Portraits of the Outlaws of the Marsh* / 水滸繡像全圖.
3. CMA 2025.108 — *Bird on Pomegranate* / 石榴上的鳥兒.

### Level D — exact or usable book position

Currently only **2 unique objects** have page-position anchors:

- Catalogue no. **52**, pp. **198–199** (page reading medium confidence) → CMA 2025.84, *Gathering Osmanthus* / 折桂圖.
- pp. **158–159** → CMA 2025.26, *Portraits of the Outlaws of the Marsh* / 水滸繡像全圖. Catalogue number unresolved.

Only one object currently has a hard catalogue-number anchor: **no. 52**.

CMA 2025.108 / *Bird on Pomegranate* is visually identified in multiple independent photographs, but its catalogue number and pages remain unresolved.

## Public book-photo pool already harvested

The current link harvest contains **14 unique likely book/sample image URLs** after exact-URL deduplication:

- 10 Wenwu / Cultural Relics Press images (`175829776.jpg`–`175829785.jpg`);
- 3 Guangzhou Daily / Huacheng images;
- 1 Shuseido Japanese bookseller product image.

These photographs should now be treated primarily as **layout / catalogue-number / page-number evidence**, not merely as visual-identification inputs.

## Newly identified public-source targets

### Muban Educational Trust book launch, 11 April 2026

The Muban Educational Trust launch page exposes multiple original event-image URLs. These should be harvested and visually checked for open-volume photographs, readable page spreads, catalogue headers, or table-of-contents material.

Page:
https://www.mubaneducationaltrust.org/news/suzhou-prints-book-launch-in-china

Observed image filenames include:

- `IMG_3159.JPG`
- `IMG_3167.JPG`
- `IMG_3160.JPG`
- `IMG_3165.JPG`
- `IMG_3164.JPG`
- `IMG_3163.JPG`
- `IMG_3161.JPG`
- `IMG_3053.jpg`

Do not count these as book-page evidence until an image actually shows readable book content.

### Souquee acquisition interview

The interview provides independent confirmation that the museum acquisition corpus is the book corpus and also illustrates named members of the collection. It is useful for corpus control and title/image cross-checking, but it does not itself establish book order.

## Next hard workflow

1. Re-read every harvested public book photograph for **page number, catalogue number, title, neighboring entry, volume, running header, and visible section heading**.
2. Treat even partial neighboring text as useful adjacency evidence.
3. Expand the public-photo hunt across publisher, bookseller, launch, review, social/news, library, and exhibition pages.
4. Maintain separate fields for:
   - museum-object identity;
   - appears-in-book evidence;
   - catalogue number;
   - physical page number;
   - volume;
   - adjacency / ordering evidence;
   - commentary-text recovery.
5. Never substitute museum accession order for book order.
6. Keep the conservative 140/220 official-image lower bound separate from book-order reconstruction coverage.

## Practical interpretation

At present the project can plausibly reconstruct a large majority of the **image corpus** if the museum records are fully harvested, but only a tiny fraction of the **book as an ordered documentary object**. The highest-value work is therefore recovering and reading more photographed book spreads, not merely increasing the museum-image count.
