# Preregistration 0080e — B-L cosmology Majorana/Dirac scenario semantics

Date frozen: 2026-09-07
Parent: 0080d `PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_EXCLUDED_GEOMETRY`.

## Question
How does the primary Esseili–Kribs source authorize the Majorana and Dirac CMB excluded regions to enter the NMIR external-constraint ledger: as alternative scenario-conditioned constraints, or through an explicitly source-authorized common combination?

## Frozen primary input
Esseili & Kribs, arXiv `2308.07955v2`, source archive SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`; main TeX `neff_arXiv_v2.tex`, SHA256 `f77b577688b3609c574985b05fc9a213709c958ded60a511478357f1f881d678`.

0080d scenario-conditioned geometries are frozen and may not be changed in this audit.

## Frozen audit method
Machine-read the primary TeX only. Record exact source contexts that:
1. define or describe the `Majorana` neutrino case;
2. define or describe the `Dirac` neutrino case;
3. state whether the cases are alternatives/assumptions or are to be statistically/physically combined;
4. state any source preference, weighting, marginalization, union/intersection, or experimentally established neutrino-nature choice relevant to Figs 5–6;
5. identify any explicit instruction that one case supersedes the other for the current-CMB constraint.

No vector geometry, external neutrino-nature inference, oscillation/0nu-beta-beta assumption, or global B-L envelope composition is allowed in this gate.

## Frozen classifications
`PASS_COSMOLOGY_B_L_SCENARIO_CONDITIONAL_AUTHORITY` iff the primary treats Majorana and Dirac as alternative model cases and supplies no source-authorized statistical/physical rule for combining them. Consequence: keep two separate external-ledger branches; no union/intersection may be called a scenario-independent exclusion.

`PASS_COSMOLOGY_B_L_COMMON_COMBINATION_AUTHORITY` iff the primary explicitly prescribes a reproducible combination, preference or supersession rule applicable to the current-CMB constraint. The exact source rule must be recorded verbatim in machine-readable form before any geometry composition.

`BLOCKED_COSMOLOGY_B_L_SCENARIO_SEMANTICS` iff primary text does not establish whether/how the cases may be composed.

`INFRASTRUCTURE_FAIL` only for source acquisition/parser/runtime failure before scientific classification.

## Forbidden
No geometry union/intersection; no choosing the stronger/weaker scenario post hoc; no external assumption that neutrinos are Majorana or Dirac; no BBN addition; no union with 0078c/0079a; no global-envelope or BSM response calculation.

## Next action
A scenario-conditional PASS authorizes keeping both 0080d branches as separate cosmology constraints and then returning to the remaining missing 0071 external families rather than fabricating one cosmology polygon. A common-combination PASS authorizes a separately preregistered composition gate implementing only the source-prescribed rule. BLOCKED retires cosmology composition while preserving both 0080d scenario-conditioned polygons.
