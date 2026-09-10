# NMIR v2 0105a6q4ft — Suh 2025 manifest transport diagnostic

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`

## Frozen scope

Transport-only diagnostic under preregistration commit `df83de59bf8cb66fcfe8009f3228f2b3a5b78174`. No dissertation PDF was downloaded or inspected; no PDF text was parsed; no likelihood, pseudo-data, systematic Monte Carlo, or observed BSM residual was evaluated.

## Hosted execution

- execution head: `30a0f99c618ab587ad99a78388fd7e4f700dc13a`
- run: `34539331035`
- job: `103078170619`
- artifact: `10176640004`, `nmir-v2-0105a6q4ft-suh-2025-manifest-transport-diagnostic`
- provider artifact digest: `sha256:e627bfb6daedc66dc2ad68bf054cb42116b5452b654d44819271431a58e651ed`
- independently downloaded ZIP SHA256: `e627bfb6daedc66dc2ad68bf054cb42116b5452b654d44819271431a58e651ed`
- inner `result.json` SHA256: `33c062746f62133a8e10636e9b5947dd6a6f611158777bbaa4515e94331a8e44`

## Frozen endpoint diagnostic

1. `https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html`
   - HTTP 200
   - final URL unchanged
   - bytes: 23370
   - content type: `text/html; charset=UTF-8`
   - payload SHA256: `f1c245e9675c1a533bc9ad03ca928820499381d576c5f6fefee59c33b91d7488`

2. Frozen ScholarWorks Discover URL
   - HTTP 404 / `HTTPError`
   - bytes: 297612
   - content type: `text/html; charset=utf-8`
   - payload SHA256: `1b766356727364228284e95a142b30b469c721bb50adb12f62463c992df36c1b`

## Classification

`BLOCKED_0105A6Q4FT_FROZEN_ENDPOINT_TRANSPORT_DIAGNOSTIC_IDENTIFIED`

The q4f failure is localized to the frozen ScholarWorks Discover endpoint. The CEEM institutional metadata endpoint is transport-valid. This is an infrastructure/authority transport result, not a Standard-Model scientific FAIL and not BSM evidence.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`

## Exact next allowed step

Only a new prospectively frozen transport-repaired q4f manifest gate may replace the broken ScholarWorks endpoint with a provenance-qualified official Indiana University canonical metadata/landing endpoint while retaining the already frozen author/title/year/institutional identity criteria. The repair must not inspect dissertation PDF content and must not alter count-law/scientific criteria.
