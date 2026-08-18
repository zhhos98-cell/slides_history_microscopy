#!/usr/bin/env python3
"""Build the Met v2 working core for the von der Burg Gusu acquisition.

Evidence state as of 2026-08-18:
- live Met search/API establishes a continuous 2025.352–2025.460 Suzhou-related
  accession block (109 accessions) once six transient-403 rows are restored
  from the prior successful API audit;
- joint acquisition total is 220 and CMA reports 113, leaving 107 for Met;
- 2025.354–2025.460 inclusive is exactly 107 accessions;
- 2025.797.1/.2 are explicit 2025 gifts from Christer von der Burg and are
  therefore retained separately rather than silently merged into the 107;
- 2025.618.4 is a Japanese painting false-positive from the broad Suzhou text
  search and is excluded.

The 354–460 boundary is a strong structural working hypothesis, NOT yet a
book-catalogue concordance. Every output preserves that epistemic status.
"""
from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

FALLBACK_ACCESSIONS = {"2025.372","2025.374","2025.376","2025.384","2025.402","2025.407"}
RESTRICTED = {"2025.424","2025.425","2025.426"}


def sortkey(acc):
    out=[]
    for p in (acc or "").split("."):
        try: out.append((0,int(p)))
        except ValueError: out.append((1,p))
    return out


def base_num(acc):
    p=(acc or "").split(".")
    if len(p)<2 or p[0] != "2025": return None
    try: return int(p[1])
    except ValueError: return None


