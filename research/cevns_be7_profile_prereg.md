# Prospective contract — Ar-40 CEvNS × physical solar Be7 dominant-line profile

Date frozen: 2026-09-06
Gate: G2 / F3-F7
Purpose: convert iteration 0041 near-boundary kinematics into a physical source-profile detector-rate calculation without changing the microscopic weak interaction.

## Frozen inputs
- Target: pure Ar-40, `Z=18`, `N=22`, atomic-mass convention `39.9623831237 u` as in iteration 0041.
- Weak charge convention: `sin^2(theta_W)=0.23857` and `Q_W=N-(1-4 sin^2 theta_W)Z`.
- Constants: `G_F=1.1663787e-5 GeV^-2`, `1 GeV^-2=0.3893793721e-27 cm^2`, `N_A=6.02214076e23 mol^-1`.
- Source profile: local frozen `data/be7_bahcall1994_ground_profile.csv`, copied byte-for-number from PEANUTS commit `59e3a2ae102d58f42cc1146eaca2cae68be879ce`, source blob `19d97e87e8b03678d2e4629598f7d7fd7794eae0`; physical reference Bahcall, Phys. Rev. D 49, 3923 (1994).
- B16 GS98 total Be7 flux: `4.93e9 cm^-2 s^-1`.
- Dominant ground-state line branch: `0.897`.
- CEvNS is active-flavor neutral-current scattering; do not multiply by electron-neutrino survival probability.
- Primary threshold: `T_thr=40 eV`. Also report sensitivity at `0, 10, 20, 30, 35, 38, 39, 40 eV`.

## Frozen differential response
Use the low-q coherent benchmark

`d sigma/dT = G_F^2 Q_W^2 M/(4 pi) [1 - M T/(2 E_nu^2)]`

in natural units, integrated only over `T_thr <= T <= T_max`, with

`T_max = 2 E_nu^2/(M+2E_nu)`.

This is a low-q ideal CEvNS benchmark. Nuclear form-factor and radiative corrections are not used to tune the result and must not be silently inferred. At the sub-MeV Be7 scale they are expected to be small; a later precision gate may add them prospectively.

## Quantities to report
For each threshold:
1. source minimum neutrino energy `E_min(T_thr)`;
2. fraction of the normalized physical Be7 dominant-line profile with `E>=E_min`;
3. profile-averaged total CEvNS cross section;
4. profile-averaged above-threshold cross section;
5. retained cross-section fraction;
6. ideal events/kg/day for pure Ar-40 under B16 GS98 Be7 flux × 0.897 branch.

## Prospective validation criteria
- Frozen profile trapezoidal normalization must be `1 ± 1e-12`.
- `E_min(40 eV)` must reproduce iteration 0041 value `0.8628609380456526 MeV` within relative `1e-12`.
- `0 < profile_fraction_above_Emin(40 eV) < 1`; otherwise the near-boundary profile premise fails scientifically.
- For every threshold, `0 <= sigma_above <= sigma_total` and event rate must be non-negative.
- Above-threshold cross section and event rate must be monotonically non-increasing as threshold rises.
- Threshold zero must retain cross-section fraction 1 within `1e-12`.
- Raw hosted output and tests must be inspected before scientific classification.

## Classification rules
- If the 40-eV physical-profile rate is positive, classify the metastable/low-threshold branch as a **DETECTION SURVIVOR** at this idealized response level, not as interaction enhancement and not as energy gain.
- If zero within the frozen numerical calculation, classify 40 eV as profile-fold CLOSED; lower-threshold rows remain diagnostics.
- Any signal amplification from a bubble/metastable reservoir remains stored-medium energy and is excluded from neutrino-supplied power.
- Detector efficiency, nucleation efficiency, dark counts and real threshold calibration are OPEN after this gate; the calculated rate is an ideal physics input, not an experimental forecast.
