#!/usr/bin/env python3
"""Combine the current CMA-113 and Met-107 working cores.

This produces a museum-unit working 220, not a finished catalogue concordance.
The table is designed so catalogue number / plate / page can be filled later
without changing museum or image identifiers.
"""
from __future__ import annotations
import argparse,csv,json
from datetime import datetime,timezone
from pathlib import Path


def read(path):
    with open(path,newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))

def sortkey(r):
    parts=[]
    for p in (r.get('accession') or '').split('.'):
        try:parts.append((0,int(p)))
        except:parts.append((1,p))
    return (r.get('museum_code',''),parts)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('cma');ap.add_argument('met');ap.add_argument('--outdir',required=True);args=ap.parse_args()
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    cma=read(args.cma);met=read(args.met)
    if len(cma)!=113:raise RuntimeError(f'CMA core count {len(cma)} != 113')
    if len(met)!=107:raise RuntimeError(f'Met core count {len(met)} != 107')
    rows=[]
    for r in cma:
        rows.append({
          'working_220_id':f"CMA:{r['accession']}",'museum_code':'CMA','museum_name':'Cleveland Museum of Art',
          'accession':r['accession'],'object_id':r.get('id',''),'record_type':r.get('record_type',''),
          'cover_accession_number':r.get('cover_accession_number',''),'title_en':r.get('title_en',''),'title_zh':r.get('title_zh',''),
          'culture':r.get('culture',''),'date_or_period':r.get('creation_date',''),'medium_or_technique':r.get('technique',''),
          'classification_or_type':r.get('type',''),'object_url':r.get('url',''),'api_url':r.get('api_url',''),
          'public_domain':'1' if r.get('share_license_status')=='CC0' else '0',
          'original_image_url':r.get('image_full',''),'print_image_url':r.get('image_print',''),'web_image_url':r.get('image_web',''),
          'additional_images':'','additional_image_count':'0',
          'downloadable_original':'1' if r.get('image_full') else '0','download_status':'official_full_tiff_CC0' if r.get('image_full') else 'no_current_CMA_API_image',
          'museum_core_version':'CMA-v1.5','museum_core_status':'working_113_unit','boundary_hypothesis':'CMA 2025.19–2025.128 + official record semantics',
          'boundary_confidence':'strong_structural_pending_book_concordance','book_catalogue_no':'','book_plate_no':'','book_page':'',
          'book_match_status':'pending_catalogue_concordance','book_match_basis':'','book_match_confidence':'',
          'notes':r.get('working_core_count_rule','')
        })
    for r in met:
        rows.append({
          'working_220_id':f"MET:{r['accession']}",'museum_code':'MET','museum_name':'The Metropolitan Museum of Art',
          'accession':r['accession'],'object_id':r.get('object_id',''),'record_type':'museum_object','cover_accession_number':'',
          'title_en':r.get('title_en',''),'title_zh':r.get('title_zh',''),'culture':r.get('culture',''),
          'date_or_period':r.get('object_date') or r.get('period',''),'medium_or_technique':r.get('medium',''),
          'classification_or_type':r.get('classification',''),'object_url':r.get('object_url',''),'api_url':r.get('api_url',''),
          'public_domain':r.get('public_domain',''),'original_image_url':r.get('primary_image',''),'print_image_url':'','web_image_url':r.get('primary_image_small',''),
          'additional_images':r.get('additional_images',''),'additional_image_count':r.get('additional_image_count','0'),
          'downloadable_original':'1' if r.get('preferred_download_url') else '0','download_status':r.get('download_status',''),
          'museum_core_version':'MET-v2','museum_core_status':'working_107_accession','boundary_hypothesis':'MET H2 2025.354–2025.460',
          'boundary_confidence':'strong_structural_pending_book_or_provenance_boundary_confirmation','book_catalogue_no':'','book_plate_no':'','book_page':'',
          'book_match_status':'pending_catalogue_concordance','book_match_basis':'','book_match_confidence':'',
          'notes':('four-panel folding screen' if r['accession']=='2025.437' else ('wooden chest with Gusu print pasted inside' if r['accession']=='2025.460' else ''))
        })
    rows.sort(key=sortkey)
    if len(rows)!=220:raise RuntimeError(f'Combined count {len(rows)} != 220')
    fields=list(rows[0].keys())
    with (out/'gusu_working_220_museum_units.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    images=[r for r in rows if r['downloadable_original']=='1']
    with (out/'gusu_working_220_official_image_manifest.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(images)
    noimg=[r for r in rows if r['downloadable_original']!='1']
    with (out/'gusu_working_220_no_public_original.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(noimg)
    summary={
      'generated_utc':datetime.now(timezone.utc).isoformat(),'version':'combined-working-v2',
      'working_museum_unit_count':len(rows),'CMA_units':len(cma),'MET_units':len(met),
      'official_original_image_rows':len(images),'no_public_original_rows':len(noimg),'museum_unit_image_coverage_percent':round(len(images)/220*100,2),
      'by_museum':{
        'CMA':{'working_units':113,'original_images':sum(r['museum_code']=='CMA' and r['downloadable_original']=='1' for r in rows)},
        'MET':{'working_units':107,'original_images':sum(r['museum_code']=='MET' and r['downloadable_original']=='1' for r in rows)}
      },
      'epistemic_warning':'140/220 is provisional museum-unit image coverage under CMA-v1.5 and MET-v2 structural boundaries. It is NOT yet a verified 140-of-220 book-entry concordance.',
      'catalogue_fields_ready':['book_catalogue_no','book_plate_no','book_page','book_match_status','book_match_basis','book_match_confidence'],
      'next_step':'Recover catalogue order/numbers and match book entries to museum units; keep multipart/accession semantics explicit.'
    }
    (out/'gusu_working_220_summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
