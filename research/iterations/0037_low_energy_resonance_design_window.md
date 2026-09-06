# Iteration 0037 — low-energy resonance design window

Date: 2026-09-06
Gate: G8 resonance kinematics/design requirement
Prospective contract: `research/low_energy_resonance_window_prereg.md`

## Funnel choice
This iteration follows the discovery funnel rather than an isotope scan. After the RIOEC source/flavor and area/profile closure (0035) and the real Glashow-resonance positive control (0036), the highest-value OPEN prerequisite was to map the kinematic window any low-energy resonance must occupy before target-specific entrance-strength ranking is allowed.

F0: interface/detection/capture design constraint only; no deposited-power claim.
F1: resonant inverse transition / stationary-electron s-channel control.
F2: production↔absorption is not yet target-specific here.
F3: this iteration closes the kinematic/source-overlap design window.
F4–F8: existence, quantum numbers, coupling/entrance strength, physical source density and constraints remain OPEN.
F9: no gain multiplication.
F10: constructive PASS for the kinematic design constraint only.

## Hosted validation
Scientific head: `0589b99e2d5d985fa02a7042473dc0c7c27a1def`.
Hosted run: `34044012213`.
Job: `101515715322`.
Raw log inspected, not inferred from green status.
Regression result: `7 passed in 0.02s`.
Artifact: `9992535787` (`low-energy-resonance-window-result`).
Artifact ZIP SHA256: `1fbb5a1d346c81e39264d0b86915496a9e6fbbbeea9729075ec2e90336e714ac`.

## A. Stationary-electron s-channel mapping
For a negligibly massive incident neutrino/antineutrino on an electron at rest,

`M_* = sqrt(m_e^2 + 2 m_e E_nu)`

with `m_e=0.51099895 MeV`.

The independent Glashow calibration using `M_W=80.4 GeV` gives

`E_res = 6.3250227811 PeV`,

only `0.3972%` above the 6.3-PeV control and therefore inside the prospectively frozen 2% tolerance.

The source-to-required-mass mapping is:

| source control | E_nu | required M_* | M_*-m_e |
|---|---:|---:|---:|
| thermal control | 10 eV | 0.5110089499 MeV | 0.0099999 keV |
| thermal control | 1 keV | 0.5119979734 MeV | 0.9990234 keV |
| pp endpoint | 0.420 MeV | 0.8308784778 MeV | 319.8795 keV |
| Be7 line | 0.8618 MeV | 1.0685867850 MeV | 557.5878 keV |
| pep line | 1.442 MeV | 1.3171335918 MeV | 806.1346 keV |
| NMIR solar ceiling | 20 MeV | 4.5498437255 MeV | 4.0388447755 MeV |

Therefore a stationary-electron s-channel resonance overlapping the frozen 0–20 MeV solar window would require an intermediate-state mass in

`0.51099895 < M_* <= 4.5498437255 MeV`.

For the thermal-solar 10 eV–5 keV subwindow the mass must lie only about 0.010–4.976 keV above the electron mass:

`0.5110089499 <= M_* <= 0.5159747246 MeV`.

This is kinematics only. No such Standard-Model state is asserted; BSM remains LOCKED.

## B. RIOEC tuning window
For RIOEC,

`E_R = -Q_epsilon + E_x + E_b`.

The prospectively frozen thermal-solar design window is `0 < E_R <= 5 keV`; the generic below-IBD window is `0 < E_R < 1.8 MeV`.

If the nuclear/atomic terms are individually of order 1 MeV, their required relative cancellation is roughly:
- 10 eV resonance: `1e-5`;
- 1 keV resonance: `1e-3`;
- 5 keV resonance: `5e-3`.

This is not a no-go: the RIOEC candidate list demonstrates that such level combinations are a real target-selection problem. It is instead a sharp F3 design condition that must be met before F4/F7 ranking.

## C. No peak-cross-section promotion
Iteration 0025/0035 remains controlling: for a continuous source, narrowing a resonance does not create integrated entrance strength. Passing the energy-window condition alone never yields a rate. A target-specific RIOEC score still requires evaluated entrance strength/area `B0`, physical shell/nuclear widths and a primary thermal-solar `anti-nu_e` spectral density at `E_R`.

## Classification
`G8_LOW_ENERGY_RESONANCE_WINDOW_PASS`.

Scientific interpretation: the low-energy resonance branch is now kinematically delimited. Ordinary solar-energy s-channel resonances on stationary electrons would require a state between the electron mass and ~4.55 MeV; the thermal-solar subwindow requires a state within only ~5 keV of `m_e`. RIOEC instead requires a nuclear/atomic cancellation that places `E_R` inside the physical thermal-antineutrino spectrum.

This result does **not** unlock BSM, does **not** establish a useful absorber and does **not** modify the SM W/kg ceiling.

## Exact next funnel gate
Return to the highest-value surviving G8 physical-rate gate: freeze a **primary thermal-solar electron-antineutrino spectral density** and one **evaluated RIOEC candidate** with `Q_epsilon`, daughter excitation, captured-shell binding/width and weak entrance strength. Then compute `B0 * phi_anti-nu_e(E_R)`, events/kg/s and neutrino-only W/kg without multiplying any other unvalidated gain.
