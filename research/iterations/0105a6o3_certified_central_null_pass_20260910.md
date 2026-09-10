# 0105a6o3 — certified Tier-B Ar central/null reproduction

Date: 2026-09-10
Classification: **PASS_0105A6O3_TIERB_ARGON_CERTIFIED_CENTRAL_NULL_REPRODUCTION_NONDISCOVERY**

## Frozen provenance

- preregistration commit: `225c1dc5bd7df6896ebeac47646fb7b80e63b5e0`;
- original pre-fit 0105a6o acceptance-contract commit: `a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e`;
- implementation commit: `d11d01f0230ea18bd2f5a713a42a1fdb6ff17a82`;
- guards commit: `34c64f7a10948c01634329ab976f730c579e0232`;
- execution head: `2ba5684e765e3b5d3f92461eaac1b824ecf95c25`;
- run/job: `34505553764/102966745805`;
- artifact: `10163693174`, `nmir-v2-0105a6o3-argon-certified-central-null`;
- provider artifact ZIP SHA256: `0a41052a255e0c97bc3572c2b85b315c39aa36fbc331eab6445367b967381bc1`;
- independently downloaded artifact ZIP SHA256: `0a41052a255e0c97bc3572c2b85b315c39aa36fbc331eab6445367b967381bc1`;
- inner `result.json` SHA256: `ea1ac038c3cd1dbac726d9884e9ff00a651e0833e9f4fb58ee4a7127b51f6114`;
- parent 0105a6o2 result SHA256 independently reverified: `e3790cb7e2459ef900fda2cfe430be8d47fe497c1365f9c12762bef3f9599d73`.

## R3152

Certified central best fit:

- `NC = 160.20495320804548...`;
- `NP = 552.11738177195724...`;
- `ND = 10.53624250236968...`;
- `NB = 3131.39681887754358...`.

Null-profile result:

- `q0 = 15.04173851118035...`;
- `Z_stat = 3.87836802162718...`;
- CEvNS profile interval: `[117.95883736785023..., 203.11127991845527...]`;
- profile half-width: `42.57622127530252...` events.

All six unchanged 0105a6o publication checks PASS.

## R3154

Certified central best fit:

- `NC = 159.70980813844213...`;
- `NP = 552.09605241011034...`;
- `ND = 10.50657649044405...`;
- `NB = 3133.16475761858775...`.

Null-profile result:

- `q0 = 14.94766567030630...`;
- `Z_stat = 3.86622110985731...`;
- CEvNS profile interval: `[117.46597344930198..., 202.61381702908651...]`;
- profile half-width: `42.57392178989227...` events.

All six unchanged 0105a6o publication checks PASS.

## Mandatory dual-anchor robustness

All thresholds copied unchanged from original preregistration commit `a94cbdf5a65618545bd4b1fb4f9fd6c120ae340e` PASS:

- `|Delta NC| = 0.49514506960335... <= 1.0`;
- `|Delta NP| = 0.02132936184690... <= 1.0`;
- `|Delta ND| = 0.02966601192563... <= 1.0`;
- `|Delta Z_stat| = 0.01214691176987... <= 0.05`;
- `|Delta sigma_profile| = 0.00229948541025... <= 0.5`.

No branch selection is performed; both R3152 and R3154 independently satisfy the publication benchmark and their differences satisfy the prospective robustness contract.

## Interpretation

This is the first successful numerical Tier-B release-consistent central/null reproduction in the 0105 Ar chain. It is not a recovery of the collaboration-internal RooFit implementation and does not erase the historical Tier-A authority BLOCKED result.

The prior 0105a6o and 0105a6o1 BLOCKED records also remain immutable. 0105a6o2 established a unique exact-objective optimum, and 0105a6o3 then used that certified machinery with the original pre-fit publication windows unchanged.

## Permissions

The next allowed Ar gate is only the prospectively frozen shape-systematic excursion reproduction specified by original 0105a6o Stage 8.

The full release-consistent Tier-B Ar SM/null layer is **not yet closed** until that systematic layer is independently classified.

- `SHAPE_SYSTEMATIC_EXCURSION_PREREGISTRATION_PERMISSION_PERCENT = 100`;
- Tier-A exact collaboration-internal likelihood remains BLOCKED;
- nuisance-cleaned observed residual remains forbidden;
- `OBSERVED_BSM_RESIDUAL_PERMISSION_PERCENT = 0`.
