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
Pure `7Li / GS98` is the largest individually validated passive-target neutrino-only ceiling: `1.06589117e-21 W/kg`, about `3.63x` the previous pure-`82Se / GS98` leader. Natural lithium, using `7Li` isotopic fraction `0.9241`, gives `9.95777156e-22 W/kg`.

The Li result is an upper bound on energy supplied by the incident neutrino. It does **not** include daughter-decay/nuclear-mass energy. Even this validated leader is about `9.38e20` below `1 W/kg`.

## Leading-allowed passive target-space bound — iteration 0024

A prospective class-level bound now replaces indefinite isotope-by-isotope extrapolation for the leading allowed one-body charged-current sector. The preregistration was committed before hosted output in `research/passive_allowed_bound_prereg.md`.

### Analytic ingredients
For the attractive point-Coulomb factor `F_pc=x/(1-exp(-x))`, `x=2*pi*alpha*Z_f*E/p`, the inequality `exp(x)>=1+x` gives

`p E F_pc <= (1+2*pi*alpha*Z_f) E^2`.

A deliberately loose, correlation-independent one-body operator-norm cap is used:

`S_F <= A^2`, `S_GT <= 3 A^2`,

therefore `S_allowed <= A^2(1+3 g_A^2)`.

The maximization deliberately favors large power: `A<=300`, `Z_f<=119`, zero threshold/excitation, `E_nu<=20 MeV`, an artificial incident **neutrino energy flux** of `2000 W/m^2`, and an additional 2% upward target-count factor.

### Hosted result
Run `34038214660`, job `101500085408`, head `5cdb30148ce7a928fdb00424723f065e54a5f104`, artifact `9990839187`, artifact ZIP SHA256 `f9e544b9aa5372f8e286e8214f2eba422f35cc8e02468501babc99cfcbbc8642`. Six dedicated tests passed; same-head baseline CI `34038214654` also passed.

| scoped envelope quantity | value |
|---|---:|
| analytic leading-allowed bound | **`9.419449302949355e-12 W/kg`** |
| deficit to `1 W/kg` | `1.0616331888e11` |
| preregistered non-theorem omitted-physics stress factor | `1e6` |
| stressed diagnostic | **`9.419449302949354e-6 W/kg`** |
| stressed deficit to `1 W/kg` | `1.0616331888e5` |
| prospective classification | **STRONG_NEGATIVE_SCOPED** |

The analytic class envelope is about `8.84e9` times above the current validated Li7 target value, so it is safely an over-envelope rather than a fit to the existing four-target ledger.

### Scope guard
This result strongly excludes macroscopic solar-neutrino power from the **leading allowed one-body charged-current passive nuclear class under the stated A/Z solar-energy domain**. It is **not** yet a global all-Standard-Model passive-nucleus theorem. First-forbidden/higher multipoles and resonant integrated-strength/bandwidth effects remain to be bounded independently; engineered collective media and focusing remain separate gates.

## 7Li response-validation history — iteration 0023
The two-state response was constructed without tuning to a published neutrino cross section:
1. Ground state fixed by evaluated `7Be(gs)->7Li(gs)` EC, `Q_EC=861.815 keV`, `log ft=3.324`.
2. First `7Be` excited state at `429 keV` opens at `~1.291 MeV`; independent allowed strengths use `B(F)=1`, `B(GT)_gs=1.19`, `B(GT)_ex=1.06`.
3. Prospective matched-`8B` gates were frozen before hosted execution: component residual `<=12%`, total residual `<=10%`.
4. First workflow `34037418081` was **infrastructure FAIL only** (`pytest` absent). Minimal dependency repair changed no physics/gate.
5. Repaired validation run `34037499594`, job `101498137412`, PASS: ground `2.50624405e-42` vs `2.470e-42` (`+1.467%`), excited `1.30740265e-42` vs `1.289e-42` (`+1.428%`), total `3.81364669e-42` vs `3.759e-42` (`+1.454%`). Artifact `9990627394`.
6. Validated B16+MSW fold `34037570254`, job `101498329856`, artifact `9990650435`.

GS98+MSW Li component highlight: B8 contributes only `7.24140 SNU` but `62.60901 SNU MeV`; low target mass plus the high-energy B8 tail drives the W/kg ranking.

## 82Se response-validation history
The 82Se entry was promoted only after a prospective sequence:
1. Point-Coulomb/Sommerfeld pp source-average `5.1362e-45 cm^2` vs published `7.62e-45`: **scientific FAIL**, `-32.6%`.
2. Relativistic finite-size Fermi response with unchanged gate: `7.5855e-45 cm^2`, **PASS**, `-0.453%`.
3. Full measured/binned GT response passed nine source-average controls.
4. Repaired frozen B16+MSW fold passed after a separately classified zero-weight-endpoint infrastructure repair.

## Scientific interpretation
The individual table is a **four-target benchmark**; iteration 0024 adds a much broader but scoped class-level negative result. The leading allowed passive nuclear sector is now bounded many orders below useful power even under intentionally excessive assumptions.

Global G3 closure still requires at minimum:
- a first-forbidden/higher-multipole solar-energy envelope;
- G8 integrated resonance-strength/linewidth/spectral-overlap bound;
- explicit treatment/segregation of engineered collective response and finite focusing.

## Provenance
- 71Ga authority: run `34028394336`, job `101473373902`, artifact `9987793879`.
- 37Cl authority: run `34031200366`, job `101480904061`, artifact `9988653883`.
- 82Se point-Coulomb scientific FAIL: run `34032960415`, artifact `9989215767`.
- 82Se finite-size pp validation PASS: run `34033049596`, artifact `9989244871`.
- 82Se full validation PASS: run `34033182939`, artifact `9989287872`.
- 82Se B16+MSW fold PASS: run `34033368287`, job `101486927672`, artifact `9989345911`.
- 7Li gs-only screen: run `34034095803`, job `101488884067`, artifact `9989580600`.
- 7Li two-state validation PASS: run `34037499594`, job `101498137412`, artifact `9990627394`.
- 7Li B16+MSW full fold PASS: run `34037570254`, job `101498329856`, artifact `9990650435`.
- Passive allowed target-space bound: run `34038214660`, job `101500085408`, artifact `9990839187`; baseline CI `34038214654`.
