#!/usr/bin/env python3
"""Build a derived analytical layer over the sealed 155-row slide catalogue.

This script never changes frozen membership or source wording. It accepts a
final backend CSV and adds seven deliberately reductive analytical fields plus
review metadata. Categories are inferred only from retained catalogue fields.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

EXPECTED_ROWS = 155


def unit_level(r):
    title=r['collection_title_or_search_entry'].lower(); phys=r['physical_structure'].lower(); count=r['stated_count'].lower(); d=r['date_range'].lower(); notes=r['notes'].lower()
    t=' | '.join([title,phys,count,d,notes])
    if re.search(r'\b(?:single|one explicitly identified|1)\s+(?:glass\s+)?(?:microscope\s+)?slide\b',t) or 'one microscope slide' in t:
        return 'single_slide','high'
    if any(k in count for k in ['mixed-period','mixed total','nineteenth-century subtotal','strict pre-1900 subtotal','subset to isolate','subtotal unresolved','pure nineteenth-century']) or re.search(r'\b18\d{2}\s*[-–]\s*19\d{2}\b',d) or 'mixed' in d:
        return 'mixed_parent_collection','high'
    if any(k in title for k in ['cabinet','box containing','case containing','case of microscope slides','wooden box','slide pieces in repurposed cardboard box']) and 'collection' not in title:
        return 'container_assemblage','high'
    if any(k in phys for k in ['cabinet object','wooden box with associated microscope slides']) and 'collection' not in title:
        return 'container_assemblage','medium'
    if any(k in title for k in ['set of','institutional copy','teaching sets','slide set']) or 'numbered microscope-slide set' in phys or (re.match(r'^\s*\d[\d,]*\s+(?:microscope\s+)?slides?\b',count) and any(k in phys for k in ['case','box','set','slipcase'])):
        return 'bounded_set','high'
    if any(k in title for k in ['historical registers','microscopical section','earliest rcse','historical and current','historical microscope-slide collection','microscopic-preparation teaching collection','historical zoological microscopic-preparation collection','scientific estate microscopic preparations','foundation layer','teaching collection / micrarium']):
        return 'institutional_layer','medium'
    if any(k in title for k in ['collection','slides','preparations','sections']):
        return 'named_collection','medium'
    return 'institutional_layer','low'


def production_period(r):
    d=r['date_range'].lower()
    if re.search(r'\b18\d{2}\s*[-–]\s*(?:19|20)\d{2}\b',d) or any(k in d for k in ['late nineteenth to early twentieth','mixed historical collection','strict nineteenth-century subset','strict subset']):
        return 'mixed_19c_plus_20c','high'
    years=[int(y) for y in re.findall(r'(?<!\d)(1[89]\d{2}|20\d{2})(?!\d)',d)]; y19=[y for y in years if 1800<=y<=1899]
    if not y19:
        if any(k in d for k in ['late nineteenth','last quarter','second half of the nineteenth']): return 'late_19c_1870_1899','medium'
        if any(k in d for k in ['mid-nineteenth','middle of the nineteenth']): return 'mid_19c_1840_1869','medium'
        if 'early nineteenth' in d or 'around 1800' in d: return 'early_19c_1800_1839','medium'
        if 'nineteenth' in d or '19th' in d: return '19c_unspecified','high'
        return '19c_unspecified','low'
    def b(y): return 0 if y<=1839 else 1 if y<=1869 else 2
    bins={b(y) for y in y19}
    if len(bins)>1: return 'spans_19c_periods','medium'
    return ['early_19c_1800_1839','mid_19c_1840_1869','late_19c_1870_1899'][next(iter(bins))],'high'


def subject_cluster(r):
    s=r['subject_scope'].lower()
    if any(k in s for k in ['diatom','phycolog','algae']): return 'diatoms_phycology','high'
    if any(k in s for k in ['foraminif','radiolaria','protist']): return 'foraminifera_protists','high'
    if any(k in s for k in ['patholog','dental','dentistry','histolog','anatomy','medical','veterinary','human remains','malaria','public health','cholera','diagnostic medicine','blood and parasite','nervous tissue','cerebral cortex','spinal cord']): return 'medical_histology_pathology','high'
    if any(k in s for k in ['embryolog','centrosome','chromosome','cell biology','development']): return 'embryology_cell_biology','high'
    if any(k in s for k in ['bacteriolog','microbiolog','infectious disease']): return 'bacteriology_microbiology','high'
    if any(k in s for k in ['petrograph','geolog','mineral','rock thin','palaeobot','paleobot','fossil wood','meteorite','coal ball','ichthyosaur','metallurg']): return 'geology_petrography_palaeobotany','high'
    if any(k in s for k in ['chemical crystall','crystalline carbon','resolution test','fluid-inclusion','experimental microscopy','instrument use']): return 'experimental_physical_science','high'
    if any(k in s for k in ['entomolog','arthropod','insect','mite','acarolog','thysanoptera','crustacean','ostracoda','copepoda']): return 'entomology_arthropods','high'
    if any(k in s for k in ['zoolog','porifera','sponge','hydroid','hydrozoa','coral','annelid','invertebrate','bryozoa','fish','marine zoolog']): return 'zoology_invertebrates','high'
    if any(k in s for k in ['botany','botanical','plant']): return 'botany','high'
    if any(k in s for k in ['microphotograph','photomicrograph','astronomy']): return 'microphotography_optical_media','high'
    if any(k in s for k in ['natural history','three kingdoms','mixed victorian','diverse subjects','commercial prepared slides','microscopy','mostly biological']): return 'general_mixed_microscopy','medium'
    return 'other_specialist','low'


def formation(r):
    t=' | '.join([r['subject_scope'],r['relationship_phrase'],r['collection_title_or_search_entry'],r['notes'],r['physical_structure']]).lower(); rel=r['relationship_phrase'].lower()
    if ('published by' in rel and ('distributed' in rel or 'issued' in rel)) or 'published exsicc' in t or 'published serial' in t: return 'published_distributed_set','high'
    commercial=any(k in t for k in ['commercial','dealer','sold by','purchased from','supplied by','business opened','slide trade','catalogue offered','commercial workshop','commercial slide'])
    institutional=any(k in t for k in ['teaching','university','museum','laboratory','course','hospital','school science','army medical museum','institutional'])
    personal=any(k in rel for k in ['from the collection of','assembled by','used by','collected by']) and not institutional
    if commercial and institutional: return 'hybrid','high'
    if commercial: return 'commercial_trade','medium'
    if institutional: return 'institutional_teaching_research','medium'
    if personal: return 'personal_research_collection','medium'
    return 'unclear','low'


def circulation(r):
    rel=r['relationship_phrase'].lower(); modes=[]
    mapping=[('sale_purchase',['purchased by','purchased from','sold by','bought from','acquired by']),('gift_donation_presentation',['donated by','presented to','gifted','bequeathed by','bequeathed to']),('exchange_distribution',['exchanged by','exchanged with','distributed by','distributed to','issued by']),('institutional_transfer_deposit',['transferred from','transferred to','deposited by','accessioned by','incorporated into']),('research_correspondence_sent',['sent to','received by','received from','transported to','transported by']),('family_descent',['passed down to descendants','descendants']),('loan_borrowing',['lent by','borrowed'])]
    for mode,keys in mapping:
        if any(k in rel for k in keys): modes.append(mode)
    if not modes:
        return ('retained_without_explicit_transfer','medium') if ('held by' in rel or 'preserved in' in rel or 'retained' in rel) else ('no_circulation_event_stated','medium')
    return ';'.join(dict.fromkeys(modes)),'high'


def count_namespace(r):
    s=r['stated_count'].lower(); ns=[]
    if 'serial range' in s or 'section-number ranges' in s or ('numbered' in s and 'identifier' in s): ns.append('serial_or_register_range')
    if any(k in s for k in ['mixed-period','mixed total','today','current wider','current aggregate','modern parent','current nhm','museum-wide','current collection','current legal inventory','current whole','overall','strict pre-1900 subtotal','nineteenth-century subtotal','subset to isolate','pure nineteenth-century','historical subset unstated','exact pre-1900 subtotal']): ns.append('current_or_mixed_period_aggregate')
    if re.search(r'\b\d[\d,]*\s+(?:microscope\s+|glass\s+|geological\s+|petrographic\s+)?slides?\b',s) or any(k in s for k in ['slide count','slides total','slides in','slides today','slides made','slides survive','slide batch']): ns.append('physical_slide_count')
    if re.search(r'\b\d[\d,]*\s+microphotographs?\b',s): ns.append('mounted_media_count')
    if re.search(r'\b\d[\d,]*\s+(?:microscopic|microscopical|histological)?\s*preparations?\b',s) or re.search(r'\b\d[\d,]*\s+thin sections?\b',s) or 'preparations total' in s: ns.append('preparation_or_thin_section_count')
    if re.search(r'\b\d[\d,]*\s+(?:specimens?|objects?|parts|samples?|drawings?|letters?|bottles?|tubes?)\b',s): ns.append('specimen_object_or_mixed_count')
    if re.search(r'\b\d[\d,]*\s+(?:drawers?|cabinets?|boxes?|trays?)\b',s) or 'designed for' in s: ns.append('container_count_or_capacity')
    if any(k in s for k in ['exact count unstated','count unstated','to enumerate','subtotal unresolved','total unstated','not stated','unresolved','exact slide total not','exact surviving count unstated','exact current survivor count unresolved']): ns.append('unstated_or_unresolved')
    if not ns:
        if any(k in s for k in ['one slide','one identified','plural glass slides','some fifty microscope slides','hundreds of thin sections','thousands of microscopic preparations','large collection','selection survives']):
            ns.append('physical_slide_count' if 'slide' in s else 'preparation_or_thin_section_count' if ('preparation' in s or 'thin section' in s) else 'source_stated_quantity_other')
        else: ns.append('source_stated_quantity_other')
    return ';'.join(dict.fromkeys(ns)),('high' if len(ns)==1 else 'medium')


def actor_roles(r):
    rel=r['relationship_phrase'].lower(); roles=[]
    mapping=[('preparer_mounter_producer',['prepared by','mounted by','produced by','made up by','created by','produced','prepared or','perhaps made by']),('collector_assembler',['collected by','assembled by','collection started by','grouped in','from the collection of','commenced by']),('user_researcher_teacher',['used by','used for','studied by','from the work of','prepared for','reviewed by','re-examined by']),('publisher_distributor_seller',['published by','distributed by','issued by','sold by','supplied by']),('buyer_recipient_donee',['purchased by','received by','presented to','acquired by']),('donor_bequeather_depositor',['donated by','bequeathed by','gifted to','deposited by','presented by']),('sender_exchanger_transporter',['sent to','exchanged by','exchanged with','transported by','transported to','distributed to']),('institutional_custodian_cataloguer',['held by','catalogued by','digitised by','preserved in','retained in','accessioned by','archived by','recovered by','rediscovered by']),('attributed_or_uncertain',['attributed to','probably','uncertain','possibly','perhaps'])]
    for role,keys in mapping:
        if any(k in rel for k in keys): roles.append(role)
    return (';'.join(dict.fromkeys(roles)),'high') if roles else ('other_explicit_role','low')


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input',type=Path); ap.add_argument('--output',type=Path,default=Path('outputs/SLIDE_155_ANALYSIS_LAYER_V1.csv')); args=ap.parse_args()
    with args.input.open(newline='',encoding='utf-8') as f: rows=list(csv.DictReader(f))
    if len(rows)!=EXPECTED_ROWS or len({r['entry_id'] for r in rows})!=EXPECTED_ROWS: raise SystemExit('Input is not the sealed 155-row catalogue')
    out=[]
    for r in rows:
        values=[]
        for name,fn in [('unit_level',unit_level),('production_period',production_period),('subject_cluster',subject_cluster),('commercial_or_institutional',formation),('circulation_mode',circulation),('count_namespace',count_namespace),('historical_actor_role',actor_roles)]:
            value,conf=fn(r); values.append((name,value,conf))
        low=[n for n,_,c in values if c=='low']; med=[n for n,_,c in values if c=='medium']; review='REVIEW' if low else ('CHECK' if len(med)>=4 else '')
        row={k:r[k] for k in ['entry_id','country','institution_current','collection_title_or_search_entry','date_range','subject_scope','stated_count','relationship_phrase','physical_structure','source_url']}
        row.update({n:v for n,v,_ in values}); row['analysis_review']=review; row['analysis_basis']=f"Derived only from frozen catalogue wording. Low-confidence fields: {', '.join(low) if low else 'none'}. Medium-confidence fields: {', '.join(med) if med else 'none'}."; out.append(row)
    args.output.parent.mkdir(parents=True,exist_ok=True); fields=list(out[0])
    with args.output.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n'); w.writeheader(); w.writerows(out)
    print(f'Wrote {len(out)} derived rows to {args.output}')

if __name__=='__main__': main()
