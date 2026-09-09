# 0098 — v2 G9 line-holding propulsion/resource gate

Date: 2026-09-09
Classification: `PASS_V2_G9_0098_REFERENCE_RESOURCE_SCALING_SURVIVES`

## Frozen provenance
- preregistration commit: `48e5904139e8782e046f4d6e7d3c548ec1880e18`
- MMRTG authority amendment commit: `fd6504fdfffe651078603eb62576610f66049424`
- required 0097a geometry amendment: `3f873eb3ab8d90b931eb41f5ba25484fde843ced`
- authoritative run: `34358823483`
- job: `102490263246`
- workflow head: `f801ce8ef38508bc226b158bd2db87e10f0bbd1b`
- artifact: `nmir-v2-g9-0098-authoritative`
- artifact ID: `10106900686`
- artifact ZIP SHA256: `a5b52efdb4b7273be473d820aeefa49e0adbc78344755681f785158194acf994`
- inner `g9_0098_result.json` SHA256: `98ee5f81035d38bdd99804ac6fa78637cc86e7451358f208d15043eb40a80116`
- parent 0097 inner SHA256: `6e0e9669ddd8c4814cde845a2f34bffd5e2fbc5d89c76dd9328394c1a235ac07`
- parent status: `PASS_V2_G9_BETELGEUSE_ACTIVE_KINEMATICS_PASSIVE_FAIL`

## Terminal result
All 12 frozen combinations of three inherited ~24-AU controls and four Advanced-NEXT operating points have positive reference resource scaling under the preregistered continuous accounting.

Global minimum resource headroom among the 12 combinations is:
`0.7417023220936317`

The frozen ten-Julian-year duration is `87660 h`.
The frozen NEXT demonstrated-duration lower bound is `48000 h`:
- one unit: coverage ratio `0.5475701574264202` -> `SINGLE_THRUSTER_DURATION_NOT_DEMONSTRATED`;
- two sequential units: coverage ratio `1.0951403148528405` -> `TWO_UNIT_HOURS_COVERAGE_SURVIVES`.

The conservative MMRTG EODL reference is `74.8 W / 45 kg` after prospective authority amendment 0098a.

## Solar-sail reference branch
Using the frozen ideal-reflection pressure reference, the static-hover total areal-density ceiling is about `1.53455 g/m^2` at 1 AU scaling. The frozen NASA integrated-sail characteristic-acceleration reference (`0.35 mm/s^2`) is only about `0.0590` of the required full solar-gravity cancellation at 1 AU, therefore the reference branch is:
`REFERENCE_SOLAR_SAIL_HOVER_FAILS`.

This is not a universal solar-sail no-go.

## Interpretation
0098 is a **necessary reference scaling PASS**, not spacecraft feasibility. It does not include integer power units, complete hardware, housekeeping/detector loads, real tankage/structure, reliability probability, isotope supply, flight qualification, thermal integration, detector-event gain, deposited-energy gain, or useful-power gain.

The correct next step is the already-preregistered 0099 discrete power-architecture gate.