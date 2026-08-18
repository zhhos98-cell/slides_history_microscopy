#!/usr/bin/env python3
"""Enrich verified Met Gusu accessions from the official Met Collection API.

Input is the backed-up canonical manifest split into deterministic parts.
Only rows already marked as verified Met records are queried. The script does
not promote sequence gaps. It reports image assets and flags possible
multi-print / multi-panel objects for later physical-count reconciliation.
"""
from __future__ import annotations
import argparse, csv, io, json, re, time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

API='https://collectionapi.metmuseum.org/public/collection/v1/objects/{}'
UA='GusuVonDerBurgMetEnricher/1.0 research-use'


def get_json(url,retries=4,timeout=45):
    last=None
    for i in range(retries):
        try:
            req=Request(url,headers={'User-Agent':UA,'Accept':'application/json'})
            with urlopen(req,timeout=timeout) as r:
                return getattr(r,'status',200),json.load(r)
        except HTTPError as e:
            if e.code==404:return 404,None
            last=e
        except (URLError,TimeoutError,json.JSONDecodeError) as e:last=e
        time.sleep(1*(i+1))
    raise RuntimeError(f'GET failed {url}: {last}')


def load_canonical(parts_dir:Path):
    text=''.join(p.read_text(encoding='utf-8') for p in sorted(parts_dir.glob('part_*')))
    return list(csv.DictReader(io.StringIO(text)))


def sortkey(acc):
    out=[]
    for p in (acc or '').split('.'):
        try:out.append((0,int(p)))
        except:out.append((1,p))
    return out


def multipart_hint(title,medium,dimensions,additional_count):
    blob=' '.join([title or '',medium or '',dimensions or '']).lower()
    reasons=[]
    patterns=[
      r'\btwo[- ](?:panel|part|sheet|print)',r'\bthree[- ](?:panel|part|sheet|print)',
      r'\bfour[- ](?:panel|part|sheet|print)',r'\bfive[- ](?:panel|part|sheet|print)',
      r'\bsix[- ](?:panel|part|sheet|print)',r'\bseven[- ](?:panel|part|sheet|print)',
      r'\beight[- ](?:panel|part|sheet|print)',r'\bnine[- ](?:panel|part|sheet|print)',
      r'\bten[- ](?:panel|part|sheet|print)',r'folding screen',r'album',r'booklet',
      r'pair of',r'set of',r'multiple',r'each panel',r'each sheet'
    ]
    for pat in patterns:
        if re.search(pat,blob):reasons.append(pat)
    if additional_count>=3:reasons.append(f'additional_images={additional_count}')
    return '|'.join(reasons)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('canonical_parts_dir')
    ap.add_argument('--outdir',required=True)
    ap.add_argument('--delay',type=float,default=0.08)
    args=ap.parse_args()
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    rows=load_canonical(Path(args.canonical_parts_dir))
    met=[r for r in rows if r.get('museum_code')=='MET' and r.get('is_verified_museum_record')=='1']
    met.sort(key=lambda r:sortkey(r['accession']))
    enriched=[]; unresolved=[]
    for i,r in enumerate(met,1):
        oid=(r.get('object_id') or '').strip()
        if not oid:
            unresolved.append({'accession':r['accession'],'reason':'verified_set_member_without_object_id','source_url':r.get('source_url','')})
            continue
        status,obj=get_json(API.format(oid))
        if not obj:
            unresolved.append({'accession':r['accession'],'reason':f'API_no_data_http_{status}','source_url':r.get('source_url','')})
            continue
        add=obj.get('additionalImages') or []
        hint=multipart_hint(obj.get('title',''),obj.get('medium',''),obj.get('dimensions',''),len(add) if isinstance(add,list) else 0)
        enriched.append({
          'machine_id':'MET:'+r['accession'],
          'accession':r['accession'],'object_id':oid,
          'title_en':obj.get('title',''),'title_zh':r.get('title_zh',''),
          'culture':obj.get('culture',''),'period':obj.get('period',''),'object_date':obj.get('objectDate',''),
          'medium':obj.get('medium',''),'dimensions':obj.get('dimensions',''),
          'classification':obj.get('classification',''),'department':obj.get('department',''),
          'credit_line':obj.get('creditLine',''),'is_public_domain':'1' if obj.get('isPublicDomain') else '0',
          'object_url':obj.get('objectURL',''),'api_url':API.format(oid),
          'primary_image':obj.get('primaryImage',''),'primary_image_small':obj.get('primaryImageSmall',''),
          'additional_image_count':len(add) if isinstance(add,list) else 0,
          'additional_images':'|'.join(add) if isinstance(add,list) else '',
          'has_primary_image':'1' if obj.get('primaryImage') else '0',
          'multipart_candidate':'1' if hint else '0','multipart_hint':hint,
          'api_checked_utc':datetime.now(timezone.utc).isoformat(),
        })
        if i%20==0:print(f'checked {i}/{len(met)}')
        time.sleep(args.delay)
    fields=list(enriched[0].keys()) if enriched else []
    with (out/'met_gusu_api_enriched.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(enriched)
    with (out/'met_gusu_api_unresolved.csv').open('w',newline='',encoding='utf-8') as f:
        uf=['accession','reason','source_url'];w=csv.DictWriter(f,fieldnames=uf);w.writeheader();w.writerows(unresolved)
    multi=[r for r in enriched if r['multipart_candidate']=='1']
    with (out/'met_gusu_api_multipart_candidates.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(multi)
    meta={
      'generated_utc':datetime.now(timezone.utc).isoformat(),
      'verified_met_accessions_input':len(met),
      'api_enriched_rows':len(enriched),
      'verified_without_object_id_or_api_data':unresolved,
      'public_domain_rows':sum(r['is_public_domain']=='1' for r in enriched),
      'primary_image_rows':sum(r['has_primary_image']=='1' for r in enriched),
      'additional_image_assets_total':sum(int(r['additional_image_count']) for r in enriched),
      'multipart_candidate_rows':len(multi),
      'multipart_accessions':[r['accession'] for r in multi],
      'note':'Multipart candidates are flags only. Additional-image count is not assumed to equal physical-print count.'
    }
    (out/'met_gusu_api_summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
