# Preregistration 0097 — NMIR v2 G9 Betelgeuse line-tracking architectures

Date frozen: 2026-09-09
Branch: NMIR v2
Execution condition: run only if 0096 returns `PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS`.

## Purpose
Prospectively compare two observer architectures for a specifically monitored nearby progenitor after, and only after, a 50-mas central numerical support region has been certified by 0096:

A. ideal active heliocentric line tracking at the inherited G9 observer distances;
B. a single passive circular heliocentric orbit whose orbital plane contains the frozen source-Sun line.

This gate is intentionally frozen before the 0096 science result is known. It may not use any 0096 support radius larger than the preregistered 50 mas even if the eventual 0096 magnification margin is enormous.

This is a geometry/dynamics actionability gate, not a spacecraft design or detector-performance gate.

## Parent authority
Required parent status:
`PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS`.

If 0096 does not PASS, classify this gate `NOT_RUN_V2_G9_0097_PARENT_NOT_PASSED`; do not shrink the source envelope or substitute another progenitor inside 0097.

NMIR v1 remains immutable and closed at 100% under its v1 contract.

## Frozen source astrometry
Use Harper et al. 2017, arXiv:1706.06020, combined radio+Hipparcos solution:
- `mu_alpha_cos_delta = 26.42 mas/yr`, sigma `0.25 mas/yr`;
- `mu_delta = 9.60 mas/yr`, sigma `0.12 mas/yr`;
- conservative per-coordinate astrometric cosmic-noise term: `2.4 mas`.

Use the cosmic-noise term independently in both sky coordinates as a conservative propagation envelope. Do not reduce it by averaging or by adding new post-result astrometry inside this gate.

The nominal proper-motion magnitude is
`mu = hypot(mu_alpha_cos_delta, mu_delta)`.

## Frozen mission tracking horizon
Primary tracking horizon: exactly `10 Julian years`, where one Julian year is `365.25 d`.

This horizon is an architecture stress-test only. 0097 makes no claim that Betelgeuse will explode within ten years and must not convert the horizon into an explosion probability.

At elapsed time `H=10 yr`, define per-coordinate one-sigma propagated uncertainties:

`sigma_alpha(H) = sqrt(2.4^2 + (0.25 H)^2) mas`

`sigma_delta(H) = sqrt(2.4^2 + (0.12 H)^2) mas`

and the conservative radial three-sigma envelope

`epsilon_3sigma(H) = 3 * hypot(sigma_alpha(H), sigma_delta(H))`.

The source-center tracking authority is geometrically compatible with the 0096 support only if `epsilon_3sigma <= 50 mas`.

Do not include annual Earth parallax: the required alignment is Sun-source-observer and is evaluated in the heliocentric frame. Finite source distance remains separately controlled in 0096.

## Frozen observer distances and support width
Use exactly the three observer-distance controls inherited by 0093 and 0096. No new G9 focal distance may be inserted.

For all architectures use only
`beta_support = 50 mas = 0.050 arcsec`
as the certified radial half-width, irrespective of any wider 0096 numerical survival.

For each observer distance `z` compute
`d_support(z) = z * AU * tan(beta_support)`.

## Constants
Use IAU exact astronomical unit and a traceable standard solar gravitational parameter. Record the numerical value and authority in the output. Do not fit either constant to NMIR results.

## Architecture A — ideal active heliocentric line tracking
Model a point observer commanded to remain at heliocentric radius `r=z*AU` on the instantaneous opposite extension of the Betelgeuse-Sun line.

Compute, for each inherited `z`:
1. radial solar-gravity cancellation acceleration
   `a_hover = GM_sun / r^2`;
2. ten-year ideal radial hover delta-v
   `Delta_v_hover = a_hover * H`;
3. nominal transverse line-tracking speed from proper motion
   `v_track = r * mu_rad_per_second`;
4. proper-motion centripetal acceleration diagnostic
   `a_track = r * mu_rad_per_second^2`;
5. ratio `a_track/a_hover`.

No propulsion efficiency, mass, power, propellant model or solar-sail model may be introduced in 0097.

