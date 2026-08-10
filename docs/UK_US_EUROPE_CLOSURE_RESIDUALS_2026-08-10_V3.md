# UK / US / Europe closure residuals — v3

Date: 2026-08-10

Status: **PUBLIC WEB CLOSURE EXHAUSTED / FOUR EXACT-SOURCE REQUESTS ONLY**

This pass does not add a new regional bibliography module and does not reopen the frozen surviving-object survey. It tests the residual UK / narrowly linked US / already-open European edges against both the public indexed layer and primary files already held locally. That distinction matters here: a relation that looked blocked on the web was actually closable from the project's own Naples source package.

## Elcock: the archive relation is narrower than the working shorthand

The St Andrews record for `ms21974–ms21975`, dated 6–8 March 1884, identifies two autograph letters from Charles Elcock to D'Arcy Wentworth Thompson plus a rubbing. The catalogue explicitly says that references are made to Challenger expedition samples. It also specifies that the main theme of the correspondence is archaeological/antiquarian discussion of a medal allegedly found in a peat bog at Oughterard, County Kildare, with natural-history discussion alongside it.

This changes the operational wording. The item is a direct Elcock–DWT correspondence record containing a Challenger-samples reference; the public catalogue is not a transcript of a Challenger transaction. Who forwarded material, which station/sample was involved, why it was sent and whether it entered Elcock's preparation/commercial system remain inside the manuscript. Further web searching is therefore stopped. The next source is simply the two letters.

## Challenger: architecture closed, full table mechanical

The current NHM dataset page states that the collection holds 4,713 physical bottles, tubes, boxes and slides/derived preparations and exposes a resource with 4,723 records. The existing diagnostic harvest already structures the historical address system, multiple slide/preparation forms, named interventions by Haeckel, Norman and Voigt/Hochgesang, and later specialist-return material. It also preserves the distinction between physical-object count and dataset-record count.

The public portal currently exposes different metadata surfaces for the resource date/format. Those are treated as portal states, not collection-history evidence. The remaining task is mechanical: obtain the current resource binary and read all 4,723 rows without early exit. No additional Challenger discovery search is justified before the file itself is available.

## Balfour / ZEISS: exact lens identity has become an archive problem

ZEISS's official historical production pages expose microscope production/dispatch lists with stand serial number, recipient, delivery place, accessories and dates. They are organized around microscope/stand numbering. Balfour's surviving Whipple objective set carries engraved numbers `573`, `1295`, `710`, `780` and `542` on individual objectives.

The publication side is already strong: Balfour's printed plate captions securely document use of matching Zeiss objective designations. What remains is exact physical-lens identity. The public stand lists do not justify treating the five objective engravings as microscope serials. The next move is a bounded ZEISS Archives query asking whether objective/accessory registers or Balfour/Cambridge dispatch entries preserve those engravings. Generic serial-number searching stops here.

## Norman: public collection-level closure is the terminal claim

St Andrews independently confirms Norman's 1872 catalogue of 2,584 mounts and preserves a Norman group inside the Bell-Pettigrew Zoology microscope-slide collection. The Norman record states that the slides have been left in situ, scattered among the slide sleeves. The parent collection preserves sleeve/pigeon-hole order and acknowledges multiple label layers for mounter, distributor and scientist.

The public Norman group does not expose a usable numerical extent or indexed item list. A row-by-row catalogue-to-object crosswalk therefore cannot be responsibly reconstructed from the website. It should resume only if St Andrews supplies a complete export/item layer with addresses and labels.

## Naples 383: closed from the local primary catalogue

The web route had stalled at the BHL article container, but the project already held the full primary OCR (`mittheilungenaus02staz_djvu.txt`) and structured 423-row catalogue. Printed p.253 reads:

`382. Delphinus phocaena L. Milz`

`383. -- Penis`

`384. -- Hode`

`385. -- Niere`

The ditto marks carry the taxon forward, so catalogue offering **383 is Delphinus phocaena L., Penis**. St Andrews `BPM/1/T8/6` independently has Stazione Zoologica Napoli labels, the left label `Delphinus phocaena`, and the right-label public transcription `Panis 383`. The conjunction of institutional origin, taxon and exact number is sufficient to identify the surviving slide as an extant instance corresponding to catalogue offering 383. The one-letter `Panis` / `Penis` discrepancy is retained rather than corrected silently.

This closes the catalogue-address relation, not the biography of the individual glass slide. The catalogue number is an offering/product address, not a unique physical serial. Manufacture date, preparator, row price and identity with any particular 1880/1881 shipment remain separate claims. Full grading and guards are in `data/analysis/naples_row383_object_catalogue_closure_v4.json`.

## Operational consequence

There are now **zero active public-web discovery targets** in the closure router and **four exact-source requests**: the two Elcock letters; the NHM Challenger resource binary; ZEISS archive guidance for the five Balfour objective engravings; and a St Andrews Norman item export. Naples 383 has moved out of the queue. The backend should resume one of the four only when the exact source arrives or supplies a new bounded identifier. Otherwise the evidentiary gain now lies in analysis and writing from the closed chains, not in extending the database sideways.
