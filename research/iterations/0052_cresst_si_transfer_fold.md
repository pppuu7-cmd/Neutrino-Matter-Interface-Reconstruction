# Iteration 0052 — CRESST-III silicon transfer-function fold

Date: 2026-09-06
Gate: G2 detector-specific recoil transfer
Classification: `PASS_CRESST_SI_TRANSFER_FOLD`

## Frozen authority
Prospective contract: `research/prereg/0052_cresst_si_transfer_fold.md`.
Prereg commit: `72a089483f001fa4ee8383d8f8d0914ddc0ec134`.
Initial scientific implementation head: `716dfc553b20d9cadecf0a306b58dc473c1a5b32`.
First dedicated hosted run/job: `34058821939 / 101555544155` — infrastructure FAIL after `5 passed`; benchmark raised `KeyError: 'Be7_ground'` before any scientific result because a special Be7 flux mapping was evaluated after a generic dictionary lookup.
Minimal infrastructure repair: source commit `c2a359eecb4596bafd3291f4aa31cca97b544da9`; regression-test commit/final scientific head `fb5cd82686006ba9c8134fac2b6dfbc9a879c079`. Frozen detector/physics inputs and PASS criteria were unchanged.
Authoritative rerun/job: `34058921851 / 101555813480`.
Artifact: `9996833564`, `cresst-si-transfer-result`.
Artifact ZIP SHA256: `67fd30cfca7e3321c4818a0a7d62343cbbdad2ca49e339dc12772ce6ad7df118`.
Raw hosted log inspected: `6 passed`; fail-closed benchmark status PASS.

## Experimental anchors
Primary source: CRESST Collaboration, G. Angloher et al., Phys. Rev. D 107, 122003 (2023), arXiv:2212.12513.
Frozen anchors:
- target module mass: `0.35 g` Si;
- fitted trigger 50%-point: `10.0 eV_nr`;
- baseline/turn-on width: `1.36 eV_nr`;
- trigger plateau: `0.8053`;
- cumulative trigger+cuts plateau above 14 eV: `0.6591`.

The paper text does not provide an analytic parametrization of the full cumulative efficiency below 14 eV. Therefore the full-cut response below 14 eV is not called measured in NMIR.

Measured trigger model:
`epsilon_trigger(T) = 0.8053 * 0.5 * [1 + erf((T-10 eV)/(sqrt(2)*1.36 eV))]`.

Explicitly labelled surrogate:
`epsilon_surrogate(T) = epsilon_trigger(T) * 0.6591/0.8053` for `T>=10 eV`.

## Results
Frozen ideal Si28 10-eV full-solar rate from 0049:
`R_ideal = 4.3476963498860904e-3 events/(kg day)`.

New differential hard-step fold exactly reproduced it:
`R_hard = 4.3476963498860904e-3 events/(kg day)`, relative error `0.0`.

Published-trigger fold:
- `R_trigger = 3.4252750501524354e-3 events/(kg day)`;
- retained fraction `R_trigger/R_ideal = 0.7878367702110055`;
- effective mass for 10 accepted events/year: `7.993083028500904 kg`;
- expected events/year in the actual 0.35-g module: `4.3787859922386193e-4`.

Factorized all-cuts surrogate:
- `R_surrogate = 2.8034257861113496e-3 events/(kg day)`;
- retained fraction `R_surrogate/R_ideal = 0.6448071715460992`;
- effective mass for 10 accepted events/year: `9.766089763088724 kg`;
- expected events/year in the actual 0.35-g module: `3.583829439320097e-4`.

Frozen plateau ratio:
`0.6591/0.8053 = 0.8184527505277537`.
The integrated surrogate/trigger rate ratio is `0.8184527505277536`, relative error `1.11e-16`.

Dominant contribution remains Be7_ground in all three folds. In the surrogate fold it contributes `2.017889605e-3 events/(kg day)` out of total `2.803425786e-3`.

## Frozen criteria audit
1. Hard-step rate reproduces 0049 within 5e-3: PASS, exact within printed precision.
2. `0 < R_surrogate < R_trigger < R_ideal`: PASS.
3. `R_trigger <= 0.8053 R_ideal`: PASS.
4. Surrogate/trigger ratio equals frozen plateau ratio within 1e-10: PASS (`1.11e-16`).
5. All rate/mass outputs finite and positive: PASS.

## Scientific interpretation
The 10-eV threshold is not the main acceptance loss: the published trigger curve still retains about 78.8% of the ideal Si28 rate above the frozen 10-eV analysis floor. A conservative factorized all-cuts surrogate retains about 64.5%, implying a detector-scale target of order 9.8 effective kg for 10 accepted events/year if the same transfer could be preserved at scale.

The present 0.35-g module is smaller than that surrogate effective mass by a factor of about `27903`; its expected solar-CEvNS count in this rate-only surrogate is only `3.58e-4/year`.

This is a detector-acceptance positive control, not evidence of solar CEvNS observation, not evidence that current CRESST low-energy backgrounds satisfy NMIR, and not weak-interaction or neutrino-energy enhancement.

## Exact next gate
Quantify the technology scaling gap using the same CRESST primary source: actual target mass/exposure and observed low-energy event regime versus the 0050/0051 accepted-background requirements. Keep raw low-energy event rate distinct from analysis-indistinguishable nuclear-recoil background. If the publication does not permit a defensible mapping to the latter, report an empirical raw-rate gap plus an explicit discrimination requirement rather than relabeling every event as background.