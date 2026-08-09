# Global microscope-slide survey priority rules

This project does not rank microscope-slide pages by institutional fame or by page count. It ranks them by evidential usefulness for collection-scale history.

## Promotion logic

A survey entry is stronger when it can preserve several of these layers at once:

1. collection or person name;
2. stated count or count-like phrase;
3. relationship phrase preserved from the source, such as `held by`, `donated by`, `prepared by`, `mounted by`, `belonging to`, `used by`, or `digitised by`;
4. physical structure, such as cabinet, drawer, box, tray, set, accession batch, storage structure, label, or barcode workflow;
5. event-side hooks, such as society reports, newspapers, catalogues, dealer records, accession registers, conservation files, movement records, or exhibition checklists.

Single item records may be thin. They become useful when they support a collection, person, batch, label, cabinet, register, damage, conservation, or circulation question.

## Generated priority queue

`python scripts/validate_survey.py` writes:

- `outputs/run_report.md`
- `outputs/coverage_summary.json`
- `outputs/priority_queue.md`

The priority queue excludes:

- D-grade method-only rows;
- blocked rows;
- rows with an explicit `exclude_reason`.

The score is intentionally simple and auditable. A high score does not mean the historical case is closed. It means the row should be considered early for either a metadata harvest or a targeted manual check.

## Guardrails

Do not collapse relationship phrases into ownership. `belonging to`, `from the collection of`, `held by`, `prepared by`, `mounted by`, `donated by`, `used by`, and `digitised by` are separate source claims.

Do not promote lantern slides, photographic slides, glass plate negatives, or 35mm slides into the microscope-slide dataset unless a source explicitly makes a microscope-slide connection.

Do not treat method-only infrastructure rows as physical collection evidence. A `GLOBAL` row normally remains D-grade unless it proves a specific collection.
