# NMIR 0053 preregistration — CRESST low-energy-excess scaling/rejection gap

Date: 2026-09-06
Gate: G2 detector background / scaleability
Status at preregistration: OPEN

## Question
If the central low-energy-excess (LEE) spectrum reported for the 0.35-g CRESST-III silicon module were naively preserved per kg when scaling the 0052 detector-transfer surrogate to the mass required for 10 accepted solar-CEvNS events/year, what accepted-event rejection/discrimination factor would be required to satisfy the 0051 discovery-background budgets?

This is deliberately a **stress extrapolation**, not a prediction that the LEE scales linearly with detector mass or persists unchanged in future detector designs.

## Frozen primary experimental inputs
Primary source: CRESST Collaboration, G. Angloher et al., Phys. Rev. D 107, 122003 (2023), arXiv:2212.12513.

For the low-energy spectrum below 300 eV, the paper fits the efficiency-corrected event-rate spectrum with

`f(E) = A E^{-alpha} + B E^{-beta}`

with E in keV and f in counts/(keV kg day), and reports central values:
- `A = 7.6e-2 (keV^(1-alpha) kg day)^-1`
- `alpha = 5.02`
- `B = 7.2e2 (keV^(1-beta) kg day)^-1`
- `beta = 2.22`.

The paper states:
- detector target mass `0.35 g`;
- gross blind-data exposure `55.06 g day`;
- events above threshold surviving selection are conservatively treated as possible recoil signals in the DM analysis;
- the LEE rises sharply below 300 eV and its origin remains unknown;
- ordinary noise triggers are negligible above the chosen threshold;
- because this Si module is non-scintillating, this analysis does not supply event-by-event ER/NR discrimination analogous to the scintillating CRESST modules.

## Frozen NMIR transfer/background inputs
From 0052:
- analysis window lower edge `10 eV = 0.010 keV`;
- upper edge `300 eV = 0.300 keV`, matching the published linear-response/LEE fit range;
- factorized all-cuts surrogate efficiency
  `epsilon_sur(T) = 0.6591 * 0.5 * [1 + erf((T_eV - 10)/(sqrt(2)*1.36))]`;
- Si mass required for exactly 10 accepted solar-CEvNS events/year under this surrogate:
  `M10 = 9.766089763088724 kg`.

From 0051, for `S=10 accepted/year`, freeze the accepted indistinguishable-background ceilings:
- 3σ, delta_B=30%: `Bmax = 4.274968302863348 /year`;
- 5σ, delta_B=30%: `Bmax = 1.0806120114381677 /year`;
- 5σ, delta_B=50%: `Bmax = 0.692094879071742 /year`.

## Frozen computation
Numerically integrate over E in `[0.010,0.300] keV`:

`R_LEE,corr = integral f(E) dE`

and the estimated **accepted** event-rate stress using the same 0052 surrogate:

`R_LEE,acc = integral f(E) epsilon_sur(E) dE`.

Use deterministic log-spaced quadrature dense enough that doubling the number of points changes `R_LEE,acc` by <= `1e-5` relative.

Then compute:
- expected accepted LEE count in the published blind exposure `0.05506 kg day`;
- accepted LEE rate per kg-year (`365.25 d/year`);
- stress-extrapolated accepted LEE count/year at `M10`;
- required rejection factor `F_rej = N_LEE(M10)/Bmax` for each frozen discovery target;
- equivalent required surviving fraction `1/F_rej`.

## Scientific PASS criteria
All must hold:
1. Integrated central-fit rates are finite/positive.
2. Dense-grid convergence of `R_LEE,acc` is <= `1e-5` relative on point-doubling.
3. `0 < R_LEE,acc < R_LEE,corr`.
4. At the scaled `M10`, all frozen discovery targets require `F_rej > 1`.
5. No claim is made that the central LEE fit is a physical background model or that LEE scales linearly with mass.

If all pass: classify `PASS_LEE_SCALING_GAP_STRESS`.

## Interpretation guard
The relevant output is a **technology/rejection stress factor** under a clearly frozen extrapolation. It is not a statement that future kg-scale Si calorimeters must have the same LEE rate. Conversely, because the present paper treats all surviving events as possible recoil signals, the LEE cannot simply be ignored in a neutrino-discovery design without a new discriminant, source elimination, spectral/time model, or demonstrated reduction.

## Scientific FAIL
Retain any failure of the frozen numerical/logic criteria. Do not change the window, fit central values, transfer surrogate, scaled mass, or background ceilings after seeing the result.

## Infrastructure FAIL
Numerical/package/runner/artifact failures may be repaired without changing frozen science inputs.

## Next action after PASS
Separate the required improvement into three independent levers: (i) intrinsic LEE reduction per kg, (ii) event-by-event or statistical discrimination/rejection, and (iii) exposure/mass architecture. Search newer primary CRESST/SOS results for demonstrated changes in LEE per kg and whether an improved detector design suppresses the excess; do not assume linear scaling is unavoidable.