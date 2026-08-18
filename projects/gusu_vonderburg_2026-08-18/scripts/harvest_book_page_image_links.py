#!/usr/bin/env python3
"""Harvest image URLs/alt text from public pages showing the Gusu catalogue.

No third-party image bytes are committed. The script stores only source-page
metadata and resolved image URLs so book-page samples can be inspected at their
original hosts and used as catalogue concordance anchors.
"""
from __future__ import annotations
import csv,html.parser,json,re,time
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request,urlopen

PAGES=[
  ("WENWU_RECOMMEND","https://www.wenwu.com/newsinfo/11120837.html"),
  ("GUANGZHOU_DAILY","https://huacheng.gz-cmc.com/pages/2026/06/17/eb9dd1f64b884f828e156a702afee4b9.html"),
  ("WENWU_LAUNCH","https://www.wenwu.com/newsinfo/11120643.html"),
]
UA="Mozilla/5.0 (Gusu catalogue research link audit; noncommercial)"

class Parser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__();self.images=[];self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag.lower() in ('img','source'):
            src=d.get('src') or d.get('data-src') or d.get('data-original') or d.get('data-url') or ''
            srcset=d.get('srcset') or d.get('data-srcset') or ''
            self.images.append({'tag':tag,'src':src,'srcset':srcset,'alt':d.get('alt',''),'title':d.get('title',''),'class':d.get('class','')})
        elif tag.lower()=='a' and d.get('href'):
            self.links.append({'href':d.get('href',''),'title':d.get('title','')})

def get(url,retries=4):
    last=None
    for i in range(retries):
        try:
            req=Request(url,headers={'User-Agent':UA,'Accept':'text/html,application/xhtml+xml,*/*;q=0.8'})
            with urlopen(req,timeout=45) as r:
                return getattr(r,'status',200),r.headers.get('Content-Type',''),r.read().decode('utf-8','replace')
        except Exception as e:
            last=e;time.sleep(1*(i+1))
    raise RuntimeError(f'{url}: {last}')

def likely_book_image(row):
    blob=' '.join([row.get('src',''),row.get('srcset',''),row.get('alt',''),row.get('title','')]).lower()
    needles=['姑苏','冯氏','实拍','gusu','book','17582977','17582978','8978','8802']
    return any(n.lower() in blob for n in needles)

def main():
    out=Path('projects/gusu_vonderburg_2026-08-18/latest/book_page_link_harvest');out.mkdir(parents=True,exist_ok=True)
    rows=[];page_meta=[]
    for code,url in PAGES:
        try:
            status,ctype,text=get(url);p=Parser();p.feed(text)
            for idx,img in enumerate(p.images,1):
                src=urljoin(url,img['src']) if img['src'] else ''
                srcset=img['srcset']
                # Resolve individual srcset URLs but preserve descriptors.
                resolved=[]
                if srcset:
                    for part in srcset.split(','):
                        part=part.strip()
                        if not part:continue
                        bits=part.split()
                        bits[0]=urljoin(url,bits[0])
                        resolved.append(' '.join(bits))
                row={'page_code':code,'page_url':url,'image_index':idx,'tag':img['tag'],'src':src,'srcset':' | '.join(resolved),'alt':img['alt'],'title':img['title'],'class':img['class']}
                row['likely_book_image']='1' if likely_book_image(row) else '0';rows.append(row)
            page_meta.append({'page_code':code,'page_url':url,'http_status':status,'content_type':ctype,'html_bytes':len(text.encode('utf-8')),'image_tag_count':len(p.images),'link_count':len(p.links),'error':''})
        except Exception as e:
            page_meta.append({'page_code':code,'page_url':url,'http_status':'','content_type':'','html_bytes':0,'image_tag_count':0,'link_count':0,'error':repr(e)})
    fields=['page_code','page_url','image_index','tag','src','srcset','alt','title','class','likely_book_image']
    with (out/'public_page_image_links.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
    likely=[r for r in rows if r['likely_book_image']=='1']
    with (out/'likely_book_sample_image_links.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(likely)
    mf=['page_code','page_url','http_status','content_type','html_bytes','image_tag_count','link_count','error']
    with (out/'page_fetch_audit.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=mf);w.writeheader();w.writerows(page_meta)
    summary={'generated_utc':datetime.now(timezone.utc).isoformat(),'pages':page_meta,'total_image_tags':len(rows),'likely_book_sample_links':len(likely),'policy':'URLs/alt metadata only; no third-party image bytes committed'}
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
