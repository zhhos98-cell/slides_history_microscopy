#!/usr/bin/env python3
"""Match public catalogue sample photos to official museum images using SIFT.

Unlike whole-image perceptual hashes, SIFT can identify a museum plate embedded
inside a photographed book spread and is relatively robust to perspective,
cropping, scale and colour changes. Source/sample image bytes are downloaded
transiently and are NOT committed; only URLs, feature statistics and ranked
candidate matches are written.
"""
from __future__ import annotations
import argparse,csv,io,json,math,time
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path
from urllib.request import Request,urlopen

import cv2
import numpy as np

UA='Mozilla/5.0 (Gusu catalogue visual concordance research)'

def fetch(url,referer='',retries=4,timeout=50):
    last=None
    for i in range(retries):
        try:
            headers={'User-Agent':UA,'Accept':'image/avif,image/webp,image/apng,image/*,*/*;q=0.8'}
            if referer:headers['Referer']=referer
            req=Request(url,headers=headers)
            with urlopen(req,timeout=timeout) as r:data=r.read()
            arr=np.frombuffer(data,dtype=np.uint8)
            im=cv2.imdecode(arr,cv2.IMREAD_COLOR)
            if im is None:raise ValueError('cv2 could not decode image')
            return im,len(data)
        except Exception as e:
            last=e;time.sleep(1*(i+1))
    raise RuntimeError(f'{url}: {last}')

def resize(im,maxdim=1800):
    h,w=im.shape[:2];m=max(h,w)
    if m<=maxdim:return im
    s=maxdim/m
    return cv2.resize(im,(max(1,round(w*s)),max(1,round(h*s))),interpolation=cv2.INTER_AREA)

def features(im,sift):
    gray=cv2.cvtColor(resize(im),cv2.COLOR_BGR2GRAY)
    # Mild CLAHE helps photographed pages without radically altering geometry.
    gray=cv2.createCLAHE(clipLimit=1.5,tileGridSize=(8,8)).apply(gray)
    kp,des=sift.detectAndCompute(gray,None)
    return kp,des,gray.shape

def geometric_score(kp1,des1,kp2,des2,bf):
    if des1 is None or des2 is None or len(des1)<6 or len(des2)<6:return (0,0,0,0.0,'')
    pairs=bf.knnMatch(des1,des2,k=2)
    good=[]
    for pair in pairs:
        if len(pair)<2:continue
        m,n=pair
        if m.distance < 0.72*n.distance:good.append(m)
    if len(good)<6:return (len(good),0,0,0.0,'')
    pts1=np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    pts2=np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    try:
        H,mask=cv2.findHomography(pts2,pts1,cv2.RANSAC,5.0) # candidate -> sample
        if mask is None:return (len(good),0,0,0.0,'')
        inliers=int(mask.ravel().sum())
        ratio=inliers/max(1,len(good))
        # emphasize real geometric support; raw good matches break ties
        score=inliers*10 + len(good)*0.7 + ratio*20
        hflat=' '.join(f'{x:.6g}' for x in H.ravel()) if H is not None else ''
        return (len(good),inliers,ratio,score,hflat)
    except cv2.error:
        return (len(good),0,0,0.0,'')

