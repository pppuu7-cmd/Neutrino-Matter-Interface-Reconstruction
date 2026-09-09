# Preregistration 0098 — NMIR v2 G9 line-holding propulsion authority

Date frozen: 2026-09-09
Branch: NMIR v2

## Execution condition
Run only if 0097 terminally returns an Architecture-A active-tracking PASS (`PASS_V2_G9_BETELGEUSE_ACTIVE_KINEMATICS_PASSIVE_FAIL` or `PASS_V2_G9_BETELGEUSE_BOTH_ARCHITECTURES`). Otherwise record `NOT_RUN_V2_G9_0098_PARENT_ACTIVE_NOT_PASSED` and do not alter the 0097 50-mas support or ten-year horizon.

This gate is frozen before either 0096 or 0097 has produced a terminal result. It therefore may not select a propulsion mechanism, spacecraft mass, power source, or lifetime criterion after seeing those results.

## Purpose
Test whether the ideal active line-holding demand from 0097 is already incompatible with traceable present/reference propulsion and power authorities, using scale-invariant resource accounting rather than a post-result arbitrary spacecraft mass.

0098 is not a full spacecraft design. It may establish a resource-closure survivor, a scoped reference-technology failure, or an external-authority block. It may not convert finite propulsion resources into detector gain, useful neutrino power, or mission TRL.

## Frozen parent quantities
Import from the authoritative 0097 artifact, without modification, for all three inherited observer-distance controls:
- `a_hover_m_s2`;
- `delta_v_hover_10yr_m_s`;
- the exact ten-Julian-year horizon;
- inherited observer distances.

Use `g0 = 9.80665 m/s^2` exactly for specific-impulse conversion.

## Frozen electric-propulsion authority
Use the four operating points in NASA's 2025 Advanced NEXT performance table (NASA NTRS / IEPC 2025 authority) exactly as published:

| point | thrust | Isp | efficiency | thrust/power |
|---|---:|---:|---:|---:|
| AN1.5B | 74 mN | 2663 s | 57% | 44 mN/kW |
| AN14 | 87 mN | 3137 s | 61% | 40 mN/kW |
| AN45A | 257 mN | 2870 s | 63% | 45 mN/kW |
| 2B | 330 mN | 3397 s | 67% | 40 mN/kW |

Authority: NASA Technical Reports Server, `Development Status and Performance Metrics of the Advanced NEXT...`, 39th International Electric Propulsion Conference (2025), NTRS citation 20250001749.

Do not select only the best throttle point after calculation. Evaluate all four points for all inherited z controls.

For each point/control calculate:
1. exhaust speed `v_e = Isp*g0`;
2. ten-year ideal propellant fraction from the rocket equation
   `f_prop = 1 - exp(-Delta_v_hover/v_e)`;
3. required propulsion electric specific power using the published thrust-to-power ratio `q=T/P`:
   `P_req/M0 = a_hover/q`;
4. maximum instantaneous supported total mass at the published thrust:
   `M_supported = T/a_hover`.

`M_supported` is a scale diagnostic, not a chosen spacecraft mass.

## Frozen radioisotope-power authority
Use the NASA MMRTG reference as the conservative flight-proven power benchmark:
- system mass: 45 kg (99 lb class);
- beginning-of-mission electric power: about 110 W;
- estimated end-of-design-life electric power at 17 years: 72 W;
- operational/design lifetime authority: 14–17 years depending the cited NASA mission/fact-sheet convention.

Primary power accounting must use the more conservative `72 W / 45 kg` end-of-design-life specific electric power, because the frozen tracking horizon is ten years. Beginning-of-life power is sensitivity only.

For each electric-propulsion point/control define the propulsion-only RPS mass fraction required by scale closure:
`f_RPS_EOL = (P_req/M0)/(72 W / 45 kg)`.

Define the necessary resource headroom sentinel
`h_resource = 1 - f_prop - f_RPS_EOL`.

Interpretation:
- `h_resource > 0` means propellant plus an idealized MMRTG mass allocation do not by themselves exhaust 100% of initial wet mass; this is only a necessary scale-closure survivor and leaves thruster/PPU/tanks/structure/thermal/control/detector mass unmodeled;
- `h_resource <= 0` is a strong reference-resource failure for that point/control.

No arbitrary 1000-kg or other mission mass may be inserted in 0098.

