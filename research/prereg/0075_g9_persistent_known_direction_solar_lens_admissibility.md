# Preregistration 0075 — G9 persistent/known-direction transparent-Sun lens admissibility

Date frozen: 2026-09-07
Parent: 0061 `PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY` for a random-direction 10-kpc Galactic CCSN; 0074c has retired the current executable B-L likelihood route.

## Scientific question

Does the transparent-Sun gravitational-focusing branch remain strongly negative when the neutrino source is **persistent and its direction is known in advance**, so that an observer/detector can in principle be deliberately placed and maintained near the appropriate solar focal geometry instead of paying the random-source occurrence/alignment probability that dominated iteration 0061?

This is a class-level G9/F3-F7 gate. It is not a scan over named sources and it does not assume that any existing astrophysical point source has the required neutrino angular size or flux.

## Frozen scope

Use the already validated extended-Sun lens model and focal mapping from iterations 0029-0030/0061. The source is parameterized only by quantities that control lens utility:

- source distance `D_s >> z`;
- angular neutrino-emission radius `theta_s` (or projected radius `s = z theta_s` at the focal plane);
- persistent unlensed neutrino flux/rate `Phi_0` only as an overall normalization, so the primary gate is a dimensionless magnification/admissibility map;
- circular receiver radius `a`;
- observer heliocentric distance `z` on a validated transparent-Sun focal branch;
- transverse pointing/position error budget `delta_y`.

Do not select a named material, detector technology or astrophysical source before the generic admissibility boundary is known.

## Frozen objective distinction

Score **receiver-integrated neutrino event/fluence magnification** relative to the same receiver exposed to the same source without solar-lens alignment. This is focusing/event gain only. It is not microscopic interaction gain and not neutrino-energy gain.

## Frozen physical accounting

For an extended persistent source, use the receiver-integrated lens mapping already validated in G9. Finite source size and receiver size must be integrated; point-caustic divergence is forbidden.

The effective source-plane blur radius is at least

`r_eff >= s + delta_y`,

with `s = z theta_s` for `D_s >> z`.

A deliberate known-direction observation may set the occurrence probability to unity only if the geometry is explicitly treated as an **actively positioned observer**. It may not set the positional/alignment duty to unity by fiat. The calculation must report the required transverse positional tolerance and, when turning a geometric magnification into a time-averaged utility, an explicit duty factor or a clearly labeled best-case `duty=1` upper bound.

## Mandatory no-free-lunch ceiling

In addition to the detailed one-ring/extended-Sun calculation, compute a deliberately optimistic whole-solar-aperture ceiling. No receiver can collect more neutrinos than an ideal device that redirects every ray crossing the relevant transparent solar aperture into the receiver. For finite source/pointing blur, this ceiling must remain finite and must be stated independently of detailed caustic strength.

Any claimed survivor must pass both the real-lens calculation and this upper-ceiling consistency check.

## Frozen parameter map

Before inspecting any result, evaluate a logarithmic class-level grid broad enough to expose the transition rather than tuning to a named source:

- receiver radius `a = 1, 10, 100 m`;
- angular source radius `theta_s` spanning `1e-18` to `1e-6 rad`;
- transverse positioning error `delta_y = 0, 0.01, 0.1, 1, 10, 100 m`;
- representative validated focal distance `z = 24.073780819657056 AU` from iteration 0061, plus a sensitivity check over at least two neighboring valid focal branches/rings if the existing extended-Sun implementation exposes them without new model assumptions.

The zero-error row is an ideal mathematical upper control, not a realizability claim.

## Prospective outputs

The benchmark must return machine-readable:

1. finite-source receiver-integrated instantaneous magnification `mu_real`;
2. ideal whole-aperture upper ceiling `mu_upper`;
3. required angular/transverse tolerance for `mu >= 2`, `10`, `1e3` where achievable;
4. critical `theta_s` above which each gain threshold is impossible even at `delta_y=0` under the optimistic ceiling;
5. sensitivity to receiver radius and focal branch;
6. explicit labels separating instantaneous `duty=1` ceiling from any time-averaged utility.

## Frozen classifications

- `PASS_G9_PERSISTENT_KNOWN_DIRECTION_SURVIVOR`: there exists a nonzero finite region in (`theta_s`, `a`, `delta_y`) where the **real extended-Sun lens**, not only the impossible aperture ceiling, yields `mu_real >= 2`; the required position tolerance is finite and explicitly reported. This establishes a geometric/focusing survivor class only, not an existing-source feasibility claim.
- `PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_PERSISTENT`: exact alignment focuses, but after finite source/receiver/position-error accounting the real-lens class map has no finite practical parameter region with `mu_real >= 2`, or the optimistic ceiling itself is <2 throughout the frozen map.
- `BLOCKED_G9_PERSISTENT_GEOMETRY`: existing validated lens code/model does not supply enough neighboring focal geometry or finite-source mapping to execute the frozen class map without a new uncontrolled assumption.
- `SCIENTIFIC_FAIL_G9_PERSISTENT_INVARIANT`: numerical result violates positivity, finite-source monotonicity, receiver integration or the whole-aperture upper bound.
- `INFRASTRUCTURE_FAIL`: code/runtime/artifact access fails before scientific classification.

## Frozen invariants

- all magnifications finite and non-negative;
- increasing source angular radius at fixed `a,z,delta_y` cannot improve the optimistic finite-source upper ceiling;
- increasing `delta_y` cannot improve that ceiling;
- `mu_real <= mu_upper` at every grid point;
- `mu -> 1` must be recovered for sufficiently large blur/source size where the focused excess is diluted away;
- no occurrence-rate penalty is used for the known-direction class, but any `duty=1` result is explicitly an upper bound unless active positioning dynamics are independently supplied.

## Implementation/reproducibility contract

Reuse existing G9 code where valid; add the smallest new source/position-smearing functions needed, dedicated tests, a machine-readable benchmark script and hosted fail-closed workflow. Preserve raw run/job/artifact/hash in the immutable iteration note. Do not weaken grid, invariants or PASS threshold after seeing output.

## Next actions

- PASS survivor -> only then open a separate primary-source audit asking whether any real persistent neutrino source occupies the surviving (`theta_s`, flux, direction, duty`) region. Do not name a source as viable before that audit.
- strong-negative -> close persistent known-direction transparent-Sun focusing in the frozen class map and return to the remaining funnel.
- blocked -> record the exact missing lens-model ingredient; do not approximate it after seeing desired gains.
