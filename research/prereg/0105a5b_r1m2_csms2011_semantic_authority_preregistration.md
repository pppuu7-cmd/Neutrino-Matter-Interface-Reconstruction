# 0105a5b R1m2 — CSMS 2011 semantic authority locator preregistration

Date: 2026-09-11
Branch: `research/0105-bsm-residual-reconstruction`
Scope: NMIR v2 authority work only; NMIR v1 remains frozen.

## Validated prerequisite
R1m1 is validated `PASS_0105A5B_R1M1_CSMS2011_ARCHIVE_STRUCTURE_LOCATED_NONDISCOVERY`, record commit `113665bef07a4688d9b496d539e5bfa60d9d2375`, run/job/artifact `34601328440 / 103269075610 / 10264242462`. Exact source SHA256 is `274b459c38d54c7b874a3353c622f9c807a1e55dcd2fc27214541e2d9f6015ce`; the complete mechanically selected source-text candidate set is exactly `nucross.tex`.

## Frozen input and allowed inspection
Use only `https://export.arxiv.org/e-print/1106.3723v1`; require the exact R1m byte lock before archive parsing; read only `nucross.tex` after verifying it is the sole frozen source-text candidate.

## Prospectively frozen semantic evidence
Emit bounded line contexts (line itself plus at most 3 neighboring lines on either side) for these predefined evidence classes only:
1. explicit terms `uncertainty`, `uncertainties`, `error`, `errors`, `PDF`, `parton`, `cross section`, `cross-section`, `neutrino`, `antineutrino`, `normalization`, `scale`, `variation`, `variations`;
2. explicit numerical uncertainty/range statements attached to the neutrino-nucleon DIS cross section or to the PDF/QCD calculation;
3. explicit statements distinguishing neutrino and antineutrino cross sections or their uncertainty behavior.

No post-read keyword additions, ranking, pruning, B4RITM mapping, nuisance-sign convention, or threshold choice is allowed.

## Frozen classification
`PASS_0105A5B_R1M2_CSMS2011_PRIMARY_DIS_UNCERTAINTY_SEMANTICS_LOCATED_NONDISCOVERY` iff the primary source supplies an explicit quantitative uncertainty/range or an explicit computational uncertainty prescription for the high-energy neutrino-nucleon DIS cross section sufficient to define what CSMS itself regards as its prediction uncertainty. Otherwise `BLOCKED_0105A5B_R1M2_CSMS2011_PRIMARY_DIS_UNCERTAINTY_SEMANTICS_INCOMPLETE`.

Even PASS does not authorize a DeepCore nuisance transformation: a separate mapping/compatibility gate against frozen B4RITM and IceCube analysis semantics is required before standard-3nu reproduction.

Observed BSM residual, systematic MC and standard 3nu remain prohibited.

`NMIR_V2_DISCOVERY_READINESS: 48%`
`OBSERVED_BSM_RESIDUAL_PERMISSION: 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION: 0%`
