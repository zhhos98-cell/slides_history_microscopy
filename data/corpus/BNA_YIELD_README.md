# BNA compact publication layer

The canonical BNA master contains 9,365 article-level records. The compact public layer does not duplicate their article payloads or OCR. It publishes all 43 query-yield rows (`BNA_QUERY_YIELD_V4.json`), all 71 year-yield rows (`BNA_YEAR_YIELD_V4.json`), all 930 derived event clusters in five compact chunks, and all 995 newspaper-yield rows in five compact chunks. `BNA_DERIVED_INDEX_V5.json` maps the complete derived tables.

The event-cluster compaction removes only repeated explanatory prose: standard cluster basis and manual-review language are stored once per chunk. Cluster IDs, type, record count, representative record ID and exceptional basis are retained. Newspaper rows retain title and A/B/C/X counts.

This keeps the derived BNA research layer available while leaving the 9,365 article-level payloads/raw OCR in the fingerprinted canonical master.
