#!/usr/bin/env python3
"""Probe a narrow live Met Collection API object-ID neighborhood.

The official bulk CSV currently stops at 2023, while this acquisition is live
in the Collection API. Known Gusu object IDs cluster tightly in 9118xx–9119xx,
with one known record at 913059. This probe audits those neighborhoods without
assuming accession-number continuity.
"""
from __future__ import annotations
import argparse,csv,json,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.error import HTTPError,URLError
from urllib.request import Request,urlopen

API='https://collectionapi.metmuseum.org/public/collection/v1/objects/{}'
UA='GusuMetLiveNeighborhoodProbe/1.0 research-use'

KNOWN={
'2025.357','2025.358','2025.359','2025.360','2025.361','2025.362','2025.364','2025.367','2025.368','2025.370','2025.371','2025.372','2025.373','2025.374','2025.375','2025.376','2025.377','2025.378','2025.379','2025.380','2025.381','2025.382','2025.383','2025.384','2025.385','2025.386','2025.387','2025.388','2025.389','2025.390','2025.391','2025.392','2025.393','2025.395','2025.396','2025.397','2025.398','2025.399','2025.400','2025.401','2025.402','2025.403','2025.405','2025.406','2025.407','2025.408','2025.409','2025.410','2025.411','2025.412','2025.413','2025.415','2025.416','2025.417','2025.418','2025.419','2025.420','2025.421','2025.423','2025.424','2025.425','2025.426','2025.427','2025.428','2025.430','2025.431','2025.432','2025.433','2025.434','2025.436','2025.437','2025.438','2025.439','2025.797.1','2025.797.2'}
GAPS={'2025.363','2025.365','2025.366','2025.369','2025.394','2025.404','2025.414','2025.422','2025.429','2025.435'}

def get(oid,retries=3,timeout=30):
    last=None
    for i in range(retries):
        try:
            req=Request(API.format(oid),headers={'User-Agent':UA,'Accept':'application/json'})
            with urlopen(req,timeout=timeout) as r:return getattr(r,'status',200),json.load(r)
        except HTTPError as e:
            if e.code==404:return 404,None
            last=e
        except (URLError,TimeoutError,json.JSONDecodeError) as e:last=e
        time.sleep(.4*(i+1))
    return 0,{'_error':repr(last)}

def accsort(a):
    out=[]
    for p in a.split('.'):
        try:out.append((0,int(p)))
        except:out.append((1,p))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--outdir',required=True);ap.add_argument('--delay',type=float,default=.035);args=ap.parse_args()
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    ranges=[range(911780,912021),range(913040,913081)]
    found=[];errors=[];checked=0
    for rg in ranges:
        for oid in rg:
            checked+=1;status,payload=get(oid)
            if status==404:
                time.sleep(args.delay);continue
            if not payload or payload.get('_error'):
                errors.append({'object_id':oid,'status':status,'error':payload.get('_error','no payload') if payload else 'no payload'})
                time.sleep(args.delay);continue
            acc=str(payload.get('accessionNumber') or '').strip()
            dept=str(payload.get('department') or '')
            if acc.startswith('2025.') and 'Asian Art' in dept:
                add=payload.get('additionalImages') or []
                found.append({
                  'accession':acc,'object_id':oid,'title':payload.get('title',''),'culture':payload.get('culture',''),
                  'period':payload.get('period',''),'object_date':payload.get('objectDate',''),'medium':payload.get('medium',''),
                  'dimensions':payload.get('dimensions',''),'classification':payload.get('classification',''),'department':dept,
                  'credit_line':payload.get('creditLine',''),'public_domain':'1' if payload.get('isPublicDomain') else '0',
                  'object_url':payload.get('objectURL',''),'primary_image':payload.get('primaryImage',''),
                  'additional_image_count':len(add) if isinstance(add,list) else 0,
                  'additional_images':'|'.join(add) if isinstance(add,list) else '',
                  'prior_known':'1' if acc in KNOWN else '0','prior_gap':'1' if acc in GAPS else '0',
                })
            time.sleep(args.delay)
    found.sort(key=lambda r:accsort(r['accession']))
    fields=list(found[0].keys()) if found else ['accession','object_id']
    with (out/'met_live_object_id_neighborhood_2025_asian.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(found)
    with (out/'met_live_object_id_probe_errors.csv').open('w',newline='',encoding='utf-8') as f:
        ef=['object_id','status','error'];w=csv.DictWriter(f,fieldnames=ef);w.writeheader();w.writerows(errors)
    discovered={r['accession'] for r in found}
    meta={
      'generated_utc':datetime.now(timezone.utc).isoformat(),'object_ids_checked':checked,
      'ranges':['911780-912020','913040-913080'],'2025_asian_rows_found':len(found),
      'accessions_found':[r['accession'] for r in found],
      'new_vs_prior_known':sorted(discovered-KNOWN,key=accsort),
      'prior_known_found':sorted(discovered&KNOWN,key=accsort),
      'prior_known_not_in_scanned_ids':sorted(KNOWN-discovered,key=accsort),
      'prior_gap_accessions_found':sorted(discovered&GAPS,key=accsort),
      'prior_gap_accessions_not_found':sorted(GAPS-discovered,key=accsort),
      'probe_errors':errors,
      'note':'Object-ID neighborhood absence is stronger than web-index absence but is not a global Met API proof; known records outside these ID ranges would not be discovered.'
    }
    (out/'met_live_object_id_probe_summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
