# Preregistration 0090f — G9 full ray-centric finite-source survivor scan

Date frozen: 2026-09-08
Parent authority: 0090e-r1 `PASS_G9_RAY_CENTRIC_DUAL_DISK_SENTINEL_AUTHORITY`, immutable record `research/iterations/0090e_r1_g9_ray_centric_dual_disk_sentinel_pass.md`.

## Scientific question
Across the exact previously frozen 1350-point G9 parameter grid, does the now-certified ray-centric exact dual-disk finite-source method yield any finite-source, nonzero-offset focusing survivor with magnification `mu >= 2` while satisfying all inherited geometry/aperture invariants?

This gate is the full numerical grid authority for the existing G9 Model-S solar-lens class. It does not yet attach any grid row to a named astrophysical neutrino source, source spectrum, real alignment probability, duty cycle or detector/material response.

## Frozen method authority
Use exactly the high (H) 0090e-r1 method:
- exact two-circle source/receiver overlap geometry;
- source integration by ray-centric overlap, with no explicit source-point quadrature;
- analytic angular topology splitting at `h=|s-a|` and `h=s+a`;
- inherited monotone signed-map root splitting at all overlap-topology thresholds;
- angular Gauss-Legendre order **32** on every nonzero analytic angular subinterval;
- radial `x` Gauss-Legendre order **64** on every nonzero prospectively split map interval;
- 0090e-r1 high-precision conformance amendment: same exact partial-overlap formula at 60 decimal digits whenever `min(s,a)/max(s,a,h) < 1e-3`, and deterministic same-formula fallback if direct binary64 partial evaluation leaves the exact range.

Frozen parent identifiers:
- 0090e prereg commit `c9d9e46860ef55bec2a5aaaafdac19f6e9de551b`;
- 0090e-r1 amendment commit `c95fd80e7b2a54d04f83103e7678acbe8c51f6c6`;
- 0090e-r1 execution head `d48f2a37e132242d2f3d4f5421ccca616d2b6b90`;
- evaluator blob SHA `4bedc9431b428292f1b09613f603bea82597f9b5`;
- 0090e-r1 authoritative run/job/artifact `34269721278/102208186432/10073322174`;
- independently verified authoritative ZIP SHA256 `0117d80967e39188e16340c6c84db5984a948dcb9bf1081afe0b7c447e49f47a`;
- inner JSON SHA256 `a598d511747c4e3e00eb2c790d9c36e2c32af90e86dc6a36b28e817505cbb9cb`.

The 0090e evaluator file is frozen for this scan and must not be modified after this preregistration. 0090f may call/import it but may not alter its scientific functions, orders, overlap fallback trigger or tolerances.

