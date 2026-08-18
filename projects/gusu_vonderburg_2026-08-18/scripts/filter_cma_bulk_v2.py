#!/usr/bin/env python3
"""CMA official-bulk filter v2 for the von der Burg Gusu acquisition.

Key corrections over v1:
- CMA bulk CSV uses image_web / image_print / image_full columns.
- Current bulk CSV omits record_type and cover_accession_number, so multipart
  structure is conservatively inferred from accession suffixes: when both a
  base accession (e.g. 2025.82) and suffixed records (2025.82.1, ...) exist,
  the base is an inferred cover and suffix rows are inferred components.
- The 2025 purchase corpus is separated from later von der Burg gifts by
  provenance wording and the contiguous 2025.19–2025.129 purchase block.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


def norm(s): return re.sub(r"[^a-z0-9]+", "", (s or "").lower())
def field_by_alias(fields, aliases):
    table={norm(f):f for f in fields}
    for a in aliases:
        if norm(a) in table: return table[norm(a)]
    return ""
def fields_containing(fields, needle):
    n=norm(needle); return [f for f in fields if n in norm(f)]
def base_accession(acc):
    p=(acc or "").split("."); return ".".join(p[:2]) if len(p)>=2 else acc
def top_number(acc):
    m=re.fullmatch(r"2025\.(\d+)", base_accession(acc or "")); return int(m.group(1)) if m else None
def suffix(acc):
    p=(acc or "").split("."); return ".".join(p[2:]) if len(p)>2 else ""
def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for ch in iter(lambda:f.read(1024*1024),b""): h.update(ch)
    return h.hexdigest()

def image_value(row, fields, size):
    f=field_by_alias(fields,[f"image_{size}",f"{size}_image",f"{size}_image_url",f"image_{size}_url",f"images_{size}_url",f"images.{size}.url"])
    return (row.get(f) or "").strip() if f else ""
def write_csv(path, rows, fields):
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction="ignore"); w.writeheader(); w.writerows(rows)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("source_csv")
    ap.add_argument("--outdir",required=True)
    ap.add_argument("--source-commit",default="")
    ap.add_argument("--source-lfs-oid",default="")
    args=ap.parse_args()
    src=Path(args.source_csv); out=Path(args.outdir); out.mkdir(parents=True,exist_ok=True)

    with src.open("r",newline="",encoding="utf-8-sig",errors="replace") as f:
        rd=csv.DictReader(f); fields=rd.fieldnames or []; rows=list(rd)
    af=field_by_alias(fields,["accession_number","accession"])
    pf=fields_containing(fields,"provenance")
    if not af or not pf: raise RuntimeError("Required accession/provenance fields not found")
    idf=field_by_alias(fields,["id"]); tf=field_by_alias(fields,["title"])
    tzf=field_by_alias(fields,["title_in_original_language"]); cf=field_by_alias(fields,["culture"])
    df=field_by_alias(fields,["creation_date"]); tyf=field_by_alias(fields,["type"])
    techf=field_by_alias(fields,["technique","medium"]); lf=field_by_alias(fields,["share_license_status"])
    uf=field_by_alias(fields,["url"]); upf=field_by_alias(fields,["updated_at"])
    def prov(r): return " ".join((r.get(f) or "") for f in pf)

    all_vdb=[r for r in rows if "christer von der burg" in prov(r).lower()]
    y2025=[r for r in all_vdb if (r.get(af) or "").startswith("2025.")]
    groups=defaultdict(list)
    for r in y2025: groups[base_accession((r.get(af) or "").strip())].append(r)

    multipart={b:sorted((r.get(af) or "").strip() for r in rs) for b,rs in groups.items()
               if any(suffix((r.get(af) or "").strip()) for r in rs)}

    compact=[]
    for r in y2025:
        acc=(r.get(af) or "").strip(); base=base_accession(acc); suf=suffix(acc); n=top_number(acc)
        p=prov(r); pl=p.lower(); companions=multipart.get(base,[])
        if companions:
            inferred_kind="component" if suf else "cover"
        else:
            inferred_kind="object"
        core=(n is not None and 19<=n<=129 and "sold to the cleveland museum of art" in pl)
        physical=1 if core and inferred_kind!="cover" else 0
        web=image_value(r,fields,"web"); prn=image_value(r,fields,"print"); full=image_value(r,fields,"full")
        compact.append({
            "machine_id":f"CMA:{acc}"+(":COVER" if inferred_kind=="cover" else ""),
            "accession":acc,"accession_base":base,"component_suffix":suf,
            "object_id":r.get(idf,"") if idf else "","inferred_record_kind":inferred_kind,
            "inferred_cover_accession":base if inferred_kind=="component" else "",
            "multipart_group_size_records":len(companions) if companions else 1,
            "title_en":r.get(tf,"") if tf else "","title_zh":r.get(tzf,"") if tzf else "",
            "culture":r.get(cf,"") if cf else "","date":r.get(df,"") if df else "",
            "type":r.get(tyf,"") if tyf else "","technique":r.get(techf,"") if techf else "",
            "provenance_raw":p,"acquisition_mode":"sold" if "sold to the cleveland museum of art" in pl else ("given" if "given to the cleveland museum of art" in pl else "other"),
            "share_license_status":r.get(lf,"") if lf else "","object_url":r.get(uf,"") if uf else f"https://clevelandart.org/art/{acc}",
            "web_image_url":web,"print_image_url":prn,"full_image_url":full,
            "has_web_image":"1" if web else "0","has_print_image":"1" if prn else "0","has_full_image":"1" if full else "0",
            "in_core_2025_purchase_block":"1" if core else "0","physical_print_contribution_inferred":str(physical),
            "cma_jpeg_caption_endpoint":f"https://openaccess-api.clevelandart.org/api/collectiononline/jpeg_and_caption/{acc}",
            "cma_tiff_endpoint":f"https://openaccess-api.clevelandart.org/api/collectiononline/tiff/{acc}",
            "updated_at":r.get(upf,"") if upf else "",
        })
    def sk(r):
        out=[]
        for p in r["accession"].split("."):
            try: out.append((0,int(p)))
            except: out.append((1,p))
        return out
    compact.sort(key=sk)
    cfields=list(compact[0].keys())
    write_csv(out/"cma_vonderburg_2025_official_bulk_v2_compact.csv",compact,cfields)
    core=[r for r in compact if r["in_core_2025_purchase_block"]=="1"]
    write_csv(out/"cma_gusu_core_113.csv",core,cfields)
    physical=[r for r in core if r["physical_print_contribution_inferred"]=="1"]
    write_csv(out/"cma_gusu_core_113_physical.csv",physical,cfields)
    dl=[r for r in physical if r["has_print_image"]=="1" or r["has_full_image"]=="1"]
    write_csv(out/"cma_gusu_core_download_manifest.csv",dl,cfields)
    gifts=[r for r in compact if r["acquisition_mode"]=="given"]
    write_csv(out/"cma_vonderburg_2025_later_gifts.csv",gifts,cfields)

    core_groups=defaultdict(list)
    for r in core: core_groups[r["accession_base"]].append(r)
    core_multi={b:[x["accession"] for x in rs] for b,rs in core_groups.items() if len(rs)>1}
    meta={
      "generated_utc":datetime.now(timezone.utc).isoformat(),
      "source_repository":"ClevelandMuseumArt/openaccess","source_commit":args.source_commit,"source_lfs_oid":args.source_lfs_oid,
      "source_csv_size":src.stat().st_size,"source_csv_sha256":sha256(src),"source_total_rows":len(rows),
      "all_years_christer_von_der_burg_rows":len(all_vdb),"year_2025_christer_von_der_burg_rows":len(y2025),
      "core_purchase_definition":"2025.19–2025.129 inclusive AND provenance contains 'sold to the Cleveland Museum of Art'",
      "core_rows_including_inferred_covers":len(core),"core_top_level_accessions":len(core_groups),
      "core_multipart_groups":core_multi,"core_multipart_group_count":len(core_multi),
      "core_component_rows":sum(r["inferred_record_kind"]=="component" for r in core),
      "core_inferred_cover_rows":sum(r["inferred_record_kind"]=="cover" for r in core),
      "core_inferred_physical_print_count":sum(int(r["physical_print_contribution_inferred"]) for r in core),
      "official_CMA_reported_physical_print_count":113,
      "core_physical_count_matches_113":sum(int(r["physical_print_contribution_inferred"]) for r in core)==113,
      "core_image_coverage":{"web":sum(r["has_web_image"]=="1" for r in physical),"print":sum(r["has_print_image"]=="1" for r in physical),"full":sum(r["has_full_image"]=="1" for r in physical)},
      "core_download_manifest_rows":len(dl),
      "later_2025_vonderburg_gifts":[{"accession":r["accession"],"title":r["title_en"],"date":r["date"],"license":r["share_license_status"]} for r in gifts],
      "note":"Multipart roles are inferred from accession suffix structure because the current official bulk CSV omits record_type and cover_accession_number."
    }
    (out/"cma_gusu_core_v2_summary.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(meta,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
