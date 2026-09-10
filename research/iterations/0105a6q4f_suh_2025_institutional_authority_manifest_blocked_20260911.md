# 0105a6q4f — validated institutional authority manifest attempt

Date recorded: 2026-09-11

Classification: **`BLOCKED_0105A6Q4F_INSTITUTIONAL_METADATA_IDENTITY_FAILURE`**.

This is a fail-closed authority/transport result, not a Standard-Model scientific FAIL and not BSM evidence. No dissertation PDF was downloaded or inspected.

## Provenance

- preregistration commit: `309aa7d389b541fb6818a56aec67f44cee65f50d`
- implementation commit: `70750d341903f4161aaa9e9b2faea0c316ee9632`
- guards commit: `021d4c640aef5d2bba9e6a4c87d833c189c3f152`
- execution head: `c555adfee134a0a1c610eeb5d517a5efc6519750`
- run/job/artifact: `34539208459 / 103077779431 / 10176594931`
- dedicated guards: `4 passed`
- provider artifact digest: `sha256:5397ab6c9e4676138f610bc52770573a1379e0fa23a8cde74af91b18897e6d17`
- independently downloaded ZIP SHA256: `5397ab6c9e4676138f610bc52770573a1379e0fa23a8cde74af91b18897e6d17`
- inner `result.json` SHA256: `4999d18324655199ebb367e054aa092aa190c2bb74ec00d4d46a907368a72719`

Hosted execution terminated on `HTTP Error 404: Not found` and returned the frozen fail-closed class. The current result does not identify which of the two frozen metadata transports produced the 404 because the first implementation intentionally retained only the terminal exception rather than per-endpoint status.

Audit booleans:
- `pdf_downloaded=false`
- `pdf_content_inspected=false`
- `pdftotext_executed=false`
- `pseudo_data_generated=false`
- `likelihood_evaluated=false`
- `observed_bsm_residual_inspected=false`
- `SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION=0%`
- `SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION=0%`
- `OBSERVED_BSM_RESIDUAL_PERMISSION=0%`

## Consequence

q4f remains historically BLOCKED and is not to be reclassified by a retry. A transport-only diagnostic may prospectively probe the exact already-frozen CEEM metadata URL and exact already-frozen ScholarWorks discovery URL independently. Such a diagnostic may record HTTP status/final URL/response hash only and must not inspect dissertation PDF content or modify the scientific/provenance criteria.