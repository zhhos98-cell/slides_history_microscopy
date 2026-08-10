#!/usr/bin/env python3
"""Validate the current microscope-slide analysis authority layer.

This script does not rebuild the frozen survey or bibliography. It checks that
current-state routing metadata remains consistent with their canonical manifests
and that superseded Naples/request states do not leak back into the live router.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(rel: str):
    with (ROOT / rel).open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    state = load_json("data/analysis/CURRENT_STATE.json")
    router = load_json("data/analysis/global_archive_research_priority_CURRENT.json")
    bib = load_json("bibliography/bibliography-manifest.json")
    closure = load_json("data/survey/07AR_CLOSURE_MANIFEST_2026-08-09.json")
    naples = load_json("data/analysis/naples_row383_object_catalogue_closure_v4.json")

    errors: list[str] = []

    # Frozen survey counts.
    final = closure["final_counts"]
    if state["frozen_survey"]["discovery_nodes"] != final["canonical_discovery_entries"]:
        errors.append("CURRENT_STATE discovery count disagrees with 07AR closure manifest")
    if state["frozen_survey"]["strict_nineteenth_century_nodes"] != final["canonical_strict_19c_entries"]:
        errors.append("CURRENT_STATE strict-19C count disagrees with 07AR closure manifest")
    if state["frozen_survey"]["status"] != closure["status"]:
        errors.append("CURRENT_STATE frozen-survey status disagrees with 07AR closure manifest")

    # Bibliography arithmetic and manifest agreement.
    if bib["research"] + bib["primary"] != bib["total_entries"]:
        errors.append("bibliography manifest arithmetic is inconsistent")
    for key_state, key_bib in [
        ("total_entries", "total_entries"),
        ("research_entries", "research"),
        ("primary_object_entries", "primary"),
        ("publication_languages", "publication_languages"),
    ]:
        if state["bibliography"][key_state] != bib[key_bib]:
            errors.append(f"CURRENT_STATE bibliography {key_state} disagrees with bibliography manifest")
    if state["bibliography"]["version"] != bib["version"]:
        errors.append("CURRENT_STATE bibliography version disagrees with bibliography manifest")

    # Current router must be request-only and exactly four items.
    if state["public_web_discovery_queue"]:
        errors.append("CURRENT_STATE public-web discovery queue must be empty")
    if router.get("public_web_queue"):
        errors.append("live router public-web queue must be empty")
    if len(state["exact_source_request_queue"]) != 4:
        errors.append("CURRENT_STATE exact-source queue must contain exactly four items")
    if len(router.get("exact_source_request_queue", [])) != 4:
        errors.append("live router exact-source queue must contain exactly four items")

    state_targets = [x["target"] for x in state["exact_source_request_queue"]]
    router_targets = [x["target"] for x in router["exact_source_request_queue"]]
    if state_targets != router_targets:
        errors.append("CURRENT_STATE and live-router exact-source target order differ")

    # Naples 383 must remain closed and absent from request queues.
    if any("Naples" in t and "383" in t for t in state_targets + router_targets):
        errors.append("Naples 383 leaked back into the live request queue")
    if "CLOSED" not in naples.get("status", ""):
        errors.append("Naples 383 current closure file is not marked closed")
    if not any("Naples catalogue offering 383" in x for x in state["closed_or_substantially_closed_relations"]):
        errors.append("CURRENT_STATE does not record Naples 383 among closed relations")

    # Quantity namespace guardrails.
    if state["bibliography"]["total_entries"] == state["frozen_survey"]["discovery_nodes"]:
        errors.append("bibliography and survey counts unexpectedly collapsed to the same namespace")

    if errors:
        raise SystemExit("\n".join(f"ERROR: {e}" for e in errors))

    print("Current analysis state OK")
    print(f"Survey: {final['canonical_discovery_entries']} discovery / {final['canonical_strict_19c_entries']} strict 19C")
    print(f"Bibliography: {bib['total_entries']} = {bib['research']} research + {bib['primary']} primary/object")
    print("Public-web queue: 0")
    print("Exact-source queue: 4")
    print("Naples 383: closed and absent from live queue")


if __name__ == "__main__":
    main()
