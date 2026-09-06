# NMIR Standard-Model solar-neutrino power ledger

Scope: neutrino-supplied deposited-energy upper bounds only. Each successful capture may receive at most the incident neutrino energy, `E_dep,nu <= E_nu`. Daughter decay energy, target nuclear-mass release, externally supplied preparation energy, and incomplete thermalization are excluded.

## Validated targets

| target / B16 branch | capture rate [SNU] | energy moment [SNU MeV] | mean captured Eν [MeV] | pure-isotope ceiling [W/kg] |
|---|---:|---:|---:|---:|
| 71Ga / GS98 | 65.00993895 | 75.78103575 | 1.16568385 | 1.03091848e-22 |
| 71Ga / AGSS09met | 62.31786849 | 66.37456240 | 1.06509680 | 9.02953653e-23 |
| 37Cl / GS98, threshold-linear residual | 3.02591026 | 22.66116076 | 7.48903926 | 5.91482818e-23 |
| 37Cl / GS98, zero-to-1 residual | 3.01244697 | 22.64856600 | 7.51832853 | 5.91154080e-23 |
| 37Cl / AGSS09met, threshold-linear residual | 2.56535349 | 18.77250688 | 7.31770766 | 4.89984400e-23 |
| 37Cl / AGSS09met, zero-to-1 residual | 2.55563709 | 18.76341779 | 7.34197271 | 4.89747164e-23 |

For the currently validated targets, pure 71Ga/GS98 is the larger ceiling at `1.03091848e-22 W/kg`. Pure 37Cl/GS98 is lower by a factor of about `1.74`, despite the much higher capture-weighted neutrino energy, because its event rate is far smaller.

The unresolved Cl response convention below 1 MeV changes the GS98 power ceiling by only `5.56e-4` fraction (`0.0556%`) and the AGSS09met ceiling by `4.84e-4` (`0.0484%`). Thus this residual is negligible for the power conclusion at current precision.

## Scientific interpretation

This table is a validated **two-target benchmark**, not a global Standard-Model cross-target ceiling. It is already sufficient to establish that two canonical radiochemical capture targets remain near `10^-22–10^-23 W/kg` even under the deliberately generous `E_dep,nu <= E_nu` accounting.

To promote G3 from a two-target benchmark to a defensible cross-target ceiling, NMIR still requires a target-screening ledger over physically relevant allowed/forbidden inverse transitions, using matched primary nuclear response or measured `ft` information, natural/pure-isotope mass normalization, threshold/spectrum overlap, and the same neutrino-only energy accounting. Resonant peak cross sections must not be ranked without integrated strength and linewidth.

## Provenance

- 71Ga scientific authority: workflow run `34028394336`, job `101473373902`, artifact `9987793879`.
- 37Cl scientific authority: workflow run `34031200366`, job `101480904061`, artifact `9988653883`, artifact ZIP SHA256 `d4ca449c691597c954fa9638f3b8fdaa15faf307f6dfc93b090a340651851837`.
- 37Cl head baseline CI: run `34031200372`, job `101480904147`, `91 passed` plus baseline executable PASS.
