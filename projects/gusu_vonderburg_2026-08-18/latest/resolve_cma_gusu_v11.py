#!/usr/bin/env python3
"""
CMA Gusu resolver v1.1

Primary mode:
  1. Query CMA's official provenance filter once.
  2. Keep only records that pass strict corpus gates:
       - accession year 2025
       - provenance contains "Christer von der Burg"
       - Chinese/Suzhou/Qing signal
       - print/woodblock signal
  3. Preserve record_type and cover_accession_number.
  4. Write exact API image URLs (web / print / full) only when supplied by CMA.
  5. Save rejects separately. Old von der Burg provenance hits (e.g. 1975 works)
     are never auto-appended.

Optional audit mode:
  --probe-year 2025 --start 1 --end 200
queries CMA's specific-artwork endpoint by accession number to discover records
that might not yet be indexed by web search. This does NOT automatically
accept every 2025 record; the same strict corpus gates are applied.

The script is conservative and sequential. No API key is required.
"""
import argparse, csv, json, re, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

UA="GusuVonDerBurgResolver/1.1 research-use"
BASE="https://openaccess-api.clevelandart.org"
SEARCH=BASE+"/api/artworks/"
SPECIFIC=BASE+"/api/artworks/{}"

def get_json(url, timeout=45, retries=4):
    last=None
    for n in range(retries):
        try:
            req=Request(url, headers={"User-Agent":UA,"Accept":"application/json"})
            with urlopen(req,timeout=timeout) as r:
                return getattr(r,"status",200), json.load(r)
        except HTTPError as e:
            if e.code==404:
                return 404, None
            last=e
        except Exception as e:
            last=e
        time.sleep(1.0*(n+1))
    raise RuntimeError(f"GET failed {url}: {last}")

def flatten_prov(x):
    try:
        return json.dumps(x or [], ensure_ascii=False).lower()
    except Exception:
        return str(x or "").lower()

def corpus_gate(art):
    acc=str(art.get("accession_number") or "").strip()
    if not acc.startswith("2025."):
        return False,"non_2025_accession"

    prov=flatten_prov(art.get("provenance"))
    if "christer von der burg" not in prov:
        return False,"no_vonderburg_provenance"

    blob=" ".join(str(x or "") for x in [
        art.get("title"), art.get("title_in_original_language"),
        art.get("culture"), art.get("technique"), art.get("type"),
        art.get("department"), art.get("collection"), art.get("description")
    ]).lower()

    chinese=any(k in blob for k in [
        "china","chinese","suzhou","qing","jiangnan",
        "中國","中国","蘇州","苏州","清"
    ])
    printish=any(k in blob for k in [
        "woodblock","wood-block","print","印"
    ])
    if not chinese:
        return False,"no_chinese_or_suzhou_signal"
    if not printish:
        return False,"no_print_or_woodblock_signal"
    return True,"accepted"

def image_url(images,key):
    if not isinstance(images,dict): return ""
    v=images.get(key)
    return v.get("url","") if isinstance(v,dict) else ""

def normalized(art, discovery):
    acc=str(art.get("accession_number") or "").strip()
    images=art.get("images") or {}
    record_type=art.get("record_type") or ""
    cover=art.get("cover_accession_number") or ""
    return {
        "machine_id":"CMA:"+acc+(":COVER" if record_type=="cover" else ""),
        "museum_code":"CMA",
        "accession":acc,
        "object_id":art.get("id",""),
        "title_en":art.get("title") or "",
        "title_zh":art.get("title_in_original_language") or "",
        "record_kind":record_type,
        "cover_accession_number":cover,
        "object_url":art.get("url") or f"https://www.clevelandart.org/art/{acc}",
        "api_object_url":f"{BASE}/api/artworks/{acc}",
        "share_license_status":art.get("share_license_status") or "",
        "web_image_url":image_url(images,"web"),
        "print_image_url":image_url(images,"print"),
        "direct_image_url":image_url(images,"full") or image_url(images,"print") or image_url(images,"web"),
        "full_image_url":image_url(images,"full"),
        "has_image":"1" if any(image_url(images,k) for k in ("web","print","full")) else "0",
        "downloadable":"1" if any(image_url(images,k) for k in ("print","full")) else "0",
        "cma_jpeg_caption_endpoint":f"{BASE}/api/collectiononline/jpeg_and_caption/{acc}",
        "cma_tiff_endpoint":f"{BASE}/api/collectiononline/tiff/{acc}",
        "discovery_method":discovery,
        "updated_at":art.get("updated_at") or "",
        "checked_utc":datetime.now(timezone.utc).isoformat(),
    }

