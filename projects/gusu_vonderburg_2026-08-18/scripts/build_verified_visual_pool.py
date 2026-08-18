#!/usr/bin/env python3
"""Build a boundary-independent Gusu visual-matching pool.

No 113/107/220 arithmetic is used here.

Museum candidates:
- CMA: every current 2025 Christer von der Burg API row exposing image_web.
- Met: every verified live record in accession range 2025.352–2025.460 exposing
  a public-domain primary image.

Book samples:
- every current likely public catalogue sample image, deduplicated by exact URL.

The output schema intentionally supplies `working_220_id` because the existing
SIFT matcher expects that legacy field name; here it is only a stable candidate
identifier and does NOT imply membership in a 220-unit reconstruction.
"""
from __future__ import annotations
import argparse, csv, json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

# Trigger marker 2026-08-18: workflow now exists on default branch; no semantic change.


def read_csv(path):
    with open(path, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--cma', required=True)
    ap.add_argument('--met', required=True)
    ap.add_argument('--samples', required=True)
    ap.add_argument('--outdir', required=True)
    args=ap.parse_args()
    out=Path(args.outdir); out.mkdir(parents=True, exist_ok=True)

    cma=read_csv(args.cma)
    met=read_csv(args.met)
    samples=read_csv(args.samples)

    museum=[]
    for r in cma:
        url=(r.get('image_web') or '').strip()
        if not url: continue
        museum.append({
            'working_220_id': r.get('machine_id') or f"CMA:{r.get('accession','')}",
            'pool_basis': 'CMA_2025_vonderburg_API_has_image_web',
            'museum_code': 'CMA',
            'accession': r.get('accession',''),
            'object_id': r.get('id',''),
            'record_type': r.get('record_type',''),
            'acquisition_mode': r.get('acquisition_mode',''),
            'title_en': r.get('title_en',''),
            'title_zh': r.get('title_zh',''),
            'object_url': r.get('url',''),
            'web_image_url': url,
            'original_image_url': r.get('image_full') or r.get('image_print') or url,
            'public_domain': '1' if (r.get('share_license_status') or '').upper()=='CC0' else '0',
        })

    for r in met:
        # This file is already the independently verified live 352–460 range.
        if (r.get('range_352_460_member') or '') != '1': continue
        if (r.get('public_domain') or '') != '1': continue
        url=(r.get('primary_image_small') or r.get('primary_image') or '').strip()
        if not url: continue
        museum.append({
            'working_220_id': r.get('machine_id') or f"MET:{r.get('accession','')}",
            'pool_basis': 'MET_verified_live_2025.352_460_public_domain_primary_image',
            'museum_code': 'MET',
            'accession': r.get('accession',''),
            'object_id': r.get('object_id',''),
            'record_type': '',
            'acquisition_mode': '',
            'title_en': r.get('title_en',''),
            'title_zh': r.get('title_zh',''),
            'object_url': r.get('object_url',''),
            'web_image_url': url,
            'original_image_url': r.get('primary_image') or url,
            'public_domain': '1',
        })

    # Deduplicate museum candidates by museum + accession; retain first exact record.
    seen=set(); museum2=[]
    for r in museum:
        k=(r['museum_code'], r['accession'])
        if k in seen: continue
        seen.add(k); museum2.append(r)
    museum=museum2

    # Exact-URL dedupe on sample photographs (Shuseido has duplicate img tags).
    sample2=[]; seen_urls=set()
    for r in samples:
        u=(r.get('src') or '').strip()
        if not u or u in seen_urls: continue
        seen_urls.add(u)
        x=dict(r)
        x['sample_dedupe_key']=u
        sample2.append(x)

    mfields=['working_220_id','pool_basis','museum_code','accession','object_id','record_type','acquisition_mode','title_en','title_zh','object_url','web_image_url','original_image_url','public_domain']
    sfields=list(sample2[0].keys()) if sample2 else ['page_code','page_url','image_index','src','sample_dedupe_key']
    write_csv(out/'verified_museum_image_pool.csv', museum, mfields)
    write_csv(out/'deduped_public_book_samples.csv', sample2, sfields)

    meta={
        'generated_utc': datetime.now(timezone.utc).isoformat(),
        'boundary_policy': 'No CMA 113, Met 107, or combined 220 count boundary used.',
        'CMA_candidates_with_web_image': sum(r['museum_code']=='CMA' for r in museum),
        'MET_candidates_public_primary_image': sum(r['museum_code']=='MET' for r in museum),
        'museum_candidate_total': len(museum),
        'museum_candidate_by_basis': dict(Counter(r['pool_basis'] for r in museum)),
        'sample_rows_input': len(samples),
        'sample_unique_urls': len(sample2),
        'sample_duplicate_urls_removed': len(samples)-len(sample2),
        'sample_sources': dict(Counter(r.get('page_code','') for r in sample2)),
        'legacy_field_warning': '`working_220_id` is used only for compatibility with the SIFT matcher and carries no 220-boundary claim.'
    }
    (out/'verified_pool_summary.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(meta, ensure_ascii=False, indent=2))

if __name__=='__main__':
    main()
