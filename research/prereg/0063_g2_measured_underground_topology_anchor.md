# NMIR preregistration 0063 — measured underground low-energy rejection × bulk-acceptance anchor

Date frozen: 2026-09-07
Status at freeze: PROSPECTIVE / NO RESULT-DEPENDENT CLASSIFICATION INSPECTED
Parent authority: iteration 0058 leaves `PUBLIC_ACHIEVEMENT_ANCHOR_OPEN`; iteration 0062 retires naive coefficient-independent finite-l unitarity as a useful G3 closure route, making the independent G2 achievement anchor the highest-value OPEN gate.

## Scientific question
Does the public primary underground detector literature contain a **measured**, quantitatively comparable low-energy background/topology rejection factor paired with a measured CEvNS-like bulk nuclear-recoil acceptance in a threshold window relevant to NMIR, strong enough to compare directly with the 0058 required envelope?

This is an achievement/technology evidence gate, not another algebraic requirement map.

## Frozen NMIR requirement comparator
Use iteration 0058 exactly as authority. At full signal acceptance, required additional rejection is

`R_req ≈ 1.44e7–1.78e7`.

At 50% fixed-exposure signal acceptance it is `9.41e7–1.11e8`; at 30% it is `4.58e8–5.25e8`.

Do not recompute or weaken these values in this gate.

## Evidence inclusion criteria
A candidate public result qualifies as a directly comparable measured anchor only if all are available from the same detector/configuration or an explicitly calibrated transfer within one collaboration analysis:
1. underground/low-background operation relevant to the quoted background population;
2. measured energy/threshold window overlapping or meaningfully adjacent to the sub-keV low-energy region, with exact window reported;
3. a measured pre-selection/background population and measured post-selection surviving population or an explicitly quoted rejection/leakage probability;
4. a measured bulk nuclear-recoil/CEvNS-like signal acceptance for the same selection or a directly calibrated NR proxy;
5. exposure/live-time normalization sufficient to distinguish raw trigger suppression from accepted-background rejection;
6. statistical confidence/upper-limit treatment when zero survivors are reported;
7. no projection-only, simulation-only, above-ground-only, or unmatched-detector factor is promoted to measured underground achievement.

Topology demonstrations without a detector-wide rejection factor are recorded separately as mechanism evidence only.

## Frozen comparison quantities
For every qualifying anchor report:
- `R_meas = N_before / N_after` when both are measured and definitions are compatible, or the collaboration-quoted rejection factor;
- `epsilon_NR` = measured acceptance of bulk nuclear recoils or calibrated proxy under the same cut;
- `F_meas = R_meas` at the quoted `epsilon_NR`; do not divide by acceptance to manufacture rejection;
- gap to 0058 full-acceptance requirement: `G = R_req,min / R_meas` and `R_req,max / R_meas`.

If only leakage probability `p_leak` is quoted, use `R_meas=1/p_leak` with its confidence interval. If zero survivors occur, use only the collaboration's stated confidence interval or a prospectively frozen Poisson upper bound; do not call it infinite rejection.

## Prospective classifications
1. `PASS_PUBLIC_UNDERGROUND_ANCHOR_MEETS_0058`
   - at least one directly comparable measured underground anchor has `R_meas >= 1.44e7` while retaining a measured NR/bulk acceptance consistent with the comparator, with no hidden projection/simulation factor.

2. `PASS_PUBLIC_UNDERGROUND_ANCHOR_BELOW_REQUIREMENT`
   - at least one directly comparable measured anchor exists, but all are quantitatively below 0058; report the best measured rejection, acceptance and exact gap.

3. `BLOCKED_PUBLIC_ACHIEVEMENT_ANCHOR`
   - primary literature contains mechanisms/thresholds/background studies but no result satisfying the inclusion criteria strongly enough for a direct rejection×acceptance comparison.

4. `FAIL_EVIDENCE_MAPPING`
   - an initially considered factor is found to mix incompatible populations, detector configurations, above-ground vs underground operation, raw trigger suppression vs accepted background, or simulated vs measured acceptance.

## Mandatory guards
- Do not combine rejection from one detector with acceptance from another.
- Do not multiply independent cuts unless the collaboration measures the combined leakage/acceptance or the correlation is explicitly calibrated.
- Do not treat a threshold as an NR efficiency curve.
- Do not treat a topology handle as a rejection factor.
- Do not treat projected future performance as achieved performance.
- Do not infer infinite rejection from zero observed leakage.
- Do not count raw site trigger-rate reduction as accepted indistinguishable-background rejection.
- Do not change the 0058 requirement comparator.

## Evidence/provenance
Prefer primary collaboration papers, official data releases/supplements, and detector theses only when they contain calibration information absent from the paper. Freeze a machine-readable authority ledger in `data/` with DOI/arXiv/publication identifiers, detector/configuration, operating environment, threshold/window, rejection, acceptance, measurement/projection status, and exact quoted provenance.

## PASS/FAIL next action
- If a measured anchor meets 0058, move G2 from achievement-blocked to experimentally demonstrated survivor and prospectively fold its actual `epsilon_NR(T,state)`, threshold distribution, live/reset dynamics and calibrated backgrounds.
- If a measured anchor exists but is below requirement, quantify the exact remaining technology gap and then return to the next independent OPEN gate.
- If blocked, record the blocker without inventing a factor and move to G8 source/entrance-strength provenance audit or the next class-level residual.
