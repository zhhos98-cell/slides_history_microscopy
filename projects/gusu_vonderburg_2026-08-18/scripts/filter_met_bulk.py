#!/usr/bin/env python3
"""Filter the official Met Open Access bulk CSV for 2025 Asian Art prints.

Outputs broad and narrow slices so discovery does not depend on one fragile
keyword. The accession-neighborhood slice is also retained to audit sequence
gaps from the previously reconstructed Gusu manifest.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,re
from datetime import datetime,timezone
from pathlib import Path


def norm(s): return re.sub(r'[^a-z0-9]+','',(s or '').lower())
def alias(fields,names):
    m={norm(f):f for f in fields}
    for n in names:
        if norm(n) in m:return m[norm(n)]
    return ''
def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for ch in iter(lambda:f.read(1024*1024),b''):h.update(ch)
    return h.hexdigest()
def objnum(s):
    m=re.fullmatch(r'2025\.(\d+)(?:\.(.+))?',(s or '').strip())
    if not m:return None,None
    return int(m.group(1)),m.group(2) or ''

def main():
    ap=argparse.ArgumentParser();ap.add_argument('csv');ap.add_argument('--outdir',required=True);ap.add_argument('--source-commit',default='');ap.add_argument('--lfs-oid',default='');args=ap.parse_args()
    src=Path(args.csv);out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    with src.open('r',newline='',encoding='utf-8-sig',errors='replace') as f:
        rd=csv.DictReader(f);fields=rd.fieldnames or [];rows=list(rd)
    fnum=alias(fields,['Object Number','ObjectNumber','accession_number'])
    fyear=alias(fields,['AccessionYear','Accession Year'])
    fdept=alias(fields,['Department'])
    fclass=alias(fields,['Classification'])
    fculture=alias(fields,['Culture'])
    ftitle=alias(fields,['Title'])
    fmedium=alias(fields,['Medium'])
    fcredit=alias(fields,['Credit Line','CreditLine'])
    flink=alias(fields,['Link Resource','LinkResource'])
    fid=alias(fields,['Object ID','ObjectID'])
    fpublic=alias(fields,['Is Public Domain','IsPublicDomain'])
    fdimensions=alias(fields,['Dimensions'])
    fobjectname=alias(fields,['Object Name','ObjectName'])
    required={'object_number':fnum,'department':fdept}
    if not all(required.values()):raise RuntimeError(f'Missing required headers: {required}; got {fields}')

    def is2025(r):
        return (r.get(fyear,'').strip()=='2025') if fyear else (r.get(fnum,'').startswith('2025.'))
    def is_asian(r):return 'asian' in r.get(fdept,'').lower()
    def is_print(r):
        blob=' '.join([r.get(fclass,''),r.get(fobjectname,''),r.get(fmedium,'')]).lower()
        return 'print' in blob or 'woodblock' in blob
    def suzhou_signal(r):
        blob=' '.join([r.get(fculture,''),r.get(ftitle,''),r.get(fmedium,''),r.get(fcredit,'')]).lower()
        return 'suzhou' in blob or 'gusu' in blob

    broad=[r for r in rows if is2025(r) and is_asian(r) and is_print(r)]
    suzhou=[r for r in broad if suzhou_signal(r)]
    neigh=[]
    for r in rows:
        if not is2025(r) or not is_asian(r):continue
        n,suf=objnum(r.get(fnum,''))
        if (n is not None and 357<=n<=439) or (n==797 and suf in ('1','2')):
            neigh.append(r)

    def write(name,data):
        p=out/name
        with p.open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
        return p
    write('met_2025_asian_art_prints_full.csv',broad)
    write('met_2025_asian_art_prints_suzhou_signal.csv',suzhou)
    write('met_2025_accession_neighborhood_357_439_797.csv',neigh)

    def compact(data,name):
        cf=['object_number','object_id','title','culture','object_name','classification','medium','dimensions','credit_line','public_domain','link_resource','suzhou_signal']
        rr=[]
        for r in data:
            rr.append({
              'object_number':r.get(fnum,''),'object_id':r.get(fid,'') if fid else '',
              'title':r.get(ftitle,'') if ftitle else '','culture':r.get(fculture,'') if fculture else '',
              'object_name':r.get(fobjectname,'') if fobjectname else '','classification':r.get(fclass,'') if fclass else '',
              'medium':r.get(fmedium,'') if fmedium else '','dimensions':r.get(fdimensions,'') if fdimensions else '',
              'credit_line':r.get(fcredit,'') if fcredit else '','public_domain':r.get(fpublic,'') if fpublic else '',
              'link_resource':r.get(flink,'') if flink else '','suzhou_signal':'1' if suzhou_signal(r) else '0'
            })
        rr.sort(key=lambda x:(objnum(x['object_number'])[0] or 999999,objnum(x['object_number'])[1]))
        with (out/name).open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=cf);w.writeheader();w.writerows(rr)
        return rr
    bcomp=compact(broad,'met_2025_asian_art_prints_compact.csv')
    scomp=compact(suzhou,'met_2025_suzhou_signal_compact.csv')
    ncomp=compact(neigh,'met_2025_accession_neighborhood_compact.csv')

    known={str(n) for n in [357,358,359,360,361,362,364,367,368,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,395,396,397,398,399,400,401,402,403,405,406,407,408,409,410,411,412,413,415,416,417,418,419,420,421,423,424,425,426,427,428,430,431,432,433,434,436,437,438,439]}
    known.update({'797.1','797.2'})
    discovered={r['object_number'].replace('2025.','',1) for r in ncomp}
    gaps=[str(n) for n in range(357,440) if str(n) not in discovered]
    new_vs_known=sorted(discovered-known,key=lambda s:objnum('2025.'+s))
    known_missing=sorted(known-discovered,key=lambda s:objnum('2025.'+s))
    meta={
      'generated_utc':datetime.now(timezone.utc).isoformat(),
      'source_repo':'metmuseum/openaccess','source_commit':args.source_commit,'source_lfs_oid':args.lfs_oid,
      'source_size':src.stat().st_size,'source_sha256':sha256(src),'source_rows':len(rows),'headers':fields,
      'broad_2025_asian_art_print_rows':len(broad),'suzhou_signal_rows':len(suzhou),'accession_neighborhood_rows':len(neigh),
      'accession_neighborhood_numbers':[r['object_number'] for r in ncomp],
      'numeric_gaps_357_439':gaps,'discovered_not_in_prior_verified_set':new_vs_known,'prior_verified_not_in_bulk_neighborhood':known_missing,
      'note':'Suzhou signal is a discovery filter, not a final corpus-membership test.'
    }
    (out/'met_bulk_discovery_summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
