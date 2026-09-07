# Preregistration 0080c — conservative current-CMB observational semantics

Date frozen: 2026-09-07
Parent: 0080b `PASS_COSMOLOGY_B_L_CMB_AXIS_CALIBRATION`.

## Question
Before inspecting or selecting any vector contour geometry, does the exact primary Esseili–Kribs v2 source authorize a conservative hard-exclusion convention for the current CMB constraint, and does it unambiguously map the Delta N_eff levels to the figure colors for both Majorana and Dirac panels?

## Frozen source
arXiv `2308.07955v2`, exact archive SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`, main TeX `neff_arXiv_v2.tex`.

## Frozen conservative rule
The source has already been identified, before any contour-path extraction, as stating current Planck sensitivity around `Delta N_eff = 0.3-0.4` depending on dataset and later calling a `0.3-0.4` 95% C.L. analysis conservative. To avoid dataset/result cherry-picking, this gate prospectively chooses the weaker/high endpoint:

**hard current-CMB exclusion threshold: `Delta N_eff >= 0.4` at 95% C.L.**

The interval `0.3 <= Delta N_eff < 0.4` is not treated as a hard exclusion in NMIR; it may be recorded only as strongly disfavored if that wording is confirmed by the primary source.

## Frozen textual checks
The exact main TeX must contain, in the relevant CMB discussion/captions:
1. `Current constraints from Planck data exclude` and the numerical range `0.3-0.4`, with dataset dependence stated;
2. a later `conservative analysis` statement containing the same `0.3-0.4` range and `95% C.L.`;
3. an explicit statement that dark and light blue regions are ruled out and the green region is strongly disfavored;
4. Fig. 5 source caption maps the ordered Delta N_eff levels `0.05, 0.1, 0.2, 0.3, 0.4, 0.5` to `(pink), (red), (orange), (green), (light blue), (dark blue)` respectively;
5. Fig. 6 states it is the same convention as Fig. 5 for the Dirac case.

## Classification
`PASS_COSMOLOGY_B_L_CMB_CONSERVATIVE_95CL_SEMANTICS` iff all five textual checks pass on the pinned primary source.

`BLOCKED_COSMOLOGY_B_L_CMB_OBSERVATIONAL_SEMANTICS` if any check is absent or ambiguous. No substitution from a secondary source is allowed inside this gate.

## Consequence of PASS
PASS authorizes a separately preregistered geometry gate to materialize only the **light-blue plus dark-blue (`Delta N_eff >= 0.4`)** regions in Majorana and Dirac panels. Green (`0.3-0.4`) must not be included in the hard excluded polygon.

## Forbidden
No vector path/color extraction in this gate; no manual figure reading; no interpolation between 0.3 and 0.4; no scenario union/intersection; no combination with BBN, fifth-force, solar-CEvNS or other B-L constraints; no response/enhancement scan.
