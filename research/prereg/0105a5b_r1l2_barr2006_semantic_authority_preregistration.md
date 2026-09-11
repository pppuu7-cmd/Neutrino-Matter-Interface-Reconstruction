# 0105a5b R1l2 — Barr 2006 semantic authority locator preregistration

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Scope: NMIR v2 authority work only; NMIR v1 remains frozen.

## Validated prerequisite
R1l1 is validated `PASS_0105A5B_R1L1_BARR2006_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY`, record commit `483006b211c7516136d4fb68745b6f2ba650b9e5`, run/job/artifact `34600551955 / 103266497710 / 10264246088`. Exact source SHA256 is `f128800ae1eb18fb58c27ce91941b726f1bbf42a7f7ac17a273664f3a81da0f7`; the complete mechanically selected source-text candidate set is exactly `uncertainflux.tex`.

## Frozen input and allowed inspection
Use only `https://export.arxiv.org/e-print/astro-ph/0611266v1`; require the exact R1l byte lock before archive parsing; read only `uncertainflux.tex` after verifying it is the sole frozen source-text candidate.

## Prospectively frozen semantic evidence
Emit bounded line contexts (line itself plus at most 3 neighboring lines on either side) for these predefined evidence classes only:
1. Barr-family label forms for W/Y/Z with explicit plus/minus or charge forms, including regex-equivalent LaTeX/plain forms such as `W+`, `W-`, `W^+`, `W^-`, and the analogous Y/Z forms;
2. explicit language containing any of `uncertainty`, `uncertainties`, `error`, `errors`, `parameter`, `parameters`, `variation`, `variations`, `vary`, `flux`, `pion`, `kaon`;
3. explicit statements tying named parameter regions/families to atmospheric-neutrino flux changes.

No post-read keyword additions, ranking, pruning or numerical mapping to B4RITM is allowed.

## Frozen classification
`PASS_0105A5B_R1L2_BARR2006_PRIMARY_NUISANCE_SEMANTICS_LOCATED_NONDISCOVERY` iff the source contains explicit named Barr-family W/Y/Z semantics and explicit variation/uncertainty meaning sufficient to establish that these are primary-source atmospheric-flux nuisance directions. Otherwise `BLOCKED_0105A5B_R1L2_BARR2006_PRIMARY_NUISANCE_SEMANTICS_INCOMPLETE`.

Even PASS does not authorize transfer of amplitudes/conventions into DeepCore. A separate mapping/compatibility gate against frozen B4RITM is required before standard-3nu reproduction.

Observed BSM residual, systematic MC and standard 3nu remain prohibited.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
