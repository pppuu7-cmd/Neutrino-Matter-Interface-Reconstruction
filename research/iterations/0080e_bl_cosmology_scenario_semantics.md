# NMIR iteration 0080e — B-L cosmology Majorana/Dirac scenario semantics

Date: 2026-09-08
Classification: **PASS_COSMOLOGY_B_L_SCENARIO_CONDITIONAL_AUTHORITY**

## Frozen contract
Prospective preregistration: `research/prereg/0080e_bl_cosmology_scenario_semantics.md`, commit `bfc19b82d3320e8b798090fdfc2e99c52602917c`.

Question: does the primary Esseili–Kribs source treat the Majorana and Dirac CMB polygons as alternative scenario-conditioned results, or prescribe a reproducible common combination/preference?

No geometry composition, external neutrino-nature assumption, BBN addition, global-envelope union or response scan was allowed.

## Primary source
- arXiv `2308.07955v2`
- source SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`
- `neff_arXiv_v2.tex` SHA256 `f77b577688b3609c574985b05fc9a213709c958ded60a511478357f1f881d678`

## Result
The exact primary TeX explicitly presents two scenarios, identifies the Dirac case as one of two cases, calls the Majorana case the alternative, and reports the scenario results separately. The fail-closed search found no source-prescribed rule for combining, weighting, marginalizing, preferring, unioning or intersecting the Majorana and Dirac constraint results.

All frozen checks passed:
- `two_scenarios_explicit=true`
- `dirac_one_of_two_cases=true`
- `majorana_explicit_alternative=true`
- `majorana_and_dirac_results_separate=true`
- `explicit_common_combination_rule_detected=false`
- `common_combination_candidate_contexts=[]`

Therefore the two 0080d CMB excluded polygons must remain **separate scenario-conditioned branches**. A scenario-independent union/intersection is not authorized by the primary source.

## Hosted authority
Successful run/job: `34164286854/101872133978`
Artifact: `10033631352`
Raw JSON SHA256: `381c0470a03cf468df56601ca04cb9a1763676fe11d05a25b5e7c049e8d1037f`
Artifact ZIP SHA256: `21f3953dad41891087004cabdc613ba9903cc62d684dd69ceb80944146856820`
Persistent authority ledger: `data/esseili_kribs_scenario_semantics_0080e_authority.json`.

## Implementation audit
The initial run `34164118315/101871667719` did not reach a scientific classification: a regression test caught a TeX sentence-splitting defect before the source audit. Commit `c1603d2e23ef114b239c57e4afae488dba0744a0` fixed only TeX-aware sentence boundaries; no scientific keyword, threshold or classification rule changed. The corrected run then passed 4/4 dedicated regression tests and the exact-source audit.

Repository baseline initially exposed missing CI-only dependencies for older 0080d vector-geometry tests. Commits `39d3ddb18a9da8d4319116c9d29f6c7e44894b0a` and `bb5df1a5135b04c6b7b552f7acac2f55d1571107` added PyMuPDF/Shapely to baseline CI only. Full baseline run/job `34164374756/101872392194` passed both `pytest` and `python -m nmir.baseline`.

## Consequence
The cosmology family is now reproducible but **conditional on neutrino-sector scenario**. No universal CMB exclusion may be claimed without an additional physical assumption external to this source.

Per the frozen 0080e decision tree, the funnel returns to remaining missing 0071 B-L authority materialization. The lowest-provenance-cost next step is the BBN part of the already frozen Esseili–Kribs source (Figs. 7/8), followed by still-unmaterialized stellar/SN families.

## Readiness
`NMIR_READINESS` remains **94%**. This iteration closes a composition ambiguity but does not yet add a new independent excluded-region family.
