# Prospective architecture audit — 0097a through 0099

Date: 2026-09-09
Scope: NMIR v2 G9 known-progenitor / Betelgeuse branch
Status: prospective/non-terminal; written while authoritative 0096 is still in progress and before any 0097/0098/0099 terminal artifact exists.

## 1. 0096 state at this audit
Authoritative run: `34319781596`
Authoritative head: `eff5996612f31c093e82a9ae0cdfdb859da8cb9a`

At the latest check:
- 30 of 36 frozen primary-family artifacts existed (`83.3%` of the primary matrix);
- all 30 completed primary jobs had `success`;
- six primary jobs remained inside the frozen 4097-point science evaluator;
- no primary aggregate, 8193-node sensitivity authority, or final 0096 artifact existed yet.

Therefore 0096 still has **no terminal PASS/FAIL classification**.

### Independently inspected heavy-receiver scale
The following receiver=100 m shards were independently downloaded and hashed during the audit chain:
- control 0 / 190 pc / 100 km: `mu_min = 314.2207802786686`;
- control 1 / 222 pc / 100 km: `mu_min = 311.70926556996454`;
- control 0 / 190 pc / 21 km: `mu_min = 314.22100905387623`;
- control 2 / 190 pc / 21 km: `mu_min = 305.96506479115`;
- control 0 / 222 pc / 100 km: `mu_min = 314.22079796311476`.

Every inspected shard had 4097/4097 evaluated nodes, `all_ge2=true`, and its sampled minimum at the frozen 50-mas endpoint. The worst inspected value is still more than 150 times the `mu=2` threshold. This is strong interim evidence, not the missing 8193-node sensitivity proof.

Latest additional shard provenance:
- artifact `10095633471`, `nmir-v2-g9-0096-primary-0-2-222-100`;
- GitHub/independent ZIP SHA256 `bb89e6bbd8e2ca8de09b130c25ac3a425d2166b7078e9391716202ca6baad3d0`;
- inner JSON SHA256 `e06d1792a54cec90cc7d147b5d0c2c3fbca10ca337a025953342c6704f08e7e9`.

## 2. 0097a geometry correction
Parent 0097 prereg commit:
`53863048c2d5b5803c9e120794c21fe415f1b319`

Prospective amendment:
`research/prereg/0097a_v2_g9_downstream_focal_halfline_geometry_amendment.md`
commit:
`3f873eb3ab8d90b931eb41f5ba25484fde843ced`

Defect: the parent passive-orbit model counted two intersections with the infinite source-Sun line as two useful lens crossings. For a fixed source the useful focal geometry is downstream (`source -> Sun -> observer`), so only one of the two antipodal orbit-line intersections is a usable lens window.

Frozen corrected passive duty:
`f_duty = t_cross/T_orb`, not `2*t_cross/T_orb`.

For 50 mas this gives approximately:
- `f_duty = 7.716049382716276e-8`;
- ideal equal-phase continuous-fleet diagnostic `N = 12,960,000`.

The active architecture is unchanged.

Independent source-astrometry arithmetic gives the already frozen 10-y 3-sigma radial envelope:
`epsilon_3sigma = 13.148764200486678 mas`, comfortably inside 50 mas.

For the three inherited ~24-AU observer controls, prospective active dynamics are dominated by solar-gravity cancellation:
- `a_hover ~ 1.007e-5 to 1.032e-5 m/s^2`;
- ideal 10-y `Delta-v ~ 3.18 to 3.26 km/s`;
- transverse proper-motion tracking velocity only ~`1.55e-2 m/s`;
- transverse tracking acceleration / hover acceleration ~`6.5e-12`.

These are pre-parent calculations, not a terminal 0097 PASS.

## 3. 0098 authority hardening
0098a MMRTG EODL amendment commit:
`fd6504fdfffe651078603eb62576610f66049424`

0098 now uses traceable conservative `74.8 W` EODL at `45 kg`, not the untraceable older 72-W value.

