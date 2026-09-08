# Iteration 0094 — generic 10-kpc CCSN prospective actionability FAIL for NMIR v1

Date: 2026-09-09
Classification: `SCIENTIFIC_FAIL_G9_CCSN_PROSPECTIVE_ACTIONABILITY_V1`

## Frozen authority
- preregistration: `research/prereg/0094_g9_ccsn_prospective_actionability_closure.md`
- prereg commit: `5f978fef2afcd2426dca50ca52fe86d63f4e2a68`
- frozen evaluator implementation: `cdaa5bb2b9b75e8f37ea0d8ff3776d15eb872bb9`
- dedicated tests: `2e074347fe30cfe01e3b7c90d80a9412f91df8ad`
- hosted workflow execution head: `8ea1696ba879e265b616a0425440d554e9133446`
- authoritative run/job: `34283127183 / 102252360926`
- authoritative artifact: `10078391371`

0094-r1 (`34282992175 / 102251931250`) is an infrastructure failure only: the hosted Python image lacked `pytest`, so execution stopped before downloading the 0093 parent artifact and before any scientific calculation. Commit `8ea1696ba879e265b616a0425440d554e9133446` changed only dependency provisioning by installing `pytest`; no scientific contract, constant, authority, formula, threshold or classification rule changed.

## Raw hosted validation
0094-r2 executed on exact head `8ea1696ba879e265b616a0425440d554e9133446`.

Raw job log confirms:
- dedicated tests: `3 passed in 0.04s`;
- exact 0093 parent ZIP SHA256 check passed: `1bef56077626433de111870e8c41c6a5460f8c6cc7d332b58171ded2015c73e6`;
- exact parent inner JSON SHA256 check passed: `9a5aea9e1d3fd00a16781870e93ee95956a3886ed47edb3a244155ce0dd23a5b`;
- result JSON SHA256 printed by the job: `b161632eae1253a53b012211bc30d3da06c29c89c26fb7ffe50e134c16cb7431`;
- artifact upload ZIP digest: `3d0d20cc6f1336009bc0b941e1b74a77b2609b9857173f226c708328d51b9971`;
- uploaded artifact ID: `10078391371`.

The artifact was independently downloaded outside the Actions job. Independent hashes exactly reproduce the raw hosted values:
- ZIP SHA256: `3d0d20cc6f1336009bc0b941e1b74a77b2609b9857173f226c708328d51b9971`;
- inner `g9_0094_result.json` SHA256: `b161632eae1253a53b012211bc30d3da06c29c89c26fb7ffe50e134c16cb7431`.

## Scientific result
Because 0093 is topology-BLOCKED, 0094 deliberately did **not** use its first threshold crossing as a global footprint. It used the more generous map-certified strict no-overlap support ceiling

`beta_zero,max = max[d_zero / (z AU)]`.

This is a necessary-condition upper support bound: outside it the inherited overlap model has `mu=1`, independent of the unresolved internal multi-band re-entry topology.

Validated widest support:
- `d_zero = 665553864.2779205 m`;
- `z = 23.97365833326344 AU`;
- `beta_zero,max = 1.855767162642536e-4 rad = 38.27794542421865 arcsec`.

Frozen published prompt 10-kpc pointing benchmark:
- `beta_prompt = 3 deg`;
- ratio `beta_prompt / beta_zero,max = 282.1468049109759`.

Frozen pre-supernova authority scope:
- operational pre-SN alert reach used by the gate: `510 pc`;
- published pre-SN directional-study scope used by the gate: `< 1 kpc`;
- benchmark source distance: `10,000 pc`.

Thus all four frozen necessary-condition flags are true:
1. prompt pointing is broader than the strict G9 support ceiling;
2. operational pre-SN reach does not cover the 10-kpc benchmark;
3. published pre-SN directional scope does not cover the 10-kpc benchmark;
4. a burst-triggered neutrino alert cannot be used as pre-positioning information for the same leading neutrino wavefront at the downstream observer.

Under the prospectively frozen taxonomy this requires

**`SCIENTIFIC_FAIL_G9_CCSN_PROSPECTIVE_ACTIONABILITY_V1`**.

The isotropic spherical-cap value `8.609679358340117e-9` is retained only as an explicit non-Galactic geometric scale control and is not promoted to a Galactic CCSN capture/actionability probability. The exact Galactic probability is not reproducibly assignable in v1 because the source direction is not prospectively known and 0093 retains unresolved multi-band topology.

## Scope and interpretation
This is a scoped scientific negative for:
- one observer;
- the already frozen generic 10-kpc future Galactic CCSN benchmark;
- the validated ~24-AU G9 geometry;
- the frozen current localization/pre-SN authorities.

It is **not** a theorem against:
- a pre-positioned multi-observer swarm;
- a specifically known nearby progenitor monitored before collapse;
- future sub-arcsecond pre-SN localization at 10 kpc;
- a different source class or a v2 engineering architecture.

Those would add new assumptions/data and require a new prospective v2 gate.

0093 remains immutable `BLOCKED_G9_CCSN_ALIGNMENT_TOPOLOGY`. 0092b-a2 remains independently `BLOCKED_G9_0092B_A2_NUCLEAR_CHANNEL_AUTHORITY_TERMINAL_V1`, so no transparent/opaque CCSN-Sun statement follows. No detector/material/BSM response multiplication or neutrino-supplied-power claim is authorized.

## NMIR v1 readiness role
This result supplies the single post-0093 prospective actionability classification required by R100-3 of `research/NMIR_V1_READINESS_100_CONTRACT.md`. Whether the repository may now declare `NMIR_READINESS: 100%` is a separate reconciliation question requiring R100-1 through R100-6 and current Actions state to be checked; this result itself does not automatically change readiness.
