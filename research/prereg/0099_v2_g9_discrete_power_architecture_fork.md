# Preregistration 0099 — NMIR v2 G9 discrete power-architecture fork

Date frozen: 2026-09-09
Branch: NMIR v2
Execution condition: run only if 0098 returns `PASS_V2_G9_0098_REFERENCE_RESOURCE_SCALING_SURVIVES`.

## Purpose
0098 is a scale-invariant reference resource test. A positive continuous mass fraction does not prove that a real spacecraft can be assembled from integer power and propulsion hardware. In particular, a kW-class ion operating point can require many ~75-W EODL MMRTGs even when the continuous mass-fraction equation has large headroom.

0099 prospectively separates three questions before any 0098 terminal result is known:

1. does the reference active line-holding architecture survive **integer hardware and power-unit accounting**?
2. does an MMRTG implementation have public authority for the required radioisotope scale?
3. if MMRTG scaling is programmatically unsupported, does a kWe-class fission branch have sufficient current flight authority to replace it?

This is a reference architecture / technology-authority gate. It is not a universal spacecraft feasibility proof and it cannot invalidate active line-holding merely because one power architecture is blocked.

## Parent authority and anti-selection guard
Required parent status:
`PASS_V2_G9_0098_REFERENCE_RESOURCE_SCALING_SURVIVES`.

The following grids, component proxies, equations and classification labels are frozen before 0098 executes. Do not delete an unfavorable propulsion point after seeing 0098. Do not substitute a new power technology inside 0099 after seeing the result.

If 0098 does not PASS, classify:
`NOT_RUN_V2_G9_0099_PARENT_REFERENCE_SCALING_NOT_PASSED`.

## Inherited active-control demand
Use exactly the three 0097 observer controls and the four Advanced NEXT operating points already frozen by 0098. Do not recompute a wider lens support or new observer distance.

Use the 0098a conservative MMRTG EODL electrical power:
`P_MMRTG_EOL = 74.8 W`
and mass:
`M_MMRTG = 45.0 kg`.

Use each parent point's exact:
- thrust `T_point`;
- `Isp`;
- thrust-to-power value;
- ideal ten-year propellant fraction `f_prop`;
- active-control `a_hover` and `Delta_v`.

## Frozen integer active-lane grid
For every observer control and Advanced NEXT operating point evaluate exactly:
`n_active in {1, 2, 4}`
identical simultaneously active thrusters.

The grid is exploratory but prospectively fixed. A reported best surviving configuration may be selected only from these predeclared 36 combinations (3 observer distances x 4 operating points x 3 active-lane counts).

## Endurance installation rule
0098 froze two-unit sequential endurance-hours coverage as a diagnostic. 0099 therefore installs exactly two complete propulsion strings per active lane:

`n_installed_strings = 2 * n_active`.

Only `n_active` strings draw full propulsion power simultaneously; the second set is an installed endurance spare. This remains an hours-coverage model, not a reliability probability.

## Frozen NEXT-C / Advanced-NEXT component mass proxy
Advanced NEXT is a derivative of NEXT-C and NASA's 2025 development report states that the higher-thrust modifications do not significantly alter system mass or volume. Use NEXT-C heritage values only as a conservative reference proxy; do not call them measured Advanced-NEXT flight masses.

Per installed string freeze:
- thruster with harness: `14.0 kg` (NASA NEXT-C public value is <14 kg; use 14.0);
- PPU: `36.0 kg` (public value <36 kg; use 36.0);
- LPA: `3.1 kg`;
- gimbal heritage proxy: `6.0 kg`.

Per spacecraft freeze two HPA units for a simple authority-level redundancy allowance:
`M_HPA_total = 2 * 1.9 kg`.

Thus
`M_propulsion_hardware = n_installed_strings*(14.0 + 36.0 + 3.1 + 6.0) + 3.8 kg`.

No DCIU, harness outside the quoted thruster harness, tank, structure, thermal-control, communications, avionics, detector or payload mass is silently set to zero. They are represented only through the residual-mass diagnostic below and remain unclosed engineering sectors.

