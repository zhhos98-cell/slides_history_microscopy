#!/usr/bin/env python3
"""
Resolve museum metadata and direct image URLs for the Christer von der Burg Gusu manifest.

Stdlib only. No API keys required.

Examples:
  python resolve_gusu_manifest.py gusu_vonderburg_catalogue_manifest_seed.csv
  python resolve_gusu_manifest.py gusu_vonderburg_catalogue_manifest_seed.csv -o gusu_resolved.csv
  python resolve_gusu_manifest.py gusu_vonderburg_catalogue_manifest_seed.csv -o gusu_resolved.csv --download images
"""
import argparse, csv, json, os, re, sys, time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

UA = "GusuCatalogueResolver/0.2 (+research use)"
CMA_BULK = "https://openaccess-api.clevelandart.org/api/artworks/"
MET_SEARCH = "https://collectionapi.metmuseum.org/public/collection/v1/search"
MET_OBJECT = "https://collectionapi.metmuseum.org/public/collection/v1/objects/{}"

def http_json(url, retries=3, timeout=30):
    last = None
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urlopen(req, timeout=timeout) as r:
                return r.status, json.load(r)
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET failed after {retries} attempts: {url}: {last}")

def get(row, key):
    v = row.get(key, "")
    return "" if v is None else str(v)

def bool01(v):
    return "1" if bool(v) else "0"

def safe_acc(acc):
    return re.sub(r"[^A-Za-z0-9]+", "_", acc).strip("_")

def filename(museum, accession, object_id=""):
    parts = [museum, safe_acc(accession)]
    if object_id:
        parts.append(str(object_id))
    return "_".join(parts) + ".jpg"

def exact_cma_map():
    params = {"provenance": "Christer von der Burg", "limit": 1000}
    status, payload = http_json(CMA_BULK + "?" + urlencode(params))
    data = payload.get("data") or []
    return status, {str(x.get("accession_number","")).strip(): x for x in data if x.get("accession_number")}

def image_url(images, size):
    if not isinstance(images, dict):
        return ""
    obj = images.get(size)
    if isinstance(obj, dict):
        return obj.get("url") or ""
    return ""

def update_cma(row, art, http_status):
    acc = str(art.get("accession_number","")).strip()
    row["object_id"] = art.get("id","")
    row["title_en"] = art.get("title") or row.get("title_en","")
    original = art.get("title_in_original_language")
    if isinstance(original, str) and original.strip():
        row["title_zh"] = original.strip()
    row["title_source"] = "CMA_API"
    row["object_url"] = art.get("url") or row.get("object_url","")
    row["api_object_url"] = f"https://openaccess-api.clevelandart.org/api/artworks/{art.get('id')}" if art.get("id") else ""
    images = art.get("images") or {}
    row["web_image_url"] = image_url(images, "web")
    row["print_image_url"] = image_url(images, "print")
    row["direct_image_url"] = image_url(images, "full") or row["print_image_url"] or row["web_image_url"]
    row["has_image"] = bool01(bool(row["web_image_url"] or row["print_image_url"] or row["direct_image_url"]))
    row["downloadable"] = bool01(bool(row["direct_image_url"]))
    lic = str(art.get("share_license_status") or "")
    row["public_domain"] = "1" if ("CC0" in lic.upper() or "PUBLIC DOMAIN" in lic.upper()) else ("0" if lic else "")
    row["image_status"] = "direct_image_resolved" if row["direct_image_url"] else "no_image_asset_in_api"
    row["record_kind"] = art.get("record_type") or row.get("record_kind","")
    cover = art.get("cover_accession_number")
    if cover and not row.get("set_id"):
        row["set_id"] = "CMA:SET:" + str(cover)
    row["is_verified_museum_record"] = "1"
    row["row_status"] = "verified_api_record"
    row["match_basis"] = "exact_accession_CMA_API"
    row["confidence"] = "high"
    row["resolver_status"] = "resolved"
    row["http_status"] = str(http_status)
    row["last_checked_utc"] = datetime.now(timezone.utc).isoformat()
    row["source_kind"] = "CMA_API"
    row["source_url"] = row["api_object_url"] or row["object_url"]
    row["filename_safe"] = filename("CMA", acc, row["object_id"])
    return row

def resolve_met_object_id(accession):
    url = MET_SEARCH + "?" + urlencode({"q": accession})
    status, payload = http_json(url)
    for oid in payload.get("objectIDs") or []:
        s2, obj = http_json(MET_OBJECT.format(oid))
        if str(obj.get("accessionNumber","")).strip() == accession:
            return s2, obj
        time.sleep(0.03)
    return status, None

