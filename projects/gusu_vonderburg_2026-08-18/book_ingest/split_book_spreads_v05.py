#!/usr/bin/env python3
"""
Split catalogue spread screenshots into page/entry crops.

Default assumes a two-page spread and 3 stacked entry bands per page.
It does not perform OCR; it creates stable crops and a machine-readable index.
"""
import argparse, csv, hashlib
from pathlib import Path
from PIL import Image

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for ch in iter(lambda:f.read(1024*1024),b""): h.update(ch)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("images", nargs="+")
    ap.add_argument("--outdir", default="book_crops")
    ap.add_argument("--rows", type=int, default=3)
    ap.add_argument("--gutter", type=float, default=0.02,
                    help="fraction of total spread width removed around central gutter")
    ap.add_argument("--top", type=float, default=0.00)
    ap.add_argument("--bottom", type=float, default=0.00)
    ap.add_argument("--index", default="book_crop_index.csv")
    args=ap.parse_args()
    outdir=Path(args.outdir); outdir.mkdir(parents=True,exist_ok=True)
    outrows=[]
    for sidx, name in enumerate(args.images,1):
        p=Path(name); im=Image.open(p).convert("RGB")
        W,H=im.size
        g=int(W*args.gutter/2)
        mid=W//2
        page_boxes={
            "left":(0,0,mid-g,H),
            "right":(mid+g,0,W,H)
        }
        source_hash=sha256(p)
        for side, box in page_boxes.items():
            page=im.crop(box)
            PW,PH=page.size
            top=int(PH*args.top); bottom=int(PH*(1-args.bottom))
            usable=max(1,bottom-top)
            for i in range(args.rows):
                y0=top+round(usable*i/args.rows)
                y1=top+round(usable*(i+1)/args.rows)
                crop=page.crop((0,y0,PW,y1))
                fn=f"{p.stem}_{side}_{i+1:02d}.jpg"
                dest=outdir/fn
                crop.save(dest, quality=95)
                outrows.append({
                    "source_file":str(p),"source_sha256":source_hash,
                    "spread_index":sidx,"page_side":side,
                    "entry_index_on_page":i+1,
                    "bbox_x0_norm":0.0,
                    "bbox_y0_norm":round(y0/PH,6),
                    "bbox_x1_norm":1.0,
                    "bbox_y1_norm":round(y1/PH,6),
                    "crop_file":str(dest)
                })
    with open(args.index,"w",newline="",encoding="utf-8") as f:
        fields=["source_file","source_sha256","spread_index","page_side","entry_index_on_page",
                "bbox_x0_norm","bbox_y0_norm","bbox_x1_norm","bbox_y1_norm","crop_file"]
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(outrows)
    print(args.index)

if __name__=="__main__":
    main()
