#!/usr/bin/env python3
"""Build a conservative 113-unit working core from official CMA API rows.

Working rule, derived from CMA's own record semantics:
- base accession range 2025.19–2025.128 is the working acquisition block;
- ordinary `object` records count once;
- a `cover` with `component` children is replaced by those independently
  meaningful component records (cover counts 0, components count 1 each);
- a `cover` with only `part` children counts once and the dependent parts count 0.

This rule yields exactly 113 count units and is kept explicit so it can be
revised if the published catalogue proves a different boundary. 2025.129 is
retained separately as a verified von der Burg purchase, not silently dropped.
"""
from __future__ import annotations
import argparse, csv, json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


def base_num(acc):
    p=(acc or '').split('.')
    if len(p)<2 or p[0] != '2025': return None
    try: return int(p[1])
    except ValueError: return None


def sortkey(acc):
    out=[]
    for p in (acc or '').split('.'):
        try: out.append((0,int(p)))
        except: out.append((1,p))
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('api_csv')
    ap.add_argument('--outdir',required=True)
    args=ap.parse_args()
    out=Path(args.outdir); out.mkdir(parents=True,exist_ok=True)
    with open(args.api_csv,newline='',encoding='utf-8-sig') as f:
        rows=list(csv.DictReader(f))

    by_base=defaultdict(list)
    for r in rows:
        n=base_num(r['accession'])
        if n is not None:
            by_base[f'2025.{n}'].append(r)

    core_rows=[]
    for n in range(19,129):
        base=f'2025.{n}'
        members=by_base.get(base,[])
        if not members:
            raise RuntimeError(f'Missing official API rows for {base}')
        cover=next((r for r in members if r['accession']==base and r['record_type']=='cover'),None)
        components=[r for r in members if r['record_type']=='component']
        parts=[r for r in members if r['record_type']=='part']
        obj=next((r for r in members if r['accession']==base and r['record_type']=='object'),None)

        selected=[]; rule=''
        if cover and components:
            selected=components
            rule='component_children_replace_cover'
        elif cover and parts:
            selected=[cover]
            rule='cover_counts_once_dependent_parts_do_not_count'
        elif obj:
            selected=[obj]
            rule='object_counts_once'
        elif cover:
            selected=[cover]
            rule='cover_counts_once_no_children_detected'
        else:
            raise RuntimeError(f'Cannot determine count unit for {base}: {[r["record_type"] for r in members]}')

        for r in selected:
            x=dict(r)
            x['working_core_version']='CMA-v1.5'
            x['working_core_base']=base
            x['working_core_member']='1'
            x['working_core_count_unit']='1'
            x['working_core_count_rule']=rule
            x['working_core_boundary_basis']='2025.19-2025.128 + CMA record_type semantics'
            x['preferred_download_url']=r.get('image_full') or r.get('image_print') or r.get('image_web') or ''
            x['preferred_download_kind']='full_tiff' if r.get('image_full') else ('print_jpeg' if r.get('image_print') else ('web_jpeg' if r.get('image_web') else ''))
            core_rows.append(x)

    core_rows.sort(key=lambda r:sortkey(r['accession']))
    if len(core_rows)!=113:
        raise RuntimeError(f'Working core did not close to 113: got {len(core_rows)}')

    # Build excluded/detail rows so no information disappears.
    core_accessions={r['accession'] for r in core_rows}
    detail=[]
    for r in rows:
        n=base_num(r['accession'])
        if n is None: continue
        reason=''
        if 19<=n<=128 and r['accession'] not in core_accessions:
            if r['record_type']=='cover': reason='cover_replaced_by_components'
            elif r['record_type']=='part': reason='dependent_part_of_counted_cover'
            else: reason='non_counting_detail_record'
        elif n==129:
            reason='verified_vonderburg_purchase_outside_working_113_core_pending_catalogue_confirmation'
        elif n in (212,213,214):
            reason='separate_2025_vonderburg_gift'
        else:
            continue
        x=dict(r); x['v15_exclusion_or_detail_reason']=reason; detail.append(x)

    fields=list(core_rows[0].keys())
    core_path=out/'cma_gusu_v15_working_core_113.csv'
    with core_path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(core_rows)

    detail_fields=list(detail[0].keys()) if detail else list(rows[0].keys())+['v15_exclusion_or_detail_reason']
    with (out/'cma_gusu_v15_noncounting_and_related.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=detail_fields); w.writeheader(); w.writerows(detail)

    image_rows=[r for r in core_rows if r['preferred_download_url']]
    image_fields=['machine_id','accession','working_core_base','record_type','title_en','title_zh','share_license_status','url','image_web','image_print','image_full','preferred_download_url','preferred_download_kind']
    with (out/'cma_gusu_v15_image_download_manifest.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=image_fields); w.writeheader(); w.writerows([{k:r.get(k,'') for k in image_fields} for r in image_rows])

    noimg=[r for r in core_rows if not r['preferred_download_url']]
    noimg_fields=['machine_id','accession','working_core_base','record_type','title_en','title_zh','url','share_license_status']
    with (out/'cma_gusu_v15_no_current_image.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=noimg_fields); w.writeheader(); w.writerows([{k:r.get(k,'') for k in noimg_fields} for r in noimg])

    meta={
      'generated_utc':datetime.now(timezone.utc).isoformat(),
      'version':'CMA-v1.5',
      'working_core_definition':'base 2025.19–2025.128 inclusive; object=1; component children replace cover; part children do not replace counted cover',
      'working_core_count':len(core_rows),
      'count_by_record_type':{t:sum(r['record_type']==t for r in core_rows) for t in ['object','cover','component','part']},
      'special_groups':{
        '2025.82':'cover excluded; four components counted independently',
        '2025.91':'cover counted once; two parts retained as detail only',
        '2025.92':'cover counted once; three parts retained as detail only'
      },
      'image_coverage_core_113':{
        'web':sum(bool(r.get('image_web')) for r in core_rows),
        'print':sum(bool(r.get('image_print')) for r in core_rows),
        'full':sum(bool(r.get('image_full')) for r in core_rows),
        'any_preferred_download':len(image_rows),
        'no_current_image':len(noimg),
        'coverage_percent':round(len(image_rows)/113*100,2)
      },
      'verified_related_not_counted':{
        '2025.129':'May You Soon Bear Noble Sons; object; CC0; Purchase from J. H. Wade Fund; von der Burg sale; excluded from working 113 boundary pending catalogue confirmation',
        '2025.212':'Zhang Xian Brings Sons; separate gift',
        '2025.213':'One Hundred Boys (1990s); separate copyrighted gift',
        '2025.214':'One Hundred Boys (1970s); separate copyrighted gift'
      },
      'epistemic_status':'working core closes exactly to CMA reported 113 using official API record semantics; 2025.129 boundary still awaits independent catalogue/acquisition-context confirmation'
    }
    (out/'cma_gusu_v15_summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