def update_met(row, obj, http_status):
    acc = str(obj.get("accessionNumber","")).strip()
    row["object_id"] = obj.get("objectID","")
    row["title_en"] = obj.get("title") or row.get("title_en","")
    row["title_source"] = "MET_API"
    row["object_url"] = obj.get("objectURL") or (
        f"https://www.metmuseum.org/art/collection/search/{obj.get('objectID')}" if obj.get("objectID") else row.get("object_url","")
    )
    row["api_object_url"] = MET_OBJECT.format(obj.get("objectID")) if obj.get("objectID") else ""
    row["web_image_url"] = obj.get("primaryImageSmall") or ""
    row["print_image_url"] = ""
    row["direct_image_url"] = obj.get("primaryImage") or ""
    addl = obj.get("additionalImages") or []
    row["additional_image_urls"] = "|".join(addl) if isinstance(addl, list) else ""
    row["has_image"] = bool01(bool(row["web_image_url"] or row["direct_image_url"] or addl))
    row["public_domain"] = bool01(obj.get("isPublicDomain"))
    row["downloadable"] = bool01(bool(obj.get("isPublicDomain") and row["direct_image_url"]))
    row["image_status"] = (
        "direct_image_resolved" if row["direct_image_url"]
        else ("image_not_Open_Access_or_unavailable" if row["has_image"] == "1" else "no_image_asset_in_api")
    )
    row["is_verified_museum_record"] = "1"
    row["row_status"] = "verified_api_record"
    row["match_basis"] = "exact_accession_MET_API"
    row["confidence"] = "high"
    row["resolver_status"] = "resolved"
    row["http_status"] = str(http_status)
    row["last_checked_utc"] = datetime.now(timezone.utc).isoformat()
    row["source_kind"] = "MET_API"
    row["source_url"] = row["api_object_url"]
    row["filename_safe"] = filename("MET", acc, row["object_id"])
    return row

def download(url, path, retries=3, timeout=60):
    if path.exists() and path.stat().st_size > 0:
        return "exists"
    last = None
    for attempt in range(retries):
        try:
            req = Request(url, headers={"User-Agent": UA})
            with urlopen(req, timeout=timeout) as r, open(path, "wb") as out:
                while True:
                    chunk = r.read(1024 * 1024)
                    if not chunk:
                        break
                    out.write(chunk)
            return "downloaded"
        except (HTTPError, URLError, TimeoutError, OSError) as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    return "error:" + str(last)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("-o", "--output", default="")
    ap.add_argument("--download", default="", help="Download resolved primary images into this directory.")
    ap.add_argument("--cma-only", action="store_true")
    ap.add_argument("--met-only", action="store_true")
    args = ap.parse_args()

    src = Path(args.csv)
    out = Path(args.output) if args.output else src.with_name(src.stem.replace("_seed","") + "_resolved.csv")

    with src.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        rows = list(reader)

    cma_map = {}
    cma_http = ""
    if not args.met_only:
        try:
            cma_http, cma_map = exact_cma_map()
            existing_cma = {r.get("accession","") for r in rows if r.get("museum_code") == "CMA"}
            template = rows[0].copy() if rows else {k:"" for k in fieldnames}
            for acc, art in sorted(cma_map.items()):
                if acc not in existing_cma:
                    r = {k:"" for k in fieldnames}
                    r.update({
                        "schema_version":"0.2",
                        "machine_id":"CMA:"+acc,
                        "museum_code":"CMA",
                        "museum_name":"Cleveland Museum of Art",
                        "accession":acc,
                        "accession_base":".".join(acc.split(".")[:2]),
                        "component_suffix":".".join(acc.split(".")[2:]) if len(acc.split("."))>2 else "",
                        "row_status":"discovered_by_CMA_provenance_API",
                        "match_basis":"CMA_provenance_bulk_discovery",
                        "confidence":"high",
                    })
                    rows.append(r)
        except Exception as e:
            print("CMA bulk query failed:", e, file=sys.stderr)

    total = len(rows)
    for i, row in enumerate(rows, 1):
        code = row.get("museum_code","")
        acc = row.get("accession","").strip()
        try:
            if code == "CMA" and not args.met_only:
                art = cma_map.get(acc)
                if art:
                    update_cma(row, art, cma_http)
                else:
                    row["resolver_status"] = "not_found_in_CMA_provenance_query"
                    row["last_checked_utc"] = datetime.now(timezone.utc).isoformat()
            elif code == "MET" and not args.cma_only:
                oid = row.get("object_id","").strip()
                if oid:
                    s, obj = http_json(MET_OBJECT.format(oid))
                    if str(obj.get("accessionNumber","")).strip() == acc:
                        update_met(row, obj, s)
                    else:
                        s, obj = resolve_met_object_id(acc)
                        if obj:
                            update_met(row, obj, s)
                        else:
                            row["resolver_status"] = "not_found_exact_accession"
                else:
                    s, obj = resolve_met_object_id(acc)
                    if obj:
                        update_met(row, obj, s)
                    else:
                        row["resolver_status"] = "not_found_exact_accession"
                time.sleep(0.04)
        except Exception as e:
            row["resolver_status"] = "error"
            row["notes"] = (row.get("notes","") + " | " if row.get("notes") else "") + str(e)
        if i % 25 == 0:
            print(f"Resolved {i}/{total}", file=sys.stderr)

    def sortkey(r):
        parts=[]
        for p in r.get("accession","").split("."):
            try: parts.append((0,int(p)))
            except: parts.append((1,p))
        return (r.get("museum_code",""), parts)
    rows.sort(key=sortkey)

    with out.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    if args.download:
        d = Path(args.download)
        d.mkdir(parents=True, exist_ok=True)
        for row in rows:
            url = row.get("direct_image_url") or row.get("print_image_url") or row.get("web_image_url")
            if not url:
                continue
            fn = row.get("filename_safe") or filename(row.get("museum_code","IMG"), row.get("accession","unknown"), row.get("object_id",""))
            result = download(url, d / fn)
            print(row.get("machine_id"), result, file=sys.stderr)

    print(out)

if __name__ == "__main__":
    main()
