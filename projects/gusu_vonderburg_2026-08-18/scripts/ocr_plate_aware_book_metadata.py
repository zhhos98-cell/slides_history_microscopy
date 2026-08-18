#!/usr/bin/env python3
"""Plate-aware OCR for matched Gusu catalogue sample photographs.

For each sample with a known museum-image identity, recompute a robust SIFT
homography from the museum scan to the photographed page/spread. The projected
plate polygon lets us OCR only the *outside-of-plate* metadata zones rather
than mixing captions with numbers/text inside the artwork.

Calibration control: Wenwu 175829778 = book no. 52 / CMA 2025.84.
Promotion rule: any ROI strategy used to infer Bird-on-Pomegranate metadata
must first recover `52` from the analogous control ROI.

No source or museum image bytes are committed.
"""
from __future__ import annotations
import csv,json,re,subprocess,tempfile,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen

import cv2
import numpy as np

UA='Mozilla/5.0 (Gusu plate-aware catalogue OCR research)'
SAMPLES=[
  {'sample_id':'WENWU_776','sample_url':'https://img.wanwang.xin/contents/sitefiles2046/10230983/images/175829776.jpg','referer':'https://www.wenwu.com/newsinfo/11120837.html','working_220_id':'CMA:2025.108','museum_url':'https://openaccess-cdn.clevelandart.org/2025.108/2025.108_web.jpg','control':0},
  {'sample_id':'WENWU_778_CONTROL','sample_url':'https://img.wanwang.xin/contents/sitefiles2046/10230983/images/175829778.jpg','referer':'https://www.wenwu.com/newsinfo/11120837.html','working_220_id':'CMA:2025.84','museum_url':'https://openaccess-cdn.clevelandart.org/2025.84/2025.84_web.jpg','control':1},
  {'sample_id':'WENWU_780','sample_url':'https://img.wanwang.xin/contents/sitefiles2046/10230983/images/175829780.jpg','referer':'https://www.wenwu.com/newsinfo/11120837.html','working_220_id':'CMA:2025.108','museum_url':'https://openaccess-cdn.clevelandart.org/2025.108/2025.108_web.jpg','control':0},
  {'sample_id':'GUANGZHOU_IMG3','sample_url':'https://oss.gz-cmc.com/pgcr/root/huacheng/upload/news/image/2026/06/17/1781674412855066475.jpg?x-oss-process=style/content','referer':'https://huacheng.gz-cmc.com/pages/2026/06/17/eb9dd1f64b884f828e156a702afee4b9.html','working_220_id':'CMA:2025.108','museum_url':'https://openaccess-cdn.clevelandart.org/2025.108/2025.108_web.jpg','control':0},
]

def fetch(url,referer=''):
    headers={'User-Agent':UA,'Accept':'image/avif,image/webp,image/apng,image/*,*/*;q=0.8'}
    if referer:headers['Referer']=referer
    req=Request(url,headers=headers)
    with urlopen(req,timeout=50) as r:data=r.read()
    im=cv2.imdecode(np.frombuffer(data,np.uint8),cv2.IMREAD_COLOR)
    if im is None:raise RuntimeError('decode failed '+url)
    return im

def resized(im,maxdim=1800):
    h,w=im.shape[:2];m=max(h,w)
    if m<=maxdim:return im,1.0
    s=maxdim/m
    return cv2.resize(im,(round(w*s),round(h*s)),interpolation=cv2.INTER_AREA),s

def homography(museum,sample):
    m,ms=resized(museum);s,ss=resized(sample)
    sift=cv2.SIFT_create(nfeatures=8000,contrastThreshold=.02,edgeThreshold=10)
    def feat(im):
        g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        g=cv2.createCLAHE(1.5,(8,8)).apply(g)
        return sift.detectAndCompute(g,None)
    mkp,md=feat(m);skp,sd=feat(s)
    bf=cv2.BFMatcher(cv2.NORM_L2)
    good=[]
    for pair in bf.knnMatch(md,sd,k=2):
        if len(pair)==2 and pair[0].distance < .72*pair[1].distance:good.append(pair[0])
    if len(good)<8:raise RuntimeError(f'only {len(good)} good matches')
    src=np.float32([mkp[x.queryIdx].pt for x in good]).reshape(-1,1,2)
    dst=np.float32([skp[x.trainIdx].pt for x in good]).reshape(-1,1,2)
    H,mask=cv2.findHomography(src,dst,cv2.RANSAC,5.0)
    if H is None or mask is None:raise RuntimeError('homography failed')
    # H maps resized museum -> resized sample. Project resized museum corners.
    mh,mw=m.shape[:2]
    corners=np.float32([[[0,0]],[[mw,0]],[[mw,mh]],[[0,mh]]])
    poly=cv2.perspectiveTransform(corners,H).reshape(-1,2)
    # Convert to original sample coords.
    poly=poly/ss
    return H,poly,len(good),int(mask.ravel().sum()),int(sample.shape[1]),int(sample.shape[0])

def clipbox(x0,y0,x1,y1,w,h,minsize=30):
    x0=max(0,min(w,int(round(x0))));x1=max(0,min(w,int(round(x1))))
    y0=max(0,min(h,int(round(y0))));y1=max(0,min(h,int(round(y1))))
    if x1-x0<minsize or y1-y0<minsize:return None
    return x0,y0,x1,y1

