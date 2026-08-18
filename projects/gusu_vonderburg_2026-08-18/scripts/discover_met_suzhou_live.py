#!/usr/bin/env python3
"""Discover currently live 2025 Suzhou records from The Met Collection API.

This replaces dependence on the stale Met bulk CSV and on guessed object-ID
ranges. It uses the official live search endpoint (`departmentId=6&q=Suzhou`),
then verifies every returned object through `/objects/{id}` and retains only
2025 Asian Art accessions. The ten previously observed accession gaps are also
queried individually and only exact accession-number matches are accepted.
"""
from __future__ import annotations
import argparse,csv,json,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.error import HTTPError,URLError
from urllib.parse import urlencode
from urllib.request import Request,urlopen

BASE='https://collectionapi.metmuseum.org/public/collection/v1'
UA='GusuMetLiveSuzhouDiscovery/1.0 research-use'
GAPS=['2025.363','2025.365','2025.366','2025.369','2025.394','2025.404','2025.414','2025.422','2025.429','2025.435']
KNOWN={
'2025.357','2025.358','2025.359','2025.360','2025.361','2025.362','2025.364','2025.367','2025.368','2025.370','2025.371','2025.372','2025.373','2025.374','2025.375','2025.376','2025.377','2025.378','2025.379','2025.380','2025.381','2025.382','2025.383','2025.384','2025.385','2025.386','2025.387','2025.388','2025.389','2025.390','2025.391','2025.392','2025.393','2025.395','2025.396','2025.397','2025.398','2025.399','2025.400','2025.401','2025.402','2025.403','2025.405','2025.406','2025.407','2025.408','2025.409','2025.410','2025.411','2025.412','2025.413','2025.415','2025.416','2025.417','2025.418','2025.419','2025.420','2025.421','2025.423','2025.424','2025.425','2025.426','2025.427','2025.428','2025.430','2025.431','2025.432','2025.433','2025.434','2025.436','2025.437','2025.438','2025.439','2025.797.1','2025.797.2'}

def get_json(url,retries=4,timeout=40):
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
        time.sleep(.7*(i+1))
    raise RuntimeError(f'GET failed {url}: {last}')

def search(q,department=6):
    url=BASE+'/search?'+urlencode({'departmentId':department,'q':q})
    _,data=get_json(url)
    return url,(data or {}).get('objectIDs') or []

def object_record(oid):
    status,data=get_json(f'{BASE}/objects/{oid}')
    return status,data

def sortkey(a):
    out=[]
    for p in a.split('.'):
        try:out.append((0,int(p)))
        except:out.append((1,p))
    return out

def normalized(o,discovery):
    add=o.get('additionalImages') or []
    return {
      'accession':str(o.get('accessionNumber') or ''),'object_id':o.get('objectID',''),
      'title_en':o.get('title',''),'culture':o.get('culture',''),'period':o.get('period',''),'object_date':o.get('objectDate',''),
      'medium':o.get('medium',''),'dimensions':o.get('dimensions',''),'classification':o.get('classification',''),'department':o.get('department',''),
      'credit_line':o.get('creditLine',''),'public_domain':'1' if o.get('isPublicDomain') else '0',
      'object_url':o.get('objectURL',''),'api_url':f"{BASE}/objects/{o.get('objectID','')}",
      'primary_image':o.get('primaryImage',''),'primary_image_small':o.get('primaryImageSmall',''),
      'additional_image_count':len(add) if isinstance(add,list) else 0,
      'additional_images':'|'.join(add) if isinstance(add,list) else '',
      'discovery_method':discovery,'prior_known':'1' if str(o.get('accessionNumber') or '') in KNOWN else '0'
    }

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--outdir',required=True);ap.add_argument('--delay',type=float,default=.05);args=ap.parse_args()
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    search_url,ids=search('Suzhou')
    found={};errors=[]
    for i,oid in enumerate(ids,1):
        try:
            _,o=object_record(oid)
            if not o:continue
            acc=str(o.get('accessionNumber') or '')
            if acc.startswith('2025.') and o.get('department')=='Asian Art':
                found[acc]=normalized(o,'live_search_suzhou')
        except Exception as e:errors.append({'stage':'suzhou_fetch','key':str(oid),'error':repr(e)})
        if i%50==0:print(f'Suzhou search fetch {i}/{len(ids)}')
        time.sleep(args.delay)

    gap_audit=[]
    for gap in GAPS:
        try:
            url,gids=search(gap)
            exact=[]
            for oid in gids:
                _,o=object_record(oid)
                if o and str(o.get('accessionNumber') or '')==gap:
                    exact.append(int(oid));found[gap]=normalized(o,'exact_accession_search')
                time.sleep(args.delay)
            gap_audit.append({'accession':gap,'search_url':url,'search_result_count':len(gids),'exact_object_ids':'|'.join(map(str,exact)),'exact_match':'1' if exact else '0'})
        except Exception as e:
            errors.append({'stage':'gap_search','key':gap,'error':repr(e)})
            gap_audit.append({'accession':gap,'search_url':'','search_result_count':'','exact_object_ids':'','exact_match':'error'})

    rows=sorted(found.values(),key=lambda r:sortkey(r['accession']))
    fields=list(rows[0].keys()) if rows else ['accession','object_id']
    with (out/'met_live_suzhou_2025_discovered.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    with (out/'met_live_gap_exact_search.csv').open('w',newline='',encoding='utf-8') as f:
        gf=['accession','search_url','search_result_count','exact_object_ids','exact_match'];w=csv.DictWriter(f,fieldnames=gf);w.writeheader();w.writerows(gap_audit)
    with (out/'met_live_suzhou_errors.csv').open('w',newline='',encoding='utf-8') as f:
        ef=['stage','key','error'];w=csv.DictWriter(f,fieldnames=ef);w.writeheader();w.writerows(errors)
    accs={r['accession'] for r in rows}
    meta={
      'generated_utc':datetime.now(timezone.utc).isoformat(),
      'official_search_url':search_url,'suzhou_search_object_id_count':len(ids),
      'live_2025_asian_suzhou_accession_count':len(rows),'accessions':sorted(accs,key=sortkey),
      'prior_known_recovered':sorted(accs&KNOWN,key=sortkey),'new_vs_prior_known':sorted(accs-KNOWN,key=sortkey),
      'prior_known_not_recovered_by_suzhou_query':sorted(KNOWN-accs,key=sortkey),
      'gap_exact_matches':[r['accession'] for r in gap_audit if r['exact_match']=='1'],
      'gap_no_exact_match':[r['accession'] for r in gap_audit if r['exact_match']=='0'],
      'public_domain_rows':sum(r.get('public_domain')=='1' for r in rows),
      'rows_with_primary_image':sum(bool(r.get('primary_image')) for r in rows),
      'errors':errors,
      'note':'Suzhou live-search membership is a discovery set, not automatically identical to the von der Burg book corpus. Exact gap searches only accept records whose returned accessionNumber exactly equals the gap accession.'
    }
    (out/'met_live_suzhou_summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
