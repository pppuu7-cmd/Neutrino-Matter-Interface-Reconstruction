# 0097 — v2 G9 Betelgeuse line-tracking architectures

Date: 2026-09-09
Classification: `PASS_V2_G9_BETELGEUSE_ACTIVE_KINEMATICS_PASSIVE_FAIL`

## Frozen provenance
- preregistration: `research/prereg/0097_v2_g9_betelgeuse_line_tracking_architectures.md`
- preregistration commit: `53863048c2d5b5803c9e120794c21fe415f1b319`
- prospective downstream-half-line amendment: `research/prereg/0097a_v2_g9_downstream_focal_halfline_geometry_amendment.md`
- amendment commit: `3f873eb3ab8d90b931eb41f5ba25484fde843ced`
- authoritative successful run: `34358785600`
- job: `102490137854`
- workflow head: `f801ce8ef38508bc226b158bd2db87e10f0bbd1b`
- authoritative artifact: `nmir-v2-g9-0097-authoritative`
- artifact ID: `10106890085`
- GitHub artifact digest / independently reproduced ZIP SHA256: `432e30d1bf72cbbd9b9cd89bc2a9dbd6c71564ffc3eb0826ec6ef0cdfea2e684`
- inner `g9_0097_result.json` SHA256: `6e0e9669ddd8c4814cde845a2f34bffd5e2fbc5d89c76dd9328394c1a235ac07`
- authoritative parent run: `34319781596`
- parent artifact ID: `10097881579`
- parent inner JSON SHA256 recorded by 0097: `be3b85c526e02447ca903600d9776b1c9241f67c7a29705493d5e81fac4b8299`
- parent status: `PASS_V2_G9_BETELGEUSE_CENTRAL_SUPPORT_50MAS`

## Infrastructure history
The first automatic 0097 run `34336438408` failed before any scientific calculation with `ModuleNotFoundError: No module named 'numpy'`. Parent download and artifact-ID capture had succeeded. The workflow was repaired only by installing the runtime dependencies `numpy` and `mpmath`; no frozen science input, threshold, equation, source value, horizon, architecture, or terminal label was changed.

Repair commit: `1db7093596360909189fb84381d3e05d47a74979`
One-use retry marker commit: `f801ce8ef38508bc226b158bd2db87e10f0bbd1b`

The repaired run completed successfully and is the only terminal 0097 authority.

## Source astrometry result
Frozen 10-Julian-year uncertainty envelope:
- proper motion alpha*cos(delta): `26.42 +/- 0.25 mas/yr`
- proper motion delta: `9.60 +/- 0.12 mas/yr`
- cosmic noise: `2.4 mas` per coordinate
- 3-sigma propagated radial envelope: `13.148764200486678 mas`
- certified 0096 support radius: `50 mas`

Therefore the frozen astrometric envelope remains inside the certified 50-mas central-support region.

Architecture A terminal sub-status:
`PASS_V2_G9_BETELGEUSE_ACTIVE_LINE_TRACKING_KINEMATICS`

## Active line-tracking kinematics
For the three inherited observer controls (~24 AU):
- `a_hover = 1.0072586e-5 ... 1.0317921e-5 m/s^2`
- ideal 10-y hover delta-v = `3178.67 ... 3256.09 m/s`
- proper-motion transverse tracking speed = `0.01549 ... 0.01568 m/s`
- transverse tracking acceleration / hover acceleration = about `6.48e-12 ... 6.72e-12`

Thus the frozen kinematic demand is dominated overwhelmingly by cancelling solar gravity, not by Betelgeuse proper-motion slewing.

This is a kinematic PASS only. `engineering_feasibility` remains `UNASSESSED` and is delegated to later propulsion/power gates.

## Passive circular-orbit result
The prospective 0097a correction is present in the authoritative artifact: only one of the two geometric intersections of a circular orbit with the infinite source-Sun line lies on the usable downstream focal half-line.

For all three inherited observer distances:
- usable downstream lens crossings/orbit: `1`
- exact crossing duration: about `285.83 ... 291.04 s`
- passive duty fraction: `7.716049382716276e-8`
- ideal equal-phase continuous-coverage diagnostic: `12,960,000` observers
- a single passive observer is not continuously covering an unknown event time.

Architecture B terminal sub-status:
`SCIENTIFIC_FAIL_V2_G9_BETELGEUSE_SINGLE_PASSIVE_CONTINUOUS_COVERAGE`

## Terminal interpretation
The combined terminal label is:

`PASS_V2_G9_BETELGEUSE_ACTIVE_KINEMATICS_PASSIVE_FAIL`

This means:
- active line tracking survives the frozen astrometry/kinematics gate;
- a single passive circular observer fails the frozen continuous unknown-event-coverage criterion;
- finite active kinematics is not proof of propulsion, power, lifetime, reliability, mission, detector-event, deposited-energy, or useful-power feasibility;
- no Betelgeuse explosion date or probability is inferred.

## Consequence
The frozen active-PASS parent condition for 0098 is satisfied. The branch may proceed to the already-preregistered propulsion/resource authority gate, which must retain exact 0097a provenance.