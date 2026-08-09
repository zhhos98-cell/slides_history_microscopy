#!/usr/bin/env python3
"""Third-wave targeted metadata harvester for the frozen microscope-slide survey.

This script is deliberately narrower than ``harvest_institution.py``. It is
used only for institutions selected after two reconnaissance Actions runs. A
JSON recipe controls a bounded catalogue-specific strategy (focused BFS,
fixed pages, form POST, Symbiota POST, or Sorbonne histology enumeration).

Public metadata only. No image binaries or IIIF image tiles are requested.
PDFs remain subject to the small-PDF limit enforced by the base harvester.
Every extracted quantity remains review-only and is assigned a conservative
namespace; catalogue/sample identifiers are never promoted to physical counts.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import deque
from pathlib import Path
from typing import Any

import harvest_institution as base
from build_institution_matrix import canonical_institution_group

TARGET_PROFILES = Path("data/survey/targeted_harvest_profiles.json")
OUT_ROOT = Path("outputs/institution_harvest")
RELATIONSHIP_PHRASES = [
    "prepared by", "mounted by", "collected by", "assembled by", "used by",
    "sent to", "received by", "exchanged by", "presented to", "donated by",
    "purchased by", "sold by", "distributed by", "lent by", "transferred from",
    "from the collection of", "belonging to", "held by", "catalogued by",
    "digitised by", "digitized by", "labelled by", "labeled by", "inscribed by",
    "part of", "from the period of",
]
QUANTITY_RE = re.compile(
    r"\b(?:(about|approximately|around|over|more than|ca\.?|circa)\s+)?"
    r"(\d[\d,]*)\s+"
    r"(microscope slides|slides|preparations|specimens|objects|drawers|cabinets|boxes|trays|sections)\b",
    re.I,
)
IDENTIFIER_CONTEXT = re.compile(
    r"(?:sample|catalog(?:ue)?|accession|registration|inventory|register|object|specimen|slide)"
    r"\s*(?:no\.?|number|#|:)?\s*$",
    re.I,
)
QUANTITY_NAMESPACE = {
    "microscope slides": "physical_slide_count",
    "slides": "physical_slide_count",
    "preparations": "preparation_count",
    "specimens": "specimen_count",
    "objects": "object_count",
    "drawers": "container_count",
    "cabinets": "container_count",
    "boxes": "container_count",
    "trays": "container_count",
    "sections": "section_count",
}


def _normalise_ws(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value or "")).strip()


def quantity_candidates(text: str) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for match in QUANTITY_RE.finditer(text or ""):
        start, end = match.span()
        before = (text or "")[max(0, start - 100):start]
        after = (text or "")[end:min(len(text or ""), end + 100)]
        unit = match.group(3).lower()
        namespace = QUANTITY_NAMESPACE.get(unit, "unclassified_count")
        if IDENTIFIER_CONTEXT.search(before[-60:]):
            namespace = "identifier_context"
        out.append({
            "surface": _normalise_ws(match.group(0)),
            "value": match.group(2),
            "qualifier": (match.group(1) or "").strip(),
            "unit": unit,
            "namespace": namespace,
            "context": _normalise_ws(before + match.group(0) + after)[:360],
            "review_required": True,
        })
        if len(out) >= 80:
            break
    return out


def relationship_candidates(text: str) -> list[dict[str, str]]:
    lower = (text or "").lower()
    out: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for phrase in RELATIONSHIP_PHRASES:
        start = 0
        while True:
            pos = lower.find(phrase, start)
            if pos < 0:
                break
            snippet = _normalise_ws((text or "")[max(0, pos - 100):min(len(text or ""), pos + len(phrase) + 140)])
            key = (phrase, snippet)
            if key not in seen:
                seen.add(key)
                out.append({"phrase": phrase, "context": snippet[:420]})
            start = pos + len(phrase)
            if len(out) >= 60:
                return out
    return out


def rows_for_institution(institution_key: str) -> list[dict[str, str]]:
    rows = base.load_rows()
    active = base.load_active()
    if active:
        rows = [row for row in rows if row.get("entry_id") in active]
    selected: list[dict[str, str]] = []
    for row in rows:
        if row.get("automation_feasibility", "") in base.SKIP_AUTOMATION:
            continue
        raw_name = row.get("institution_current", "").strip()
        if not raw_name:
            continue
        key, _label = canonical_institution_group(raw_name)
        if key == institution_key:
            selected.append(row)
    return selected


def request_post(url: str, data: dict[str, Any], max_bytes: int, charset: str = "utf-8") -> tuple[bytes, str, str, dict[str, Any]]:
    encoded = urllib.parse.urlencode(data, doseq=True, encoding=charset, errors="replace").encode("ascii")
    req = urllib.request.Request(
        url,
        data=encoded,
        headers={
            "User-Agent": base.USER_AGENT,
            "Accept": "text/html,application/json,application/ld+json,text/plain,text/csv;q=0.8,*/*;q=0.2",
            "Content-Type": f"application/x-www-form-urlencoded; charset={charset}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=40) as resp:  # noqa: S310
        ctype = resp.headers.get("content-type", "").split(";", 1)[0].strip().lower()
        final_url = resp.geturl()
        content_length = base._content_length(resp.headers)
        body = resp.read(max_bytes + 1)
    truncated = len(body) > max_bytes
    if truncated:
        body = body[:max_bytes]
    return body, ctype, final_url, {
        "skipped_large_pdf": False,
        "content_length": content_length,
        "truncated": truncated,
    }


def request_signature(method: str, url: str, data: dict[str, Any] | None) -> str:
    payload = json.dumps(data or {}, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(f"{method}\n{url}\n{payload}".encode("utf-8")).hexdigest()


def allowed(url: str, hosts: set[str]) -> bool:
    return base.host_allowed(url, hosts) and not base.skip_binary(url)


def target_link(url: str, label: str, recipe: dict[str, Any]) -> bool:
    hay = f"{url} {label}"
    return any(re.search(pat, hay, re.I) for pat in recipe.get("follow_url_regex", []))


def extract_table_rows(raw: str, source_url: str, request_label: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for tr in re.findall(r"(?is)<tr\b[^>]*>(.*?)</tr>", raw):
        cells = re.findall(r"(?is)<t[dh]\b[^>]*>(.*?)</t[dh]>", tr)
        values = [_normalise_ws(base.html_to_text(cell)) for cell in cells]
        values = [value for value in values if value]
        if not values:
            continue
        rows.append({
            "row_type": "html_table_row",
            "source_url": source_url,
            "request_label": request_label,
            "cells": values[:30],
            "review_required": True,
        })
        if len(rows) >= 1000:
            break
    return rows


def extract_sorbonne_cards(raw: str, source_url: str, request_label: str) -> tuple[list[dict[str, Any]], list[str], int | None]:
    cards: list[dict[str, Any]] = []
    detail_urls: list[str] = []
    total: int | None = None
    total_match = re.search(r'data-nbresultats=["\'](\d+)["\']', raw, re.I)
    if total_match:
        total = int(total_match.group(1))
    pattern = re.compile(
        r'(?is)<figure\b[^>]*class=["\'][^"\']*\bimage\b[^"\']*["\'][^>]*data-lnk=["\']([^"\']+)["\'][^>]*>(.*?)</figure>'
    )
    for link, block in pattern.findall(raw):
        detail_url = base.normalise_url(link, source_url)
        fields: dict[str, str] = {}
        for cls, value in re.findall(r'(?is)<div\b[^>]*class=["\']detail-([^"\']+)["\'][^>]*>(.*?)</div>', block):
            clean = _normalise_ws(base.html_to_text(value))
            if clean:
                fields[cls.strip()] = clean[:2000]
        counter = re.search(r'(?is)<div\b[^>]*class=["\']counter["\'][^>]*>(.*?)</div>', block)
        card = {
            "row_type": "sorbonne_search_card",
            "source_url": source_url,
            "request_label": request_label,
            "detail_url": detail_url,
            "counter": _normalise_ws(base.html_to_text(counter.group(1))) if counter else "",
            "query_total": total,
            "fields": fields,
            "review_required": True,
        }
        cards.append(card)
        if detail_url:
            detail_urls.append(detail_url)
    return cards, detail_urls, total


def augment_record(record: dict[str, Any], request_method: str, request_label: str, posted_fields: dict[str, Any] | None = None) -> None:
    sample = record.get("text_sample", "") or ""
    qc = quantity_candidates(sample)
    record["quantity_candidates"] = qc
    record["count_candidates"] = [item["surface"] for item in qc[:30]]
    record["relationship_candidates"] = relationship_candidates(sample)
    record["request_method"] = request_method
    record["request_label"] = request_label
    if posted_fields is not None:
        record["posted_fields"] = posted_fields
    record["schema_version"] = "slide-survey-targeted-harvest-record-v1"


def append_catalogue_rows(store: dict[str, dict[str, Any]], rows: list[dict[str, Any]]) -> None:
    for row in rows:
        detail = row.get("detail_url")
        if detail:
            key = f"detail:{detail}"
        else:
            key = "row:" + hashlib.sha256(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
        if key in store and row.get("request_label"):
            existing = store[key]
            labels = set(existing.get("matched_request_labels", []))
            if existing.get("request_label"):
                labels.add(existing["request_label"])
            labels.add(row["request_label"])
            existing["matched_request_labels"] = sorted(labels)
        else:
            store[key] = row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--institution-key", required=True)
    parser.add_argument("--adapter", required=True)
    parser.add_argument("--mode", choices=["dry-run", "full"], default="full")
    parser.add_argument("--depth", choices=["quick", "balanced", "deep"], default="balanced")
    parser.add_argument("--delay", type=float, default=0.65)
    args = parser.parse_args()

    cfg = json.loads(TARGET_PROFILES.read_text(encoding="utf-8"))
    if args.adapter not in cfg.get("adapters", {}):
        raise SystemExit(f"Unknown targeted adapter: {args.adapter}")
    recipe = cfg["adapters"][args.adapter]
    if recipe.get("institution_key") != args.institution_key:
        raise SystemExit(
            f"Adapter {args.adapter} is bound to {recipe.get('institution_key')}, not {args.institution_key}"
        )

    rows = rows_for_institution(args.institution_key)
    if not rows:
        raise SystemExit(f"No active automatable rows for targeted institution {args.institution_key}")

    institution = canonical_institution_group(rows[0].get("institution_current", ""))[1]
    out_dir = OUT_ROOT / args.institution_key
    out_dir.mkdir(parents=True, exist_ok=True)

    defaults = cfg.get("defaults", {})
    base_budget = int(recipe.get("request_budget", 40))
    factor = {"quick": 0.6, "balanced": 1.0, "deep": 1.2}[args.depth]
    request_budget = max(1, int(base_budget * factor))
    request_budget = min(request_budget, int(defaults.get("absolute_request_cap", 140)))
    max_bytes = int(recipe.get("max_bytes", defaults.get("max_bytes", 4_000_000)))
    max_pdf_bytes = int(recipe.get("max_pdf_bytes", defaults.get("max_pdf_bytes", 5_000_000)))
    allowed_hosts = {host.lower() for host in recipe.get("allowed_hosts", [])}
    active_ids = [row.get("entry_id", "") for row in rows if row.get("entry_id")]

    seed_to_ids: dict[str, list[str]] = {}
    for row in rows:
        url = base.normalise_url(row.get("source_url", ""))
        if url and allowed(url, allowed_hosts):
            seed_to_ids.setdefault(url, []).append(row.get("entry_id", ""))
    for url in recipe.get("extra_seed_urls", []):
        url = base.normalise_url(url)
        if url and allowed(url, allowed_hosts):
            seed_to_ids.setdefault(url, list(active_ids))

    plan = {
        "schema_version": "slide-survey-targeted-harvest-plan-v1",
        "institution_key": args.institution_key,
        "institution": institution,
        "targeted_adapter": args.adapter,
        "strategy": recipe.get("strategy"),
        "mode": args.mode,
        "depth": args.depth,
        "request_budget": request_budget,
        "max_pdf_bytes": max_pdf_bytes,
        "active_entry_ids": active_ids,
        "seed_urls": list(seed_to_ids),
        "allowed_hosts": sorted(allowed_hosts),
        "recipe_relevance_terms": recipe.get("relevance_terms", []),
    }
    (out_dir / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.mode == "dry-run":
        summary = {**plan, "status": "dry-run", "fetched": 0, "errors": 0, "catalogue_rows": 0}
        (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return 0

    strategy = recipe.get("strategy", "targeted_bfs")
    queue: deque[dict[str, Any]] = deque()
    queued_signatures: set[str] = set()

    def enqueue(method: str, url: str, *, data: dict[str, Any] | None = None, label: str = "", seed_ids: list[str] | None = None) -> None:
        url = base.normalise_url(url)
        if not url or not allowed(url, allowed_hosts):
            return
        signature = request_signature(method, url, data)
        if signature in queued_signatures:
            return
        queued_signatures.add(signature)
        queue.append({
            "method": method,
            "url": url,
            "data": data,
            "label": label or "seed",
            "seed_ids": seed_ids or list(active_ids),
            "signature": signature,
        })

    if strategy == "sorbonne_histology":
        query_urls = recipe.get("query_urls", [])
        if query_urls:
            for item in query_urls:
                enqueue("GET", item["url"], label=item.get("label", "sorbonne query"))
        else:
            base_query = "https://colluniv.sorbonne-universite.fr/recherche/*/f:isPartOf--collection=Collections+m%C3%A9dicales+et+d%27anatomie+pathologique/"
            enqueue("GET", base_query + "f:description--typologie=Lame+histologique/", label="all medical histology")
            enqueue("GET", base_query + "f:isPartOf--fonds=Fondation+Dejerine/f:description--typologie=Lame+histologique/", label="Fondation Dejerine histology")
            enqueue("GET", base_query + "f:isPartOf--fonds=Dejerine%2C+Joseph-Jules+%281849+-+1917%29/f:description--typologie=Lame+histologique/", label="Joseph-Jules Dejerine histology")
            enqueue("GET", base_query + "f:isPartOf--fonds=Dejerine-Klumpke%2C+Augusta+%281859+-+1927%29/f:description--typologie=Lame+histologique/", label="Augusta Dejerine-Klumpke histology")
    else:
        for url, ids in seed_to_ids.items():
            enqueue("GET", url, label="targeted seed", seed_ids=ids)

    if strategy in {"symbiota_post", "form_post"}:
        for req in recipe.get("post_requests", []):
            enqueue(
                "POST", recipe["post_url"], data=req.get("data", {}),
                label=req.get("label", "targeted POST"), seed_ids=list(active_ids),
            )

    fetched_signatures: set[str] = set()
    records: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    skipped_large_pdfs: list[dict[str, Any]] = []
    catalogue_store: dict[str, dict[str, Any]] = {}
    query_totals: list[dict[str, Any]] = []

    while queue and len(fetched_signatures) < request_budget:
        item = queue.popleft()
        signature = item["signature"]
        if signature in fetched_signatures:
            continue
        fetched_signatures.add(signature)
        method = item["method"]
        url = item["url"]
        data = item.get("data")
        label = item.get("label", "")
        try:
            if method == "POST":
                body, ctype, final_url, fetch_meta = request_post(
                    url, data or {}, max_bytes,
                    charset=recipe.get("post_charset", "iso-8859-1" if args.adapter == "copenhagen_desmid" else "utf-8"),
                )
            else:
                body, ctype, final_url, fetch_meta = base.fetch(url, max_bytes, max_pdf_bytes)
            if fetch_meta.get("skipped_large_pdf"):
                skipped_large_pdfs.append({
                    "url": url,
                    "final_url": final_url,
                    "reason": fetch_meta.get("reason"),
                    "content_length": fetch_meta.get("content_length"),
                    "limit_bytes": fetch_meta.get("limit_bytes"),
                    "request_label": label,
                    "seed_entry_ids": item.get("seed_ids", []),
                })
                continue

            record, discovered = base.build_record(
                url, final_url, body, ctype, item.get("seed_ids", []),
                f"targeted:{args.adapter}", len(records) + 1, out_dir, fetch_meta,
            )
            augment_record(record, method, label, data if method == "POST" else None)
            records.append(record)

            if "html" in ctype or not ctype:
                raw = body.decode("utf-8", errors="replace")
                append_catalogue_rows(catalogue_store, extract_table_rows(raw, final_url, label))

                if strategy == "sorbonne_histology":
                    cards, detail_urls, total = extract_sorbonne_cards(raw, final_url, label)
                    append_catalogue_rows(catalogue_store, cards)
                    if total is not None:
                        query_totals.append({"request_label": label, "url": final_url, "result_count": total})
                    for detail_url in detail_urls:
                        enqueue("GET", detail_url, label=f"detail from {label}", seed_ids=item.get("seed_ids", []))
                elif strategy != "fixed_pages":
                    for link_url, link_label in discovered:
                        if target_link(link_url, link_label, recipe):
                            enqueue("GET", link_url, label=f"follow from {label}", seed_ids=item.get("seed_ids", []))
        except urllib.error.HTTPError as exc:
            errors.append({"url": url, "method": method, "request_label": label, "error": f"HTTP {exc.code}"})
        except Exception as exc:  # noqa: BLE001
            errors.append({"url": url, "method": method, "request_label": label, "error": repr(exc)})
        time.sleep(max(args.delay, 0.0))

    with (out_dir / "records.jsonl").open("w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")
    with (out_dir / "catalogue_rows.jsonl").open("w", encoding="utf-8") as f:
        for row in catalogue_store.values():
            f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

    ctype_counts: dict[str, int] = {}
    relationship_total = 0
    quantity_total = 0
    for record in records:
        key = record.get("content_type", "") or "unknown"
        ctype_counts[key] = ctype_counts.get(key, 0) + 1
        relationship_total += len(record.get("relationship_candidates", []))
        quantity_total += len(record.get("quantity_candidates", []))

    summary = {
        **plan,
        "status": "complete",
        "fetched": len(records),
        "requests_attempted": len(fetched_signatures),
        "errors": len(errors),
        "catalogue_rows": len(catalogue_store),
        "relationship_candidates": relationship_total,
        "quantity_candidates": quantity_total,
        "skipped_large_pdfs": len(skipped_large_pdfs),
        "skipped_large_pdf_detail": skipped_large_pdfs,
        "queued_remaining": len(queue),
        "request_budget_reached": len(fetched_signatures) >= request_budget,
        "content_type_counts": ctype_counts,
        "query_totals": query_totals,
        "errors_detail": errors,
    }
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"{institution}: targeted={args.adapter} fetched={len(records)} "
        f"catalogue_rows={len(catalogue_store)} errors={len(errors)} budget={request_budget}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
