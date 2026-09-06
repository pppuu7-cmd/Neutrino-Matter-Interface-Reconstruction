# NMIR 0054 preregistration — CRESST LEE mitigation evidence gate

Date: 2026-09-06
Gate: G2 demonstrated LEE suppression/discrimination
Status at preregistration: OPEN

## Question
Do newer primary CRESST measurements provide a quantitatively defensible reduction/rejection factor that can be multiplied into the 0053 CRESST-Si LEE scaling stress, or do they currently establish only a physical discrimination/mitigation mechanism without enough comparable data to close the numerical gap?

## Frozen authorities
1. CRESST Collaboration, G. Angloher et al., *DoubleTES detectors to investigate the CRESST low energy background: results from above-ground prototypes*, Eur. Phys. J. C 84, 1001 (2024), DOI 10.1140/epjc/s10052-024-13282-8, arXiv:2404.02607.
2. CRESST Collaboration, G. Angloher et al., *The CRESST experiment towards the next generation of sub GeV direct dark matter detection*, Communications Physics (2026 version of 2025 preprint), DOI 10.1038/s42005-025-02476-5, arXiv:2505.01183.
3. CRESST Collaboration, G. Angloher et al., *First observation of single photons in a CRESST detector and new dark matter exclusion limits*, Phys. Rev. D 110, 083038 (2024), DOI 10.1103/PhysRevD.110.083038, arXiv:2405.06527, only as a low-threshold/SOS cross-check; do not infer a comparable LEE suppression factor unless the same normalization/window can be frozen.

## Frozen evidence criteria
A **measured quantitative reduction factor** may be promoted into the 0053 technology-gap product only if a primary source supplies enough information to reconstruct, without figure-only eyeballing or private data:
- a common or transformable energy interval;
- exposure/mass normalization or directly normalized rates;
- pre/post selection or configuration counts/rates;
- the relevant selection definition;
- a defensible signal/bulk acceptance or survival probability.

Qualitative phrases such as “significantly reduces,” planned/forecast reduction factors, or a cut boundary without pre/post counts are not sufficient for a measured multiplicative suppression factor.

## Frozen observed facts to audit
DoubleTES 2024:
- event-by-event two-sensor readout distinguishes a diagonal bulk population from low-energy single-TES populations;
- conservative absorber/bulk selection requires the two sensor energies to differ by no more than 35%;
- the paper says this cut significantly reduces near-threshold events;
- a single-TES LEE component can in principle be tagged efficiently;
- an absorber-band LEE component remains and shows a measured time constant `10.2 ± 1.1 d` in the above-ground campaign;
- datasets/code are available only on reasonable request, not as a public machine-readable table in the paper.

Next-generation CRESST report:
- DoubleTES is foreseen as the future baseline because it can reject the LEE component originating in a single TES;
- maintaining stable cryogenic conditions is expected to reduce LEE;
- projections state approximately 10× reduction after ~450 d and 100× after ~900 d;
- the report explicitly treats 10× and 100× as benchmark/projection reduction factors, not as already demonstrated detector-wide measured suppression in the 0053 Si configuration.

## Frozen numerical stress comparison
Use the authoritative 0053 total reduction/rejection requirement for `S=10/year`, 5σ, 30% background-normalization nuisance:
`G0053 = 4.1485517170734453e9`.

For projection-only factors `R={10,100}`, report the residual improvement requirement `G0053/R` and do not label the projection as measured.

## Classification logic
- If a primary source satisfies all quantitative comparability criteria: `PASS_MEASURED_LEE_MITIGATION_FACTOR`, with a frozen measured factor and residual gap.
- If a mechanism is experimentally demonstrated but no comparable measured factor is reconstructible: `MECHANISM_SURVIVOR_QUANTITATIVE_GAP_OPEN`.
- If no physical discrimination/mitigation handle is experimentally demonstrated: `FAIL_NO_LEE_MITIGATION_HANDLE`.

## Guard
This gate does not assume the 0053 linear-per-kg LEE stress is a prediction. It only asks how much of that deliberately severe gap can be retired by demonstrated evidence. Projection factors and private/on-request datasets do not count as measured public suppression.

## Exact next action
If `MECHANISM_SURVIVOR_QUANTITATIVE_GAP_OPEN`, use the measured DoubleTES topology and time dependence to formulate the next experiment/design requirement: what intrinsic reduction and/or classification performance would have to be demonstrated to bridge the remaining gap, and whether a segmented multi-module coincidence/time-likelihood architecture can supply orthogonal rejection without sacrificing solar-CEvNS acceptance.