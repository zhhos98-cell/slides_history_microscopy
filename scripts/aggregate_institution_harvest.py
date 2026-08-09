#!/usr/bin/env python3
"""Aggregate institution-harvest artifacts into one workflow-run index."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="bundle")
    parser.add_argument("--out", default="bundle/bundle_index.json")
    args = parser.parse_args()

    root = Path(args.root)
    summaries: list[dict[str, Any]] = []
    for path in sorted(root.rglob("summary.json")):
        try:
            item = json.loads(path.read_text(encoding="utf-8"))
            item["_summary_path"] = str(path)
            summaries.append(item)
        except Exception as exc:
            summaries.append({"_summary_path": str(path), "parse_error": repr(exc)})

    totals = {
        "institutions": len(summaries),
        "fetched": sum(int(x.get("fetched", 0) or 0) for x in summaries),
        "errors": sum(int(x.get("errors", 0) or 0) for x in summaries),
        "dry_runs": sum(1 for x in summaries if x.get("status") == "dry-run"),
    }
    payload = {
        "schema_version": "slide-survey-institution-harvest-bundle-index-v1",
        "totals": totals,
        "institutions": summaries,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(totals, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
