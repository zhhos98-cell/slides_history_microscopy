# Naples 1880 catalogue → UK circulation crosswalk — v1

Date: 2026-08-09

This is a **derived analysis layer** over the sealed 155-row nineteenth-century slide catalogue and the parsed Naples 1880 423-offering price catalogue. It does not alter the frozen 155 membership and it does not assert that any British circulation event is the same physical object as the surviving St Andrews material unless a source explicitly closes that identity.

## Source base

The Naples catalogue is the `Preis-Verzeichniss der mikroskopischen Präparate, welche durch die Zoologische Station zu Neapel zu beziehen sind`, in *Mittheilungen aus der Zoologischen Station zu Neapel*, Bd. II. The catalogue text is signed `Neapel, August 1880`. The numbered offering list runs from 1 to 423.

The British side is drawn from the existing UK microscopy corpus, including JRMS, Quekett, the Northern Microscopist/local-society material, *The Midland Naturalist*, and the BNA master. Newspaper and society records are treated as separate events unless physical identity is explicitly established.

## Match levels

- `DIRECT_CATALOGUE_IDENTITY`: the British text explicitly discusses the same Naples priced catalogue.
- `ITEM_LEVEL_PARTIAL_9_EXACT_3_BOUNDED`: a British physical shipment supplies enough item detail to map most named slides to individual catalogue offerings while leaving explicitly bounded ambiguities.
- `FAMILY_STRONG`: taxon/stage language aligns closely with a bounded catalogue block, but the British text supplies no exact Naples catalogue number.
- `FAMILY_BROAD` / `PROGRAMME_BROAD`: only a broad taxonomic or production-programme correspondence is safe.
- `UNRESOLVED`: Naples provenance is explicit but the British text lacks enough object detail to map to catalogue rows.
- `OFF_CATALOGUE_REWORKING`: Naples supplied biological material subsequently remade into a new slide in Britain; this is not one of the parsed 423 catalogue offerings.

## Item-level breakthrough: RMS, 9 June 1880

The first crosswalk pass initially treated the 9 June 1880 Royal Microscopical Society event only as a twelve-slide shipment. A reverse taxon/preparation scan recovered the detailed exhibit list in the same JRMS issue.

- `R24204`, printed p. 733: the Society records `Zoological Station of Naples—12 slides`, donated by the Station through A. W. Waters; Mr Crisp called special attention to them and they were exhibited under microscopes.
- `R24207`, printed p. 736: the twelve physical slides are named individually.

Comparison with the Naples 1–423 catalogue yields **nine exact/strong item matches and three bounded matches**.

### Exact / strong catalogue matches

- Asterias glacialis — Gastrula → no. **42**.
- Asterias glacialis — formation of mesoderm → no. **43**.
- Echinocardium cordatum — larva → no. **72**; the catalogue adds `3 Tage` while the RMS label omits the age.
- Pyrosoma elegans — young colony → no. **186**.
- Pseudodidemnum Listerianum — ova with embryo → no. **182**.
- Toxopneustes brevispinosus — larva, 3rd day → no. **67**, under the catalogue synonymy `Sphaerechinus granularis (Toxopneustes brevispinosus)`.
- the same, 5th day → no. **68**.
- the same, 15th day → no. **71**.
- Stichopus regalis — ovary → no. **86**, by continuation of the Stichopus block.

### Bounded matches

- Amphioxus lanceolatus → no. **231 or 232** because the RMS label gives the taxon but not `Vorderer Körpertheil` versus `Ganzes Thier`.
- Ascetta bianca → no. **5 or 6** because the RMS label does not say unstained versus stained.
- Asteracanthion glacialis — larva → the Asterias/Asteracanthion developmental block, **43–49**, because the RMS label omits the developmental qualifier.

The row-level mapping is stored in `NAPLES_1880_RMS_12_SLIDES_ITEM_CROSSWALK_V1.csv`.

This is the first defensible **catalogue offering → named British physical slide shipment/exhibition** closure in this Naples pass. It is still only a two-point closure. No source yet establishes that any of these twelve 1880 RMS slides is the same physical object as a surviving St Andrews slide.

## British object/specimen circulation sequence

The bounded pass currently retains **eleven** distinct British object/specimen exhibition or circulation events. These are separate events unless a source closes physical identity.

