# Preregistration 0092a — G9 cross-section authority for solar transmission

Date frozen: 2026-09-08
Parent density/column result: `research/iterations/0092_g9_model_s_solar_column_authority_pass.md`, record commit `dab1a5c0ea08c4d2dcbcdc53947027b9d18be21c`, classification `PASS_G9_0092_MODEL_S_COLUMN_AUTHORITY`.
Parent transmission contract: `research/prereg/0092_g9_solar_transmission_authority.md`.

## Question
Can the Standard-Model interaction cross-section authority needed to convert the validated 0092 Model-S column into source-regime optical depths be frozen reproducibly without extrapolating an inapplicable interaction model across energy regimes?

This is an authority gate. It may compute conservative optical-depth sentinels only where the cited measurement/review directly supports the required cross section or a one-sided bound. It must not silently complete the MeV branch with a DIS formula and must not infer practical source realizability.

## Frozen solar column
Use only the validated 0092 value

`N_N = 1.7659857664161126e36 nucleons cm^-2`

for the `b/Rsun=0.024` reference chord. No alternate solar model/column is allowed in this subgate.

## Frozen high-energy authority
Primary direct TeV sentinel:
- FASER Collaboration, `First Measurement of the nu_e and nu_mu Interaction Cross Sections at the LHC with FASER's Emulsion Detector`, PRL 133, 021802 (2024), arXiv:2403.12520.
- For nu_mu, reported charged-current cross-section coefficient over `520–1760 GeV`: `(0.5 +/- 0.2)e-38 cm^2 GeV^-1`.
- For a deliberately conservative one-sided opacity sentinel at the frozen NGC-1068 low endpoint `E=1.5 TeV`, use the reported central-minus-1sigma coefficient `0.3e-38 cm^2 GeV^-1`, giving `sigma_CC_lower = 0.3e-38 * E_GeV`.

This 1.5-TeV point lies inside the reported FASER nu_mu energy interval; no energy extrapolation is allowed for this direct sentinel.

Independent high-energy consistency authority:
- Cooper-Sarkar, Mertsch & Sarkar, JHEP 08 (2011) 042, arXiv:1106.3723v2, for Standard-Model high-energy nu/antinu CC+NC predictions and uncertainties.
- IceCube, Nature 551 (2017), arXiv:1711.08119, direct Earth-absorption cross-section measurement over `6.3–980 TeV`, reported as consistent with the Cooper-Sarkar et al. Standard-Model prediction.

For the `290 TeV` TXS sentinel, 0092a may establish only a conservative opacity lower bound by using the already-directly-supported 1.5-TeV CC lower sentinel as a floor if, and only if, the cited Standard-Model authority explicitly supports that the inclusive CC cross section does not decrease between 1.5 and 290 TeV. Otherwise the 290-TeV numerical optical depth remains `BLOCKED_G9_0092A_HIGH_ENERGY_AUTHORITY` pending an exact tabulated value.

## Frozen MeV authority rule
The `5–50 MeV` CCSN branch must use a low-energy weak-interaction authority (e.g. the Formaggio-Zeller cross-section review plus primary low-energy channel authority) and must account for the fact that coherent nuclear scattering can exceed an incoherent per-nucleon estimate. A DIS `sigma proportional E` formula is forbidden.

A MeV `PASS_G9_SOLAR_TRANSMISSION_THIN` requires an authority-backed conservative *upper bound on total interaction optical depth* at every frozen endpoint needed to cover `5–50 MeV`, including coherent nuclear scattering where relevant to solar composition. If such an upper bound cannot be made reproducible from available composition/channel authority, classify the MeV branch `BLOCKED_G9_0092A_MEV_TOTAL_CROSS_SECTION_AUTHORITY`; do not guess a composition.

## Frozen calculations
For every accepted cross-section sentinel,

`tau = N_target * sigma`

and

`T0 = exp(-tau)`.

For a nucleon-normalized CC cross section use `N_target=N_N`.

The FASER 1.5-TeV conservative lower sentinel is frozen exactly as

`E = 1500 GeV`
`sigma_CC_lower = 0.3e-38 * 1500 cm^2`
`tau_CC_lower = N_N * sigma_CC_lower`.

No post-result change of the uncertainty multiple or energy is permitted.

## Frozen classification
- `PASS_G9_0092A_CROSS_SECTION_AUTHORITY` only if all source-regime cross-section inputs required by 0092 are reproducibly authoritative.
- A source regime may independently classify `SCIENTIFIC_FAIL_G9_TRANSPARENT_SUN_ASSUMPTION` when an authority-backed *lower* interaction optical depth satisfies `tau >= 1`.
- A source regime may independently classify `PASS_G9_SOLAR_TRANSMISSION_THIN` only when an authority-backed *upper* total optical depth satisfies `tau <= 0.1` throughout its frozen interval.
- `BLOCKED_G9_0092A_MEV_TOTAL_CROSS_SECTION_AUTHORITY` if the MeV total upper bound cannot be made reproducible without an un-frozen solar-composition/channel assumption.
- `BLOCKED_G9_0092A_HIGH_ENERGY_AUTHORITY` if an exact/direct high-energy input required for a claimed classification is unavailable.
- `INFRASTRUCTURE_FAIL_G9_0092A` only for execution/download/tool failure.

Gate-level classification may be mixed. A TeV opacity failure does not invalidate the MeV CCSN branch or gravitational focusing in general.

## PASS/BLOCKED consequences
A validated TeV `tau>=1` closes only the transparent/unattenuated-Sun assumption for that frozen high-energy source regime/ray. It does not erase the 0090f geometry PASS.

If the MeV branch is BLOCKED, the next gate must freeze solar composition and low-energy channel accounting prospectively before any thinness claim. No post-hoc composition choice is allowed.

## Guards
No detector PSF as source morphology. No EM size as neutrino size. No fourth 0091 source. No DIS extrapolation into MeV. No multiplication of focusing magnification by detector/material/BSM gain. No cross-section threshold relaxation after seeing `tau`.
