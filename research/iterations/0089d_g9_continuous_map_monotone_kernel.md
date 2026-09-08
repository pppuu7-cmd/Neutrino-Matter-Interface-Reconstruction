# NMIR iteration 0089d — G9 continuous-map monotone-segment radial kernel

Date: 2026-09-08
Classification: **`BLOCKED_G9_CONTINUOUS_MAP_MONOTONE_KERNEL`**
NMIR_READINESS: **98%** (unchanged)

## Frozen authority
Parent prereg: `research/prereg/0089d_g9_continuous_map_monotone_kernel.md`, commit **`8eab0935d54cb930495b55cbc3025225729f109c`**.
Result-independent bulk-evaluator amendment: `research/prereg/0089d_amendment_bulk_evaluator.md`, commit **`33f7b72b7429993b09321cd5674fa1eff3219812`**.
Upstream turning-root authority: 0089c `PASS_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION`, immutable commit `e8fc4e6856d6326e6c273a96cb46f6b660467d96`.
Model-S source commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`, exact git blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`.

Scope remained radial accepted-preimage geometry only. `K=A_acc/(pi r^2)` is a geometry diagnostic only and is not interaction gain, detector gain, neutrino-energy gain, finite-source gain, alignment gain, or persistent-source utility.

## Implementation lineage
- monotone-kernel primitives: `db501a87920dcb1940ce76f8271fe553cb588aa4`;
- benchmark: `4d30cd8a6e8dfe76441666fb0f1a204da72801a3`;
- dedicated tests: `4b1feef7ce623995a20ee37cd6698895fd11207b`;
- initial hosted workflow: `87a9acf95a5c138746c19cd30cd24d453cfb18a8`;
- residual-aware bisection implementation: `ec05400cef1ddf770e47730d5b8a73e6649307e4`;
- frozen B0 mass/focal bulk conformance preflight: `f90ae6db81b62fc048a2a8edd6d577be361379e7`;
- bisection stagnation bug fix: `03f1308b7e2bb62cf68b9033e1f394374cbad642`;
- workflow requiring B0 before science: `975676cf5a7197c0685ea2d1306a5fdaa5a3f642`;
- exact frozen-V3 contract wrapper: `00831800b842fa7c50a92afa2523db518f4ae7e7`;
- authoritative hosted head: **`2e49e9c196cc8560cdc1b68f696172b5849ee6e7`**.

## Non-authoritative candidates
Several hosted candidates were explicitly rejected before choosing the final scientific classification.

1. Run `34217419249`, job `102032361885`: green, but the B0 amendment had not yet been fully implemented (focal-only conformance, no required mass check). Its scientific-looking payload is non-authoritative.
2. Run `34217644369`, job `102033088448`: implementation failure in the bisection loop; dedicated tests failed before the benchmark. No scientific result.
3. Run `34217735166`, job `102033378301`: green but still lacked the required mass half of B0. Non-authoritative.
4. Run `34217895934`, job `102033892242`: B0 and tests passed, but implementation contained an extra, non-preregistered zero-tolerance assertion `K_global >= exact_one_ring_mu`. The frozen V3 contract requires structural inherited-one-ring containment and reproduction of its accepted area within 0.5%, not that extra comparison. Therefore the run-4 `SCIENTIFIC_FAIL` payload is non-authoritative. The extra assertion was removed by a contract-conformance wrapper without changing any preregistered tolerance or criterion.

No result from these candidates was used to weaken the parent gate.

## Authoritative hosted execution
Run/job: **`34218369356 / 102035420870`**
Hosted head: **`2e49e9c196cc8560cdc1b68f696172b5849ee6e7`**
GitHub conclusion: success (infrastructure only; not used as scientific classification)
Dedicated tests: **`4 passed in 0.04s`**
Artifact: **`10052800239`**
Artifact size: 564 bytes
Raw JSON SHA256: **`72de2daaf4118cf9869b3e4a271a8c99bdd718471d8c535e20c71f336fc703f9`**
Artifact ZIP SHA256: **`72d18d3cae44d44a6194ed67940ee4e4b71973fedcdb349fc479f899cb397905`**

Both hashes were independently re-computed after downloading the hosted artifact and exactly matched the raw Actions log.

## Frozen validation result
B0 bulk/scalar conformance passed before scientific evaluation:
- point count: 79;
- max mass symmetric-relative discrepancy: `5.8129131561973325e-16`;
- max focal symmetric-relative discrepancy: `5.4862457280150332e-16`;
- frozen limit: `2e-11`.

The exact-contract benchmark then returned:

`BLOCKED_G9_CONTINUOUS_MAP_MONOTONE_KERNEL`

with reason:

`fixed indicator replica cannot resolve a finite narrow accepted interval`

and diagnostics:
- max branch-vs-`N=2^19` indicator relative difference: **`1.0`**;
- max `N=2^18`-vs-`N=2^19` indicator relative difference: **`1.0`**.

The parent prereg explicitly states that if a finite accepted preimage interval is too narrow for the globally fixed indicator meshes, the gate is **BLOCKED** and the mesh must not be refined after seeing the result. That exact frozen consequence is applied here.

## Scientific interpretation
0089d does **not** show that the continuous signed-map branch construction is physically false. It shows that the prospectively frozen independent validation route cannot certify the full radial kernel because at least one finite accepted interval is unresolved by the fixed global midpoint meshes.

Therefore:
- 0089c turning-root authority remains PASS;
- 0089d full radial-kernel authority is BLOCKED;
- no result-selected denser indicator grid is allowed inside 0089d;
- no finite-source, positioning, duty-cycle, persistent-source or focusing-utility calculation is authorized by 0089d;
- the diagnostic `K` must not be promoted to a physical gain.

A future G9 attempt, if pursued, must be a new prospectively frozen scientific question using a genuinely independent validation method. It may not retroactively reclassify 0089d.
