#!/usr/bin/env python3
"""
Fetch book/sample image assets conservatively and resumably.

Designed for slow or throttle-prone sources:
- sequential by default
- retries with backoff
- skips existing non-empty files
- records HTTP status, bytes, content-type, SHA256
- supports Referer header when a source needs it
- no aggressive crawling: reads only URLs supplied in a CSV
"""
import argparse, csv, hashlib, mimetypes, os, time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

UA = "Mozilla/5.0 (research asset fetch; conservative rate)"
def sha256_file(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()

def fetch(url, dest, referer="", retries=5, timeout=60, delay=2.0):
    if dest.exists() and dest.stat().st_size>0:
        return {"status":"exists","http_status":"","bytes":dest.stat().st_size,
                "sha256":sha256_file(dest),"content_type":"","retry_count":0}
    last=""
    for attempt in range(retries):
        try:
            headers={"User-Agent":UA,"Accept":"image/avif,image/webp,image/apng,image/*,*/*;q=0.8"}
            if referer: headers["Referer"]=referer
            req=Request(url,headers=headers)
            with urlopen(req,timeout=timeout) as r, open(dest,"wb") as out:
                ctype=r.headers.get("Content-Type","")
                total=0
                while True:
                    chunk=r.read(1024*1024)
                    if not chunk: break
                    out.write(chunk); total+=len(chunk)
                code=getattr(r,"status",200)
            return {"status":"downloaded","http_status":code,"bytes":total,
                    "sha256":sha256_file(dest),"content_type":ctype,"retry_count":attempt}
        except (HTTPError,URLError,TimeoutError,OSError) as e:
            last=str(e)
            if dest.exists():
                try: dest.unlink()
                except: pass
            time.sleep(delay*(attempt+1))
    return {"status":"error","http_status":"","bytes":0,"sha256":"",
            "content_type":"","retry_count":retries,"error":last}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv", help="CSV with source_url/image_url and optional local_filename/referer")
    ap.add_argument("--outdir",default="book_assets")
    ap.add_argument("--log",default="asset_fetch_log.csv")
    ap.add_argument("--delay",type=float,default=2.0,help="seconds between requests")
    ap.add_argument("--url-column",default="image_url")
    args=ap.parse_args()
    outdir=Path(args.outdir); outdir.mkdir(parents=True,exist_ok=True)
    with open(args.csv,newline="",encoding="utf-8-sig") as f:
        rows=list(csv.DictReader(f))
    logs=[]
    for idx,row in enumerate(rows,1):
        url=(row.get(args.url_column) or row.get("source_url") or "").strip()
        if not url: continue
        fn=(row.get("local_filename") or row.get("crop_filename") or f"asset_{idx:04d}.jpg").strip()
        if not Path(fn).suffix:
            fn += ".jpg"
        dest=outdir/fn
        res=fetch(url,dest,row.get("referer",""),delay=args.delay)
        logs.append({
            "source_url":url,"local_file":str(dest),
            "status":res.get("status",""),"http_status":res.get("http_status",""),
            "bytes":res.get("bytes",0),"sha256":res.get("sha256",""),
            "content_type":res.get("content_type",""),
            "retry_count":res.get("retry_count",0),"error":res.get("error","")
        })
        print(idx, res.get("status"), fn)
        time.sleep(args.delay)
    with open(args.log,"w",newline="",encoding="utf-8") as f:
        fields=["source_url","local_file","status","http_status","bytes","sha256","content_type","retry_count","error"]
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(logs)

if __name__=="__main__":
    main()
