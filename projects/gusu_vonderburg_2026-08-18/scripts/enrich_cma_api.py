#!/usr/bin/env python3
"""Enrich CMA von der Burg 2025 bulk rows via the official artwork API.

The bulk CSV currently omits record_type / cover_accession_number and our
research needs those fields to distinguish cover records, parts and components.
The API also supplies current web/print/full image permalinks.
"""
from __future__ import annotations

import argparse
import csv
import json
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

BASE = "https://openaccess-api.clevelandart.org/api/artworks/{}"
UA = "GusuVonDerBurgAPIEnricher/1.0 research-use"


def get_json(url, retries=4, timeout=45):
    last = None
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urlopen(req, timeout=timeout) as r:
                return getattr(r, "status", 200), json.load(r)
        except HTTPError as e:
            if e.code == 404:
                return 404, None
            last = e
        except (URLError, TimeoutError, json.JSONDecodeError) as e:
            last = e
        time.sleep(1.0 * (attempt + 1))
    raise RuntimeError(f"GET failed: {url}: {last}")


def image_url(images, key):
    if not isinstance(images, dict):
        return ""
    v = images.get(key)
    if isinstance(v, dict):
        return v.get("url", "") or ""
    return v if isinstance(v, str) else ""


def provenance_text(p):
    if p is None:
        return ""
    if isinstance(p, str):
        return p
    return json.dumps(p, ensure_ascii=False)


def sortkey(acc):
    out=[]
    for p in (acc or "").split("."):
        try: out.append((0,int(p)))
        except ValueError: out.append((1,p))
    return out


