#!/usr/bin/env python3
"""Match a catalogue-page plate against official museum web images.

The user-supplied screenshot is NOT uploaded. Only dHash/aHash fingerprints of
its tightly cropped plate are stored. Candidate images are official museum web
renditions already listed in the combined working-220 manifest.

Target = catalogue entry 52 plate from the supplied book-layout screenshot.
This lightweight version requires Pillow only; no scipy/ImageHash dependency.
"""
from __future__ import annotations
import argparse,csv,io,json,time
from pathlib import Path
from urllib.request import Request,urlopen
from PIL import Image

TARGET_DHASH=int('0f7d5d63634d7969',16)
TARGET_AHASH=int('ff3f010101019dff',16)
UA='GusuBookAnchorMatcher/1.1 research-use'

def hamming(a,b): return (a^b).bit_count()

def ahash(im):
    g=im.convert('L').resize((8,8),Image.Resampling.LANCZOS)
    vals=list(g.getdata()); mean=sum(vals)/64
    bits=0
    for v in vals: bits=(bits<<1)|(1 if v>mean else 0)
    return bits

def dhash(im):
    g=im.convert('L').resize((9,8),Image.Resampling.LANCZOS)
    vals=list(g.getdata()); bits=0
    for y in range(8):
        row=vals[y*9:(y+1)*9]
        for x in range(8): bits=(bits<<1)|(1 if row[x]>row[x+1] else 0)
    return bits

def fetch_image(url,retries=3,timeout=45):
    last=None
    for i in range(retries):
        try:
            req=Request(url,headers={'User-Agent':UA,'Accept':'image/*,*/*;q=0.8'})
            with urlopen(req,timeout=timeout) as r:data=r.read()
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
            im=fetch_image(url);dh=dhash(im);ah=ahash(im)
            dd=hamming(TARGET_DHASH,dh);ad=hamming(TARGET_AHASH,ah);score=dd*2+ad
            results.append({
              'rank':'','working_220_id':r.get('working_220_id',''),'museum_code':r.get('museum_code',''),'accession':r.get('accession',''),
              'title_en':r.get('title_en',''),'title_zh':r.get('title_zh',''),'object_url':r.get('object_url',''),'candidate_image_url':url,
              'candidate_dhash':f'{dh:016x}','candidate_ahash':f'{ah:016x}','dhash_distance':dd,'ahash_distance':ad,'weighted_score':score
            })
        except Exception as e:errors.append({'working_220_id':r.get('working_220_id',''),'error':repr(e)})
        if i%25==0:print(f'checked {i}/{len(rows)}')
        time.sleep(.02)
    results.sort(key=lambda r:(int(r['weighted_score']),int(r['dhash_distance']),int(r['ahash_distance'])))
    for i,r in enumerate(results,1):r['rank']=i
    fields=list(results[0].keys()) if results else []
    for name,data in [('book_entry_52_hash_match_all.csv',results),('book_entry_52_hash_match_top20.csv',results[:20])]:
        with (out/name).open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(data)
    with (out/'book_entry_52_hash_match_errors.csv').open('w',newline='',encoding='utf-8') as f:
        ef=['working_220_id','error'];w=csv.DictWriter(f,fieldnames=ef);w.writeheader();w.writerows(errors)
    meta={
      'target':'book_catalogue_entry_52_plate_from_user_screenshot','target_image_uploaded':False,
      'target_hashes':{'dhash':f'{TARGET_DHASH:016x}','ahash':f'{TARGET_AHASH:016x}'},
      'candidate_count':len(rows),'successfully_hashed':len(results),'errors':len(errors),
      'top10':[{k:r[k] for k in ['rank','working_220_id','title_en','title_zh','dhash_distance','ahash_distance','weighted_score']} for r in results[:10]],
      'known_independent_identification':'Book no. 52 has already been independently identified as CMA 2025.84 / 折桂圖 from readable title plus official composition description. Hash rank is now a validation/benchmark, not the primary identification basis.',
      'interpretation_rule':'Hash ranking is a candidate generator only; title/composition evidence governs final concordance.'
    }
    (out/'book_entry_52_hash_match_summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
