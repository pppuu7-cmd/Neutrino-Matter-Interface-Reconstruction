# 0105a4c — archival-vs-original checksum block

Status: `BLOCKED_0105A4C_DATAVERSE_TABULAR_REPRESENTATION_MISMATCH`

This is an authority-representation block, not a neutrino-physics FAIL.

## Hosted execution

- workflow run: `34427503778`
- job: `102715752890`
- head SHA: `e4548a10437f52a653df3d0dbdbacf15cf0e6ed1`
- deterministic authority/byte-lock tests: `7 passed`
- live B4RITM metadata exact-match: true
- exact file count: 11
- all downloaded byte sizes matched the frozen Dataverse `filesize`
- SHA256 was computed for every downloaded representation
- provider MD5 comparison failed for Dataverse-ingested tabular files
- `example.ipynb` and `readme.md` provider MD5 values matched exactly
- no scientific payload parsing occurred
- observed residual remained locked

The run therefore correctly returned:

`BLOCKED_0105A4C_DEEPCORE_B4RITM_BYTE_LOCK_INCOMPLETE`.

## Root cause

The raw 0105a4 Dataverse metadata explicitly marks the affected `.tab` assets as `tabularData=true` and records a saved original CSV representation, e.g. for `data.tab`:

- archival name: `data.tab`
- archival content type: `text/tab-separated-values`
- `originalFileName`: `data.csv`
- `originalFileFormat`: `text/csv`
- `originalFileSize`: `4091`
- provider MD5: `59d03738e7fe61fe06a06b2140708373`

The 0105a4c route `/api/access/datafile/<id>` requested Dataverse's default archival tabular representation. The frozen provider checksum corresponds to the saved original representation, so checksum equality was not a valid predicate for the default archival bytes.

This diagnosis is consistent across the run: the non-tabular notebook/readme matched provider MD5, while the ingested tabular assets did not.

## Immutable disposition

Do not change the executed 0105a4c PASS contract or reinterpret the mismatched MD5 as acceptable after the fact. Preserve this run as a useful provenance failure.

A new prospective gate may use the Dataverse-documented `format=original` access route for `tabularData=true` assets, while keeping the ordinary route for non-tabular assets. That new gate must freeze the original filenames/formats/sizes and provider checksums before executing.

Observed BSM residual permission remains `0%`.
