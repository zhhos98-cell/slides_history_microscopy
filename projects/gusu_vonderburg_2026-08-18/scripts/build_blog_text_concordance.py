#!/usr/bin/env python3
"""Build a text concordance between the 220 Gusu museum records and Christer von der Burg's blog.

This deliberately treats blog text as candidate pre-publication evidence, not as a substitute
for the published catalogue. Exact Chinese/English title hits are promoted; fuzzy hits remain
review candidates. The output preserves snippets and provenance for manual checking.
"""

from __future__ import annotations

import csv
import html
import json
import re
import sys
import time
import unicodedata
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import requests
from bs4 import BeautifulSoup
from rapidfuzz import fuzz

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "latest" / "combined_v2" / "gusu_working_220_official_image_manifest.csv"
OUTDIR = ROOT / "latest" / "blog_text_concordance"
BLOG = "https://chiwoopri.wordpress.com"
UA = "GusuTextConcordance/1.0 (+research; non-commercial)"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    s = html.unescape(s)
    s = s.replace("–", "-").replace("—", "-").replace("’", "'")
    s = s.lower()
    s = re.sub(r"[^0-9a-z\u3400-\u9fff]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def norm_zh(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    return re.sub(r"[^\u3400-\u9fff]", "", s)


def strip_html(raw: str) -> str:
    soup = BeautifulSoup(raw or "", "html.parser")
    return "\n".join(x.strip() for x in soup.stripped_strings if x.strip())


def fetch_rest_posts(session: requests.Session) -> List[Dict[str, str]]:
    posts: List[Dict[str, str]] = []
    page = 1
    endpoint = BLOG + "/wp-json/wp/v2/posts"
    while True:
        r = session.get(
            endpoint,
            params={"per_page": 100, "page": page, "_fields": "date,link,title,content"},
            timeout=45,
        )
        if r.status_code == 400 and "rest_post_invalid_page_number" in r.text:
            break
        r.raise_for_status()
        batch = r.json()
        if not batch:
            break
        for p in batch:
            title = strip_html((p.get("title") or {}).get("rendered", ""))
            body = strip_html((p.get("content") or {}).get("rendered", ""))
            posts.append({
                "post_title": title,
                "post_url": p.get("link", ""),
                "post_date": (p.get("date") or "")[:10],
                "post_text": body,
                "harvest_method": "wordpress_rest",
            })
        total_pages = int(r.headers.get("X-WP-TotalPages", page))
        if page >= total_pages:
            break
        page += 1
        time.sleep(0.15)
    return posts


def fetch_archive_posts(session: requests.Session, max_pages: int = 40) -> List[Dict[str, str]]:
    posts: List[Dict[str, str]] = []
    seen = set()
    empty = 0
    for page in range(1, max_pages + 1):
        url = BLOG + ("/" if page == 1 else f"/page/{page}/")
        r = session.get(url, timeout=45)
        if r.status_code >= 400:
            empty += 1
            if empty >= 2:
                break
            continue
        soup = BeautifulSoup(r.text, "html.parser")
        articles = soup.find_all("article")
        if not articles:
            empty += 1
            if empty >= 2:
                break
            continue
        empty = 0
        for article in articles:
            h = article.select_one("h1.entry-title a, h2.entry-title a, .entry-title a")
            body = article.select_one(".entry-content")
            if not h or not body:
                continue
            link = h.get("href", "")
            if not link or link in seen:
                continue
            seen.add(link)
            time_el = article.find("time")
            posts.append({
                "post_title": h.get_text(" ", strip=True),
                "post_url": link,
                "post_date": (time_el.get("datetime", "")[:10] if time_el else ""),
                "post_text": "\n".join(x.strip() for x in body.stripped_strings if x.strip()),
                "harvest_method": "archive_html",
            })
        time.sleep(0.15)
    return posts


def fetch_posts() -> List[Dict[str, str]]:
    session = requests.Session()
    session.headers.update({"User-Agent": UA})
    try:
        posts = fetch_rest_posts(session)
        if posts:
            return posts
    except Exception as e:
        print(f"REST harvest failed, falling back to archive HTML: {e}", file=sys.stderr)
    posts = fetch_archive_posts(session)
    if not posts:
        raise RuntimeError("No blog posts could be harvested")
    return posts


def context_for(text: str, needle: str, radius: int = 360) -> str:
    if not needle:
        return ""
    low = text.lower()
    idx = low.find(needle.lower())
    if idx < 0:
        return ""
    a = max(0, idx - radius)
    b = min(len(text), idx + len(needle) + radius)
    return re.sub(r"\s+", " ", text[a:b]).strip()


def best_fuzzy_line(title: str, text: str) -> Tuple[float, str]:
    title_n = norm(title)
    if len(title_n) < 8:
        return 0.0, ""
    best_score = 0.0
    best_line = ""
    for raw in text.splitlines():
        line = re.sub(r"\s+", " ", raw).strip()
        line_n = norm(line)
        if len(line_n) < 5:
            continue
        # Cap very long paragraphs so a generic title cannot score highly against an essay block.
        candidate = line if len(line) <= 500 else line[:500]
        score = max(
            fuzz.WRatio(title_n, norm(candidate)),
            fuzz.partial_ratio(title_n, norm(candidate)),
        )
        if score > best_score:
            best_score, best_line = float(score), line
    return best_score, best_line


def match_record(rec: Dict[str, str], post: Dict[str, str]) -> Dict[str, str] | None:
    en = (rec.get("title_en") or "").strip()
    zh = (rec.get("title_zh") or "").strip()
    text = post["post_text"]
    text_n = norm(text)
    text_zh = norm_zh(text)
    en_n = norm(en)
    zh_n = norm_zh(zh)

    match_type = ""
    score = 0.0
    snippet = ""
    matched_phrase = ""

    if zh_n and len(zh_n) >= 2 and zh_n in text_zh:
        match_type = "exact_zh"
        score = 100.0
        # Prefer the raw title for a readable context; otherwise use first two Chinese chars.
        snippet = context_for(text, zh) or context_for(text, zh_n[:2])
        matched_phrase = zh
    elif en_n and len(en_n) >= 8 and en_n in text_n:
        match_type = "exact_en"
        score = 98.0
        snippet = context_for(text, en)
        matched_phrase = en
    else:
        fuzzy_score, fuzzy_line = best_fuzzy_line(en, text)
        # Fuzzy matches are deliberately conservative. They are review leads only.
        if fuzzy_score >= 88.0:
            match_type = "fuzzy_text"
            score = fuzzy_score
            snippet = fuzzy_line
            matched_phrase = en
        else:
            return None

    sn_norm = norm(snippet)
    author_collection = any(
        x in sn_norm for x in ("author s collection", "author collection", "author's collection")
    )
    # Whole-post flag is useful when the title and ownership caption are on adjacent lines.
    author_collection_post = "author s collection" in norm(text) or "author's collection" in text.lower()

    if match_type.startswith("exact") and author_collection:
        confidence = "very_high"
    elif match_type.startswith("exact") and author_collection_post:
        confidence = "high"
    elif match_type.startswith("exact"):
        confidence = "high_candidate"
    elif score >= 95:
        confidence = "medium_high_candidate"
    else:
        confidence = "review_candidate"

    return {
        "working_220_id": rec.get("working_220_id", ""),
        "museum_code": rec.get("museum_code", ""),
        "accession": rec.get("accession", ""),
        "object_id": rec.get("object_id", ""),
        "title_en": en,
        "title_zh": zh,
        "object_url": rec.get("object_url", ""),
        "book_catalogue_no": rec.get("book_catalogue_no", ""),
        "book_page": rec.get("book_page", ""),
        "post_title": post["post_title"],
        "post_date": post["post_date"],
        "post_url": post["post_url"],
        "match_type": match_type,
        "match_score": f"{score:.1f}",
        "confidence": confidence,
        "author_collection_near_match": "1" if author_collection else "0",
        "author_collection_in_post": "1" if author_collection_post else "0",
        "matched_phrase": matched_phrase,
        "evidence_snippet": re.sub(r"\s+", " ", snippet).strip(),
        "status": "candidate_prepublication_text_concordance",
        "notes": "Blog text can be a precursor/comparandum for catalogue prose; do not treat as verbatim book text without page evidence.",
    }


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    posts = fetch_posts()
    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        records = list(csv.DictReader(f))

    post_fields = ["post_title", "post_date", "post_url", "harvest_method", "text_chars"]
    with (OUTDIR / "blog_posts_index.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=post_fields)
        w.writeheader()
        for p in posts:
            w.writerow({
                "post_title": p["post_title"],
                "post_date": p["post_date"],
                "post_url": p["post_url"],
                "harvest_method": p["harvest_method"],
                "text_chars": len(p["post_text"]),
            })

    matches: List[Dict[str, str]] = []
    for rec in records:
        for post in posts:
            m = match_record(rec, post)
            if m:
                matches.append(m)

    # De-duplicate exact duplicate row/post matches, then sort strongest first.
    unique = {}
    for m in matches:
        key = (m["working_220_id"], m["post_url"], m["match_type"])
        prev = unique.get(key)
        if prev is None or float(m["match_score"]) > float(prev["match_score"]):
            unique[key] = m
    matches = sorted(
        unique.values(),
        key=lambda x: (
            0 if x["match_type"] == "exact_zh" else 1 if x["match_type"] == "exact_en" else 2,
            -float(x["match_score"]),
            x["working_220_id"],
        ),
    )

    fields = [
        "working_220_id", "museum_code", "accession", "object_id", "title_en", "title_zh", "object_url",
        "book_catalogue_no", "book_page", "post_title", "post_date", "post_url", "match_type", "match_score",
        "confidence", "author_collection_near_match", "author_collection_in_post", "matched_phrase", "evidence_snippet",
        "status", "notes",
    ]
    with (OUTDIR / "candidate_matches.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(matches)

    high = [m for m in matches if m["confidence"] in {"very_high", "high"}]
    with (OUTDIR / "high_confidence_matches.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(high)

    matched_ids = sorted({m["working_220_id"] for m in matches})
    high_ids = sorted({m["working_220_id"] for m in high})
    summary = {
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "manifest_records": len(records),
        "blog_posts_harvested": len(posts),
        "candidate_match_rows": len(matches),
        "unique_museum_records_with_any_candidate": len(matched_ids),
        "high_confidence_match_rows": len(high),
        "unique_museum_records_high_confidence": len(high_ids),
        "method": "Exact Chinese title; exact normalized English title; conservative fuzzy English line match. Author's Collection proximity upgrades confidence.",
        "interpretation_rule": "A blog match is evidence for pre-publication research/textual ancestry, not proof that wording is verbatim in the 2025/2026 catalogue.",
    }
    (OUTDIR / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    readme = f"""# Gusu blog-text concordance\n\nGenerated from the current 220-record museum manifest and Christer von der Burg's public blog.\n\n- Blog posts harvested: **{len(posts)}**\n- Museum records: **{len(records)}**\n- Records with any candidate blog-text match: **{len(matched_ids)}**\n- Records with high-confidence match (exact title + Author's Collection evidence somewhere in the post): **{len(high_ids)}**\n\n## Evidence rule\n\nThese matches identify likely pre-publication research notes, earlier descriptions, or comparanda for catalogue entries. They are **not** labelled as verbatim book text unless independent photographed/OCR book-page evidence establishes that. Exact Chinese-title matches are strongest; fuzzy English matches remain review candidates.\n"""
    (OUTDIR / "README.md").write_text(readme, encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
