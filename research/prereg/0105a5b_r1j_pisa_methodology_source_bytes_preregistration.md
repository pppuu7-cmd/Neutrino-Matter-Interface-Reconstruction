# NMIR v2 0105a5b-R1j — cited IceCube PISA methodology source-byte acquisition

Date frozen: 2026-09-11
Parent observation: validated R1i1 found that IceCube analysis `arXiv:2304.12236` explicitly cites `arXiv:1803.05390` as the PISA computational-techniques reference, while naming no frozen PISA tag.

## Purpose
Acquire and byte-lock the exact source bundle of the directly cited IceCube PISA methodology publication before inspecting any member names or source text. This is a provenance-only acquisition gate.

## Frozen source
Only:
`https://export.arxiv.org/e-print/1803.05390`

No HTML abstract page, PDF, repository README, PISA source code/tree/blob/archive, GitHub issue/PR, documentation, package/container, or other publication may be requested.

## Frozen procedure
Perform one HTTP GET with a fixed user agent. Record HTTP status, final URL, Content-Type, byte count, MD5, and SHA256 of the opaque response body. Do not open/decompress/list the archive; do not search member names or content.

## Classification
- `PASS_0105A5B_R1J_PISA_METHODOLOGY_SOURCE_BYTES_ACQUIRED_NONDISCOVERY` iff HTTP 200 and body length > 0.
- transport/HTTP failure or empty body: `INFRASTRUCTURE_FAIL_0105A5B_R1J`.

A PASS permits only a separately preregistered archive-structure locator. It does not permit source-text semantic inspection, PISA version selection, PISA implementation inspection, standard-3nu execution, systematics MC, observed residuals, or BSM scans.

Hard prohibitions: `archive_opened=false`, `member_listed=false`, `source_text_inspected=false`, `pisa_repository_content_inspected=false`, `standard_3nu_executed=false`, `systematic_monte_carlo_executed=false`, `observed_bsm_residual_inspected=false`.

`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
