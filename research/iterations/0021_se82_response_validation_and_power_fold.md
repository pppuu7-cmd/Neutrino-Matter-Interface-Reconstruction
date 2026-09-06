# Iteration 0021 — 82Se response validation and G3 power fold

Date: 2026-09-06

## Objective
Promote a third solar-neutrino capture target only if its nuclear response can reproduce external source-average cross sections prospectively, then fold it through the same frozen B16 spectra + production-averaged MSW authority used for 71Ga and 37Cl.

## Primary input
Frekers et al., Phys. Rev. C 94, 014614 (2016): high-resolution `82Se(3He,t)82Br` GT distribution.

Frozen response data:
- dominant `75-keV 1+` state: `B(GT)=0.338(31)`;
- ground-state mass difference `~96.6 keV` → dominant capture threshold `~171.6 keV`;
- individual measured states through 2.498 MeV plus published 0.5-MeV GT bins to 7.6 MeV;
- source-average external controls for pp, pep, hep, Be7-862, Be7-384, B8, N13, O15, F17.

## Step A — first Coulomb model: scientific FAIL
Prospective pp validation limit: `|relative residual| <= 15%`, frozen before hosted execution.

Point-Coulomb/Sommerfeld result:
- calculated pp source-average `5.136214871e-45 cm^2`;
- published `7.62e-45 cm^2`;
- residual `-32.596%`.

Run `34032960415`, job `101485801800`, artifact `9989215767`.

Classification: **scientific FAIL of the point-Coulomb approximation**. Gate was not loosened.

## Step B — relativistic finite-size Fermi function: PASS
Physics-only repair: replace the point Sommerfeld factor by the standard relativistic finite-size Fermi function for the emitted electron; keep the same measured `B(GT)` and the same 15% acceptance limit.

Result:
- calculated pp source-average `7.585497452e-45 cm^2`;
- published `7.620000000e-45 cm^2`;
- residual `-0.452789%`.

Run `34033049596`; artifact `9989244871`; digest `sha256:3f3393e30a70c938ab97e43072305cab919b6d81432d81c5c9bb6feab09a1c1d`.

Classification: **PASS**.

## Step C — full measured/binned GT response: PASS all external controls
Prospective component limits were frozen before hosted execution:
- pp 5%;
- pep / Be7 lines 10%;
- N13/O15/F17 15%;
- B8/hep 20%.

| source | absolute residual |
|---|---:|
| pp | 0.453% |
| pep | 0.731% |
| Be7-862 | 0.680% |
| Be7-384 | 2.382% |
| N13 | 0.437% |
| O15 | 0.609% |
| F17 | 0.304% |
| B8 | 5.000% |
| hep | 7.121% |

Run `34033182939`; artifact `9989287872`; digest `sha256:514d20ad0999b2bdfc709ac7b8a67a48b689885f41d14be6070d508a5091b7ab`.

Classification: **full response validation PASS**.

## Step D — first B16+MSW fold: infrastructure FAIL, no science classification
Run `34033250446` failed because a frozen spectrum contains an exact `E_nu=0` endpoint with zero spectral weight and the code evaluated `Pee(0)` before recognizing its contribution was mathematically zero.

This changed no physics. Minimal repair: skip zero-weight / zero-cross-section samples before calling `Pee`. Regression test: `tests/test_se82_solar_fold.py`.

## Step E — repaired B16+MSW fold: PASS
Run `34033368287`; job `101486927672`; artifact `9989345911`; digest `sha256:aefa3804429d80ede17ba511dbcf5c65f675a6250705ef6ffab50c3c68934ca0`.
Raw artifact downloaded and inspected before promotion.

### GS98+MSW
- total rate: `355.03190979 SNU`;
- energy moment: `249.61364032 SNU MeV`;
- capture-weighted incident energy: `0.70307382 MeV`;
- pure 82Se neutrino-only ceiling: **`2.94006655e-22 W/kg`**;
- natural Se ceiling: `2.66241785e-23 W/kg`;
- pure response-scale envelope from quoted `±60/668` systematic: `[2.67599e-22, 3.20414e-22] W/kg`.

Main GS98 component rates:
- pp `246.76598 SNU`;
- Be7 `84.38534 SNU`;
- B8 `9.05979 SNU`.

Main energy moments:
- pp `76.22791 SNU MeV`;
- Be7 `71.21515 SNU MeV`;
- B8 `84.26207 SNU MeV`.

### AGSS09met+MSW
- total rate `345.60519781 SNU`;
- energy moment `226.65979252 SNU MeV`;
- pure 82Se ceiling **`2.66970537e-22 W/kg`**;
- natural Se ceiling `2.41758855e-23 W/kg`.

## Scientific result
Pure 82Se/GS98 is now the largest validated NMIR G3 target ceiling, about **2.85×** pure 71Ga/GS98 (`1.03091848e-22 W/kg`). This is a real cross-target improvement but not a technological energy result: even the upper 82Se response envelope is still `~3.1e21` below `1 W/kg`.

The result also reinforces a nontrivial pattern: the target maximizing event count need not maximize capture-weighted energy. pp dominates 82Se events, but B8 becomes comparably important in the neutrino-energy moment.

## Reproducibility / authority
- measured GT table: `data/se82_frekers2016_gt_response.csv`;
- external controls: `data/se82_frekers2016_source_average.csv`;
- response: `src/nmir/se82_response.py`, `src/nmir/se82_full_response.py`;
- full fold: `src/nmir/se82_solar_fold.py`;
- power ledger: `research/sm_power_ledger.md`;
- regression test: `tests/test_se82_solar_fold.py`;
- baseline CI after promotion: `34033479337` SUCCESS.

## Status
- ✅ 82Se pp normalization closed;
- ✅ full measured GT response externally validated across nine sources;
- ✅ B16+MSW rate + energy-moment + W/kg fold closed;
- ✅ infrastructure endpoint bug repaired and regression-tested;
- ✅ third target added to G3 ledger; 82Se is current leader;
- ❌ point-Coulomb approximation retained as scientific FAIL;
- 🟡 G3 remains globally open: three targets are not a theorem over all SM target space.

**NMIR_READINESS: 42%** (audit estimate).

## Exact next gate
1. Screen 7Li and modern measured-GT targets with the same authority standard.
2. Begin a theorem-style passive-target upper bound using target nuclei/kg, allowed-transition sum rules, solar spectral energy flux, and weak coupling.
3. Implement G8 integrated resonance-strength/linewidth overlap before any resonant target can challenge the nonresonant ledger.
