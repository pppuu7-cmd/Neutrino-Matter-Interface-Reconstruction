# NMIR iteration 0089e-r1 — G9 mesh-free replica infrastructure timeout

Date: 2026-09-08
Parent prereg: `research/prereg/0089e_g9_mesh_free_narrow_preimage_replica.md`
Frozen prereg commit: `da8e7c5664cf0980b3490926036231bea9270fcb`
Scientific classification: **not reached**
Infrastructure classification: **`INFRASTRUCTURE_FAIL_G9_0089E`**

## Scope
This record preserves the first hosted execution of the frozen 0089e mesh-free high-precision replica. It does not change, reinterpret, or weaken any H0-H4 scientific criterion from the parent preregistration.

## Exact hosted provenance
- implementation commit: `35f47fa28f949ccfaaa2cef044b28f4bcc60e79f`
- dedicated tests commit: `84106cd5d8843641618897c76abe9c7fea9a62de`
- workflow/head commit: `23a6d5b247bac7d9a923473d7a83d976902f69cf`
- run/job: `34222930733 / 102050078006`
- workflow conclusion: `cancelled`
- dedicated regression tests: `4 passed in 0.15s`
- scientific benchmark step: cancelled by the workflow timeout before a result JSON was produced
- artifact upload: failed because `g9_0089e_result.json` did not exist
- artifacts returned by the run: none
- artifact ID: none
- artifact ZIP SHA256: none
- inner JSON SHA256: none

## Raw-log classification
The raw job log shows the exact frozen scientific command started at 2026-09-08T11:52:03Z and was cancelled at 2026-09-08T12:37:14Z. The run therefore terminated at the previous `timeout-minutes: 45` boundary while the high-precision replica was still executing. H0 regression tests had already passed, but no H1-H4 machine-readable result was emitted.

Under the prospectively frozen taxonomy, runtime failure before scientific classification is `INFRASTRUCTURE_FAIL_G9_0089E`. It is **not** `BLOCKED_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`, **not** `SCIENTIFIC_FAIL_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`, and provides no evidence for PASS.

## Infrastructure-only continuation
No scientific formula, source, precision, branch partition, receiver radius, tolerance, PASS/BLOCKED/FAIL threshold, or next-science consequence was changed after this result. The hosted workflow timeout alone was extended from 45 to 180 minutes at commit `466f6fee04f6052e4c758cb613290f33610373e8` so the identical frozen calculation can complete. That push starts a new candidate run; it must be consumed from raw log and independently verified artifact before any scientific classification.

## Guards retained
- 0089d remains immutably BLOCKED.
- No result-selected precision or spatial refinement is allowed.
- No finite-source, alignment, duty-cycle, persistent-source, interaction, detector, neutrino-energy, or BSM calculation is authorized by this infrastructure record.
