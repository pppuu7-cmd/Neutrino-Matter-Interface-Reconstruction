# Prospective contract — real-nucleus full-solar CEvNS inverse optimization

Date frozen: 2026-09-06
Gate: G2 / F3-F7
Purpose: replace iteration 0043 continuous-A/fixed-Q_W/A envelope by a physical-nucleus scan over the full frozen B16 GS98 solar source mixture, at fixed detector mass and recoil threshold.

## Frozen target set
Authority: `data/cevns_target_candidates.csv`.
Targets are treated as pure isotopic nuclei for this physics-only gate. Chemistry, natural abundance and availability are not optimization variables here.

## Frozen source set
Flux authority: `data/solar_flux_b16.csv`, B16 GS98 column.
Spectrum provenance authority: `data/solar_spectrum_manifest.csv`.
Use:
- continuum: pp, hep, B8 (Ortiz default in manifest), N13, O15, F17;
- physical thermally broadened Be7 ground and excited profiles, with branch weights 0.897 and 0.103 respectively;
- pep line at 1.442 MeV.

Every external numerical spectrum must be read from the exact source repo/commit/path in the manifest and its Git blob SHA recomputed and matched before use. The already-local Be7-ground file may be used directly but its provenance must remain identical to the manifest. A missing/mismatched external file is `INFRASTRUCTURE_FAIL`, never silently replaced by a different spectrum.

CEvNS is neutral current; no electron-neutrino MSW survival factor is applied.

## Frozen thresholds
`T_thr = [1, 3, 5, 10, 20, 40] eV`.
The 1–20 eV range is the primary inverse-design region; 40 eV is retained as the iteration-0042 boundary control.

## Nuclear response
Use actual integer `Z,N=A-Z` and

`Q_W = N - (1 - 4 sin^2 theta_W) Z`, `sin^2 theta_W=0.23857`.

Mass convention for this scan: `M=A m_u`, `m_u=931.49410242 MeV`. This approximation is prospectively accepted because the gate ranks broad target classes; exact isotope masses may be added later without retuning this scan.

Differential CEvNS:

`d sigma/dT = G_F^2 Q_W^2 M/(4 pi) [1 - M T/(2 E_nu^2)] F_Helm(q)^2`,

`q=sqrt(2 M T)`.

Use Helm neutron form factor with frozen conventional parameters

`c = 1.23 A^(1/3) - 0.60 fm`, `a=0.52 fm`, `s=0.90 fm`,
`R = sqrt(c^2 + 7 pi^2 a^2/3 - 5 s^2)`,
`F(q)=3 j1(qR)/(qR) exp[-(q s)^2/2]`,

with `q` converted by `hbar c = 197.3269804 MeV fm`. At `qR -> 0`, use `F=1` stably.

Integrate numerically over recoil from threshold to exact

`T_max=2 E_nu^2/(M+2E_nu)`.

Then integrate each continuum/profile over its normalized physical energy distribution and multiply by the B16 GS98 source flux and branch weight. Report ideal events/kg/day using `1000/A * N_A` target nuclei per kg under the stated mass convention.

## Quantities to report
For every threshold and target:
- total ideal solar CEvNS events/(kg day);
- source-resolved pp, Be7, pep, N13, O15, F17, B8, hep contributions;
- winning target and runner-up;
- dominant solar component of the winning rate;
- numerical winner mass compared with the monoenergetic design intuition from iteration 0043.

Also report the zero-form-factor counterpart for the winning target at each threshold and the Helm suppression ratio, so form-factor relevance is explicit.

## Prospective validation gates
1. Every downloaded pinned spectrum must reproduce the manifest Git blob SHA exactly.
2. Each continuum/profile trapezoidal normalization after explicit normalization must be positive and finite.
3. `F_Helm(q=0)=1` within `1e-12` and `0<=F^2<=1.000001` over scanned recoil support.
4. All source rates are finite and non-negative.
5. For each fixed target, total rate is monotonically non-increasing with threshold.
6. Reproduce iteration 0042 Ar40 dominant-Be7-only ideal rates at 10, 20 and 40 eV to within 1% when Helm is disabled; with Helm enabled the ratio must remain <=1.
7. At 40 eV, do not infer usefulness merely from kinematic opening; rank by integrated rate.
8. No detector efficiency, avalanche gain or stored medium energy is multiplied into this gate.

## Classification
- `PASS_REAL_NUCLEUS_SOLAR_OPTIMIZATION` if all provenance and numerical gates pass and a stable target ranking is produced.
- A winner is a **physics-only ideal target** for CEvNS counts/kg at that threshold, not automatically a realizable metastable material.
- Any target change relative to Ar is a detector-design result, not microscopic interaction enhancement.
- No neutrino-energy gain is claimed.

## Next action after PASS
Take the best physically plausible metastable candidates from the threshold-dependent ranking into a separate detector ledger containing nucleation efficiency, threshold distribution, dark counts/backgrounds, reset/dead time and stored-energy cost.
