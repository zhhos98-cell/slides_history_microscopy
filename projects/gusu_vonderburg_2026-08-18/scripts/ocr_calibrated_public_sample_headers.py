#!/usr/bin/env python3
"""Small, calibrated OCR audit for four public catalogue sample photographs.

This is deliberately narrow: use the already-identified publisher sample
175829778 (known book entry 52 / Gathering Osmanthus) as a calibration control,
then inspect only 175829776, 175829780 and Guangzhou Daily's image 3, all of
which SIFT independently matches to CMA 2025.108 Bird on Pomegranate.

OCR is restricted to page/header regions and Latin/digit recognition. Results
are evidence candidates only; the known control must succeed before any number
from the Bird-on-Pomegranate samples is promoted.
"""
from __future__ import annotations
import csv,json,re,subprocess,tempfile,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen
import cv2,numpy as np

SAMPLES=[
 ('WENWU_776','https://img.wanwang.xin/contents/sitefiles2046/10230983/images/175829776.jpg','https://www.wenwu.com/newsinfo/11120837.html','CMA:2025.108'),
 ('WENWU_778_CONTROL','https://img.wanwang.xin/contents/sitefiles2046/10230983/images/175829778.jpg','https://www.wenwu.com/newsinfo/11120837.html','CMA:2025.84'),
 ('WENWU_780','https://img.wanwang.xin/contents/sitefiles2046/10230983/images/175829780.jpg','https://www.wenwu.com/newsinfo/11120837.html','CMA:2025.108'),
 ('GUANGZHOU_IMG3','https://oss.gz-cmc.com/pgcr/root/huacheng/upload/news/image/2026/06/17/1781674412855066475.jpg?x-oss-process=style/content','https://huacheng.gz-cmc.com/pages/2026/06/17/eb9dd1f64b884f828e156a702afee4b9.html','CMA:2025.108'),
]
UA='Mozilla/5.0 (Gusu catalogue header OCR calibration research)'

def fetch(url,referer):
    req=Request(url,headers={'User-Agent':UA,'Referer':referer,'Accept':'image/*,*/*;q=0.8'})
    with urlopen(req,timeout=50) as r:data=r.read()
    im=cv2.imdecode(np.frombuffer(data,np.uint8),cv2.IMREAD_COLOR)
    if im is None:raise RuntimeError('decode failed')
    return im,len(data)

def prep(im):
    h,w=im.shape[:2]
    # Several broad header/text regions; photographed spreads vary in crop.
    rois={
      'full':im,
      'top_45':im[:max(1,int(h*.45)),:],
      'top_left':im[:max(1,int(h*.55)),:max(1,int(w*.55))],
      'top_right':im[:max(1,int(h*.55)),int(w*.45):],
      'left_70':im[:,:max(1,int(w*.70))],
      'right_70':im[:,int(w*.30):],
    }
    return rois

def tesseract_text(im,psm):
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    scale=min(4.0,max(1.5,2200/max(gray.shape)))
    gray=cv2.resize(gray,None,fx=scale,fy=scale,interpolation=cv2.INTER_CUBIC)
    gray=cv2.createCLAHE(2.0,(8,8)).apply(gray)
    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        cv2.imwrite(f.name,gray)
        p=subprocess.run(['tesseract',f.name,'stdout','-l','eng','--psm',str(psm),'quiet'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=90)
    return ' '.join(p.stdout.split())

def nums(text):
    vals=[]
    for x in re.findall(r'(?<!\d)(\d{1,3})(?!\d)',text):
        n=int(x)
        if 1<=n<=751:vals.append(n)
    return vals

def main():
    out=Path('projects/gusu_vonderburg_2026-08-18/latest/public_sample_header_ocr');out.mkdir(parents=True,exist_ok=True)
    rows=[];summary=[]
    for sid,url,referer,known in SAMPLES:
        im,nbytes=fetch(url,referer);h,w=im.shape[:2]
        alltext=[]
        for region,roi in prep(im).items():
            for psm in (6,11,12):
                try:text=tesseract_text(roi,psm)
                except Exception as e:text=f'ERROR {e!r}'
                ns=nums(text);alltext.append(text)
                rows.append({'sample_id':sid,'known_visual_match':known,'region':region,'psm':psm,'image_width':w,'image_height':h,'ocr_text':text,'candidate_numbers':'|'.join(map(str,ns))})
        joined=' '.join(alltext).lower()
        summary.append({
          'sample_id':sid,'known_visual_match':known,'bytes':nbytes,'width':w,'height':h,
          'control_detects_52':'1' if sid=='WENWU_778_CONTROL' and re.search(r'(?<!\d)52(?!\d)',joined) else ('NA' if sid!='WENWU_778_CONTROL' else '0'),
          'control_detects_gathering_or_osmanthus':'1' if sid=='WENWU_778_CONTROL' and ('gathering' in joined or 'osmanthus' in joined) else ('NA' if sid!='WENWU_778_CONTROL' else '0'),
          'all_candidate_numbers':'|'.join(map(str,sorted(set(nums(joined))))),
          'bird_title_detected':'1' if sid!='WENWU_778_CONTROL' and ('bird' in joined or 'pomegranate' in joined) else ('NA' if sid=='WENWU_778_CONTROL' else '0')
        })
        time.sleep(.1)
    fields=['sample_id','known_visual_match','region','psm','image_width','image_height','ocr_text','candidate_numbers']
    with (out/'ocr_region_results.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    sf=list(summary[0].keys())
    with (out/'ocr_sample_summary.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=sf);w.writeheader();w.writerows(summary)
    control=next(x for x in summary if x['sample_id']=='WENWU_778_CONTROL')
    meta={'generated_utc':datetime.now(timezone.utc).isoformat(),'samples':summary,'calibration_pass_number_52':control['control_detects_52']=='1','calibration_pass_english_title':control['control_detects_gathering_or_osmanthus']=='1','promotion_rule':'Do not promote OCR-derived Bird-on-Pomegranate catalogue/page numbers unless the control detects known entry 52. OCR text remains candidate evidence only.'}
    (out/'summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
