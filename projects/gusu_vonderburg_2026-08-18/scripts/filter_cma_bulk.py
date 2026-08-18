#!/usr/bin/env python3
"""Filter the official Cleveland Museum of Art Open Access CSV for the 2025
Christer von der Burg acquisition.

This script is designed to run in GitHub Actions after `git lfs pull` has
materialized ClevelandMuseumArt/openaccess/data.csv. It deliberately writes
both the complete source rows and a compact machine-oriented derivative so
that no museum fields are lost while the research table remains easy to use.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (s or "").lower())


def field_by_alias(fields, aliases):
    table = {norm(f): f for f in fields}
    for a in aliases:
        if norm(a) in table:
            return table[norm(a)]
    return ""


def fields_containing(fields, needle):
    n = norm(needle)
    return [f for f in fields if n in norm(f)]


def maybe_json(value):
    if not value:
        return None
    s = value.strip()
    if not s or s[0] not in "[{":
        return None
    try:
        return json.loads(s)
    except Exception:
        return None


def image_url(row, fields, size):
    # First prefer flattened columns if present.
    aliases = [
        f"{size}_image_url", f"image_{size}_url", f"images_{size}_url",
        f"images.{size}.url", f"{size}imageurl",
    ]
    f = field_by_alias(fields, aliases)
    if f and row.get(f):
        return row[f]
    # Then parse a nested `images` JSON cell if the CSV uses one.
    image_field = field_by_alias(fields, ["images", "image"])
    if image_field:
        obj = maybe_json(row.get(image_field, ""))
        if isinstance(obj, dict):
            v = obj.get(size)
            if isinstance(v, dict):
                return v.get("url", "") or ""
            if isinstance(v, str):
                return v
    return ""


def accession_num(acc):
    m = re.fullmatch(r"2025\.(\d+)", acc or "")
    return int(m.group(1)) if m else None


def base_accession(acc):
    p = (acc or "").split(".")
    return ".".join(p[:2]) if len(p) >= 2 else acc


def sha256(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source_csv")
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--source-commit", default="")
    ap.add_argument("--source-lfs-oid", default="")
    args = ap.parse_args()

    src = Path(args.source_csv)
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    with src.open("r", newline="", encoding="utf-8-sig", errors="replace") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        rows = list(reader)

    accession_field = field_by_alias(fields, ["accession_number", "accessionNumber", "accession"])
    if not accession_field:
        raise RuntimeError(f"Could not identify accession field. Headers: {fields}")

    prov_fields = fields_containing(fields, "provenance")
    if not prov_fields:
        raise RuntimeError(f"Could not identify provenance field. Headers: {fields}")

    record_type_field = field_by_alias(fields, ["record_type", "recordType"])
    cover_field = field_by_alias(fields, ["cover_accession_number", "coverAccessionNumber"])
    id_field = field_by_alias(fields, ["id", "object_id", "objectID"])
    title_field = field_by_alias(fields, ["title"])
    title_zh_field = field_by_alias(fields, ["title_in_original_language", "titleInOriginalLanguage"])
    culture_field = field_by_alias(fields, ["culture"])
    technique_field = field_by_alias(fields, ["technique", "medium"])
    type_field = field_by_alias(fields, ["type"])
    date_field = field_by_alias(fields, ["creation_date", "creationDate", "date"])
    license_field = field_by_alias(fields, ["share_license_status", "shareLicenseStatus"])
    url_field = field_by_alias(fields, ["url", "object_url", "objectURL"])
    updated_field = field_by_alias(fields, ["updated_at", "updatedAt"])

    def provenance_blob(r):
        return " ".join((r.get(f) or "") for f in prov_fields)

    all_vdb = [r for r in rows if "christer von der burg" in provenance_blob(r).lower()]
    matched = [r for r in all_vdb if (r.get(accession_field) or "").startswith("2025.")]

    # Preserve every original column verbatim for the 2025 provenance hits.
    full_path = out / "cma_vonderburg_2025_official_bulk_full_rows.csv"
    with full_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(matched)

    compact_fields = [
        "machine_id", "accession", "accession_base", "object_id", "record_type",
        "cover_accession_number", "title_en", "title_zh", "culture", "date",
        "type", "technique", "provenance_raw", "share_license_status",
        "object_url", "web_image_url", "print_image_url", "full_image_url",
        "has_web_image", "has_print_image", "has_full_image",
        "in_H1_2025_19_to_128", "physical_contribution_using_record_type",
        "source_row_sha256",
    ]
    compact = []
    for r in matched:
        acc = (r.get(accession_field) or "").strip()
        rt = (r.get(record_type_field) or "").strip() if record_type_field else ""
        cover = (r.get(cover_field) or "").strip() if cover_field else ""
        topn = accession_num(base_accession(acc))
        provenance_raw = provenance_blob(r)
        row_payload = json.dumps(r, ensure_ascii=False, sort_keys=True).encode("utf-8")
        web = image_url(r, fields, "web")
        prn = image_url(r, fields, "print")
        full = image_url(r, fields, "full")
        compact.append({
            "machine_id": f"CMA:{acc}",
            "accession": acc,
            "accession_base": base_accession(acc),
            "object_id": r.get(id_field, "") if id_field else "",
            "record_type": rt,
            "cover_accession_number": cover,
            "title_en": r.get(title_field, "") if title_field else "",
            "title_zh": r.get(title_zh_field, "") if title_zh_field else "",
            "culture": r.get(culture_field, "") if culture_field else "",
            "date": r.get(date_field, "") if date_field else "",
            "type": r.get(type_field, "") if type_field else "",
            "technique": r.get(technique_field, "") if technique_field else "",
            "provenance_raw": provenance_raw,
            "share_license_status": r.get(license_field, "") if license_field else "",
            "object_url": r.get(url_field, "") if url_field else "",
            "web_image_url": web,
            "print_image_url": prn,
            "full_image_url": full,
            "has_web_image": "1" if web else "0",
            "has_print_image": "1" if prn else "0",
            "has_full_image": "1" if full else "0",
            "in_H1_2025_19_to_128": "1" if topn is not None and 19 <= topn <= 128 else "0",
            "physical_contribution_using_record_type": "0" if rt.lower() == "cover" else "1",
            "source_row_sha256": hashlib.sha256(row_payload).hexdigest(),
        })

    def sortkey(r):
        bits = []
        for p in r["accession"].split("."):
            try:
                bits.append((0, int(p)))
            except ValueError:
                bits.append((1, p))
        return bits
    compact.sort(key=sortkey)

    compact_path = out / "cma_vonderburg_2025_official_bulk_compact.csv"
    with compact_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=compact_fields)
        w.writeheader()
        w.writerows(compact)

    top_level_nums = sorted({
        accession_num(base_accession(r["accession"]))
        for r in compact
        if accession_num(base_accession(r["accession"])) is not None
    })
    top_level_nums = [n for n in top_level_nums if n is not None]
    h1_missing = [n for n in range(19, 129) if n not in top_level_nums]
    outside = sorted(n for n in top_level_nums if n < 19 or n > 128)
    record_types = Counter((r["record_type"] or "<blank>") for r in compact)
    cover_records = [r["accession"] for r in compact if r["record_type"].lower() == "cover"]
    physical = sum(int(r["physical_contribution_using_record_type"]) for r in compact)

    meta = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source_repository": "ClevelandMuseumArt/openaccess",
        "source_commit": args.source_commit,
        "source_lfs_oid": args.source_lfs_oid,
        "source_csv_size": src.stat().st_size,
        "source_csv_sha256": sha256(src),
        "source_total_rows": len(rows),
        "source_headers": fields,
        "detected_fields": {
            "accession": accession_field,
            "provenance": prov_fields,
            "record_type": record_type_field,
            "cover_accession_number": cover_field,
        },
        "all_years_christer_von_der_burg_rows": len(all_vdb),
        "year_2025_christer_von_der_burg_rows": len(matched),
        "unique_accessions_2025": len({r["accession"] for r in compact}),
        "top_level_accession_numbers": top_level_nums,
        "top_level_count": len(top_level_nums),
        "h1_range_2025_19_to_128_complete": not h1_missing,
        "h1_missing_top_level_numbers": h1_missing,
        "top_level_numbers_outside_H1": outside,
        "boundary_presence": {f"2025.{n}": (n in top_level_nums) for n in [18,19,20,128,129,130]},
        "record_type_counts": dict(record_types),
        "cover_records": cover_records,
        "physical_count_using_record_type": physical,
        "official_CMA_reported_physical_print_count": 113,
        "physical_count_matches_official_113": physical == 113,
        "image_coverage": {
            "web": sum(r["has_web_image"] == "1" for r in compact),
            "print": sum(r["has_print_image"] == "1" for r in compact),
            "full": sum(r["has_full_image"] == "1" for r in compact),
        },
        "full_rows_csv": full_path.name,
        "compact_csv": compact_path.name,
    }
    meta_path = out / "cma_vonderburg_2025_official_bulk_summary.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
