#!/usr/bin/env python3
"""Build a one-click Actions matrix for institution-specific slide harvesting."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

SURVEY = Path("data/survey/07A_Global_Microscope_Slide_Collections_Survey.csv")
ACTIVE = Path("data/normalized/scope_19c_active_ids.json")
PROFILES = Path("data/survey/institution_harvest_profiles.json")
OUT = Path("outputs/institution_harvest_matrix.json")
SKIP_AUTOMATION = {"manual only", "blocked"}
ACTIONS_BLOCKED_PROFILES = {"smg", "smithsonian", "museums_victoria"}

# These aliases are intentionally narrow. They collapse spelling/custody variants
# that hit the same public catalogue, while leaving genuinely different museums
# separate when their catalogues and custody are distinct.
INSTITUTION_GROUP_RULES = [
    (r"Farlow Herbarium", "farlow-herbarium", "Farlow Herbarium, Harvard University"),
    (r"Mus[eéu-]*um national d.Histoire naturelle.*Paris|MNHN.*Paris", "mnhn-paris", "Muséum national d'Histoire naturelle, Paris"),
    (r"Powerhouse", "powerhouse-collection", "Powerhouse Collection"),
    (r"Royal College of Surgeons of England|Hunterian Museum.*Royal College of Surgeons", "rcs-hunterian", "Royal College of Surgeons of England / Hunterian Museum"),
    (r"Naturhistorisches Museum Wien", "nhmw-vienna", "Naturhistorisches Museum Wien"),
    (r"Harvard(?: University)? Museum of Comparative Zoology|Harvard Museum of Comparative Zoology", "harvard-mcz", "Harvard Museum of Comparative Zoology"),
    (r"Museum f(?:u|ü|uer|ür) Naturkunde Berlin|Museum für Naturkunde Berlin", "museum-fuer-naturkunde-berlin", "Museum für Naturkunde Berlin"),
    (r"(?:University of Manchester,? )?Museum of Medicine and Health|Museum of Medicine and Health,? University of Manchester", "university-of-manchester-museum-of-medicine-and-health", "University of Manchester Museum of Medicine and Health"),
    (r"National Library of New Zealand(?: / Alexander Turnbull Library)?|Alexander Turnbull Library", "national-library-of-new-zealand", "National Library of New Zealand / Alexander Turnbull Library"),
]

# Third-wave adapters. These institutions were selected only after the first two
# reconnaissance runs demonstrated structured metadata or unusually high yield.
# The targeted harvester uses bounded catalogue-specific request recipes instead
# of simply doubling a generic crawl budget.
TARGETED_DEEP_ADAPTERS = {
    "university-of-st-andrews-libraries-and-museums": "standrews_items",
    "farlow-herbarium": "farlow_series",
    "whipple-museum-of-the-history-of-science-university-of-cambridge": "whipple_related",
    "sorbonne-universite-medical-and-pathological-anatomy-collections": "sorbonne_histology",
    "academy-of-natural-sciences-of-drexel-university": "ansp_diatom",
    "natural-history-museum-of-denmark-university-of-copenhagen": "copenhagen_desmid",
    "harvard-mcz": "mcz_slides",
    "ucl-grant-museum-of-zoology": "ucl_provenance",
}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "institution"


def canonical_institution_group(institution: str) -> tuple[str, str]:
    for pattern, key, label in INSTITUTION_GROUP_RULES:
        if re.search(pattern, institution, flags=re.I):
            return key, label
    return slugify(institution), institution


def load_rows() -> list[dict[str, str]]:
    with SURVEY.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_active() -> set[str]:
    if not ACTIVE.exists():
        return set()
    payload = json.loads(ACTIVE.read_text(encoding="utf-8"))
    return set(payload.get("entry_ids", []))


def host_of(url: str) -> str:
    try:
        return urlparse(url).hostname or ""
    except Exception:
        return ""


def choose_profile(institution: str, rows: list[dict[str, str]], profiles: dict[str, dict]) -> str:
    for key, profile in profiles.items():
        if profile.get("fallback"):
            continue
        if any(re.search(pat, institution, flags=re.I) for pat in profile.get("institution_patterns", [])):
            return key
        hosts = set(profile.get("match_hosts", []))
        if hosts and any(host_of(row.get("source_url", "")) in hosts for row in rows):
            return key

    automations = {row.get("automation_feasibility", "") for row in rows}
    if automations & {"API", "IIIF"}:
        return "generic_structured"
    if "paginated HTML" in automations:
        return "generic_catalogue"
    if "downloadable finding aid" in automations:
        return "generic_document"
    return "generic_seed"


def bundle_match(bundle: str, institution: str, profile_key: str, profile: dict, rows: list[dict[str, str]]) -> bool:
    if bundle == "all-automatable":
        return profile_key not in ACTIONS_BLOCKED_PROFILES
    if bundle == "remaining-automatable":
        return "high-yield" not in profile.get("tags", []) and profile_key not in ACTIONS_BLOCKED_PROFILES
    if bundle == "high-yield":
        return "high-yield" in profile.get("tags", [])
    if bundle == "uk-high-yield":
        return "high-yield" in profile.get("tags", []) and any(row.get("country") == "UK" for row in rows)

    text = " ".join([
        institution,
        *[row.get("collection_title_or_search_entry", "") for row in rows],
        *[row.get("subject_scope", "") for row in rows],
        *[row.get("person_or_collection_name", "") for row in rows],
    ]).lower()
    if bundle == "diatoms":
        return "diatom" in text
    if bundle == "medical-histology":
        return bool(re.search(r"histolog|patholog|anatom|medical|dental|embryolog|neurol|malaria", text))
    if bundle == "geology-petrology":
        return bool(re.search(r"petrograph|geolog|thin[- ]section|mineral|rock|palaeobot|fossil wood", text))
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", default="targeted-deep", choices=[
        "targeted-deep", "high-yield", "remaining-automatable", "all-automatable",
        "uk-high-yield", "diatoms", "medical-histology", "geology-petrology", "single",
    ])
    parser.add_argument("--institution-key", default="")
    parser.add_argument("--github-output", default="")
    args = parser.parse_args()

    cfg = json.loads(PROFILES.read_text(encoding="utf-8"))
    profiles = cfg["profiles"]
    rows = load_rows()
    active = load_active()
    if active:
        rows = [row for row in rows if row.get("entry_id") in active]

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    labels: dict[str, str] = {}
    raw_names: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if row.get("automation_feasibility", "") in SKIP_AUTOMATION:
            continue
        institution = row.get("institution_current", "").strip()
        if not institution:
            continue
        key, label = canonical_institution_group(institution)
        grouped[key].append(row)
        labels[key] = label
        raw_names[key].add(institution)

    include = []
    skipped_actions_blocked: list[dict[str, str]] = []
    for key in sorted(grouped):
        institution = labels[key]
        inst_rows = grouped[key]
        profile_key = choose_profile(institution, inst_rows, profiles)
        profile = profiles[profile_key]
        targeted_adapter = TARGETED_DEEP_ADAPTERS.get(key, "")

        if args.bundle == "single":
            if key != args.institution_key:
                continue
        elif args.bundle == "targeted-deep":
            if not targeted_adapter:
                continue
        elif not bundle_match(args.bundle, institution, profile_key, profile, inst_rows):
            if profile_key in ACTIONS_BLOCKED_PROFILES and args.bundle in {"all-automatable", "remaining-automatable"}:
                skipped_actions_blocked.append({"institution_key": key, "institution": institution, "profile": profile_key})
            continue

        include.append({
            "institution_key": key,
            "institution": institution,
            "profile": profile_key,
            "targeted_adapter": targeted_adapter,
            "row_count": len(inst_rows),
            "institution_alias_count": len(raw_names[key]),
        })

    payload = {
        "schema_version": "slide-survey-institution-matrix-v3-targeted-deep",
        "bundle": args.bundle,
        "active_strict_only": bool(active),
        "institution_count": len(include),
        "include": include,
        "skipped_actions_blocked": skipped_actions_blocked,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    matrix = json.dumps({"include": include}, ensure_ascii=False, separators=(",", ":"))
    print(matrix)
    if args.github_output:
        with Path(args.github_output).open("a", encoding="utf-8") as f:
            f.write(f"matrix={matrix}\n")
            f.write(f"institution_count={len(include)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
