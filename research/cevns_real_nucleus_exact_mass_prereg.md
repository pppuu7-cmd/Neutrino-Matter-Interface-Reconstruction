# Prospective contract — corrected real-nucleus full-solar CEvNS optimization with exact isotope masses

Date frozen: 2026-09-06
Iteration: 0045
Gate: G2 / F3–F7
Purpose: rerun the 0044 real-nucleus full-solar target optimization after the prospectively detected failure of the `M=A m_u` approximation at the Ar-40/Be7 40-eV endpoint.

## Frozen correction and why it is allowed
Iteration 0044 remains a scientific/approximation FAIL; its 1% criterion is not changed. The sole physics correction in 0045 is to replace `M=A m_u` by the exact frozen NIST atomic isotope mass `atomic_mass_u * u` for every candidate, both in recoil kinematics and targets/kg.

Local mass authority: `data/cevns_target_candidates_exact_mass.csv`.
Provenance: `data/cevns_target_exact_mass_provenance.md`.
NIST central masses are frozen before any corrected ranking is inspected.

## Everything else remains frozen from 0044
- B16 GS98 flux authority: `data/solar_flux_b16.csv`.
- Spectrum provenance: `data/solar_spectrum_manifest.csv`.
- Sources: pp, hep, Ortiz B8, N13, O15, F17, physical Be7 ground/excited profiles with 0.897/0.103 branch weights, pep line 1.442 MeV.
- Every external spectrum must match the manifest Git blob SHA before use.
- CEvNS is active-flavour neutral current: no `P_ee` factor.
- Thresholds: `[1,3,5,10,20,40] eV`.
- Actual integer `Z,N=A-Z`; `sin^2(theta_W)=0.23857`.
- Same low-energy differential CEvNS form and same Helm form-factor convention as 0044.
- Same source-resolved and total ideal events/(kg day) ranking.
- Same no-detector-efficiency/no-avalanche/no-energy-gain guards.

## Prospective validation gates
1. Exact-mass Ar-40 no-Helm dominant-Be7 rates at 10, 20 and 40 eV must reproduce iteration 0042 within 1%; **the 40-eV 1% criterion is unchanged from the failed 0044 contract**.
2. Every pinned external spectrum Git blob SHA must match.
3. `F_Helm(0)^2=1` within `1e-12`; scanned `F^2` must be in `[0,1.000001]`.
4. All component/total rates finite and non-negative.
5. Each fixed target total rate monotonically non-increasing with threshold.
6. Helm rate for each threshold winner must not exceed its no-Helm counterpart.
7. At least one physical target must have a positive total rate at every frozen threshold; otherwise classify the corresponding threshold search as CLOSED rather than modifying candidates.
8. The benchmark must finish with verified source provenance and machine-readable source-resolved rows before any winner is called scientific authority.

## Classification
- `PASS_REAL_NUCLEUS_SOLAR_EXACT_MASS_OPTIMIZATION` only if all frozen gates pass.
- Target winners are physics-only ideal CEvNS-count optima within the frozen candidate set, not automatically realizable metastable materials.
- Any improvement over Ar is target/threshold matching, not enhancement of the fundamental weak interaction.
- Neutrino-energy gain remains NONE.

## Exact next action after PASS
Use the threshold-dependent winners and runners-up to define a separate **metastable-realizability funnel**: target chemistry/phase, achievable nucleation threshold, recoil efficiency, threshold dispersion, dark counts, backgrounds, reset/dead-time and stored-energy budget. Do not fold those effects into this corrected microscopic physics gate.
