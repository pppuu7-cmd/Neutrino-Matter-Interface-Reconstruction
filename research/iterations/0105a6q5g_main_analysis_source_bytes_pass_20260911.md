# 0105a6q5g — validated main Analysis-A arXiv source acquisition

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5G`
Classification: `PASS_0105A6Q5G_MAIN_ANALYSIS_ARXIV_SOURCE_BYTES_ACQUIRED_NONDISCOVERY`
Scope: source-byte provenance only; NONDISCOVERY.

## Prospective chain

- parent q5f2 record: `81047ef0048a55f64aa1aff9ce4b14a7ce51b453`
- preregistration: `e88ced9395b09c99b9634f39b8c11df5133fe754`
- implementation: `5822c265594c11b2b1d5d4be591f3e2c222ff922`
- guards: `29f0a346dea604f31bc1233dd0ae86da69294b35`
- execution head: `d89ad4d51bd17198a9aac332e2a1055b279ca3f3`

## Hosted validation

- run/job/artifact: `34551847964/103116224715/10181098335`
- dedicated guards: `4 passed`
- provider artifact ZIP SHA256: `1dfb90e4cab401937cd0ae151a13c6829e2d9ba61d9315088c308add233c3e8b`
- independently downloaded ZIP SHA256: `1dfb90e4cab401937cd0ae151a13c6829e2d9ba61d9315088c308add233c3e8b`
- independent inner `result.json` SHA256: `6e517fd9a20445011f944abd24579fda117096891e1dddf2178481d2a5ad8ccb`

Frozen source identity established for `arXiv:2003.10630`:

- HTTP 200
- final URL `https://arxiv.org/src/2003.10630`
- content type `application/gzip`
- bytes `446096`
- MD5 `3fc8333abf50dcb49683bc079fd6d7bb`
- SHA256 `2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114`

The hosted result explicitly records `archive_opened=false`, `member_listed=false`, and `source_text_inspected=false`. No source member contents were inspected. No likelihood, pseudo-data, systematic Monte Carlo, nuisance profiling, observed residual or BSM scan was executed.

Green workflow success was not treated as scientific PASS; raw job and artifact bytes were independently validated against the preregistered gate.

`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact continuation rule

PASS permits only a separately prospectively frozen archive-structure/member-name locator bound to exact source SHA256 `2edeb3dcc3df99de575c8b2091f48099a7538eedf9f382996d943c7fbe7e2114` and byte count `446096`. Source-member payloads must remain unread until a later semantic gate is prospectively frozen over the complete deterministic candidate set.