## Frozen physical/model inputs
Use the same existing 0090 grid and upstream Model-S authority:
- Model-S blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`;
- solar radius `R=6.96e10 cm`;
- three observer controls:
  - `x0=0.020`, `z=23.97365833326344 AU`, turning root `0.01150432239489928`;
  - `x0=0.024`, `z=24.07633010302372 AU`, turning root `0.013783440937996098`;
  - `x0=0.030`, `z=24.263861625478885 AU`, turning root `0.01718034337813724`;
- receiver radii `{1,10,100} m`;
- source angular radii
  `theta_k = 10^(-18 + 0.5*k) rad`, `k=0..24`, exactly 25 values;
- source-centre offsets `{0,0.01,0.1,1,10,100} m`, exactly 6 values.

Total frozen grid cardinality:
`3 observers * 3 receivers * 25 theta values * 6 offsets = 1350 rows`.

Shard exactly by the 9 `(observer,receiver)` pairs; each passing shard must contain exactly 150 rows.

## Frozen magnification and survivor semantics
For each row:
- `s = z * AU_CM * theta`;
- `d = delta_m * 100 cm`;
- `a = receiver_m * 100 cm`;
- compute high-method accepted incident area `A_H`;
- `mu = 1 + A_H/(pi*a^2)`.

Retain the original 0090 diagnostic flags:
- `ge2 = (mu >= 2)`;
- `ge10 = (mu >= 10)`;
- `ge1e3 = (mu >= 1e3)`.

Primary survivor criterion is inherited unchanged from 0090:

`finite_nonzero_survivor = (theta > 0) and (delta_m > 0) and (mu >= 2)`.

All frozen theta values are positive, but the explicit `theta>0` term remains in the recorded definition for semantic continuity. Aligned `delta_m=0` rows are controls/upper-alignment cases and are **not** counted as finite-nonzero survivors.

No source-name, duty-cycle or practicality criterion is added in this gate.

## Frozen validation criteria
H0 provenance/cardinality:
- exact Model-S blob;
- evaluator blob must equal `4bedc9431b428292f1b09613f603bea82597f9b5`;
- exact parent prereg/amendment identifiers above;
- focal-distance relative drift `<=2e-11`;
- signed-map batch/scalar conformance `<=2e-11`;
- exactly 9 unique shards and exactly 1350 rows in a PASS aggregate.

H1 point controls:
For each shard, inherited `point_area_exact` at its receiver radius must match the frozen 0089e-r2 reference area within `0.5%` before full-grid rows are accepted.

H2 overlap/area physical invariants:
- exact overlap and kernel range semantics from 0090e-r1 remain active;
- each `A_H` finite and in `[0, pi*R^2*(1+1e-9)]`;
- each `mu` finite and `>=1`.

H3 whole-aperture ceiling:
For every row require
`mu <= perfect_whole_sun_mu_upper(a,R)*(1+1e-12)`
using the same inherited 0090 function and convention.

H4 large-source aperture bound:
For every row with `s>0`, require
`mu-1 <= large_source_ring_excess_upper(s,R)*(1+1e-9)`
using the same inherited 0090 bound. A violation is a scientific invariant failure, not a survivor.

No L/H re-estimation is performed on the full grid: 0090e-r1 already prospectively certified the H method on the fixed sentinel suite. No adaptive refinement, source quadrature, interpolation, result-selected nodes or order escalation is allowed.

## Frozen outputs
Each row must record at least:
- observer/control index and `x0,z`;
- receiver index/radius;
- `theta_index`, `theta_rad`, `source_radius_cm`;
- `delta_m`;
- `area_h_cm2`;
- `mu`;
- `ge2`, `ge10`, `ge1e3`;
- `finite_nonzero_survivor`.

Each shard must report its survivor count and row maximum/minimum magnification. Aggregate must report:
- total row count;
- total finite-nonzero survivor count;
- counts `ge2/ge10/ge1e3` both over all rows and over nonzero-offset rows;
- global `mu_min`, `mu_max`;
- top finite-nonzero survivor rows sorted prospectively by descending `mu`, then observer index, receiver index, theta index, delta value, limited to 50 records for audit convenience;
- counts grouped by receiver, observer, theta index and offset where practical.

The sorting rule is descriptive only and does not change classification.

## Frozen classifications
If provenance/cardinality/runtime/artifact identity prevents scientific classification:
`INFRASTRUCTURE_FAIL_G9_0090F`.

If any exact map/overlap/accepted-area/whole-aperture/large-source invariant fails:
`SCIENTIFIC_FAIL_G9_FULL_RAY_CENTRIC_INVARIANT`.

If all 1350 rows are valid and `finite_nonzero_survivor_count == 0`:
`PASS_G9_FULL_GRID_NO_FINITE_NONZERO_SURVIVOR`.

If all 1350 rows are valid and `finite_nonzero_survivor_count > 0`:
`PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS`.

Both PASS classes are terminal numerical classifications for this frozen grid. A survivor PASS is not yet a practical/named-source PASS.

## Exact next action after result
- On `PASS_G9_FULL_GRID_NO_FINITE_NONZERO_SURVIVOR`: record the scoped negative result; G9 Model-S finite-source grid closes with no `mu>=2` nonzero-offset survivor under the frozen grid. Do not invent denser/result-selected points without a new physical assumption.
- On `PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS`: prospectively freeze a named-source realizability gate before using any survivor: actual source angular size and emission-region morphology, neutrino energy/flavor spectrum, source distance, alignment window/probability, observer duty cycle and persistence must be jointly mapped to the surviving numerical region. No detector or interaction-rate multiplication yet.
- On scientific fail: audit the violated upstream invariant without changing survivor threshold.
- On infrastructure fail: repair infrastructure only.

## Guards
No BSM response scan. No detector/material multiplication. No named-source claim from grid rows alone. No aligned `delta=0` row counted as a finite-nonzero survivor. No post-hoc change of `mu>=2`, grid values, H method, high-precision trigger, orders or aperture bounds.
