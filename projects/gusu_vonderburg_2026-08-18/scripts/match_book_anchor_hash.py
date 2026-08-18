#!/usr/bin/env python3
"""Match a catalogue-page plate against official museum web images.

The user-supplied screenshot is NOT uploaded. Only three perceptual hashes of
its tightly cropped plate are stored here. Candidate images are the official
web renditions already present in the combined 220 manifest.

Target = catalogue entry 52 plate from the supplied book-layout screenshot.
"""
from __future__ import annotations
import argparse,csv,io,json,time
from pathlib import Path
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError

from PIL import Image
import imagehash

TARGET_PHASH=imagehash.hex_to_hash('aaa5d464cd5a715a')
TARGET_DHASH=imagehash.hex_to_hash('0f7d5d63634d7969')
TARGET_AHASH=imagehash.hex_to_hash('ff3f010101019dff')
UA='GusuBookAnchorMatcher/1.0 research-use'

def fetch_image(url,retries=3,timeout=45):
    last=None
    for i in range(retries):
        try:
            req=Request(url,headers={'User-Agent':UA,'Accept':'image/*,*/*;q=0.8'})
            with urlopen(req,timeout=timeout) as r:
                data=r.read()
            return Image.open(io.BytesIO(data)).convert('RGB')
        except Exception as e:
            last=e;time.sleep(.5*(i+1))
    raise RuntimeError(f'{url}: {last}')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('manifest');ap.add_argument('--outdir',required=True);args=ap.parse_args()
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    with open(args.manifest,newline='',encoding='utf-8-sig') as f:rows=list(csv.DictReader(f))
    results=[];errors=[]
    for i,r in enumerate(rows,1):
        url=(r.get('web_image_url') or r.get('original_image_url') or '').strip()
        if not url:
            errors.append({'working_220_id':r.get('working_220_id',''),'error':'no_candidate_image_url'});continue
        try:
            im=fetch_image(url)
            ph=imagehash.phash(im);dh=imagehash.dhash(im);ah=imagehash.average_hash(im)
            pd=TARGET_PHASH-ph;dd=TARGET_DHASH-dh;ad=TARGET_AHASH-ah
            # pHash gets greatest weight; dHash/aHash break near ties.
            score=pd*3+dd+ad
            results.append({
              'rank':'','working_220_id':r.get('working_220_id',''),'museum_code':r.get('museum_code',''),'accession':r.get('accession',''),
              'title_en':r.get('title_en',''),'title_zh':r.get('title_zh',''),'object_url':r.get('object_url',''),'candidate_image_url':url,
              'candidate_phash':str(ph),'candidate_dhash':str(dh),'candidate_ahash':str(ah),
              'phash_distance':pd,'dhash_distance':dd,'ahash_distance':ad,'weighted_score':score
            })
        except Exception as e:
            errors.append({'working_220_id':r.get('working_220_id',''),'error':repr(e)})
        if i%25==0:print(f'checked {i}/{len(rows)}')
        time.sleep(.02)
    results.sort(key=lambda r:(int(r['weighted_score']),int(r['phash_distance']),int(r['dhash_distance'])))
    for i,r in enumerate(results,1):r['rank']=i
    fields=list(results[0].keys()) if results else []
    with (out/'book_entry_52_hash_match_all.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(results)
    with (out/'book_entry_52_hash_match_top20.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(results[:20])
    with (out/'book_entry_52_hash_match_errors.csv').open('w',newline='',encoding='utf-8') as f:
        ef=['working_220_id','error'];w=csv.DictWriter(f,fieldnames=ef);w.writeheader();w.writerows(errors)
    meta={
      'target':'book_catalogue_entry_52_plate_from_user_screenshot','target_image_uploaded':False,
      'target_hashes':{'phash':str(TARGET_PHASH),'dhash':str(TARGET_DHASH),'ahash':str(TARGET_AHASH)},
      'candidate_count':len(rows),'successfully_hashed':len(results),'errors':len(errors),
      'top10':[{k:r[k] for k in ['rank','working_220_id','title_en','title_zh','phash_distance','dhash_distance','ahash_distance','weighted_score']} for r in results[:10]],
      'interpretation_rule':'Hash ranking is a visual candidate generator, not final identification. Confirm top candidates by visual inspection before writing book_catalogue_no=52.'
    }
    (out/'book_entry_52_hash_match_summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
