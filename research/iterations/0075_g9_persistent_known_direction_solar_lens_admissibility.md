# NMIR iteration 0075 — persistent/known-direction transparent-Sun lens admissibility

Date: 2026-09-07
Classification: **BLOCKED_G9_PERSISTENT_GEOMETRY**

## Funnel target
Test the loophole left open by iteration 0061: a persistent neutrino source with known direction and an actively positioned observer, so the random-source occurrence/alignment penalty is removed while finite angular source size, receiver size and transverse positioning error remain explicit.

## Prospective contract
Frozen before any 0075 result-dependent calculation in commit `60dfd94c269e8d5b3a23f73043c779099cd15783`, file `research/prereg/0075_g9_persistent_known_direction_solar_lens_admissibility.md`.

Frozen map: receiver radius `a = 1,10,100 m`; `theta_s = 1e-18...1e-6 rad`; `delta_y = 0,0.01,0.1,1,10,100 m`; representative validated ring `b/Rsun=0.024`, `z=24.073780819657056 AU`, plus neighboring valid focal rings exposed by the same pinned Model-S lens. A survivor required a nonzero finite region with real-lens `mu_real>=2`; exact alignment alone was insufficient. The prereg explicitly required `BLOCKED_G9_PERSISTENT_GEOMETRY` if the existing validated lens geometry could not cover the frozen map without a new uncontrolled assumption.

## Implementation
The 0061 radial extended-Sun lens was reused rather than replaced:
- finite-source/position convolution module: `src/nmir/g9_persistent_lens.py`, commit `394d2ccaebcaa768727a230ff2b601df679c9eea`;
- dedicated regression tests: `tests/test_g9_persistent_lens.py`, initial commit `50b9dccfd6e6dd1628894d6582da2c164d99933f`, corrected test-only quadrature expectation commit `844ca8fcd5bfd46649a48bc37df39eb8a44c6c98`;
- fail-closed benchmark: `scripts/g9_persistent_lens_benchmark.py`, commit `943c72cd5a64d7ed9253940567f8870204ca8560`;
- hosted workflow: `.github/workflows/g9-persistent-lens.yml`, commit `9636808657831a55c69353f153ca8773b29e88a8`.

The benchmark parameterized a uniform angular source disk and observer-centre error, integrated the accepted incident annulus in impact parameter, and retained an impossible full-solar-aperture duty=1 ceiling. It also added pre-result implementation guards: point-annulus reproduction <=3% and source quadrature refinement <=5% if the branch map reached the required support.

## Hosted scientific authority
Corrected hosted run/job:
- run `34149433817`
- job `101828380178`
- scientific head `844ca8fcd5bfd46649a48bc37df39eb8a44c6c98`
- artifact `10028826311`
- artifact ZIP SHA256 `1c60e0ce3756250d82632df8b407202df98cd1bfe74774216950e8c4a0864ed8`

The artifact metadata digest is `sha256:1c60e0ce3756250d82632df8b407202df98cd1bfe74774216950e8c4a0864ed8`; the downloaded ZIP was independently hashed and matched exactly. The machine-readable artifact itself was opened and inspected, not inferred from green workflow status.

The stale earlier run `34149348350` was generated before the test-only correction and is explicitly non-authoritative regardless of its eventual status.

## Raw scientific result
The corrected artifact contains exactly:

```json
{
  "branches_completed": [],
  "model_s_git_blob_sha1": "e3a0fad3ff877338aad926dbd0a9a43e6c0a897f",
  "reason": "local focal branch turned before requested support",
  "status": "BLOCKED_G9_PERSISTENT_GEOMETRY"
}
```

Repository copy: `data/g9_persistent_lens_0075.json`, commit `576c0ce88195686743d1c4d0651ae322a14e0f92`.

## Scientific interpretation
This is **not** evidence that persistent known-direction solar focusing fails physically. It is also not a survivor. The local one-ring monotone mapping inherited from 0061 cannot be extended far enough to cover the largest frozen combined source/position/receiver blur before the radial map turns. Continuing through that turn with the local-root algorithm would silently mix another image/branch and would violate the preregistered fail-closed geometry rule.

The blocker is therefore sharply localized: the pinned Model-S lens equation itself remains available globally in `b/Rsun`, but 0075 lacks a validated **global multi-image mapping/integration rule across radial turning points**. A later calculation may address that only under a new prospective contract that defines image segmentation, turning-point treatment, no-double-counting and validation before inspecting utility results. No 0075 grid point or `mu>=2` region is claimed.

## F10 classification
**BLOCKED_G9_PERSISTENT_GEOMETRY**.

Readiness is not increased by this blocker.
