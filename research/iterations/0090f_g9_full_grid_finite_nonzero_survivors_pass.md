# Iteration 0090f — G9 full ray-centric finite-source grid PASS with finite nonzero survivors

Date: 2026-09-08
Classification: `PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS`

## Frozen contract
Preregistration: `research/prereg/0090f_g9_full_ray_centric_finite_source_survivor_scan.md`.
Prereg commit / contract: `fc277e3695ebeb2628d133b9385e7d7d2e12a5d5`.
Execution head: `f0f2a857b9fb5dbeecdd7abe4788f0e826516025`.

Parent finite-source method authority: 0090e-r1 `PASS_G9_RAY_CENTRIC_DUAL_DISK_SENTINEL_AUTHORITY`, using evaluator blob `4bedc9431b428292f1b09613f603bea82597f9b5`, parent prereg `c9d9e46860ef55bec2a5aaaafdac19f6e9de551b`, and floating-point conformance amendment `c95fd80e7b2a54d04f83103e7678acbe8c51f6c6`.

The full scan used exactly the preregistered H method: analytic two-circle source/receiver overlap, angular GL32 and radial GL64 on prospectively split intervals, with no explicit source-point quadrature, no adaptive refinement, no post-result order escalation and no survivor-threshold change.

## Frozen grid and survivor semantics
Grid cardinality:
- 3 observer controls;
- 3 receiver radii `{1,10,100} m`;
- 25 source angular radii `10^(-18+0.5*k) rad`, `k=0..24`;
- 6 source-centre offsets `{0,0.01,0.1,1,10,100} m`;
- total `1350` rows.

Primary survivor criterion inherited from 0090:

`finite_nonzero_survivor = (theta > 0) and (delta_m > 0) and (mu >= 2)`.

Aligned `delta_m=0` rows are controls and are not counted as finite-nonzero survivors.

## Hosted authority
- workflow run: `34270367643`
- aggregate job: `102211319629`
- aggregate artifact: `10073678384`
- independently verified ZIP SHA256: `1f55ba0d1c041d8711e12b63b02aaa6be820359f62c2541e2bd59b99532b8ff0`
- independently verified inner `g9_0090f_result.json` SHA256: `71831e971932c2d347e2f79c4c315c839ae853b2968d75545bb6a3b97ead6083`
- `shard_count=9`, `pair_count=9`, `row_count=1350`
- all 9 raw scientific shards: `SHARD_PASS_G9_FULL_RAY_CENTRIC_SCAN`.

No infrastructure failure and no map/overlap/accepted-area/whole-aperture/large-source invariant failure occurred anywhere in the 1350-row authority scan.

## Authoritative aggregate result
- finite nonzero survivor count: **1125 / 1350**;
- `mu >= 2`: all `1350` rows; nonzero-offset `1125`;
- `mu >= 10`: all `1350` rows; nonzero-offset `1125`;
- `mu >= 1e3`: `1242` all rows; nonzero-offset `1035`;
- global `mu_min = 157.28015230029052`;
- global `mu_max = 2852164397.158548`;
- maximum focal drift `0.0`;
- maximum batch/scalar signed-map relative discrepancy `4.466366117002431e-14`;
- maximum inherited point-control relative error `2.085291751613404e-09`.

Every nonzero offset in the frozen set (`0.01,0.1,1,10,100 m`) contributes exactly 225 survivors. Each observer control contributes 375 survivors, each receiver radius contributes 375 survivors, and every theta index contributes 45 survivors. Therefore all 1125 nonzero-offset grid rows satisfy the primary `mu>=2` survivor criterion.

The strongest finite-nonzero row in the aggregate audit is at observer control `x0=0.020`, receiver radius `1 m`, `theta_index=1`, `theta=3.1622776601683795e-18 rad`, offset `0.01 m`, with `mu=2852093091.4929914`.

## Interpretation and strict limits
This is a terminal numerical PASS for the frozen Model-S finite-source grid. It establishes that the previously certified solar-lens map plus exact finite-source convolution has a broad finite-source, nonzero-offset numerical survivor region under the frozen abstract source-size/offset grid.

It does **not** establish that any named real astrophysical neutrino source occupies that region. It also does not establish source alignment probability, time persistence, duty cycle, flux enhancement at a practical detector, detector/material response gain, interaction-rate gain, or neutrino-supplied energy gain.

The very large `mu` values must not be multiplied into any detector or power estimate before a separate named-source realizability gate passes.

## Next mandatory G9 gate
Prospectively freeze a named-source realizability / source-morphology gate before using any numerical survivor. At minimum it must establish for one or more real candidate neutrino sources:
1. source distance and emitting-region physical/angular size in the relevant neutrino channel;
2. neutrino energy/flavor spectrum compatible with the Model-S lens assumptions;
3. source direction relative to the Sun-observer optical axis and the mapping from sky-angle misalignment to the frozen source-plane offset parameter;
4. achievable alignment window/probability and temporal duty/persistence for an observer near the relevant 24-AU focal geometry;
5. whether the real source parameters actually overlap the 0090f survivor region.

Only after that gate may G9 be classified as a practical/named-source survivor or scoped negative. No detector/material or BSM gain is authorized here.
