# NMIR preregistration 0086 — De Romeri updated COHERENT combined source-asset authority

Date frozen: 2026-09-08
Parent authority: 0074c `BLOCKED_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY`; current F8 maturity includes 0085 `PASS_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE`.

## Scientific question
Can the exact primary source package for De Romeri et al., arXiv `2211.11905v2` / JHEP 04 (2023) 035, be acquired and frozen reproducibly as a source-native asset suitable for a later prospectively registered audit of an updated CsI+LAr combined-likelihood numerical benchmark?

This gate is provenance-only. It does not inspect or classify numerical physics results.

## Frozen source
- Primary source identity: V. De Romeri et al., arXiv `2211.11905v2`.
- Acquisition URL: `https://export.arxiv.org/e-print/2211.11905v2`.
- Permitted operations: download bytes; compute SHA256 and byte size; archive-type detection; safe extraction; deterministic inventory of member names, sizes, and per-member SHA256; identify source-native text/TeX files by extension only.
- Forbidden in 0086: reading or searching scientific text; extracting numerical likelihood values; interpreting figures/tables; OCR/raster/manual reading; evaluating B-L points; constructing a likelihood or contour.

## PASS criterion
`PASS_DEROMERI_COHERENT_UPDATED_SOURCE_ASSET_AUTHORITY` requires all of:
1. exact versioned archive downloads successfully from the frozen URL;
2. archive SHA256 and size are recorded;
3. safe extraction succeeds with no path traversal, duplicate-member ambiguity, or unsupported archive corruption;
4. every extracted regular file has deterministic relative path, byte size, and SHA256 recorded;
5. at least one source-native `.tex` or equivalent text source file exists;
6. two independent inventory passes over the same downloaded bytes produce identical archive and member hashes.

## Failure classes
- Network/download/extraction/parser/serialization problem -> `INFRASTRUCTURE_FAIL`, never scientific FAIL.
- Hash or inventory instability on identical bytes -> `INFRASTRUCTURE_FAIL_REPRODUCIBILITY`.
- Valid archive but no source-native text/TeX suitable for later source-text audit -> `BLOCKED_DEROMERI_SOURCE_TEXT_ASSET_AUTHORITY`.

## Guards
- No scientific text search or numerical result inspection in this gate.
- No PDF figure reading, OCR, raster extraction, or manual digitization.
- No use of publisher HTML as substitute for exact arXiv source bytes.
- No likelihood implementation and no B-L scan.
- A PASS here authorizes only a separate preregistered source-text benchmark-authority audit; it does not reopen 0074c by itself.

## Frozen next action
If PASS, record the exact archive/member hashes and prospectively preregister 0086a before inspecting source-native text for a non-circular numerical combined-likelihood benchmark. If BLOCKED or infrastructure-failed, preserve 0074c unchanged.