def read_csv(path):
    with open(path,newline="",encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def normalize_live(r, source):
    return {
        "machine_id":"MET:"+r.get("accession",""),
        "accession":r.get("accession",""),
        "object_id":r.get("object_id",r.get("object_id","")),
        "title_en":r.get("title_en",r.get("title","")),
        "title_zh":r.get("title_zh",""),
        "culture":r.get("culture",""),
        "period":r.get("period",""),
        "object_date":r.get("object_date",""),
        "medium":r.get("medium",""),
        "dimensions":r.get("dimensions",""),
        "classification":r.get("classification",""),
        "department":r.get("department",""),
        "credit_line":r.get("credit_line",""),
        "public_domain":r.get("public_domain",r.get("is_public_domain","")),
        "object_url":r.get("object_url",r.get("url","")),
        "api_url":r.get("api_url",""),
        "primary_image":r.get("primary_image",""),
        "primary_image_small":r.get("primary_image_small",""),
        "additional_image_count":r.get("additional_image_count","0") or "0",
        "additional_images":r.get("additional_images",""),
        "source_merge":source,
    }


def normalize_fallback(r):
    return {
        "machine_id":"MET:"+r.get("accession",""),
        "accession":r.get("accession",""),
        "object_id":r.get("object_id",""),
        "title_en":r.get("title_en",""),
        "title_zh":r.get("title_zh",""),
        "culture":r.get("culture",""),
        "period":r.get("period",""),
        "object_date":r.get("object_date",""),
        "medium":r.get("medium",""),
        "dimensions":r.get("dimensions",""),
        "classification":r.get("classification",""),
        "department":r.get("department",""),
        "credit_line":r.get("credit_line",""),
        "public_domain":r.get("is_public_domain",""),
        "object_url":r.get("object_url",""),
        "api_url":r.get("api_url",""),
        "primary_image":r.get("primary_image",""),
        "primary_image_small":r.get("primary_image_small",""),
        "additional_image_count":r.get("additional_image_count","0") or "0",
        "additional_images":r.get("additional_images",""),
        "source_merge":"prior_successful_api_fallback_after_transient_403",
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("live_csv")
    ap.add_argument("fallback_api_csv")
    ap.add_argument("--outdir",required=True)
    args=ap.parse_args()
    out=Path(args.outdir); out.mkdir(parents=True,exist_ok=True)

    live=read_csv(args.live_csv)
    fallback=read_csv(args.fallback_api_csv)

    merged={}
    false_positive=[]
    for r in live:
        acc=r.get("accession","")
        if acc=="2025.618.4":
            x=normalize_live(r,"live_search_false_positive")
            x["exclusion_reason"]="Japanese Edo painting; broad Suzhou text-search false positive"
            false_positive.append(x)
            continue
        merged[acc]=normalize_live(r,"live_suzhou_search")

    for r in fallback:
        acc=r.get("accession","")
        if acc in FALLBACK_ACCESSIONS:
            merged[acc]=normalize_fallback(r)

    # Verify the complete live 352–460 range.
    missing=[]
    live_range=[]
    for n in range(352,461):
        acc=f"2025.{n}"
        if acc not in merged:
            missing.append(acc)
        else:
            x=dict(merged[acc])
            x["range_352_460_member"]="1"
            x["working_107_member"]="1" if 354<=n<=460 else "0"
            x["boundary_role"]=("lower_boundary_candidate_outside_H2" if n in (352,353) else "H2_working_core")
            x["book_match_status"]="pending_catalogue_concordance"
            x["working_core_hypothesis"]="H2: 2025.354–2025.460 = 107 accessions"
            x["preferred_download_url"]=x.get("primary_image","") if x.get("public_domain")=="1" else ""
            x["download_status"]=("official_original_public_domain" if x["preferred_download_url"] else ("known_restricted_non_PD" if acc in RESTRICTED else "no_current_public_original"))
            live_range.append(x)
    if missing:
        raise RuntimeError(f"Incomplete 2025.352–460 live range after fallback merge: {missing}")

    core=[r for r in live_range if r["working_107_member"]=="1"]
    if len(core)!=107:
        raise RuntimeError(f"H2 core count is {len(core)}, expected 107")

    # Explicit separate gifts from von der Burg.
    gifts=[]
    for acc in ("2025.797.1","2025.797.2"):
        if acc in merged:
            x=dict(merged[acc])
            x["relationship_status"]="explicit_Gift_of_Christer_von_der_Burg_2025"
            x["book_match_status"]="pending_catalogue_concordance"
            gifts.append(x)

    fields=list(live_range[0].keys())
    with (out/"met_suzhou_2025_live_range_352_460.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(live_range)

    with (out/"met_gusu_v2_working_core_107.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(core)

    image_fields=["machine_id","accession","object_id","title_en","title_zh","medium","classification","credit_line","public_domain","object_url","primary_image","primary_image_small","additional_image_count","additional_images","preferred_download_url","download_status","book_match_status"]
    image_rows=[r for r in core if r.get("preferred_download_url")]
    with (out/"met_gusu_v2_image_manifest.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=image_fields); w.writeheader(); w.writerows([{k:r.get(k,"") for k in image_fields} for r in image_rows])

    noimg=[r for r in core if not r.get("preferred_download_url")]
    with (out/"met_gusu_v2_no_public_original.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=image_fields); w.writeheader(); w.writerows([{k:r.get(k,"") for k in image_fields} for r in noimg])

    gift_fields=list(gifts[0].keys()) if gifts else list(merged.values())[0].keys()
    with (out/"met_gusu_v2_related_vonderburg_gifts.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=gift_fields); w.writeheader(); w.writerows(gifts)

    fp_fields=list(false_positive[0].keys()) if false_positive else ["machine_id","accession","exclusion_reason"]
    with (out/"met_gusu_v2_false_positive.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=fp_fields); w.writeheader(); w.writerows(false_positive)

    boundary=[
        {"accession":"2025.352","status":"verified_live_Suzhou_related","H1_352_460":1,"H2_354_460":0,"role":"lower_excluded_candidate_under_H2","reason":"same-year live Suzhou accession; no von der Burg provenance hard-linked yet"},
        {"accession":"2025.353","status":"verified_live_Suzhou_related","H1_352_460":1,"H2_354_460":0,"role":"lower_excluded_candidate_under_H2","reason":"same-year live Suzhou accession; no von der Burg provenance hard-linked yet"},
        {"accession":"2025.354","status":"verified_live_Suzhou_related","H1_352_460":1,"H2_354_460":1,"role":"lowest_working_core_accession","reason":"354–460 inclusive contains exactly 107 accessions"},
        {"accession":"2025.460","status":"verified_live_Suzhou_related","H1_352_460":1,"H2_354_460":1,"role":"highest_working_core_accession","reason":"special Furniture record containing Gusu Beauty in Winter print; retained because accession is inside H2 boundary"},
        {"accession":"2025.797.1","status":"verified_explicit_vonderburg_gift","H1_352_460":0,"H2_354_460":0,"role":"separate_related_gift","reason":"credit line explicitly Gift of Christer von der Burg, 2025"},
        {"accession":"2025.797.2","status":"verified_explicit_vonderburg_gift","H1_352_460":0,"H2_354_460":0,"role":"separate_related_gift","reason":"credit line explicitly Gift of Christer von der Burg, 2025"},
    ]
    bfields=list(boundary[0].keys())
    with (out/"met_gusu_v2_boundary_audit.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=bfields); w.writeheader(); w.writerows(boundary)

    meta={
        "generated_utc":datetime.now(timezone.utc).isoformat(),
        "version":"MET-v2",
        "verified_live_range_352_460_count":len(live_range),
        "verified_live_range_complete":True,
        "H1":{"definition":"2025.352–2025.460","count":109,"status":"verified_contiguous_live_Suzhou_related_range_not_corpus_boundary"},
        "H2":{"definition":"2025.354–2025.460","count":len(core),"status":"strong_structural_working_core_pending_catalogue_or_provenance_boundary_confirmation","arithmetic_basis":"220 joint total - 113 CMA = 107 Met"},
        "working_core_107_image_coverage":{
            "public_original_primary_image":len(image_rows),
            "no_public_original":len(noimg),
            "restricted_expected_accessions":sorted(RESTRICTED,key=sortkey),
            "coverage_percent":round(len(image_rows)/107*100,2)
        },
        "working_core_record_notes":{
            "2025.437":"four-panel folding screen; one accession, primary image plus four additional original photographs",
            "2025.460":"Furniture classification; wooden chest with print Gusu Beauty in Winter pasted inside"
        },
        "lower_boundary_unresolved_membership":["2025.352","2025.353"],
        "separate_explicit_vonderburg_gifts":[r["accession"] for r in gifts],
        "excluded_false_positive":[r["accession"] for r in false_positive],
        "book_entry_coverage_status":"not yet equivalent to accession-level image coverage; catalogue concordance pending"
    }
    (out/"met_gusu_v2_summary.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps(meta,ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