0098 additionally requires exact 0097a provenance before accepting a PASS parent:
- code commit `074d76a010cdb584c341e4bf5be22e19f992d34e`;
- test pin commit `eafd0dad599b2056fd48760512ba8c1c827cd9f6`;
- baseline CI run `34330497048` completed `success`.

## 4. Why 0099 was opened prospectively
Conditional 0098 arithmetic indicates the continuous reference mass fractions may remain positive, but published Advanced NEXT points are kW-class while one conservative EODL MMRTG supplies only 74.8 W. A continuous fraction can therefore hide a large integer-unit problem.

0099 was preregistered before any 0098 result:
`research/prereg/0099_v2_g9_discrete_power_architecture_fork.md`
commit:
`7792fb3412eb9f3c932bc04f8ae357bdc4c0129f`

A pre-execution algebra audit then found that evaluating xenon throughput at the thrust ceiling `M0_max` was too restrictive because that ceiling is not a required spacecraft mass. The prospective correction was frozen before parent execution:
`research/prereg/0099a_v2_g9_mass_interval_closure_amendment.md`
commit:
`01642bfdb9e96044dfdf4b81986eafbb51cb3bea`

Correct closure now asks whether a non-empty spacecraft initial-mass interval exists between:
- lower bound from fixed integer power/propulsion hardware plus ideal propellant fraction;
- upper bound from thrust and conservative 450-kg/string xenon throughput.

## 5. Conditional 0099 scale before parent execution
Using the already frozen prospective active-control demands only as a code/algebra test:
- all 36 prospectively declared configurations have a non-empty mass interval;
- under the primary 25% non-propulsion electrical reserve, integer MMRTG demand spans roughly `30` to `589` units across the full frozen grid;
- even the low-power one-active-lane AN1.5B reference needs `30 MMRTGs` under the primary reserve;
- that low case corresponds to `144 kg` PuO2, `102.24 kg` Pu-238 by the frozen NASA composition figure, and about `60 kW` BOL thermal power;
- `144 kg / (1.5 kg/yr) = 96` production-equivalent years at the frozen public production-scale reference, before existing inventory, allocations, yield, other missions, or future policy are considered.

This does **not** mean an actual procurement time is 96 years; it means the MMRTG implementation has moved from a simple mass-fraction question to a severe isotope/integration authority problem.

## 6. Power-architecture interpretation
Current NASA authority supports:
- Advanced NEXT as a NEXT-C derivative with 330 mN demonstrated and broadly similar system mass/volume scale;
- flight-qualified/flight-demonstrated NEXT-C heritage component scales;
- MMRTG use and the physical possibility of multiple MMRTGs on one spacecraft;
- 1–10 kWe Kilopower technology-scale work and current tens-kWe fission-surface-power development.

But the audit does not find directly applicable authority for either:
1. allocatable tens-to-hundreds of MMRTGs / corresponding Pu-238 inventory for an NMIR spacecraft, or
2. an already flight-qualified free-flying deep-space kWe-class fission power unit suitable for the ~24-AU line-holding architecture.

Therefore the strongest prospective expectation for 0099, **if 0096 -> 0097 -> 0098 all pass their required parent gates**, is not a practical-mission PASS but a likely scoped external-authority block in the power architecture. This is deliberately frozen before seeing those terminal results.

## 7. Current research interpretation
The active known-progenitor branch is separating into two qualitatively different layers:

1. **geometry/astrometry/kinematics:** currently looks numerically strong inside the frozen 50-mas support, subject to terminal 0096/0097 authority;
2. **flight power/integration:** now appears to be the dominant practical bottleneck, especially for an MMRTG-fed continuous ion-hover architecture.

A power-architecture block does not invalidate the neutrino-lens geometry and cannot be promoted to a physics no-go. Conversely, numerical lens support cannot be promoted to detector-event, deposited-energy, useful-power, or mission-feasibility gain.