def provenance_bulk():
    params={"provenance":"Christer von der Burg","limit":1000}
    status,payload=get_json(SEARCH+"?"+urlencode(params))
    return status, (payload or {}).get("data") or []

def probe_year(year,start,end,delay):
    found=[]
    missing=[]
    for n in range(start,end+1):
        acc=f"{year}.{n}"
        status,payload=get_json(SPECIFIC.format(acc))
        if status==404 or not payload:
            missing.append(acc)
        else:
            art=payload.get("data") if isinstance(payload,dict) else None
            if art: found.append(art)
        time.sleep(delay)
    return found,missing

def write_csv(path, rows, fields):
    with open(path,"w",newline="",encoding="utf-8-sig") as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore")
        w.writeheader(); w.writerows(rows)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("-o","--output",default="cma_gusu_resolved.csv")
    ap.add_argument("--reject-log",default="cma_vonderburg_rejects.csv")
    ap.add_argument("--missing-log",default="cma_accession_probe_missing.csv")
    ap.add_argument("--probe-year",default="")
    ap.add_argument("--start",type=int,default=1)
    ap.add_argument("--end",type=int,default=200)
    ap.add_argument("--delay",type=float,default=0.15)
    args=ap.parse_args()

    _, arts=provenance_bulk()
    discovery={str(a.get("accession_number","")):"provenance_bulk" for a in arts}
    allarts={str(a.get("accession_number","")):a for a in arts if a.get("accession_number")}
    missing=[]

    if args.probe_year:
        probed,missing=probe_year(args.probe_year,args.start,args.end,args.delay)
        for a in probed:
            acc=str(a.get("accession_number",""))
            allarts[acc]=a
            discovery.setdefault(acc,"specific_accession_probe")

    accepted=[]; rejected=[]
    for acc,art in allarts.items():
        ok,reason=corpus_gate(art)
        if ok:
            accepted.append(normalized(art,discovery.get(acc,"unknown")))
        else:
            rejected.append({
                "accession":acc,
                "title":art.get("title") or "",
                "reason":reason,
                "object_url":art.get("url") or "",
                "record_type":art.get("record_type") or "",
            })

    def skey(r):
        parts=[]
        for p in r["accession"].split("."):
            try: parts.append((0,int(p)))
            except: parts.append((1,p))
        return parts
    accepted.sort(key=skey)
    rejected.sort(key=lambda r:r["accession"])

    fields=[
        "machine_id","museum_code","accession","object_id","title_en","title_zh",
        "record_kind","cover_accession_number","object_url","api_object_url",
        "share_license_status","web_image_url","print_image_url","direct_image_url",
        "full_image_url","has_image","downloadable","cma_jpeg_caption_endpoint",
        "cma_tiff_endpoint","discovery_method","updated_at","checked_utc"
    ]
    write_csv(args.output,accepted,fields)
    write_csv(args.reject_log,rejected,["accession","title","reason","object_url","record_type"])
    write_csv(args.missing_log,[{"accession":a} for a in missing],["accession"])

    print(json.dumps({
        "accepted_rows":len(accepted),
        "accepted_physical_estimate":sum(0 if r["record_kind"]=="cover" else 1 for r in accepted),
        "covers":[r["accession"] for r in accepted if r["record_kind"]=="cover"],
        "components":[r["accession"] for r in accepted if r["record_kind"]=="component"],
        "with_web_image":sum(r["has_image"]=="1" for r in accepted),
        "with_downloadable_print_or_full":sum(r["downloadable"]=="1" for r in accepted),
        "rejected_provenance_hits":len(rejected),
        "probed_missing":len(missing),
        "output":args.output
    },ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
