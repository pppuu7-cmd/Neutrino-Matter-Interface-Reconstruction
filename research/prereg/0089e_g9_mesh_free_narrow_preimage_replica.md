# NMIR prereg 0089e — G9 independent mesh-free narrow-preimage replica

Date frozen: 2026-09-08

## Motivation and scope
0089d is immutably `BLOCKED_G9_CONTINUOUS_MAP_MONOTONE_KERNEL` because its prospectively frozen global midpoint indicator replicas at N=2^18 and 2^19 do not resolve at least one finite narrow accepted interval. This gate does **not** modify, reopen, or retroactively pass 0089d.

0089e asks a distinct question: can the accepted-preimage intervals implied by the already accepted 0089b continuous piecewise-linear Model-S projection and the already certified 0089c monotone partition be independently reproduced by a mesh-free high-precision scalar implementation whose numerical error is controlled without any result-selected spatial mesh?

This gate remains geometry-only. It does not compute finite-source, positioning/alignment, duty-cycle, persistent-source utility, interaction gain, detector gain, neutrino-energy gain, or BSM response.

## Exact frozen provenance and inputs
- Model-S upstream commit: `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`.
- Exact Model-S git blob SHA1: `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`.
- Accepted continuous projection authority: iteration 0089b, immutable commit `40f88288c7996d105446918e78cce29aa4c99d83`.
- Accepted turning-root authority: iteration 0089c, immutable commit `e8fc4e6856d6326e6c273a96cb46f6b660467d96`.
- Observer controls are frozen exactly as 0089c/0089d:
  - x0=0.020, z=23.97365833326344 AU, turn=0.01150432239489928;
  - x0=0.024, z=24.07633010302372 AU, turn=0.013783440937996098;
  - x0=0.030, z=24.263861625478885 AU, turn=0.01718034337813724.
- x domain: [1e-4,1].
- receiver radii: 1,10,...,1e9 cm by decades.
- R_sun=6.96e10 cm; G=6.67430e-8 cgs; c=2.99792458e10 cm/s; AU=1.495978707e13 cm.

## Independent numerical authority
Implement a standalone high-precision scalar replica using `mpmath`; it must not import `nmir.g9_continuous_projection`, `nmir.g9_continuous_kernel`, or the 0089d benchmark for the high-precision mass/focal/map calculation.

The density between adjacent frozen Model-S radii is the same continuously linearly interpolated law rho(r)=a_i r+c_i used by 0089b. Re-derive/evaluate projected cylindrical mass shell-by-shell from the accepted closed-form continuous projection equations using arbitrary-precision arithmetic. No raster, sampled interpolation of the map, or spatial scan is allowed.

Two fixed precision replicas are required: **60 decimal digits and 90 decimal digits**. Precision may not be increased selectively after results.

For each frozen monotone branch and each target y=0,+r,-r that is bracketed by the branch endpoints, solve the target by pure high-precision bisection. Stop only after branch x-width <=1e-20. No scan-seeded root discovery is permitted; the 0089c branch endpoints alone supply brackets.

Construct accepted branch subsets from the target roots exactly as in the mathematical definition |y|<=r. Merge only zero-width/touching boundaries; any positive-width overlap between branch contributions is a scientific contradiction. Compute

A_acc(r,z)=pi R_sun^2 sum_i (x_hi,i^2-x_lo,i^2)

with arbitrary-precision summation. Define K=A_acc/(pi r^2) only as a stored geometry diagnostic.

## Frozen validation criteria
### H0 provenance / implementation
Before science, verify the exact Model-S blob. Run deterministic toy profiles with analytically known accepted intervals: one monotone linear map, one one-turn quadratic surrogate, and one narrow linear preimage. Any source/hash/dependency/toy failure is `INFRASTRUCTURE_FAIL_G9_0089E`.

### H1 precision replica
For every control/radius and every target root present in both 60-dps and 90-dps replicas:
- |x_60-x_90| <= **2e-15**;
- both map residuals <= max(**1e-8 cm**, **2e-14*r**).

The accepted interval topology (interval count and parent branch identity) must be exactly identical between the two precisions.

### H2 area replica
For every control/radius:
- relative |A60-A90|/max(|A60|,|A90|,1) <= **5e-7**;
- A is finite, nonnegative, nondecreasing with r, and <=pi R_sun^2(1+1e-12);
- no positive-width double counting.

### H3 independent agreement with double branch construction
Run the existing 0089d double-precision branch/crossing construction **without using its blocked V4 indicator-grid classifier**. This is a comparison object, not scientific authority. Require:
- same accepted interval count and parent identities as 90-dps;
- each interval endpoint agrees with 90-dps within **2e-11 in x**;
- branch-area versus 90-dps area agrees within the inherited **0.5%** for every control/radius.

No N=2^18/N=2^19 mesh is used or reinterpreted in 0089e. 0089d remains BLOCKED regardless of this result.

### H4 inherited one-ring guard
For x0=0.024 and receiver radii 100,1000,10000 cm, the 90-dps accepted interval set must contain the inherited one-ring preimage and its corresponding interval area must reproduce the established exact one-ring accepted-area value within **0.5%**.

## Classification frozen before calculation
- `PASS_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`: H0-H4 all pass for all 30 control/radius cases.
- `BLOCKED_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`: high-precision target bracketing/topology is numerically ambiguous despite the frozen branch authority, or a finite interval cannot be unambiguously represented under the fixed 60/90-dps contract.
- `SCIENTIFIC_FAIL_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`: topology is unambiguous but any frozen H1-H4 scientific criterion fails.
- `INFRASTRUCTURE_FAIL_G9_0089E`: source/hash/dependency/runtime/toy/artifact failure before scientific classification.

## Consequences
PASS would establish a new mesh-free numerical authority for the narrow accepted-preimage geometry; it would **not** change the immutable 0089d BLOCKED classification. PASS may only authorize a separately preregistered finite-source/alignment/persistent-source gate.

BLOCKED/FAIL forbids such a convolution gate and returns the funnel to other open/blocked classes. No tolerance, precision, branch partition, radius set, or next action may be changed after viewing results.
