# NMIR iteration 0029 — transparent-Sun focal benchmark and finite-source control

Date: 2026-09-06
Classification: **G9_FOCAL_SCALE_PASS / FINITE_SOURCE_LIOUVILLE_PASS / G9 overall PARTIAL**

## Funnel target
Highest-value OPEN funnel gate from `research/NMIR_FUNNEL.md`: G9 gravitational focusing, because it changes incident phase-space geometry/flux rather than attempting another material response enhancement.

## Prospective contract
`research/gravity_focusing_prereg.md`, commit `30f93fa94267fafdc1ca14d05b30f97b6af471ee`, frozen before implementation.

Primary authority: Patla & Nemiroff, ApJ 685 (2008) 1297, arXiv:0711.4811. They report a transparent-Sun minimum focal distance `23.5 +/- 0.1 AU` and quote an independent rounded interior check using projected enclosed mass `0.0137 M_sun` at impact radius `0.024 R_sun`.

## Implementation
- `src/nmir/gravity_focusing.py` commit `1afc10d2c6272a55ef007506113b1aed5ac1a364`:
  - transparent-Sun rounded interior focal check;
  - exact on-axis uniform finite-source disk magnification `mu=sqrt(rho^2+4)/rho`;
  - numerical disk-average cross-check;
  - explicit Liouville/surface-brightness flux-area control.
- regression tests commit `5d339d180441458c0f8e137382e0ece6eba2de0e`.

## Numerical result
Using current SI solar constants and the paper's rounded `0.024 R_sun`, `0.0137 M_sun` values gives

`F = 23.0291102335 AU`,

which is `-2.004%` from 23.5 AU and therefore inside the prospectively frozen 3% tolerance appropriate to the rounded quoted inputs.

The finite-source point-lens control removes the point-caustic divergence exactly. For source angular radius ratio `rho`,

`mu_fs(rho)=sqrt(rho^2+4)/rho`,

so any nonzero physical source size has finite magnification. This is a control theorem for point-lens finite-source regularization and Liouville bookkeeping, not yet a full transparent-Sun extended-lens magnification.

## Hosted validation
Baseline CI run `34040499051`, job `101506252362`, head `5d339d180441458c0f8e137382e0ece6eba2de0e` completed SUCCESS. Raw job log was inspected before classification:
- `141 passed in 1.29s`;
- baseline physics executable SUCCESS;
- no physics-threshold changes after execution.

Therefore the preregistered rounded focal-scale reproduction and finite-source/Liouville control are scientific PASS subgates.

## Scientific scope
- The `23.5 AU` scale applies to distant radiation traversing the Sun, including suitable neutrinos; it does not focus the Sun's own neutrinos with the Sun as lens.
- Liouville conservation forbids assigning a surface-brightness increase; total flux gain comes from increased image solid angle / ray redistribution.
- No focusing gain is multiplied by Li-7 capture or any other NMIR gain at this stage.
- The point-lens finite-source formula is a regularization/control benchmark; the physically required extended transparent-Sun finite-source magnification remains OPEN.

## Exact next gate
Build an extended transparent-Sun projected-mass lens using primary SSM density/profile data and compute receiver-integrated finite-source magnification versus source angular size and observer distance. Only after a source-specific finite `mu(E)` survives Liouville/geometry checks may it enter F9 composition with capture.

Readiness recommendation: `NMIR_READINESS: 55%`, +1 only for the prospectively frozen, hosted/raw-inspected G9 focal-scale + finite-source/Liouville subgate; G9 remains globally open.
