# NMIR iteration 0072d — Wagner blue-chain identity result

Date: 2026-09-07
Classification: **SCIENTIFIC_FAIL_WAGNER_BLUE_IDENTITY**

## Authority
Parent 0072c remains immutable as `PARTIAL_PASS_WAGNER_VECTOR_CURVES`.
Prospective identity contract: `research/prereg/0072d_wagner_blue_identity_resolution.md`, commit `2014d3d7f8a027fe4065965b6d1a8dc5131e4075`.
Pre-result overlap-logic correction: `research/amendments/0072d_overlap_logic_correction.md`, commit `73fcfa69c0b5ab28098f85e55c739cf6bb0980cd`.
Deterministic resolver: commit `70f0ceef559c6fa67b422e3a6a413b2346f642ae`.
Hosted run/job: `34112933849 / 101713070731`.
Artifact: `10015072386`, digest `sha256:ce4db4c90c234e79b60d019f3e8b9326bf81860a9ec365e75400fd40d58ea8ce`.
Persisted result: `data/wagner_blue_identity_0072d.json`, bot commit `590ed0850984446f9cecb0e3d6e05a19cda95d46`.

## Result
The primary EPS contains four connected blue paths, consistent in count with the visual fact that Figure 6 prints one EW99, one EW and two disconnected EW94 trace components. However, the prospectively frozen pairwise-order identity test fails scientifically: the relevant curves cross rather than retaining a source-unique global vertical order.

Frozen pairwise diagnostics include:
- chain 0 vs 1: chain 1 is consistently above chain 0 on EPS-x `[2.349,3.678]`;
- chain 0 vs 2: chain 2 is consistently above chain 0 on `[4.348,6.680]`;
- chain 2 vs 3: chain 3 is consistently above chain 2 on `[4.348,5.361]`;
- chain 1 vs 2: disconnected;
- **chain 0 vs 3 crosses** on `[2.154,5.361]`, with `y0-y3` spanning `-2.925 ... +1.15` EPS;
- **chain 1 vs 3 crosses** on `[2.349,3.678]`, with `y1-y3` spanning `-0.6579787 ... +0.9835333` EPS.

Therefore there is no unique top candidate and no unique bottom candidate under the frozen source-order rule. The semantic assignments `EW`, `EW94`, `EW99` are not promoted from this route.

## What remains valid
This FAIL does **not** invalidate:
- 0072b `PASS_WAGNER_AXIS_CALIBRATION`;
- the four already-unambiguous primary curves materialized by 0072c: Princeton, Moscow, LLR inverse-square/precession and LLR differential-acceleration;
- the physical coordinate transform and primary EPS provenance.

No post-hoc curve-shape or hand-label proximity criterion is introduced to rescue the blue identities. 0072c remains a partial primary Wagner materialization.

## Exact next action
Follow the frozen 0072/0072d decision tree: switch to the independent same-convention direct-detection route using De Romeri–Papoulias–Ternes (JHEP 05 (2024) 165, arXiv:2402.05506) with primary PandaX-4T solar-neutrino electron-recoil information. Prospectively freeze the exact experimental bins/exposure/background treatment, B-L scattering convention, solar flux and likelihood/statistic before reproduction. No raster/manual contour digitization and no B-L NMIR enhancement scan are permitted.

## Readiness
No authoritative readiness increase is claimed solely from this negative identity gate. `NMIR_READINESS` remains 89% pending recovery/funnel reconciliation; the negative result narrows the permitted route without closing global 0072.