Architecture-A classification:
- `PASS_V2_G9_BETELGEUSE_ACTIVE_LINE_TRACKING_KINEMATICS` iff the three-sigma astrometric envelope is <=50 mas and all required accelerations/speeds/delta-v values are finite and positive for all inherited z controls.
- `SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_ACTIVE_ASTROMETRY_50MAS` if the frozen three-sigma astrometric envelope exceeds 50 mas.
- Engineering feasibility is explicitly `UNASSESSED` regardless of PASS.

## Architecture B — single passive circular orbit
For each inherited `z`, assume a circular Keplerian orbit with its plane containing the frozen source-Sun line, the most favorable passive single-orbit orientation.

Compute:
- `v_orb = sqrt(GM_sun/r)`;
- `T_orb = 2*pi*sqrt(r^3/GM_sun)`;
- exact half-width `d_support(z)`;
- central crossing duration for one passage
  `t_cross = 2*d_support/v_orb`;
  this straight-chord expression must also be compared with the exact angular result `2*asin(d_support/r)/omega`; report the relative difference;
- two crossings per orbit;
- passive time duty fraction
  `f_duty = 2*t_cross/T_orb` using the exact angular duration for authority;
- minimum number of equally phased identical observers needed to cover all orbital phases under this idealized architecture
  `N_continuous = ceil(1/f_duty)`.

A single passive observer FAILS continuous unknown-event coverage if `f_duty < 1`. This is a geometric statement, not an engineering-cost statement.

Record the KamLAND+Super-K Betelgeuse-like optimistic early-warning value of up to 12 hours as external context only. Do not use it to promote a passive orbit to guaranteed coverage: an alert cannot guarantee favorable pre-existing orbital phase.

Architecture-B classification:
- `SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_SINGLE_PASSIVE_CONTINUOUS_COVERAGE` if `f_duty < 1` for every inherited z control;
- otherwise `PASS_V2_G9_BETELGEUSE_SINGLE_PASSIVE_CONTINUOUS_COVERAGE`.

## Combined 0097 classification
Allowed terminal combined statuses:
- `PASS_V2_G9_BETELGEUSE_ACTIVE_KINEMATICS_PASSIVE_FAIL` if A passes and B fails;
- `PASS_V2_G9_BETELGEUSE_BOTH_ARCHITECTURES` if both pass;
- `SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_LINE_TRACKING_ACTIONABILITY` if A fails and B fails;
- `BLOCKED_V2_G9_BETELGEUSE_LINE_TRACKING_AUTHORITY` if an external constant/astrometric authority required by the frozen formulas is unavailable;
- `INFRASTRUCTURE_FAIL_V2_G9_0097` for execution/provenance failure;
- `NOT_RUN_V2_G9_0097_PARENT_NOT_PASSED` if 0096 does not PASS.

The combined `PASS_...ACTIVE_KINEMATICS_PASSIVE_FAIL` means only that active tracking is kinematically finite and source astrometry fits inside the certified 50-mas envelope. It is not a spacecraft-feasibility PASS.

## Reproducibility
Produce one deterministic JSON artifact containing:
- parent 0096 terminal status, result hash and artifact/run identifiers;
- source authority citation and frozen astrometric numbers;
- constants and units;
- all three z-family calculations;
- three-sigma astrometric envelope;
- A and B classifications;
- combined status;
- exact script/blob/head provenance and SHA256.

All unit conversions must be implemented explicitly and independently cross-checked by algebraically equivalent formulas where specified.

## Interpretation guards
- Do not claim Betelgeuse explosion timing or probability.
- Do not claim propulsion feasibility from finite delta-v alone.
- Do not claim detector event gain, material response, deposited energy or useful power.
- Do not use a wider-than-50-mas lens support even if 0096 reveals one.
- Do not use pre-SN warning to rescue a passive observer that is geometrically out of phase.
- Do not relabel NMIR v1 results.

## Exact next action if Architecture A passes
Open a separate engineering-authority gate comparing prospectively specified line-holding mechanisms (continuous propulsion and/or radiation-pressure concepts) against the frozen acceleration and delta-v demand. That gate must freeze mass/area/thrust/power assumptions before calculation.
