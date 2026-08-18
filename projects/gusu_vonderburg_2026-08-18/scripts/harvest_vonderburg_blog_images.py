#!/usr/bin/env python3
"""Index public images on Christer von der Burg's Chinese Woodblock Printing blog
and match captions/context to the working Gusu 220 museum-unit manifest.

Blog images are NOT treated as Open Access museum assets. Output policy is
link-only unless an independent rights statement permits reuse. The purpose is
to measure *online visual availability* beyond museum download coverage and to
provide visual/title anchors for catalogue concordance.
"""
from __future__ import annotations
import argparse,csv,html.parser,json,re,time,unicodedata
from collections import defaultdict
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen

API='https://chiwoopri.wordpress.com/wp-json/wp/v2/posts'
UA='GusuVonDerBurgBlogImageIndex/1.0 research-use'

class PostParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__();self.images=[];self.text=[];self._fig=False;self._figbuf=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag.lower()=='figure':self._fig=True;self._figbuf=[]
        if tag.lower()=='img':
            self.images.append({'src':d.get('src',''),'alt':d.get('alt',''),'title':d.get('title',''),'figcaption':''})
    def handle_endtag(self,tag):
        if tag.lower()=='figure' and self._fig:
            cap=' '.join(self._figbuf).strip()
            if self.images and cap:self.images[-1]['figcaption']=cap
            self._fig=False;self._figbuf=[]
    def handle_data(self,data):
        s=' '.join(data.split())
        if s:
            self.text.append(s)
            if self._fig:self._figbuf.append(s)

def get_json(url,retries=4):
    last=None
    for i in range(retries):
        try:
            req=Request(url,headers={'User-Agent':UA,'Accept':'application/json'})
            with urlopen(req,timeout=50) as r:
                return json.load(r),dict(r.headers)
        except Exception as e:
            last=e;time.sleep(1*(i+1))
    raise RuntimeError(f'{url}: {last}')

def strip_html(s):
    p=PostParser();p.feed(s or '');return ' '.join(p.text)

def norm(s):
    s=unicodedata.normalize('NFKC',s or '').lower()
    return ''.join(ch for ch in s if ch.isalnum() or '\u3400'<=ch<='\u9fff')

def eng_tokens(s):
    s=unicodedata.normalize('NFKC',s or '').lower()
    stop={'the','a','an','of','and','in','on','with','from','to','part','print','picture','view','scenic'}
    return {x for x in re.findall(r'[a-z]+',s) if len(x)>2 and x not in stop}

def fetch_all_posts():
    posts=[];page=1
    while True:
        url=API+'?'+urlencode({'per_page':100,'page':page,'orderby':'date','order':'desc'})
        try:data,headers=get_json(url)
        except Exception as e:
            if '400' in repr(e) and page>1:break
            raise
        if not data:break
        posts.extend(data)
        total_pages=int(headers.get('X-WP-TotalPages') or headers.get('x-wp-totalpages') or page)
        if page>=total_pages:break
        page+=1;time.sleep(.2)
    return posts

