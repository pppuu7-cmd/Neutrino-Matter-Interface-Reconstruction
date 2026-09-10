# 0105a6o1 — optimizer convergence diagnostic terminal result

Date: 2026-09-10
Classification: **BLOCKED_0105A6O1_OPTIMIZER_OR_OBJECTIVE_DIAGNOSTIC_UNRESOLVED**
Scope: numerical diagnostic only / NONDISCOVERY

## Frozen provenance

- preregistration: `research/prereg/0105a6o1_argon_optimizer_convergence_diagnostic_preregistration.md`
- preregistration commit: `1588298dbd04e4cc4c451b3993f43f61080d1339`
- software-only call-signature repair: `911703e13f68cac8d83ddef31a6ae93ed5dd863a`
- replacement execution head: `911703e13f68cac8d83ddef31a6ae93ed5dd863a`
- run/job: `34504351544/102962695449`
- artifact: `10163180947`, `nmir-v2-0105a6o1-argon-optimizer-diagnostic`
- provider artifact ZIP SHA256: `1a72a32199bae615b0000bdfeebf3383915b6d22c5c2a9d508190a008abc37b4`
- independently downloaded artifact ZIP SHA256: `1a72a32199bae615b0000bdfeebf3383915b6d22c5c2a9d508190a008abc37b4`
- inner `result.json` SHA256: `30f7da1bab68aaf2ae53460773765e1f28f152bcfda7fc4875ec3a49798366c5`

The first hosted attempt `34503706125/102960529111` is retained separately as a software-only failure and has no D1-D3 scientific classification.

## Structural gate

PASS for exact 0105a6p bytes. Central sums:

- data: `3752.0`;
- CEvNS: `128.0000052667117`;
- prompt BRN: `496.99999306999996`;
- delayed BRN: `33.00001642`;
- steady-state template: `3152.0001600000005`.

## Frozen D1-D3 adjudication

For both R3152 and R3154, every frozen check passes except `D2_agreement`.

### R3152

- original finite-difference 4/4 successful;
- original Q spread: `6.496451533166692e-06` <= `1e-4` PASS;
- original analytic-gradient infinity norms all < `1.89e-4` <= `5e-3` PASS;
- analytic-gradient 4/4 successful;
- analytic Q spread: `9.094947017729282e-13` <= `1e-9` PASS;
- analytic per-parameter spread: `[2.9947286066089873e-05, 9.58209500367957e-06, 2.1720070719766227e-07, 3.28258283843752e-06]`;
- frozen all-parameter agreement threshold `1e-5`: **FAIL only for NC**, `2.9947286066089873e-05 > 1e-5`;
- analytic KKT/gradient checks PASS;
- minimum Hessian eigenvalue: `0.0009072304200053586` > 0;
- SLSQP cross-check: `dx_max=0`, `dQ=0` PASS.

### R3154

- original finite-difference 4/4 successful;
- original Q spread: `4.456286660570186e-06` <= `1e-4` PASS;
- original gradient check PASS;
- analytic-gradient 4/4 successful;
- analytic Q spread: `2.7284841053187847e-12` <= `1e-9` PASS;
- analytic per-parameter spread: `[2.959013511372177e-05, 9.486692647442396e-06, 1.539600305022759e-07, 3.1657659746997524e-06]`;
- frozen all-parameter agreement threshold `1e-5`: **FAIL only for NC**, `2.959013511372177e-05 > 1e-5`;
- analytic KKT/gradient checks PASS;
- minimum Hessian eigenvalue: `0.0009072121064631999` > 0;
- SLSQP cross-check: `dx_max=0`, `dQ=0` PASS.

## Interpretation

The frozen 0105a6o1 PASS definition is conjunctive, therefore the gate remains BLOCKED and is not relaxed after viewing the result.

The observed pattern is nevertheless strongly localized: objective values agree at roughly `1e-12`, analytic gradients satisfy the frozen stationarity criterion, the closed-form Hessian is positive definite at the retained optimum, and the independent SLSQP check agrees exactly. The only failed condition is an absolute normalization-coordinate spread of roughly `3e-5` event in NC versus the prospectively frozen `1e-5` requirement.

This does not establish a Standard-Model scientific failure and is not BSM evidence. It motivates a new prospective precision/uniqueness certificate rather than weakening 0105a6o1.

## Permissions

- 0105a6o remains historical BLOCKED;
- 0105a6o1 remains terminal BLOCKED under its frozen threshold;
- publication-target classification is not performed here;
- systematic excursions remain unauthorized pending a central null reproduction PASS;
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`.
