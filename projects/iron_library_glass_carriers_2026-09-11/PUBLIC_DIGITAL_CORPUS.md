# Public digital corpus — acquisition map

Updated: 2026-09-11

Purpose: record what can be obtained remotely before any Iron Library residency application, and separate **remote-accessible evidence** from **onsite-only or object-dependent evidence**.

## Acquisition policy

The public repository stores stable locators, manifests, metadata and acquisition code. It does **not** automatically mirror whole third-party image corpora or recent copyrighted PDFs.

For research use:

- e-codices manuscript images may be downloaded for non-commercial research under its terms, but public republication can require source-specific permission. Keep bulk image downloads in a local ignored cache unless rights are explicitly clear.
- recent scholarship such as Droste 2024 should be downloaded locally for research if needed, not committed as a mirrored PDF.
- nineteenth-century public-domain books can be cached locally; commit only where repository size and source terms make that sensible.
- retain DOI/permalink/IIIF metadata in git so the corpus remains reproducible even when raw files stay local.

## A. Hermann Wedding: complete digitised manuscript baseline

| ID | Shelfmark | Date | Extent | Stable page | IIIF manifest | Status |
|---|---|---:|---:|---|---|---|
| WED-23 | Eisenbibliothek Mss 23 | 1856–1857 | 208 pp. | https://www.e-codices.ch/en/list/one/ebs/0023 | https://www.e-codices.ch/metadata/iiif/ebs-0023/manifest.json | fully digitised; remote baseline |
| WED-24 | Eisenbibliothek Mss 24 | 1858 | 98 pp. | https://www.e-codices.ch/en/list/one/ebs/0024 | https://www.e-codices.ch/metadata/iiif/ebs-0024/manifest.json | fully digitised; remote baseline |
| WED-25 | Eisenbibliothek Mss 25 | 1860–1862 | 328 + 48 pp. | https://www.e-codices.ch/en/list/one/ebs/0025 | https://www.e-codices.ch/metadata/iiif/ebs-0025/manifest.json | fully digitised; priority for Sheffield/Bessemer/person-network pass |

DOIs:

- `10.5076/e-codices-ebs-0023`
- `10.5076/e-codices-ebs-0024`
- `10.5076/e-codices-ebs-0025`

All three were placed online by e-codices on 2017-12-14.

### What to harvest

1. IIIF manifest JSON for reproducible metadata and canvas order.
2. Page images into a local `raw/e_codices/` cache only when needed.
3. A project-local page index recording date/place/person/process terms after manual reading.
4. For Mss 25, explicitly index `Sheffield`, `Bessemer`, named iron/steel works, introductions, hosts, engineers, metallurgists and any microscope/mineralogical language.

No OCR assumption: these are handwritten manuscripts. Image acquisition and reading are separate tasks.

## B. Johann Conrad Fischer digital travel-journal corpus

Digital edition:

- https://www.johannconradfischer.com/en/content/about
- https://www.johannconradfischer.com/en/travels
- editorial basis: https://www.johannconradfischer.com/en/content/editorial-guidelines

The 2023 edition contains seven journals (1794, 1814, 1825, 1825–1827, 1845, 1846, 1851), uses TEI Publisher, and is based on Iron Library copies digitised on e-rara. The editorial guidelines state that the texts were OCR-read from e-rara and checked against the reference copies.

Priority routes already identified:

- 1845 Sheffield itinerary: https://johannconradfischer.com/en/1845/28
- browse all journeys: https://www.johannconradfischer.com/en/travels

Use this corpus as an indexed pre-visit comparator. Do not mirror the complete modern digital edition into this public repository without an explicit reuse basis.

## C. Droste / Martens microphotographic plates

Bernhard Droste, `Bücher für die Eisenbibliothek. Reflexionen über gespendete Bücher zur Bestandserweiterung der Bibliothek`, *Ferrum* 93 (2024), 128–135.

Public article asset:

- https://archives.georgfischer.com/media/web/94722

Status:

- article accessible remotely;
- article documents donation of three original early microphotographic glass plates;
- figure credit connects the illustrated plates to `G 745,1`, but item-level semantics remain unresolved;
- the article itself is a research download, not a file to mirror into the public repo.

Local action: cache a copy for annotation if desired; keep its URL and bibliographic data under version control.

## D. Martens printed corpus

### 1893 volume

`Mitteilungen aus den Königlichen technischen Versuchsanstalten`, Band 11 (1893), Springer, 400 pp.

Google Play / Google Books record:

- https://play.google.com/store/books/details?id=ShwKAAAAIAAJ

The record is marked `Get for free`.

SLUB serial catalogue:

- https://katalog.slub-dresden.de/en/id/0-130127590

Important retrieval issue: SLUB catalogues a separate `Atlas: 10/11.1892/93` under shelfmark `01 8 00423`. Therefore text-volume access does not yet guarantee that Tafeln IV–XIII are present in the same digital object. Treat the plate sequence as unresolved until inspected.

Priority articles named by Droste:

- Adolf Martens, `Die mikroskopische Ausrüstung der königlichen mechanisch-technischen Versuchsanstalt` (1891), 278–293, Tafeln IV–VI;
- Adolf Martens, `Ueber die Ausstellung der Versuchsanstalt auf der Weltausstellung zu Chicago im Jahr 1893` (1893), 247f., Tafeln IV–VI;
- Adolf Martens, `Das mikroskopische Gefüge von Flusseisen in gegossenen Blöcken` (1893), 273–292, Tafeln VII–XIII.

Current acquisition status: exact free volume identified; stable automated binary endpoint for the 1893 Google copy not yet controlled; atlas remains a separate acquisition problem.

## E. Sorby / Wedding historiographical and contemporary controls

### Modern historical study

R. Edyvean and C. Hammond, `The metallurgical work of Henry Clifton Sorby and an annotated catalogue of his extant metallurgical specimens`, *Historical Metallurgy* 31.2, 54–85.

- landing page: https://hmsjournal.org/index.php/home/article/view/317

Use: establishes that Sorby/Wedding specimen-preparation and illumination disagreement is already historiographically visible; prevents false novelty claims.

### Contemporary microscopical discussion

*Journal of the Royal Microscopical Society* (1886) public PDF:

- https://www.microscopemuseum.eu/jrms/JRMS_1886.pdf

Use: contemporary discussion of Sorby's comments on Wedding's malleable-iron paper, including grinding/polishing and illumination.

## F. Story-Maskelyne / Percy / preparation network controls

Royal Society `Science in the Making`:

- Story-Maskelyne person page: https://makingscience.royalsociety.org/people/na6363/mervyn-herbert-nevil-story-maskelyne
- John Percy referee report on Story-Maskelyne's 1865 Cornish-minerals paper: `RR/5/143`, reachable from the person page.
- Story-Maskelyne referee report on Alfred Edwin Howard Tutton's section-cutting/grinding/polishing instrument, `RR/12/397`, 28 Dec 1894: https://makingscience.royalsociety.org/items/rr_12_397/referees-report-by-mervyn-herbert-nevil-story-maskelyne-on-a-paper-an-instrument-for-cutting-grinding-and-polishing-section-plates-and-prisms-of-mineral-or-other-crystals-accurately-in-the-desired-directions-by-alfred-edwin-howard-tutton

These are external controls, not Iron Library holdings unless independently found in IRONCAT.

## G. What cannot yet be replaced by remote acquisition

The following remain the high-value onsite / staff-enquiry layer:

- individual physical identities and full metadata of the three Droste glass plates;
- any unpublished markings, plate backs, mounts, envelopes, ordering or working sequence;
- undigitised GFA working papers/correspondence after item-level ANTON recheck;
- material features of historical photographs/albums/objects that catalogue images do not capture;
- the relationship between physical plates, printed Tafeln and archival description where no complete digital chain exists.

## H. Corpus architecture

Recommended local layout after running the acquisition helper:

```text
public_corpus/
  manifest.tsv
  fetch_public_corpus.py
  fetch_public_corpus.ps1
  raw/                     # ignored by git
    e_codices/
      WED-23/
      WED-24/
      WED-25/
    files/
  derived/                 # small research indexes may be committed selectively
```

The point is reproducibility, not mirroring. The git history should preserve **what source was used, where it came from, what was fetched, and what evidential role it has**.

## I. PowerShell acquisition workflow

The PowerShell helper is intended for a Windows checkout of the repository and works from `manifest.tsv`.

From the project directory:

```powershell
cd .\projects\iron_library_glass_carriers_2026-09-11\public_corpus
```

First test only the priority Wedding volume and fetch its IIIF manifest plus canvas/page index:

```powershell
.\fetch_public_corpus.ps1 -Only WED-25
```

Then fetch the complete Mss 25 image sequence into the git-ignored local cache:

```powershell
.\fetch_public_corpus.ps1 -Only WED-25 -IiifImages
```

Fetch all three Wedding manifests/indexes without downloading page images:

```powershell
.\fetch_public_corpus.ps1
```

Fetch all three Wedding image corpora:

```powershell
.\fetch_public_corpus.ps1 -IiifImages
```

Fetch rows explicitly marked `local_file` in `manifest.tsv`, such as the Droste public asset and JRMS 1886, into `raw/files/`:

```powershell
.\fetch_public_corpus.ps1 -LocalFiles
```

Combine selectors when desired:

```powershell
.\fetch_public_corpus.ps1 -Only WED-25,JRMS-1886 -IiifImages -LocalFiles
```

Existing files are skipped by default, making the downloader resumable. Use `-Force` only to overwrite existing local files. `-DelayMs 200` is the default pause between IIIF image requests and can be increased for a slower, more conservative harvest.

The PowerShell script supports both IIIF Presentation 2 and Presentation 3 structures. For each IIIF manuscript it writes:

- `manifest.json` — the source manifest;
- `canvas_index.tsv` — sequence number, page/canvas label and resolved image URL;
- `pages/*.jpg` — only when `-IiifImages` is supplied.

Raw downloads remain excluded from git by `public_corpus/.gitignore`.
