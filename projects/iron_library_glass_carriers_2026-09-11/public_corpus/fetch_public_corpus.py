#!/usr/bin/env python3
"""Fetch remote-accessible Iron Library research sources into a local ignored cache.

Default behaviour is conservative:
- fetch IIIF manifests listed in manifest.tsv;
- do not fetch page images unless --iiif-images is supplied;
- do not fetch local_file rows unless --local-files is supplied;
- never writes outside public_corpus/raw/.

Raw downloads are research working files and should not be committed automatically.
"""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "manifest.tsv"
RAW = ROOT / "raw"


def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value.strip())
    return value.strip("_") or "source"


def fetch_bytes(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "slides-history-microscopy research fetcher/1.0"},
    )
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()


def fetch_json(url: str) -> dict:
    return json.loads(fetch_bytes(url).decode("utf-8"))


def save_bytes(path: pathlib.Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def iiif_image_url(resource: dict) -> str | None:
    service = resource.get("service")
    if isinstance(service, list) and service:
        service = service[0]
    if isinstance(service, dict):
        base = service.get("@id") or service.get("id")
        if base:
            return base.rstrip("/") + "/full/full/0/default.jpg"
    return resource.get("@id") or resource.get("id")


def harvest_iiif(row: dict, include_images: bool) -> None:
    source_id = slug(row["id"])
    out_dir = RAW / "e_codices" / source_id
    out_dir.mkdir(parents=True, exist_ok=True)

    manifest = fetch_json(row["url"])
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    canvases = []
    sequences = manifest.get("sequences") or []
    if sequences:
        canvases = sequences[0].get("canvases") or []

    index_rows = []
    for i, canvas in enumerate(canvases, start=1):
        label = canvas.get("label", str(i))
        images = canvas.get("images") or []
        image_url = None
        if images:
            resource = images[0].get("resource") or {}
            image_url = iiif_image_url(resource)
        index_rows.append((i, label, image_url or ""))

        if include_images and image_url:
            suffix = pathlib.Path(image_url.split("?", 1)[0]).suffix or ".jpg"
            filename = f"{i:04d}_{slug(str(label))}{suffix}"
            save_bytes(out_dir / "pages" / filename, fetch_bytes(image_url))
            print(f"downloaded {row['id']} page {i}: {label}")

    with (out_dir / "canvas_index.tsv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, delimiter="\t")
        writer.writerow(["sequence", "label", "image_url"])
        writer.writerows(index_rows)

    print(f"saved IIIF manifest/index: {row['id']} ({len(index_rows)} canvases)")


def harvest_local_file(row: dict) -> None:
    source_id = slug(row["id"])
    url = row["url"]
    suffix = pathlib.Path(url.split("?", 1)[0]).suffix
    if not suffix or len(suffix) > 8:
        suffix = ".bin"
    out = RAW / "files" / f"{source_id}{suffix}"
    save_bytes(out, fetch_bytes(url))
    print(f"saved local research copy: {row['id']} -> {out.relative_to(ROOT)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--iiif-images",
        action="store_true",
        help="also download all IIIF page images; can be large",
    )
    parser.add_argument(
        "--local-files",
        action="store_true",
        help="download rows marked local_file into ignored raw/files/",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help="limit to one or more manifest IDs, e.g. --only WED-25",
    )
    args = parser.parse_args()

    selected = set(args.only)
    RAW.mkdir(parents=True, exist_ok=True)

    with MANIFEST.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))

    for row in rows:
        if selected and row["id"] not in selected:
            continue
        mode = row["fetch_mode"]
        try:
            if mode == "iiif":
                harvest_iiif(row, include_images=args.iiif_images)
            elif mode == "local_file" and args.local_files:
                harvest_local_file(row)
            else:
                print(f"link only / skipped by policy: {row['id']} -> {row['url']}")
        except Exception as exc:  # keep batch progress visible
            print(f"ERROR {row['id']}: {exc}")


if __name__ == "__main__":
    main()