def base_accession(acc):
    p=(acc or "").split(".")
    return ".".join(p[:2]) if len(p)>=2 else acc


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("compact_bulk_csv")
    ap.add_argument("--outdir",required=True)
    ap.add_argument("--delay",type=float,default=0.08)
    args=ap.parse_args()

    src=Path(args.compact_bulk_csv)
    out=Path(args.outdir); out.mkdir(parents=True,exist_ok=True)
    with src.open("r",newline="",encoding="utf-8-sig") as f:
        bulk=list(csv.DictReader(f))

    rows=[]; errors=[]; raw=[]
    for i,b in enumerate(bulk,1):
        acc=b["accession"]
        url=BASE.format(quote(acc,safe="."))
        try:
            status,payload=get_json(url)
            art=(payload or {}).get("data") if isinstance(payload,dict) else None
            if not art:
                errors.append({"accession":acc,"http_status":status,"error":"no_data"})
                continue
            raw.append(art)
            images=art.get("images") or {}
            prov=provenance_text(art.get("provenance"))
            rows.append({
                "machine_id":f"CMA:{acc}",
                "accession":acc,
                "accession_base":base_accession(acc),
                "id":art.get("id",b.get("object_id","")),
                "record_type":art.get("record_type") or "",
                "cover_accession_number":art.get("cover_accession_number") or "",
                "title_en":art.get("title") or b.get("title_en","") or "",
                "title_zh":art.get("title_in_original_language") or b.get("title_zh","") or "",
                "culture":art.get("culture") or b.get("culture","") or "",
                "creation_date":art.get("creation_date") or b.get("date","") or "",
                "type":art.get("type") or b.get("type","") or "",
                "technique":art.get("technique") or b.get("technique","") or "",
                "share_license_status":art.get("share_license_status") or b.get("share_license_status","") or "",
                "legal_status":art.get("legal_status") or "",
                "accession_date":art.get("accession_date") or "",
                "url":art.get("url") or b.get("object_url","") or "",
                "api_url":url,
                "image_web":image_url(images,"web"),
                "image_print":image_url(images,"print"),
                "image_full":image_url(images,"full"),
                "has_web_image":"1" if image_url(images,"web") else "0",
                "has_print_image":"1" if image_url(images,"print") else "0",
                "has_full_image":"1" if image_url(images,"full") else "0",
                "provenance_raw":prov,
                "acquisition_mode":"given" if "given to the cleveland museum" in prov.lower() else ("sold" if "sold to the cleveland museum" in prov.lower() else "other"),
                "api_http_status":status,
                "api_checked_utc":datetime.now(timezone.utc).isoformat(),
            })
        except Exception as e:
            errors.append({"accession":acc,"http_status":"","error":repr(e)})
        if i % 20 == 0:
            print(f"checked {i}/{len(bulk)}")
        time.sleep(args.delay)

    rows.sort(key=lambda r:sortkey(r["accession"]))
    fields=list(rows[0].keys()) if rows else []
    csv_path=out/"cma_vonderburg_2025_api_enriched.csv"
    with csv_path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
    (out/"cma_vonderburg_2025_api_raw.json").write_text(json.dumps(raw,ensure_ascii=False,indent=2),encoding="utf-8")
    with (out/"cma_vonderburg_2025_api_errors.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["accession","http_status","error"]); w.writeheader(); w.writerows(errors)

    sale=[r for r in rows if r["acquisition_mode"]=="sold"]
    gifts=[r for r in rows if r["acquisition_mode"]=="given"]
    groups=defaultdict(list)
    for r in sale:
        groups[r["accession_base"]].append(r)

    group_summary=[]
    for base,members in sorted(groups.items(),key=lambda kv:sortkey(kv[0])):
        if len(members)>1 or any(r["record_type"] in ("cover","part","component") for r in members):
            group_summary.append({
                "base_accession":base,
                "row_count":len(members),
                "accessions":"|".join(r["accession"] for r in members),
                "record_types":"|".join((r["record_type"] or "<blank>") for r in members),
                "titles":" | ".join(r["title_en"] for r in members),
                "cover_links":"|".join(r["cover_accession_number"] for r in members if r["cover_accession_number"]),
            })
    with (out/"cma_vonderburg_2025_api_set_structure.csv").open("w",newline="",encoding="utf-8") as f:
        gf=["base_accession","row_count","accessions","record_types","titles","cover_links"]
        w=csv.DictWriter(f,fieldnames=gf); w.writeheader(); w.writerows(group_summary)

    # Count several plausible museum conventions rather than imposing one.
    sale_type_counts=Counter(r["record_type"] or "<blank>" for r in sale)
    sale_top={r["accession_base"] for r in sale}
    sale_19_128=[r for r in sale if r["accession_base"].startswith("2025.") and r["accession_base"].split(".")[1].isdigit() and 19<=int(r["accession_base"].split(".")[1])<=128]
    sale_19_129=[r for r in sale if r["accession_base"].startswith("2025.") and r["accession_base"].split(".")[1].isdigit() and 19<=int(r["accession_base"].split(".")[1])<=129]

    def top_count(sub): return len({r["accession_base"] for r in sub})
    def noncover_count(sub): return sum(r["record_type"]!="cover" for r in sub)
    def object_component_count(sub): return sum(r["record_type"] in ("object","component","") for r in sub)

    meta={
        "generated_utc":datetime.now(timezone.utc).isoformat(),
        "api_rows":len(rows),
        "api_errors":errors,
        "sale_rows":len(sale),
        "gift_rows":len(gifts),
        "sale_accessions":[r["accession"] for r in sale],
        "gift_accessions":[r["accession"] for r in gifts],
        "sale_record_type_counts":dict(sale_type_counts),
        "sale_top_level_accession_count":len(sale_top),
        "sale_set_structures":group_summary,
        "counts":{
            "sale_19_128_rows":len(sale_19_128),
            "sale_19_128_top_level":top_count(sale_19_128),
            "sale_19_128_noncover":noncover_count(sale_19_128),
            "sale_19_128_object_plus_component_or_blank":object_component_count(sale_19_128),
            "sale_19_129_rows":len(sale_19_129),
            "sale_19_129_top_level":top_count(sale_19_129),
            "sale_19_129_noncover":noncover_count(sale_19_129),
            "sale_19_129_object_plus_component_or_blank":object_component_count(sale_19_129),
        },
        "boundary_types":{r["accession"]:{"record_type":r["record_type"],"cover":r["cover_accession_number"],"title":r["title_en"],"mode":r["acquisition_mode"]} for r in rows if r["accession"] in {"2025.19","2025.20","2025.128","2025.129","2025.212","2025.213","2025.214"}},
        "image_coverage":{
            "all_api_rows":{"web":sum(r["has_web_image"]=="1" for r in rows),"print":sum(r["has_print_image"]=="1" for r in rows),"full":sum(r["has_full_image"]=="1" for r in rows)},
            "sale_rows":{"web":sum(r["has_web_image"]=="1" for r in sale),"print":sum(r["has_print_image"]=="1" for r in sale),"full":sum(r["has_full_image"]=="1" for r in sale)},
        },
        "official_reported_suzhou_prints":113,
        "note":"Counts are reported under multiple record-type conventions; no convention is forced until compared with CMA's 113-print statement and set semantics."
    }
    (out/"cma_vonderburg_2025_api_summary.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(meta,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
