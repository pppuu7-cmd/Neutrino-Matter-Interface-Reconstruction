# NMIR Standard-Model solar-neutrino power ledger

Scope: neutrino-supplied deposited-energy upper bounds only. Each successful capture may receive at most the incident neutrino energy, `E_dep,nu <= E_nu`. Daughter decay energy, target nuclear-mass release, externally supplied preparation energy, and incomplete thermalization are excluded.

## Validated targets

| target / B16 branch | capture rate [SNU] | energy moment [SNU MeV] | mean captured Eν [MeV] | pure-isotope ceiling [W/kg] |
|---|---:|---:|---:|---:|
| **7Li / GS98** | **19.34881333** | **77.50707776** | **4.00577939** | **1.06589117e-21** |
| 7Li / AGSS09met | 16.84165298 | 65.03364861 | 3.86147658 | 8.94354349e-22 |
| 82Se / GS98 | 355.03190979 | 249.61364032 | 0.70307382 | 2.94006655e-22 |
| 82Se / AGSS09met | 345.60519781 | 226.65979252 | 0.65583444 | 2.66970537e-22 |
| 71Ga / GS98 | 65.00993895 | 75.78103575 | 1.16568385 | 1.03091848e-22 |
| 71Ga / AGSS09met | 62.31786849 | 66.37456240 | 1.06509680 | 9.02953653e-23 |
| 37Cl / GS98, threshold-linear residual | 3.02591026 | 22.66116076 | 7.48903926 | 5.91482818e-23 |
| 37Cl / GS98, zero-to-1 residual | 3.01244697 | 22.64856600 | 7.51832853 | 5.91154080e-23 |
| 37Cl / AGSS09met, threshold-linear residual | 2.56535349 | 18.77250688 | 7.31770766 | 4.89984400e-23 |
| 37Cl / AGSS09met, zero-to-1 residual | 2.55563709 | 18.76341779 | 7.34197271 | 4.89747164e-23 |

### Current validated leader
Pure `7Li / GS98` is now the largest validated passive-target neutrino-only ceiling: `1.06589117e-21 W/kg`, about `3.63x` the previous pure-`82Se / GS98` leader. Natural lithium, using `7Li` isotopic fraction `0.9241`, gives `9.95777156e-22 W/kg`, still about `3.39x` the pure-82Se benchmark.

The Li result remains an upper bound on energy supplied by the incident neutrino. It does **not** include daughter-decay/nuclear-mass energy, and it is not a global Standard-Model theorem across all nuclei. Even the new validated leader is about `9.38e20` below `1 W/kg`.

## 7Li response-validation history — iteration 0023

The two-state response was constructed without tuning to a published neutrino cross section:
1. Ground state is fixed by evaluated `7Be(gs)->7Li(gs)` EC, `Q_EC=861.815 keV`, `log ft=3.324`.
2. The first `7Be` excited state at `429 keV` opens at `~1.291 MeV`; its independent allowed strength uses measured `B(GT)=1.06`, while the ground branch uses `B(F)=1`, `B(GT)=1.19`.
3. Prospective matched-`8B` gates were frozen before hosted execution: component residual `<=12%`, total residual `<=10%`.
4. First workflow `34037418081` was **infrastructure FAIL only** because `pytest` was absent. Minimal dependency repair changed no physics or gate.
5. Repaired validation run `34037499594`, job `101498137412`, PASS after raw-log inspection: ground `2.50624405e-42` vs published `2.470e-42` (`+1.467%`), excited `1.30740265e-42` vs `1.289e-42` (`+1.428%`), total `3.81364669e-42` vs `3.759e-42` (`+1.454%`). Artifact `9990627394`, SHA256 `a3ecbf1d489c215576b9e7b99c3ae7017509070c77104aa4a7265576246e9eb6`.
6. Only after that PASS was the same frozen B16 spectra + production-averaged MSW pipeline run. Hosted fold `34037570254`, job `101498329856`, artifact `9990650435`, SHA256 `320331ff1d3c068d78a27ff09d61a0e07965ff6ef7f2884d940fc7f214fb41cd`.

GS98+MSW Li component highlights: B8 `7.24140 SNU` but `62.60901 SNU MeV`; Be7 `4.07166 SNU`; pep `4.80745 SNU`. Thus the low atomic mass and high-energy B8 tail, rather than the largest event count, drive the W/kg ranking.

## 82Se response-validation history

The 82Se entry was promoted only after a prospective response-validation sequence:
1. Point-Coulomb/Sommerfeld pp source-average `5.1362e-45 cm^2` vs published `7.62e-45`: **scientific FAIL**, `-32.6%`.
2. Relativistic finite-size Fermi function with same nuclear input and unchanged gate: `7.5855e-45 cm^2`, **PASS**, `-0.453%`.
3. Full measured/binned GT response passed nine published source-average controls: pp `0.45%`, pep `0.73%`, Be7-862 `0.68%`, Be7-384 `2.38%`, N13 `0.44%`, O15 `0.61%`, F17 `0.30%`, B8 `5.00%`, hep `7.12%` absolute residual.
4. Only then was the frozen B16 spectra + production-averaged MSW pipeline used for the modern rate and energy moment.

## Scientific interpretation

The validated table is now a **four-target benchmark**, not yet a global Standard-Model cross-target ceiling. Li7 materially raises the best validated passive-target power from `2.94e-22` to `1.07e-21 W/kg`, demonstrating why low-A targets matter. The gain is still only a factor of a few and leaves roughly 21 orders of magnitude to `1 W/kg`.

A global G3 closure still requires broader competitive-target screening plus a formal upper-bound argument across target space. Resonant peak cross sections remain outside this ranking unless G8 integrated-strength, linewidth and solar-spectrum-overlap constraints are passed.

## Provenance
- 71Ga scientific authority: run `34028394336`, job `101473373902`, artifact `9987793879`.
- 37Cl scientific authority: run `34031200366`, job `101480904061`, artifact `9988653883`.
- 82Se point-Coulomb pp validation scientific FAIL: run `34032960415`, artifact `9989215767`.
- 82Se finite-size pp validation PASS: run `34033049596`, artifact `9989244871`.
- 82Se full nine-component validation PASS: run `34033182939`, artifact `9989287872`.
- 82Se repaired B16+MSW fold PASS: run `34033368287`, job `101486927672`, artifact `9989345911`.
- 7Li direct crossed gs-only screen: run `34034095803`, job `101488884067`, artifact `9989580600`.
- 7Li two-state matched-B8 validation PASS: run `34037499594`, job `101498137412`, artifact `9990627394`.
- 7Li validated B16+MSW full fold PASS: run `34037570254`, job `101498329856`, artifact `9990650435`.
