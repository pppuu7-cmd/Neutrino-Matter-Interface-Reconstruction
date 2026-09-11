# 0105a6q5a2 — validated Argon official-release structural provenance binding

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q5A2`
Classification: `PASS_0105A6Q5A2_ARGON_OFFICIAL_RELEASE_STRUCTURAL_PROVENANCE_BOUND_NONDISCOVERY`
Scope: authority/provenance only; NONDISCOVERY.

## Prospective chain

- q5a historical BLOCKED record: `d7c888741d0c7c807c5cdfa8c6083593ac8a1b47`
- q5a1 validated structural diagnostic PASS record: `ae59a47532ca0411e315a00a33494a69a5336e70`
- q5a2 preregistration: `2897bd6c6d55f312dd4ab07cd528d4f3a3fa33fa`
- implementation: `7304a8cf1b819ee3671ad838f771d4650439033a`
- guards: `c7d85b87428cc3d853f3d71d1d38d5e02061ce85`
- execution head: `e1d8548cff358de86e2b0f00590fead3bf27c0db`

## Hosted execution and byte validation

- run: `34548098074`
- job: `103104972721`
- artifact: `10179757861`, `nmir-v2-0105a6q5a2-argon-structural-provenance`
- dedicated guards: `6 passed`
- provider artifact ZIP SHA256: `0fd133a8664e2e4dffacb93f76bc9b6456da776ba12917fcb1f1886dd72611a5`
- independently downloaded ZIP SHA256: `0fd133a8664e2e4dffacb93f76bc9b6456da776ba12917fcb1f1886dd72611a5`
- independent inner `result.json` SHA256: `46a2cc9b0fe6f8416dcde20203cc9535599cb43d9cf215cb2b07c9e7b1f9f339`

Green CI was not treated as scientific PASS; the raw result/artifact was checked against the frozen q5a2 gate.

## Frozen predicate result

All four required authority predicates passed:

- immutable local 0105a3 binding: PASS;
- ORNL Data Releases structural route: PASS with exactly one Zenodo-record-3903810 href match;
- exact Zenodo 3903810 metadata predicate: PASS;
- exact arXiv 2006.12659 id/title predicate: PASS.

Thus the public provenance chain `COHERENT/ORNL Data Releases -> Zenodo 3903810 -> arXiv 2006.12659`, bound to the immutable 0105a3 byte lock, is now closed under the prospectively frozen structural-href criterion. Historical q5a remains BLOCKED under its own stronger visible-text predicate and is not rewritten.

No release file bytes were downloaded or re-hashed by q5a2; no scientific release content was inspected; no pseudo-data, likelihood, systematics fit or observed residual was evaluated.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`

## Exact next allowed action

q5a2 PASS permits only a new prospectively frozen q5b release-file locator/semantic-authority step. q5b must specify its filename/metadata selection rules before any new file content inspection. It does not permit observed BSM residual analysis.