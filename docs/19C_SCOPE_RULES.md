# Nineteenth-century scope rule

The global survey discovers present-day institutional holdings, finding aids, databases, digitisation projects, collection histories, donation records, specialist catalogues, and search-engine leads. The historical object of study is narrower.

## Core temporal rule

A survey entry enters the active historical census only when the surviving slide collection, batch, set, object, or provenance chain has explicit evidence that at least one historically meaningful node falls within **1800-1899**.

Qualifying nineteenth-century nodes include:

- slide preparation or mounting;
- collecting or acquisition;
- ownership / belonging / collection attribution;
- sale, exchange, gift, donation, loan, posting, distribution, or transfer;
- use in teaching, research, demonstration, exhibition, or publication;
- formation of a named collection, cabinet, drawer sequence, box, set, or accession batch.

A modern museum page or digitisation project may be the source used to establish the historical collection. The publication date of the web page is therefore not a scope criterion.

## Scope statuses

- `CORE_19C`: explicit evidence ties the object, collection, or provenance chain to 1800-1899.
- `POSSIBLE_19C`: collection may contain nineteenth-century material, but the current survey row does not yet prove the connection. Keep for review; do not harvest automatically.
- `MODERN_COMPARATOR`: useful for digitisation, collection-management, media, or metadata method, but the material itself is modern. Exclude from the historical harvest queue.
- `OUT_OF_SCOPE`: explicit evidence places the relevant collection/material outside 1800-1899 and no nineteenth-century node has been established. Exclude from the historical harvest queue.

## Conservative default

Uncertainty never promotes a record. If nineteenth-century evidence is absent or ambiguous, the default is `POSSIBLE_19C`, not `CORE_19C`.

Counts also inherit this rule. A present-day total may describe a mixed collection that includes nineteenth-century material. Such a total is not automatically a nineteenth-century slide count. Preserve the present-day aggregate as source evidence, then isolate the nineteenth-century subset where possible.

A twentieth-century collector may have assembled nineteenth-century slides. The later collector/custody event and earlier slide manufacture are separate temporal layers. Likewise, a present museum may combine formerly separate nineteenth-century collections; current sequence and former institutional custody must both be retained.

## Search and source rule

Search engines may be used for high-recall discovery, especially because historical slides are often documented in departmental pages, collection stories, grant records, old catalogues, biographies, or digitisation notes rather than museum navigation. A candidate is promoted only after verification against an institutional, archival, catalogue, scholarly collection guide, or otherwise authoritative source.

Maker-first and serial-set searches are encouraged. Published slide collections/exsiccatae must preserve `set / part / serial number / copy institution` so replicate collections can be modelled as distinct physical copies linked by a common edition/serial identity.

## Source and relation guards

Current institutional custody does not imply nineteenth-century ownership. Preserve relationship phrases such as `belonging to`, `from the collection of`, `prepared by`, `mounted by`, `collected by`, `sold by`, `distributed by`, `donated by`, `lent by`, `held by`, `received by`, `exchanged by`, and `transferred from` as distinct claims.

Likewise, a modern donation of nineteenth-century slides is a modern custody event attached to nineteenth-century objects. It does not move the slide itself out of the historical scope.

## Current repository milestone

The discovery layer currently contains **192 survey entries**. Of these, **41 entries in strict batches `07K` through `07R` were added after the nineteenth-century lock and already carry explicit 1800-1899 evidence in their survey rows**. Earlier discovery entries remain subject to the scope audit; they are not assumed to be historical merely because they concern microscope slides.