def make_rois(im,poly):
    h,w=im.shape[:2]
    xs=poly[:,0];ys=poly[:,1]
    x0,x1=float(xs.min()),float(xs.max());y0,y1=float(ys.min()),float(ys.max())
    pad=max(8,round(min(w,h)*.015))
    # Broad metadata candidates around the detected artwork plus page-edge bands.
    boxes={
      'above_plate':clipbox(0,0,w,y0-pad,w,h),
      'below_plate':clipbox(0,y1+pad,w,h,w,h),
      'left_of_plate':clipbox(0,0,x0-pad,h,w,h),
      'right_of_plate':clipbox(x1+pad,0,w,h,w,h),
      'plate_left_context':clipbox(max(0,x0-.55*w),max(0,y0-.20*h),x0-pad,min(h,y1+.20*h),w,h),
      'plate_right_context':clipbox(x1+pad,max(0,y0-.20*h),min(w,x1+.55*w),min(h,y1+.20*h),w,h),
      'page_top_25':clipbox(0,0,w,.25*h,w,h),
      'page_top_40':clipbox(0,0,w,.40*h,w,h),
      'left_half':clipbox(0,0,.52*w,h,w,h),
      'right_half':clipbox(.48*w,0,w,h,w,h),
    }
    return {k:v for k,v in boxes.items() if v}

def ocr(im,psm):
    g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    scale=min(4.0,max(1.5,2400/max(g.shape)))
    g=cv2.resize(g,None,fx=scale,fy=scale,interpolation=cv2.INTER_CUBIC)
    g=cv2.createCLAHE(2.0,(8,8)).apply(g)
    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        cv2.imwrite(f.name,g)
        p=subprocess.run(['tesseract',f.name,'stdout','-l','eng','--psm',str(psm),'quiet'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,timeout=90)
    return ' '.join(p.stdout.split())

def candnums(text):
    vals=[]
    for x in re.findall(r'(?<!\d)(\d{1,3})(?!\d)',text):
        n=int(x)
        if 1<=n<=751:vals.append(n)
    return vals

def main():
    out=Path('projects/gusu_vonderburg_2026-08-18/latest/plate_aware_ocr');out.mkdir(parents=True,exist_ok=True)
    geom=[];rows=[]
    for spec in SAMPLES:
        sample=fetch(spec['sample_url'],spec['referer']);museum=fetch(spec['museum_url'])
        H,poly,good,inliers,w,h=homography(museum,sample)
        xs=poly[:,0];ys=poly[:,1]
        geom.append({
          'sample_id':spec['sample_id'],'working_220_id':spec['working_220_id'],'sample_width':w,'sample_height':h,
          'poly_xy':'|'.join(f'{x:.1f},{y:.1f}' for x,y in poly),'bbox_x0':round(float(xs.min()),1),'bbox_y0':round(float(ys.min()),1),'bbox_x1':round(float(xs.max()),1),'bbox_y1':round(float(ys.max()),1),
          'sift_good_matches':good,'homography_inliers':inliers,'control':spec['control']
        })
        for name,box in make_rois(sample,poly).items():
            x0,y0,x1,y1=box;roi=sample[y0:y1,x0:x1]
            for psm in (6,11,12):
                try:text=ocr(roi,psm)
                except Exception as e:text='ERROR '+repr(e)
                rows.append({
                  'sample_id':spec['sample_id'],'working_220_id':spec['working_220_id'],'control':spec['control'],'region':name,
                  'x0':x0,'y0':y0,'x1':x1,'y1':y1,'psm':psm,'ocr_text':text,'candidate_numbers':'|'.join(map(str,candnums(text))),
                  'detects_52':'1' if re.search(r'(?<!\d)52(?!\d)',text) else '0','detects_gathering':'1' if ('gathering' in text.lower() or 'osmanthus' in text.lower()) else '0'
                })
        time.sleep(.1)
    gf=list(geom[0].keys())
    with (out/'plate_geometry.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=gf);w.writeheader();w.writerows(geom)
    rf=list(rows[0].keys())
    with (out/'plate_aware_ocr_regions.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=rf);w.writeheader();w.writerows(rows)
    # Identify region+PSM strategies that recover 52 in the control, then report Bird numbers only under those calibrated strategies.
    valid={(r['region'],r['psm']) for r in rows if r['sample_id']=='WENWU_778_CONTROL' and r['detects_52']=='1'}
    calibrated=[]
    for r in rows:
        if r['sample_id']!='WENWU_778_CONTROL' and (r['region'],r['psm']) in valid:
            x=dict(r);x['calibration_basis']='same region+psm recovered known book no.52 in control';calibrated.append(x)
    with (out/'bird_calibrated_roi_results.csv').open('w',newline='',encoding='utf-8') as f:
        cf=rf+['calibration_basis'];w=csv.DictWriter(f,fieldnames=cf);w.writeheader();w.writerows(calibrated)
    bysample={}
    for sid in ['WENWU_776','WENWU_780','GUANGZHOU_IMG3']:
        rr=[r for r in calibrated if r['sample_id']==sid]
        nums=[]
        for r in rr:nums.extend(candnums(r['ocr_text']))
        counts={n:nums.count(n) for n in sorted(set(nums))}
        bysample[sid]={'calibrated_roi_rows':len(rr),'candidate_number_counts':counts,'numbers_repeated_across_calibrated_rois':[n for n,c in counts.items() if c>=2]}
    cross={}
    for sid,v in bysample.items():
        for n in v['numbers_repeated_across_calibrated_rois']:cross.setdefault(n,[]).append(sid)
    meta={
      'generated_utc':datetime.now(timezone.utc).isoformat(),'control_valid_region_psm':[{'region':a,'psm':b} for a,b in sorted(valid)],
      'bird_samples':bysample,'numbers_repeated_in_at_least_two_bird_samples':{str(n):sids for n,sids in cross.items() if len(sids)>=2},
      'promotion_rule':'A number remains OCR evidence only. Strong candidate requires control-calibrated ROI recurrence plus geometric plausibility/page-header inspection; never infer from accession number.'
    }
    (out/'summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
