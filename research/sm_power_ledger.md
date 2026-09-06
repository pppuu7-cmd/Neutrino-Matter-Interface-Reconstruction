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
Pure `82Se / GS98` is the largest currently validated ceiling:

`2.94006655e-22 W/kg`.

It exceeds the previous `71Ga / GS98` leader by a factor of about `2.85`. The reason is primarily the much larger low-threshold capture rate; its capture-weighted incident-neutrino energy (`~0.703 MeV`) is actually lower than Ga's (`~1.166 MeV`).

For natural selenium, the `82Se` isotopic fraction (`~0.0873`) reduces the GS98 ceiling to `2.66241785e-23 W/kg`; enriched `82Se` is therefore essential for the pure-target ranking and this distinction must not be hidden.

The propagated response-scale systematic adopted from Frekers et al.'s quoted total `668 ± 60_sys SNU` gives a GS98 pure-82Se ceiling envelope of approximately `[2.676e-22, 3.204e-22] W/kg`. Even the upper edge remains about `3.1e21` times below `1 W/kg`.

The unresolved Cl response convention below 1 MeV changes the GS98 power ceiling by only `5.56e-4` fraction (`0.0556%`) and the AGSS09met ceiling by `4.84e-4` (`0.0484%`). Thus this residual is negligible for the power conclusion at current precision.

## 82Se response-validation history

The 82Se entry is promoted only after a prospective response-validation sequence:

1. A point-Coulomb/Sommerfeld approximation to the dominant `75-keV 1+` transition gave a pp source-average cross section `5.1362e-45 cm^2`, **32.6% below** the published `7.62e-45 cm^2`; this approximation is retained as a scientific FAIL.
2. Replacing only the Coulomb treatment with a relativistic finite-size Fermi function, without changing the prospective `15%` acceptance gate, gave `7.5855e-45 cm^2`, only **0.453% low** — PASS.
3. The full measured/binned GT response through the neutron threshold was then tested against nine published source-average controls with prospectively frozen component-specific limits. All passed: pp `0.45%`, pep `0.73%`, Be7-862 `0.68%`, Be7-384 `2.38%`, N13 `0.44%`, O15 `0.61%`, F17 `0.30%`, B8 `5.00%`, hep `7.12%` absolute residual.
4. Only after these gates was the same frozen B16 spectra + production-averaged MSW pipeline used to compute the modern oscillated rate and neutrino-energy moment.

## Scientific interpretation

This table is now a validated **three-target benchmark**, not yet a global Standard-Model cross-target ceiling. It establishes that even a modern, low-threshold, high-capture-rate measured-GT target remains at only a few `10^-22 W/kg` under deliberately generous neutrino-only accounting.

The 82Se result materially strengthens the emerging NMIR pattern: maximizing event count and lowering threshold can improve the ceiling by factors of a few, but has not produced anything remotely close to a technologically useful power density. A global G3 closure still requires screening more physically competitive allowed/forbidden inverse transitions and a formal upper-bound argument across target space.

Resonant peak cross sections remain outside this ranking unless G8 integrated-strength, linewidth and solar-spectrum-overlap constraints are passed.

## Provenance

- 71Ga scientific authority: workflow run `34028394336`, job `101473373902`, artifact `9987793879`.
- 37Cl scientific authority: workflow run `34031200366`, job `101480904061`, artifact `9988653883`, artifact ZIP SHA256 `d4ca449c691597c954fa9638f3b8fdaa15faf307f6dfc93b090a340651851837`.
- 82Se initial point-Coulomb pp validation scientific FAIL: run `34032960415`, job `101485801800`, artifact `9989215767`.
- 82Se relativistic finite-size pp validation PASS: run `34033049596`, artifact `9989244871`, digest `sha256:3f3393e30a70c938ab97e43072305cab919b6d81432d81c5c9bb6feab09a1c1d`.
- 82Se full nine-component response validation PASS: run `34033182939`, artifact `9989287872`, digest `sha256:514d20ad0999b2bdfc709ac7b8a67a48b689885f41d14be6070d508a5091b7ab`.
- 82Se first full solar fold run `34033250446`: infrastructure FAIL from evaluating `Pee(0)` at a zero-weight spectral endpoint; no scientific result assigned.
- Repaired 82Se B16+MSW fold: run `34033368287`, job `101486927672`, artifact `9989345911`, digest `sha256:aefa3804429d80ede17ba511dbcf5c65f675a6250705ef6ffab50c3c68934ca0`.