def main():
    ap=argparse.ArgumentParser();ap.add_argument('manifest');ap.add_argument('--outdir',required=True);args=ap.parse_args()
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    with open(args.manifest,newline='',encoding='utf-8-sig') as f:museum=list(csv.DictReader(f))
    posts=fetch_all_posts()
    image_rows=[];post_rows=[]
    for post in posts:
        title=strip_html((post.get('title') or {}).get('rendered',''))
        content=(post.get('content') or {}).get('rendered','')
        p=PostParser();p.feed(content)
        text=' '.join(p.text)
        post_url=post.get('link','');date=post.get('date','')
        post_rows.append({'post_id':post.get('id',''),'date':date,'post_title':title,'post_url':post_url,'image_count':len(p.images),'text_excerpt':text[:1500]})
        for i,img in enumerate(p.images,1):
            image_rows.append({
              'blog_image_id':f"WP:{post.get('id')}:{i}",'post_id':post.get('id',''),'date':date,'post_title':title,'post_url':post_url,
              'image_index':i,'image_url':img.get('src',''),'alt':img.get('alt',''),'title_attr':img.get('title',''),'figcaption':img.get('figcaption',''),
              'image_text':' | '.join(x for x in [img.get('alt',''),img.get('title',''),img.get('figcaption','')] if x),
              'post_text_excerpt':text[:1500],
            })
    image_fields=list(image_rows[0].keys()) if image_rows else []
    with (out/'vonderburg_blog_image_index.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=image_fields);w.writeheader();w.writerows(image_rows)
    post_fields=list(post_rows[0].keys()) if post_rows else []
    with (out/'vonderburg_blog_post_index.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=post_fields);w.writeheader();w.writerows(post_rows)

    exact=[];candidates=[]
    for m in museum:
        zh=(m.get('title_zh') or '').strip();en=(m.get('title_en') or '').strip()
        nzh=norm(zh);nen=norm(en);et=eng_tokens(en)
        for im in image_rows:
            itext=' '.join([im['image_text'],im['post_title']]);nit=norm(itext);tokens=eng_tokens(itext)
            basis=[];confidence=''
            if nzh and len(nzh)>=2 and nzh in nit:
                basis.append('exact_normalized_Chinese_title_in_image_caption_or_post_title');confidence='high'
            if nen and len(nen)>=6 and nen in nit:
                basis.append('exact_normalized_English_title_in_image_caption_or_post_title');confidence='high'
            overlap=len(et & tokens);den=max(1,len(et))
            if not basis and len(et)>=2 and overlap>=max(2,math.ceil(len(et)*0.7)):
                basis.append(f'English_token_overlap_{overlap}_of_{len(et)}');confidence='medium'
            if basis:
                row={
                  'working_220_id':m.get('working_220_id',''),'museum_code':m.get('museum_code',''),'accession':m.get('accession',''),
                  'museum_title_en':en,'museum_title_zh':zh,'museum_has_OA_original':m.get('downloadable_original',''),
                  'blog_image_id':im['blog_image_id'],'blog_post_title':im['post_title'],'blog_post_url':im['post_url'],'blog_image_url':im['image_url'],
                  'blog_image_text':im['image_text'],'match_basis':'|'.join(basis),'match_confidence':confidence,
                  'rights_status':'author_blog_publicly_viewable_not_assumed_Open_Access','download_policy':'link_only_unless_rights_confirmed'
                }
                (exact if confidence=='high' else candidates).append(row)
    match_fields=list(exact[0].keys()) if exact else (list(candidates[0].keys()) if candidates else ['working_220_id'])
    with (out/'vonderburg_blog_high_confidence_visual_matches.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=match_fields);w.writeheader();w.writerows(exact)
    with (out/'vonderburg_blog_candidate_visual_matches.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=match_fields);w.writeheader();w.writerows(candidates)
    matched_units={r['working_220_id'] for r in exact}
    new_visual={r['working_220_id'] for r in exact if r['museum_has_OA_original']!='1'}
    meta={
      'generated_utc':datetime.now(timezone.utc).isoformat(),'posts_indexed':len(posts),'images_indexed':len(image_rows),
      'high_confidence_match_rows':len(exact),'high_confidence_unique_museum_units':len(matched_units),
      'medium_candidate_rows':len(candidates),'new_online_visual_units_without_museum_OA_original':len(new_visual),
      'new_online_visual_unit_ids':sorted(new_visual),
      'rights_policy':'Blog images are link-only research references; public visibility is not treated as Open Access or permission to redistribute.',
      'coverage_interpretation':'Add new_online_visual_units_without_museum_OA_original only to online-viewable coverage, never to museum-OA-download coverage.'
    }
    (out/'summary.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(meta,ensure_ascii=False,indent=2))

if __name__=='__main__':
    import math
    main()