## Frozen electric-thruster duration authority
NASA's NEXT long-duration test demonstrated more than 48,000 operating hours and was voluntarily terminated with the thruster still operational. Compare this with the exact ten-Julian-year duration `87660 h`.

Report:
- single-unit demonstrated-hours coverage `48000/87660`;
- a prospectively frozen two-unit sequential redundancy diagnostic `96000/87660`.

The two-unit diagnostic is not a reliability proof and does not license simple multiplication of failure probabilities. It only asks whether two independently available units, each assigned no more than the demonstrated operating-hours envelope, can cover the frozen duration in hours. Hardware mass for redundancy remains outside the scale-only resource headroom unless a later mass authority gate is opened.

## Frozen solar-sail comparison
Use a separate propulsion-free reference comparison; do not select it only if electric propulsion fails.

Absolute photon-pressure authority:
- NASA solar-sail physics gives approximately `4.56e-6 N/m^2` for perfect absorption at 1 AU and `9.1e-6 N/m^2` for ideal perfect reflection.

Compute the ideal perfectly reflecting total-system areal-density ceiling for a radial statite at 1 AU:
`Sigma_required_ideal = p_reflect_1AU / (GM_sun/AU^2)`.
Because both gravity and solar radiation pressure scale as `r^-2`, this ideal areal-density condition is independent of heliocentric distance in the two-force model.

Heritage/reference system authority:
NASA solar-sail integrated design reference reports characteristic acceleration about `0.35 mm/s^2` at 1 AU (with reflectivity about 0.85; reference total flight mass 200 kg, 100 m x 100 m-or-greater class sail).

Compare that published characteristic acceleration directly with `GM_sun/AU^2`.

Classification of the heritage/reference sail is scoped only to that reference performance. Failure does not constitute a no-go for future ultralight sails.

## Frozen terminal classification logic
Allowed terminal outcomes:

- `PASS_V2_G9_0098_REFERENCE_RESOURCE_SCALING_SURVIVES` if all four Advanced-NEXT operating points at all inherited z controls have finite values and positive `h_resource`, and at least the prospectively frozen two-unit demonstrated-hours diagnostic covers 87660 h. This means only that reference propulsion/power scaling has not produced a resource no-go.
- `SCIENTIFIC_FAIL_V2_G9_0098_REFERENCE_RESOURCE_CLOSURE` if any required electric point/control has `h_resource <= 0` under the frozen conservative EODL MMRTG accounting.
- `BLOCKED_V2_G9_0098_PROPULSION_OR_POWER_AUTHORITY` if a frozen source value cannot be traced or a required published quantity is ambiguous enough to prevent the calculation.
- `NOT_RUN_V2_G9_0098_PARENT_ACTIVE_NOT_PASSED` if 0097 active tracking does not pass.
- `INFRASTRUCTURE_FAIL_V2_G9_0098` for execution/provenance failure.

Also report, without changing the combined terminal status:
- `REFERENCE_SOLAR_SAIL_HOVER_SURVIVES` or `REFERENCE_SOLAR_SAIL_HOVER_FAILS`;
- `SINGLE_THRUSTER_DURATION_DEMONSTRATED` or `SINGLE_THRUSTER_DURATION_NOT_DEMONSTRATED`;
- `TWO_UNIT_HOURS_COVERAGE_SURVIVES` or `TWO_UNIT_HOURS_COVERAGE_FAILS`.

## Interpretation guards
- Positive resource headroom is necessary, not sufficient, for spacecraft feasibility.
- MMRTG electrical output used here is propulsion-only; spacecraft housekeeping, thermal management, communications and detector loads are not included.
- Published thrust-to-power is not automatically whole-spacecraft wall-plug efficiency; do not hide PPU/system losses. Record this as an engineering caveat unless a source explicitly closes it.
- Two sequential 48,000-hour units are an endurance-hours diagnostic, not a reliability probability.
- Solar-sail reference failure is not a universal solar-sail no-go.
- No result in 0098 modifies NMIR v1 or the MeV solar-transmission authority block.
- Never multiply lens magnification by interaction, detector, deposited-energy or power gains without independent authority.

## Exact next action after 0098
If reference resource scaling survives, open a separate mass/PPU/thermal/attitude-control closure gate before calling active stationkeeping engineering-feasible. If resource scaling fails, do not rescue it by selecting a post-result spacecraft mass or propulsion point; a new v2 architecture would require a new preregistration.