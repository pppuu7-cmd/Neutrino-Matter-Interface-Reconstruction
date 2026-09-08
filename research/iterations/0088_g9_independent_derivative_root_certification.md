# NMIR iteration 0088 — G9 independent derivative/root certification

Date: 2026-09-08

## Classification

`BLOCKED_G9_ROOT_CERTIFICATION`

This is the terminal outcome of the preregistered 0088 numerical route. It is **not** a scientific refutation of transparent-Sun radial geometry and it does not reclassify or patch 0077. Under the frozen 0088 next-action rule, this route is closed at the exact failure and must not be post-hoc repaired or tuned.

## Frozen prospective authority

- preregistration: `research/prereg/0088_g9_independent_derivative_root_certification.md`
- prereg commit / frozen contract commit: `7471acdf876e5a990505369db8a6888225052913`
- prereg SHA256 recorded by authoritative artifact: `210e29c2e288d3310e1f6aa95d0c8810a76fe4cd692e28e5c4ee22ddfac3630b`

The frozen contract explicitly required:
- pinned Model-S payload / transparent-Sun map semantics;
- a new independent continuous derivative/root construction used only to propose/certify turning roots;
- original-map finite-difference confirmation at frozen step scales `1, 1/2, 1/4`;
- fixed dyadic validation points independent of results;
- quadrature repeated at 4x tighter tolerance;
- root stability, map-root agreement, area invariants, grid/step replicas and one-ring controls;
- all final area/kernel controls at `<=0.5%` where specified;
- no result-selected nodes, relaxed tolerances or post-result numerical tuning.

Most importantly, the preregistered next action states that a `BLOCKED` or `FAIL` closes this numerical route and returns NMIR to another frontier; 0077/0088 must not be patched post hoc.

## Final hosted authority

- final head SHA: `902864b8dd40c4781de253fb3ef8920889c8e3ea`
- head commit message: `route frozen 0088 locator through globally converged quadrature`
- workflow run: `34196995659`
- job: `101968787464`
- workflow infrastructure conclusion: `success`
- artifact: `10044630410`
- artifact ZIP SHA256: `2275feb6c86a7d21f8ae282120819b6bcfef31be3f98346bca66cfbd237813ab`
- raw `g9_0088_result.json` SHA256: `2e19a1125ea4737f584d3dc5e36f0ef61fce97aad9b4187080ed309bff95b57d`
- benchmark JSON SHA256: `5146378af85e88b46f37a47cec70b3f9e6e098dfac0cab339430e17008c26578`

A green workflow is therefore **not** a scientific PASS: the hosted runtime/tests/artifact path completed successfully, while the fail-closed scientific artifact returned a terminal blocker.

## Exact scientific artifact outcome

The authoritative result reports:

- gate: `G9_0088_INDEPENDENT_DERIVATIVE_ROOT_CERTIFICATION`
- classification: `BLOCKED_G9_ROOT_CERTIFICATION`
- exact detail: `RuntimeError('composite Simpson convergence exhausted')`.

The independent benchmark itself remained exact:

- expected: `3.3603942459095247`
- reference: `3.3603942459095247`
- simulator: `3.3603942459095247`
- expected/computed relative error: `0.0`
- expected/reference relative error: `0.0`
- benchmark relative error: `0.0`
- benchmark signature: `0809c4c12dc809d4a2925a5d4965f123ad66e872674d3f3563208eedd7d55b62`.

Thus the blocker is not benchmark corruption or hosted infrastructure. The root-certification calculation could not complete under its frozen deterministic quadrature contract.

## Interpretation

The final 0088 implementation evaluates a continuous interpolated-density projected-mass representation and its derivative with deterministic globally refined composite Simpson quadrature. The frozen tolerance is `1e-11`, repeated at `2.5e-12`; failure to converge within the fixed implementation cap causes fail-closed root certification.

Separately, the authoritative transparent-Sun map implementation in `src/nmir/gravity_extended.py` computes `projected_mass_g` by trapezoidal integration over the Model-S radial knots, augmented by the moving split point `x=b/R`. Therefore 0088 was intentionally an independent continuous-geometry locator rather than the algebraic derivative of the discrete trapezoidal map itself.

This distinction suggests a future **new gate**, not an 0088 repair: derive and validate a map-exact piecewise derivative of the frozen trapezoidal projected-mass algorithm, with no continuous Simpson quadrature. Such a gate must be prospectively preregistered under a new number and may not inherit or relax 0088's failed convergence mechanism.

## What 0088 does not authorize

- no root-certified G9 global kernel;
- no finite-source or positioning-error convolution;
- no persistent-source convolution;
- no BSM response/enhancement scan;
- no change to 0077 classification;
- no post-hoc increase of Simpson node cap, tolerance change, derivative threshold, result-selected scan nodes or 0.5% relaxation.

## Next frontier

Close 0088 exactly here. The highest-leverage executable G9 continuation is a separately preregistered map-exact derivative **authority gate** for the frozen discrete trapezoidal projected-mass implementation. That first gate should authorize only the derivative evaluator itself; root certification should be a later gate only if the derivative authority passes.