1. **9 June 1880, RMS** — twelve slides sent/donated through A. W. Waters and exhibited under microscopes. Nine exact/strong catalogue-item matches and three bounded matches are now available.
2. **11 May 1881, RMS** — Mr Crisp exhibited a selection of slides from the Naples Zoological Station. Exact catalogue identity unresolved; bounded adjacency inspection recovered no detailed item list.
3. **10 February 1882, Bolton Microscopical Society** — A. S. Pennington exhibited Naples `zoophytes`, explicitly alongside preparations made by Pennington and Mr Russell. This is only a broad Coelenterata/Hydromedusae catalogue correspondence.
4. **26 April 1882, RMS Conversazione** — C. Baker exhibited preparations from the Zoological Station, Naples (`R26854`, p. 444). The adjacent Curties `Triton` and `Synapta` exhibits are not assigned Naples provenance because the source does not state that relation. No detailed Naples item list was recovered in the bounded adjacency check.
5. **August 1882, Quekett Microscopical Club** — chick-embryo specimens/series are explicitly said to have been prepared by Prof. Fritz Meyer at Naples. These form a strong family-level correspondence with the `Gallus domesticus` developmental block, catalogue nos. **308–368**, but no exact catalogue number is given.
6. **February 1883, Zoological Society** — a *Field* report of 24 February records F. Jeffrey Bell exhibiting a **selection of microscopical preparations received from the Zoological Station at Naples** and making remarks. Number and taxa are unstated.
7. **14 March 1883, RMS** — Bell separately called attention to **nineteen slides** received from the Naples Station and explained their points (`R27785`, p. 318; exhibit list `R27787`, p. 320). Adjacent proceedings do not name the nineteen taxa. This must not be conflated with the February Zoological Society event. Physical overlap between the two Bell exhibitions is possible but **not asserted**.
8. **1883, Birmingham Natural History and Microscopical Society** — a series illustrating the embryology of Asteriadae and Echinidae, prepared at the Naples Station from Mediterranean material, was used in a microscopic demonstration. This aligns strongly with the catalogue's Asteroidea/Echinoidea developmental block, approximately nos. **41–73**, while exact items remain unresolved.
9. **11 November 1884, Birmingham Biological Section** — T. Bolton exhibited **preserved specimens from the zoological stations at Naples**. The source then separately lists mounted specimens from Watson, Ward, C. Vance Smith, Joshua and Vize. The Naples material is therefore retained as `preserved specimens`, not silently recoded as slides.
10. **28 November 1884, Quekett** — Arthur Pennington described one slide bearing ten longitudinal sections of *Cerianthus solitarius*. The specimen came from Naples, but Pennington himself stained, embedded, cut and mounted it. *Cerianthus solitarius* is absent from the parsed 423 offering list. This is therefore an **off-catalogue local reworking** event.
11. **May 1886, RMS second Conversazione** — C. Baker exhibited `Marine Objects from Zoological Station, Naples` (`R31342`, p. 911). The source does not call these slides and gives no item list. The date heading is OCR'd as `bth May, 1886`; likely 5 May, but the exact day is left unasserted until page-image verification.

## Correction to the first pass

The earlier crosswalk treated the *Field*, 24 February 1883, Bell notice as corroboration of the RMS nineteen-slide event. That was incorrect. The newspaper explicitly reports a **Zoological Society** exhibition, while the JRMS nineteen-slide notice belongs to the later **14 March 1883 RMS** meeting. They are now two independent events. The shared actor and Naples provenance are insufficient to assert that the same physical preparations appeared at both meetings.

## Separate reception and method layers

A contemporary British JRMS review directly summarizes the Naples priced catalogue itself and repeats the 423-offering structure, slide format, scientific-value argument, departmental supervision and price framework. This is catalogue reception, not object movement.

Naples methods also circulated independently of Naples objects. JRMS carried the Station's microscopical methods; Northern microscopy periodicals recommended the methods to preparers; Alfred Gibbs Bourne explicitly credited Naples staff for serial-section fastening/mounting practice. Method circulation is therefore analytically separate from physical slide/specimen circulation.

## Main result

The British Naples trail is not a single commercial-sales channel. It includes:

- institutional dispatch through an intermediary;
- named physical slide shipments that can now be mapped back to individual catalogue offerings;
- repeated metropolitan society exhibition across different societies;
- provincial club demonstration;
- preserved-specimen circulation where the source does not establish a slide;
- family-level use of catalogue embryology series;
- local reprocessing of Naples specimens into new British slides;
- parallel circulation of preparation technique.

The most important search consequence is that future corpus expansion should include taxon + preparation-stage combinations and formulations such as `obtained from the Zoological Station at Naples`, `preserved specimens from Naples`, `prepared from Naples specimens`, and local British preparation verbs, not only `slides from Naples` or commercial catalogue language.

No further open-ended Naples discovery is recommended. Future work should remain bounded to explicit Naples events and adjacent item lists or object descriptions.
