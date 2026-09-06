# NMIR 0052 preregistration — CRESST-III silicon transfer-function fold

Date: 2026-09-06
Gate: G2 detector-specific recoil transfer
Status at preregistration: OPEN

## Question
How much of the ideal 10-eV Si28 full-solar CEvNS rate survives when folded through detector-response anchors actually published for the CRESST-III 0.35-g silicon calorimeter?

## Frozen physics inputs
Use the exact same NMIR authority as iteration 0045/0049:
- exact-mass Si28 target from `data/cevns_target_candidates_exact_mass.csv`;
- B16-GS98 fluxes from `data/solar_flux_b16.csv`;
- pinned pp/hep/B8/CNO spectra + local thermally broadened Be7 profile;
- standard weak charge and Helm form factor from `src/nmir/cevns_solar_optimize.py`;
- analysis recoil floor `T >= 10.0 eV`.

Frozen ideal reference from 0049: `Si28_10eV = 4.3476963498860904e-3 events/(kg day)`.

## Frozen detector anchors
Primary source: CRESST Collaboration, G. Angloher et al., Phys. Rev. D 107, 122003 (2023), arXiv:2212.12513.

Published injected-pulse results:
- fitted trigger 50%-point `E50 = 10.0 eV_nr`;
- baseline resolution/turn-on width `sigma = 1.36 eV_nr`;
- trigger plateau including dead-time loss `p_trigger_plateau = 0.8053`;
- trigger efficiency at E50 is therefore ~0.40265, consistent with the paper's quoted 40.3%;
- cumulative trigger+cuts survival is flat above 14 eV at `p_all_plateau = 0.6591`.

The paper does not provide an analytic parametrization of the full green cumulative efficiency below 14 eV in its text. Therefore NMIR MUST NOT call a factorized extrapolation there 'measured full efficiency'.

## Frozen response functions
Measured trigger-turn-on model from the published error-function fit:

`epsilon_trigger(T) = 0.8053 * 0.5 * [1 + erf((T - 10.0 eV)/(sqrt(2)*1.36 eV))]`.

For `T < 10 eV`, the analysis floor sets accepted efficiency to zero in this gate.

Define a clearly labelled factorized analysis surrogate, not a measured full curve:

`epsilon_surrogate(T) = epsilon_trigger(T) * (0.6591/0.8053)` for `T >= 10 eV`.

This assumes the non-trigger cut survival ratio is energy-independent down to threshold. That assumption is only a technology-gap surrogate; it is directly supported only by the published plateau above 14 eV.

## Frozen outputs
For Si28 full-solar CEvNS compute:
1. hard-step 10-eV ideal rate using the new differential-fold integrator;
2. trigger-folded rate;
3. factorized-surrogate folded rate;
4. each rate divided by the 0049 ideal rate;
5. effective kg required for 10 accepted events/year (`365.25 d/yr`);
6. expected events/year for the actual 0.35-g CRESST target, for scale only.

## Scientific PASS criteria
All must hold:
1. New hard-step integrator reproduces the frozen 0049 Si28 ideal rate within relative tolerance `5e-3`.
2. `0 < R_surrogate < R_trigger < R_ideal`.
3. Trigger-folded rate is <= `0.8053 * R_ideal` (because the trigger efficiency never exceeds its measured plateau).
4. Surrogate/trigger rate ratio reproduces the frozen plateau ratio `0.6591/0.8053` to relative tolerance `1e-10`.
5. All event-rate/mass outputs are finite and positive.

If all pass: `PASS_CRESST_SI_TRANSFER_FOLD`.

## Scientific interpretation guard
PASS means only that a detector transfer anchored to a real 10-eV calorimeter can be quantitatively folded into NMIR. It does NOT mean CRESST has observed solar CEvNS, that its current low-energy excess/background satisfies 0050/0051, or that the factorized surrogate is a measured full efficiency curve.

## Scientific FAIL
Retain any failure of the frozen criteria. Do not change the threshold, plateau factors, resolution or tolerance after seeing the result.

## Infrastructure FAIL
Pinned spectrum download/package/runner failures may be repaired minimally without changing the frozen scientific inputs.

## Next action after PASS
Compare the required mass and accepted-background budget with the actual CRESST 0.35-g exposure/background regime, then define the technology scaling gap (mass x background x stability). Separately search whether a public machine-readable/digitizable full Fig. 3 survival curve exists; if not, keep the below-14-eV full-cut transfer uncertainty explicit.