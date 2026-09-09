# 0099 — v2 G9 discrete power-architecture gate

Date: 2026-09-09
Classification: `BLOCKED_V2_G9_0099_MMRTG_SUPPLY_AND_FISSION_FLIGHT_AUTHORITY`

## Frozen provenance
- preregistration: `research/prereg/0099_v2_g9_discrete_power_architecture_fork.md`
- preregistration commit: `7792fb3412eb9f3c932bc04f8ae357bdc4c0129f`
- mass-interval amendment: `research/prereg/0099a_v2_g9_mass_interval_closure_amendment.md`
- amendment commit: `01642bfdb9e96044dfdf4b81986eafbb51cb3bea`
- authoritative run: `34358847151`
- job: `102490343207`
- workflow head: `f801ce8ef38508bc226b158bd2db87e10f0bbd1b`
- artifact: `nmir-v2-g9-0099-authoritative`
- artifact ID: `10106913371`
- artifact ZIP SHA256: `83c0bec11f9e26d9751ad2100a99d0cf04f9743df9e99128926ed9bad533f37a`
- inner `g9_0099_result.json` SHA256: `f987b5898fb1ca2bba2f9c0c6308ceb63d46a81d089631fdf0dc80ffc47bf84d`
- parent run: `34358823483`
- parent artifact ID: `10106900686`
- parent inner SHA256: `98ee5f81035d38bdd99804ac6fa78637cc86e7451358f208d15043eb40a80116`
- parent status: `PASS_V2_G9_0098_REFERENCE_RESOURCE_SCALING_SURVIVES`

## Algebraic/discrete result
The frozen grid contains 36 configurations (three observer controls x four Advanced-NEXT points x one/two/four active lanes with two installed endurance strings per active lane).

Result:
- surviving configurations: `36/36`;
- `discrete_mass_power_throughput_status = PASS_REFERENCE_DISCRETE_MASS_POWER`;
- every configuration has a non-empty initial-mass interval after integer MMRTG count, represented propulsion hardware, ideal propellant fraction, thrust ceiling and conservative 450-kg/string xenon-throughput ceiling are imposed.

Global surviving scale:
- minimum primary integer MMRTG count: `30`;
- maximum primary integer MMRTG count: `589`;
- minimum PuO2 requirement: `144 kg`;
- maximum PuO2 requirement: `2827.2 kg`;
- minimum BOL thermal power: `60 kW`;
- maximum BOL thermal power: `1.178 MW`;
- minimum positive residual-mass fraction at the allowed upper mass: `0.20519563464403368`;
- maximum: `0.6854235867577828`.

The lightest frozen MMRTG implementation therefore already requires 30 units, 144 kg PuO2 and 102.24 kg Pu-238 under the frozen composition accounting. The `96 production-equivalent years` diagnostic is only `144 kg / 1.5 kg/yr`; it is not a procurement-time prediction and ignores existing inventory, allocations, future production, yield and other missions.

## Fission branch
The propulsion input-power scale of the frozen configurations can fall within the 1–10 kWe or tens-kWe technology scale represented by public NASA fission-development authorities. However those authorities do not establish an already flight-qualified free-flying deep-space power system for this ~24-AU line-holding architecture.

Thus:
- `mmrtg_supply_status = BLOCKED_CURRENT_ALLOCATABLE_PU238_MMRTG_AUTHORITY`
- `fission_branch_status = POWER_SCALE_COMPATIBLE_BUT_FLIGHT_AUTHORITY_BLOCKED`

and the terminal result is:
`BLOCKED_V2_G9_0099_MMRTG_SUPPLY_AND_FISSION_FLIGHT_AUTHORITY`.

## Scientific interpretation
This is **not** a physics no-go for active line holding. The upstream chain has already established central numerical support (0096), active astrometric/kinematic survival (0097), and positive continuous reference resource scaling (0098). 0099 localizes the remaining practical bottleneck to flight-power/supply/integration authority.

A non-empty mass interval is not spacecraft feasibility. Residual mass is not payload mass. Thermal integration, tankage, structure, avionics, detector/payload, reliability, real mission transfer and power-system flight qualification remain unclosed. No detector-event, interaction, deposited-energy or useful-power gain is inferred.