Primary NASA authorities:
- NASA NEXT-C fact sheet / NTRS 20210024276: 0.6–7.4 kW system input, thruster mass <14 kg, PPU mass <36 kg.
- NASA NEXT guide / NTRS 20090004685 and NASA system data: HPA 1.9 kg, LPA 3.1 kg.
- NASA NEXT IPS characteristics / AIAA-2007-5199: heritage gimbal 6 kg.
- NASA Advanced NEXT 2025 / NTRS 20250008168 (also 20250001749): derivative of NEXT-C with increased thrust-to-power without significantly altering system mass or volume; 330 mN demonstrated; PPU efficiency 92–95%.

## Frozen non-propulsion electrical reserve
Do not pretend propulsion is the only spacecraft load. Require exactly 25% of EODL MMRTG electrical capacity to remain unavailable to propulsion:

`P_propulsion_allowed = 0.75 * N_MMRTG * 74.8 W`.

For each configuration choose the smallest integer

`N_MMRTG = ceil(P_active / (0.75 * 74.8 W))`,

where `P_active` is the published operating-point propulsion input power multiplied by `n_active`.

The 25% reserve is an explicit reference stress-test assumption, not a measured spacecraft housekeeping requirement. Record also zero-reserve and 10% reserve sensitivities, but neither may replace the frozen 25% primary result.

## Frozen thrust / mass closure
Maximum initial mass supported at the inherited hover acceleration is

`M0_max = n_active*T_point / a_hover`.

Using the parent's ideal ten-year propellant fraction, define

`M_prop = f_prop * M0_max`.

Define the discrete known-hardware residual

`M_residual = M0_max - M_prop - N_MMRTG*45 kg - M_propulsion_hardware`.

and

`f_residual = M_residual / M0_max`.

This residual is the maximum room left for xenon tankage, structure, thermal integration, DCIU/avionics, communications, detector/payload and margins within this reference maximum-thrust architecture. It is **not** payload mass.

Reference discrete mass-power subgate:
- `PASS_REFERENCE_DISCRETE_MASS_POWER` if, for each of the three observer controls, at least one prospectively declared operating-point / active-lane configuration has `M_residual > 0` under the primary 25% reserve;
- otherwise `SCIENTIFIC_FAIL_REFERENCE_DISCRETE_MASS_POWER_CLOSURE`.

Record the globally smallest and largest positive `f_residual`, and the best configuration per observer control, but do not remove failed configurations.

## Propellant-throughput authority
For each configuration compute total ideal xenon mass `M_prop`.

Use NASA NEXT long-duration-test authority:
- original qualification throughput requirement `450 kg` per thruster;
- demonstrated LDT exceeded 900 kg / 50,000 h;
- retain the conservative frozen `450 kg per installed active-lane thruster over its required service segment` authority threshold for the primary qualification comparison.

Because two sequential strings share the ten-year duty in the 0098 endurance model, primary throughput demand per operating string is

`M_prop_per_used_string = M_prop / (2*n_active)`.

Primary throughput subgate passes iff this is `<=450 kg` for the selected reference configuration. Report the >900 kg LDT only as sensitivity/context; do not use it to rescue a 450-kg primary failure.

## MMRTG radioisotope scale
NASA public authority states:
- one MMRTG uses eight GPHS modules;
- one MMRTG contains `4.8 kg` of plutonium oxide;
- Pu-238 is 71% of that oxide mass by weight;
- multiple MMRTGs can in principle be combined on one spacecraft.

For every integer configuration record:

`M_PuO2 = 4.8 kg * N_MMRTG`

`M_Pu238 = 0.71 * M_PuO2`.

For supply-scale context freeze the NASA FY2025 budget authority target of approximately `1.5 kg plutonium oxide/year` full operational capability by 2026. Record the production-equivalent time

`t_production_equiv = M_PuO2 / (1.5 kg/yr)`.

This is a scale diagnostic only. It is **not** a procurement schedule because existing inventory, other mission allocations, processing/yield and future production policy matter.

No current public authority found before preregistration establishes that the required tens-to-hundreds of MMRTGs or corresponding isotope inventory is allocatable to an NMIR mission. Therefore an MMRTG branch may receive a positive discrete mass-power substatus but may not receive a full flight-resource PASS solely from this arithmetic.

