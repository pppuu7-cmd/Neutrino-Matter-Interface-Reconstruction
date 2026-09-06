# NMIR Standard-Model solar-neutrino power ledger

Scope: neutrino-supplied deposited-energy upper bounds only. Each successful capture may receive at most the incident neutrino energy, `E_dep,nu <= E_nu`. Daughter decay energy, target nuclear-mass release, externally supplied preparation energy, and incomplete thermalization are excluded.

## Validated targets

| target / B16 branch | capture rate [SNU] | energy moment [SNU MeV] | mean captured Eν [MeV] | pure-isotope ceiling [W/kg] |
|---|---:|---:|---:|---:|
| **82Se / GS98** | **355.03190979** | **249.61364032** | **0.70307382** | **2.94006655e-22** |
| 82Se / AGSS09met | 345.60519781 | 226.65979252 | 0.65583444 | 2.66970537e-22 |
| 71Ga / GS98 | 65.00993895 | 75.78103575 | 1.16568385 | 1.03091848e-22 |
| 71Ga / AGSS09met | 62.31786849 | 66.37456240 | 1.06509680 | 9.02953653e-23 |
| 37Cl / GS98, threshold-linear residual | 3.02591026 | 22.66116076 | 7.48903926 | 5.91482818e-23 |
| 37Cl / GS98, zero-to-1 residual | 3.01244697 | 22.64856600 | 7.51832853 | 5.91154080e-23 |
| 37Cl / AGSS09met, threshold-linear residual | 2.56535349 | 18.77250688 | 7.31770766 | 4.89984400e-23 |
| 37Cl / AGSS09met, zero-to-1 residual | 2.55563709 | 18.76341779 | 7.34197271 | 4.89747164e-23 |

### Current validated leader
Pure `82Se / GS98` is the largest currently validated ceiling: `2.94006655e-22 W/kg`.

It exceeds the previous `71Ga / GS98` leader by a factor of about `2.85`. For natural selenium, the `82Se` isotopic fraction (`~0.0873`) reduces the GS98 ceiling to `2.66241785e-23 W/kg`.

The propagated response-scale systematic adopted from Frekers et al.'s quoted total `668 ± 60_sys SNU` gives a GS98 pure-82Se ceiling envelope of approximately `[2.676e-22, 3.204e-22] W/kg`. Even the upper edge remains about `3.1e21` times below `1 W/kg`.

## Non-authoritative screening results

These rows are deliberately excluded from the validated ranking until the target-specific response gate passes.

| target / B16 branch | response scope | rate [SNU] | energy moment [SNU MeV] | screen [W/kg] | authority status |
|---|---|---:|---:|---:|---|
| **7Li / GS98** | direct crossed gs-only | **15.95028372** | **54.47194863** | **7.49107965e-22** pure | **SCREEN ONLY — full response not externally validated** |
| 7Li / AGSS09met | direct crossed gs-only | 13.94391862 | 45.90248591 | 6.31259183e-22 pure | SCREEN ONLY |
| natural Li / GS98 | 7Li gs-only, abundance 0.9241 | 15.95028372 | 54.47194863 | 6.99831856e-22 | SCREEN ONLY |

The Li7 screen is important because its GS98 pure-isotope value is about `2.55x` the validated pure-82Se leader even before adding any independently authorized excited-state strength. It is **not** promoted: the crossed `7Be(gs)->7Li(gs)` `log ft=3.324` anchor is direct, but a complete `7Li(nu_e,e-)7Be` response and near-threshold atomic convention still require matched external validation.

The GS98 no-oscillation gs-only lithium total is `35.43394353 SNU`; historical full-response calculations quote a scale near `39.4 SNU`, but because the solar and nuclear conventions are unmatched this comparison is context only, not an acceptance test.

## 82Se response-validation history

The 82Se entry was promoted only after a prospective response-validation sequence:
1. Point-Coulomb/Sommerfeld pp source-average `5.1362e-45 cm^2` vs published `7.62e-45`: **scientific FAIL**, `-32.6%`.
2. Relativistic finite-size Fermi function with same nuclear input and unchanged gate: `7.5855e-45 cm^2`, **PASS**, `-0.453%`.
3. Full measured/binned GT response passed nine published source-average controls: pp `0.45%`, pep `0.73%`, Be7-862 `0.68%`, Be7-384 `2.38%`, N13 `0.44%`, O15 `0.61%`, F17 `0.30%`, B8 `5.00%`, hep `7.12%` absolute residual.
4. Only then was the frozen B16 spectra + production-averaged MSW pipeline used for the modern rate and energy moment.

## Scientific interpretation

The validated table is a **three-target benchmark**, not yet a global Standard-Model cross-target ceiling. The Li7 screen shows why broader target validation still matters: a low-A crossed transition can plausibly move the passive-target ceiling upward by another factor of a few, but the number is not authoritative until the full nuclear response passes the same standard used for Se82.

Even a several-fold movement around `10^-22 W/kg` remains many orders of magnitude from useful power density. A global G3 closure still requires more competitive allowed/forbidden inverse transitions plus a formal upper-bound argument across target space.

Resonant peak cross sections remain outside this ranking unless G8 integrated-strength, linewidth and solar-spectrum-overlap constraints are passed.

## Provenance
- 71Ga scientific authority: run `34028394336`, job `101473373902`, artifact `9987793879`.
- 37Cl scientific authority: run `34031200366`, job `101480904061`, artifact `9988653883`.
- 82Se point-Coulomb pp validation scientific FAIL: run `34032960415`, artifact `9989215767`.
- 82Se finite-size pp validation PASS: run `34033049596`, artifact `9989244871`.
- 82Se full nine-component validation PASS: run `34033182939`, artifact `9989287872`.
- 82Se repaired B16+MSW fold PASS: run `34033368287`, job `101486927672`, artifact `9989345911`.
- 7Li direct crossed gs-only screen: run `34034095803`, job `101488884067`, artifact `9989580600`, ZIP SHA256 `3b66dfe40cd3403ed97b87bedc4e7f76002170de715c5e264390d0184cdc5bc8`; **screen only, not validated-target authority**.