def main():
    ap=argparse.ArgumentParser();ap.add_argument('samples_csv');ap.add_argument('museum_manifest');ap.add_argument('--outdir',required=True);args=ap.parse_args()
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    with open(args.samples_csv,newline='',encoding='utf-8-sig') as f:samples=[r for r in csv.DictReader(f) if r.get('src')]
    with open(args.museum_manifest,newline='',encoding='utf-8-sig') as f:museum=list(csv.DictReader(f))
    sift=cv2.SIFT_create(nfeatures=7000,contrastThreshold=0.025,edgeThreshold=10)
    bf=cv2.BFMatcher(cv2.NORM_L2)

    candidates=[];download_errors=[]
    # Download/feature museum images once.
    for i,r in enumerate(museum,1):
        url=(r.get('web_image_url') or r.get('original_image_url') or '').strip()
        if not url:continue
        try:
            im,n=fetch(url);kp,des,shape=features(im,sift)
            candidates.append((r,kp,des,shape,n))
        except Exception as e:download_errors.append({'kind':'museum','id':r.get('working_220_id',''),'url':url,'error':repr(e)})
        if i%25==0:print(f'museum prepared {i}/{len(museum)}')

    allrows=[];sample_summary=[]
    for si,s in enumerate(samples,1):
        try:
            im,n=fetch(s['src'],s.get('page_url',''));skp,sdes,sshape=features(im,sift)
        except Exception as e:
            download_errors.append({'kind':'sample','id':f"{s.get('page_code')}:{s.get('image_index')}",'url':s.get('src',''),'error':repr(e)});continue
        scores=[]
        for r,kp,des,shape,bytes_ in candidates:
            good,inliers,ratio,score,H=geometric_score(skp,sdes,kp,des,bf)
            scores.append({
              'sample_id':f"{s.get('page_code')}:{s.get('image_index')}",'sample_page_code':s.get('page_code',''),'sample_image_index':s.get('image_index',''),
              'sample_alt':s.get('alt',''),'sample_url':s.get('src',''),'sample_keypoints':len(skp),'museum_working_220_id':r.get('working_220_id',''),
              'museum_code':r.get('museum_code',''),'accession':r.get('accession',''),'title_en':r.get('title_en',''),'title_zh':r.get('title_zh',''),
              'object_url':r.get('object_url',''),'good_matches':good,'homography_inliers':inliers,'inlier_ratio':round(ratio,4),'geometric_score':round(score,4),'homography_candidate_to_sample':H
            })
        scores.sort(key=lambda x:(-float(x['geometric_score']),-int(x['homography_inliers']),-int(x['good_matches'])))
        for rank,x in enumerate(scores,1):x['rank']=rank
        allrows.extend(scores[:20])
        top=scores[:10]
        strong=[x for x in scores if int(x['homography_inliers'])>=10 and float(x['inlier_ratio'])>=0.35]
        sample_summary.append({
          'sample_id':f"{s.get('page_code')}:{s.get('image_index')}",'sample_alt':s.get('alt',''),'sample_url':s.get('src',''),'sample_bytes':n,'sample_keypoints':len(skp),
          'strong_geometric_candidates':len(strong),'top_candidate':top[0]['museum_working_220_id'] if top else '',
          'top_candidate_title':top[0]['title_en'] if top else '','top_inliers':top[0]['homography_inliers'] if top else 0,'top_inlier_ratio':top[0]['inlier_ratio'] if top else 0,'top_score':top[0]['geometric_score'] if top else 0
        })
        print(f"sample {si}/{len(samples)} {sample_summary[-1]['sample_id']} -> {sample_summary[-1]['top_candidate']} inliers={sample_summary[-1]['top_inliers']}")

    fields=['sample_id','sample_page_code','sample_image_index','sample_alt','sample_url','sample_keypoints','museum_working_220_id','museum_code','accession','title_en','title_zh','object_url','good_matches','homography_inliers','inlier_ratio','geometric_score','homography_candidate_to_sample','rank']
    with (out/'public_book_samples_sift_top20.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(allrows)
    sf=['sample_id','sample_alt','sample_url','sample_bytes','sample_keypoints','strong_geometric_candidates','top_candidate','top_candidate_title','top_inliers','top_inlier_ratio','top_score']
    with (out/'public_book_samples_sift_summary.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=sf);w.writeheader();w.writerows(sample_summary)
    ef=['kind','id','url','error']
    with (out/'public_book_samples_sift_errors.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=ef);w.writeheader();w.writerows(download_errors)
    meta={'generated_utc':datetime.now(timezone.utc).isoformat(),'sample_count_input':len(samples),'sample_count_matched':len(sample_summary),'museum_candidates_input':len(museum),'museum_images_prepared':len(candidates),'download_errors':len(download_errors),'strong_rule':'homography_inliers >= 10 and inlier_ratio >= 0.35','interpretation':'SIFT is candidate generation. Promote a book concordance only after title/layout/visual inspection confirms the match. Source image bytes are not committed.'}
    (out/'summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
