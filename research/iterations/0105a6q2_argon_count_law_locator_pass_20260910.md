# 0105a6q2 — validated Ar pseudo-data count-law locator PASS

Date: 2026-09-10
Classification: **PASS_0105A6Q2_CANDIDATE_PAGES_LOCATED_NONDISCOVERY**

This PASS is a mechanical locator result only. It does not establish a pseudo-data count law and does not authorize Monte Carlo execution.

## Frozen provenance

Preregistration commit: `f1607e221b775feb0fbdb081986fca160d4cd155`.
Repair execution head: `6e1250777d68d10f1f4bafb388f694a92cdaf7a2`.
Hosted run/job: `34516620445 / 103003504742`.
Artifact: `10167939898`, `nmir-v2-0105a6q2-argon-pseudodata-count-law-locator`.
Dedicated guards: `6 passed`.

Provider artifact ZIP SHA256: `0db4fd55a3a3a09110f7f60c2dd388b1d65089b04e549961806fbdd360a286a3`.
Independent downloaded ZIP SHA256: same.
Inner `result.json` SHA256: `c0d913c442130817b7b59e2a785784b40b85e3c501ce9309699a55b0e66e88f3`.

Exact parent q1 result SHA256: `f1d0495fd17ed99fef54086da373a666aa33ef49b3dd61e390297f507b63b201`.
Exact thesis: 34,641,327 bytes, SHA256 `6dd2fde86601dea28d323fc38e289935723ad1bf0f8c5f2dcfd845fe2e6badf9`.
Physical page count: `186`.

## Frozen locator result

The complete mechanically returned candidate-page set is:

`[145, 152, 153]`

- physical page 145: normalized text SHA256 `5a96deead926de7effdc82a6f9d8f842c57ad848ddbfd315b25f9726d1677c42`; categories `IMPLEMENTATION_CONTRACT_CANDIDATE`, `COUNT_GENERATION_CANDIDATE`; L1/L3/L4 true, generation and count token true, L2 false.
- physical page 152: normalized text SHA256 `922b45c4a92f1dc0085b506dcd59e627c394d05d7b70951c6d2bd19bdbb73cea`; category `IMPLEMENTATION_CONTRACT_CANDIDATE`; L1/L3/L4 true, L2 false.
- physical page 153: normalized text SHA256 `96622db01938d38707e3a9945cd34c581ae08debada402ffc434bd5de5adbd52`; category `IMPLEMENTATION_CONTRACT_CANDIDATE`; L1/L3/L4 true, L2 false.

The q2 artifact retained no page text. Page 145 therefore remains semantically uninspected at q2 classification time. Pages 152–153 were already boundedly inspected under q1 and did not close the count law.

## First q2 attempt provenance

Run/job `34516376339 / 103002697161` failed at guards (`1 failed, 5 passed`) before parent recovery or thesis access because a pure predicate test used mixed-case `RooMCStudy/NumEvents` while production input is normalized lowercase. This is retained as **INFRASTRUCTURE/IMPLEMENTATION FAIL**. Repair commit `6e1250777d68d10f1f4bafb388f694a92cdaf7a2` only normalizes predicate input and did not alter the frozen lexical/candidate rules.

## Authorization consequence

The only newly authorized next action is a prospectively frozen semantic audit of the entire fixed candidate set `[145,152,153]`, with the original q1 Q3-P/Q3-F/Q3-O decision rule unchanged.

No pseudo-data generation, likelihood evaluation, systematic Monte Carlo, observed residual, or BSM fit is authorized.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`.