## MMRTG thermal scale
Freeze `2000 W thermal per MMRTG at beginning-of-mission` as the public NASA reference value and record:

`P_thermal_BOL = 2000 W * N_MMRTG`.

Do not invent a radiator or spacecraft thermal layout. Existing MMRTG fins and direct radiation do not by themselves authorize close-packed multi-unit spacecraft integration. Thermal integration remains separately unassessed.

## Fission alternative branch
Do not interpret an MMRTG supply block as a no-go for kWe-class power.

Frozen external authority:
- NASA's Kilopower project demonstrated relevant-environment fission power subsystem technology for the 1–10 kWe class and completed as a technology project; NASA described systems up to 10 kWe continuous for at least ten years.
- Current NASA Fission Surface Power work is an active technology project for lunar/Mars **surface** systems, not authority for an existing flight-qualified free-flying deep-space ~24-AU spacecraft power unit.

For each active propulsion point record whether its primary propulsion electrical demand is `<=10 kWe` and `<=40 kWe` as technology-scale comparisons only.

Do not assign a flight-ready fission mass, radiator mass, launch safety approval, reactor shadow-shield mass or conversion-system lifetime unless prospectively supplied by a directly applicable authority. Surface-system masses may not be silently imported to a free-flying NMIR spacecraft.

Fission branch status:
- `POWER_SCALE_COMPATIBLE_BUT_FLIGHT_AUTHORITY_BLOCKED` if the required electrical power lies within the published 1–10 kWe / tens-kWe technology scale but no directly applicable flight-qualified free-flying system authority closes the architecture;
- `POWER_SCALE_OUTSIDE_FROZEN_FISSION_REFERENCE` if it exceeds the frozen comparison scale.

## Terminal 0099 classifications
Allowed overall statuses:

1. `PASS_V2_G9_0099_DISCRETE_REFERENCE_ARCHITECTURE_SUPPORTED`
   only if discrete mass-power and conservative throughput pass **and** a currently applicable power architecture has enough direct authority to close integer power units, source/fuel availability, and required integration within this gate.

2. `BLOCKED_V2_G9_0099_MMRTG_SUPPLY_AND_FISSION_FLIGHT_AUTHORITY`
   if discrete mass-power/throughput can close but MMRTG allocation is not publicly authorized at the required scale and the fission alternative is power-scale-compatible yet lacks directly applicable free-flying flight authority.

3. `SCIENTIFIC_FAIL_V2_G9_0099_DISCRETE_MASS_POWER_OR_THROUGHPUT`
   if no prospectively declared discrete configuration closes mass/power or conservative throughput for at least one inherited observer control.

4. `BLOCKED_V2_G9_0099_EXTERNAL_HARDWARE_AUTHORITY`
   if a frozen component authority required to evaluate the equations cannot be recovered or is materially inconsistent.

5. `INFRASTRUCTURE_FAIL_V2_G9_0099`
   for code/provenance/artifact failure.

6. `NOT_RUN_V2_G9_0099_PARENT_REFERENCE_SCALING_NOT_PASSED`
   if 0098 parent does not PASS.

## Interpretation guards
- A blocked MMRTG supply branch is not a physics no-go for active neutrino-lens tracking.
- A power-scale-compatible fission concept is not a flight-feasibility PASS.
- `M_residual` is not payload mass and cannot be advertised as delivered science mass.
- No detector-event, interaction, deposited-energy or useful-power gain is inferred.
- Do not infer an explosion date or probability for Betelgeuse.
- Do not revise the 50-mas 0097 support using a later wider numerical result.
- Do not use future Pu-238 production improvements or future flight fission systems inside this frozen gate; those require a new explicit scope.

## Exact output requirements
Produce deterministic JSON containing:
- parent 0098 status/hash/provenance;
- all 36 discrete configurations;
- integer active and installed string counts;
- integer MMRTG count, electric reserve and power;
- component masses and residual mass fraction;
- xenon throughput per used string;
- PuO2/Pu238 scale and production-equivalent years;
- BOL thermal scale;
- 10-kWe and 40-kWe fission-scale comparisons;
- all substatuses and final status;
- exact code/prereg/head hashes.
