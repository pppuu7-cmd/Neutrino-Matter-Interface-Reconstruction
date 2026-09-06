# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`

## Mission
Reconstruct the low-energy neutrino↔matter interface, distinguish detection/state control from irreversible neutrino-sourced energy deposition, establish a quantitative Standard-Model ceiling, and only then open BSM model-building as a solution branch.

Frozen organizing principles: response reconstruction; production↔absorption/crossed weak channels; finite gravitational focusing; staggered-layer/multi-isotope response engineering.

Central objective:
\[
P_{dep}=N_T\int dE\,\mu(E,\mathbf x)\Phi(E)\sigma_{cap}(E)E_{dep}(E).
\]

## Validated baseline authority

### Weak / inverse-capture anchors
- Xe-132 ideal CEvNS at 1 MeV: `sigma≈2.405e-41 cm^2`; liquid-Xe-like mean free path `~3.08e16 m`; optical-depth-one mass column `~9.07e18 g/cm^2`.
- Minimal Dirac magnetic moment for `m_nu=0.05 eV`: `~1.6e-20 mu_B`; ideal 1-m magnetic-precession maximum requires `~3.35e17 T`.
- Tritium measured-ft route: `sigma(v/c)≈7.785e-45 cm^2`, within ~0.7% of published `7.84e-45 cm^2`; CI `34004890286`, job `101410168170`.

### Solar inputs
- B16 GS98/AGSS09met integrated fluxes frozen in `data/solar_flux_b16.csv`.
- Exact pinned pp/hep/B8/CNO and thermally broadened Be7 spectra in `data/solar_spectrum_manifest.csv`; materialization run `34012460541`, artifact `9982880231`.
- B16 matter blobs: GS98 `f73c47cf6f2d77086634a5c180b50039e10805e7`; AGSS09met `d9bd29f3374c63e8ea898733a55fb7aa566a2c96`; materialization run `34014923087`, artifact `9983598047`.
- Frozen oscillation convention: `sin^2(theta12)=0.307`, `sin^2(theta13)=0.0220`, `Delta m^2_21=7.53e-5 eV^2`, normal ordering, day-side adiabatic three-flavour MSW, Earth regeneration OFF.
- Exact B16 survival authority: run `34015021346`, artifact `9983624802`. Representative GS98 `Pee`: pp(0.300)=0.544186; Be7(0.862)=0.526972; pep(1.442)=0.516871; B8(5)=0.393449; B8(10)=0.327017.

### Ga-71 response and full solar fold
Primary response: J. N. Bahcall, Phys. Rev. C 56, 3391 (1997). `data/ga71_bahcall1997_response.csv`: 58 points, 0.240–30 MeV, best and ±3σ branches.

Source-average validation run `34017366528`, artifact `9984322724`: relative errors vs Bahcall pp 0.205%, pep 0.796%, Be7 0.022%, N13 0.085%, O15 0.161%, F17 0.581%.

Authoritative full Ga fold: run `34020272911`, artifact `9985246195`.

| component SNU | GS98 | AGSS09met |
|---|---:|---:|
| pp | 38.17593 | 38.49195 |
| pep | 1.53045 | 1.55119 |
| Be7 | 18.66889 | 17.03715 |
| B8 | 4.49332 | 3.70099 |
| hep | 0.02095 | 0.02159 |
| N13 | 0.88944 | 0.65312 |
| O15 | 1.19983 | 0.84271 |
| F17 | 0.03112 | 0.01917 |
| **total** | **65.00994** | **62.31787** |

Classification: full component-specific B16 × spectrum × production-averaged MSW × Ga response folding PASS.

### Ga-71 neutrino-only deposited-energy ceiling — iteration 0018
For G3, the conservative definition is `E_dep,nu <= E_nu` per successful capture. This credits at most the incident-neutrino energy and explicitly excludes daughter-decay energy, nuclear-mass release, and other target-internal energy reservoirs. It is therefore a strict upper bound on neutrino-sourced deposited power, not an assumption of complete local thermalization.

Hosted authority: run `34028394336`, job `101473373902`, head `a1bbb60f90cfd5146c24861098a15220db6bd1a1`, artifact `9987793879`, artifact ZIP SHA256 `bc0193112f2bdfb63438322a0b5cb702145dd6fd1e938f1be99ae4d5b66ade65`.

| Ga-71 ceiling quantity | GS98 | AGSS09met |
|---|---:|---:|
| total rate [SNU] | 65.00993895 | 62.31786849 |
| energy moment [SNU MeV] | 75.78103575 | 66.37456240 |
| capture-weighted incident Eν [MeV] | 1.16568385 | 1.06509680 |
| pure-71Ga neutrino-energy ceiling [W/kg] | **1.03091848e-22** | **9.02953653e-23** |

For GS98, B8 contributes `42.69685 SNU MeV`, Be7 `15.80371`, and pp `12.58974`; thus pp dominates the event count but B8 dominates the neutrino-carried energy moment. The larger validated Ga ceiling is only `~1.03e-22 W/kg`; reaching 1 W/kg would require `~9.7e21` times this power before any further thermalization losses. Classification: Ga-71 neutrino-carried energy upper-bound observable PASS.

### Cl-37 authority and historical convention audit
Primary numerical response: Bahcall et al., Phys. Rev. C 54, 411 (1996), frozen in `data/cl37_bahcall1996_response.csv`: 19 representative points from 1–30 MeV plus Bahcall-Ulrich comparison column; physical threshold `0.814 MeV`.

Bahcall & Ulrich, Rev. Mod. Phys. 60, 297 (1988) source averages are frozen in `data/cl37_bahcall_ulrich1988_source_average.csv`. Be7 source-average authority removes the old non-authoritative 0.862-MeV threshold interpolation. Hosted Cl fold `34022999659`, artifact `9986121953`:

| Cl component/total SNU | GS98 | AGSS09met |
|---|---:|---:|
| Be7 authority | 0.6235128 | 0.5690128 |
| B8 | 2.1395856 | 1.7623578 |
| pep | 0.1433597 | 0.1453031 |
| total, threshold-linear residual | **3.0259103** | **2.5653535** |
| total, zero-to-1 residual | **3.0124470** | **2.5556371** |

Residual sensitivity to the unresolved `0.814–1.0 MeV` continuum interval is only ~0.4% of total SNU. The earlier threshold-linear Be7 result (`~0.317 SNU` GS98) is a scientific FAIL of that interpolation model.

Iteration 0017 fixed the historical B8/Cl convention classification. The old `1.06e-42 cm2` target jointly used an older B8 spectrum and older A=37/B(GT) response inputs; it is not a pure spectral benchmark. The mixed Ortiz-2000 × historical-target result `1.1914503e-42 cm2` (+12.40%) remains a valid negative result for mixed authority. Frozen 1996 spectrum × sparse 1996 improved response gives `~1.15972e-42 cm2`, within ~1.73% of the published full-response `1.14e-42 cm2`; with the Bahcall-Ulrich sparse response it gives `~1.07259e-42 cm2`, within ~0.69% of the paper's stated `1.08e-42 cm2`. Repair CI after removing an undeclared numpy dependency: `34025731270` SUCCESS.

### Cl-37 neutrino-only deposited-energy ceiling — iteration 0019
The same prospective rule as Ga was used without post-result changes: `E_dep,nu <= E_nu`. Be7 remains source-average authority; because only its 0.862-MeV line is above the Cl threshold, its energy moment is the authoritative capture rate times 0.862 MeV. The unresolved sub-1-MeV continuum is propagated under the two already-frozen conventions.

Hosted scientific authority: run `34031200366`, job `101480904061`, head `f8c825802d02909bfcba49c31f6363e17887b4a8`, artifact `9988653883`, artifact ZIP SHA256 `d4ca449c691597c954fa9638f3b8fdaa15faf307f6dfc93b090a340651851837`. Raw benchmark JSON was inspected before classification. Same-head baseline CI `34031200372`, job `101480904147`: **91 passed** plus baseline physics executable PASS.

| Cl-37 ceiling quantity | GS98 threshold-linear | GS98 zero-to-1 | AGSS09met threshold-linear | AGSS09met zero-to-1 |
|---|---:|---:|---:|---:|
| total rate [SNU] | 3.02591026 | 3.01244697 | 2.56535349 | 2.55563709 |
| energy moment [SNU MeV] | 22.66116076 | 22.64856600 | 18.77250688 | 18.76341779 |
| mean captured Eν [MeV] | 7.48903926 | 7.51832853 | 7.31770766 | 7.34197271 |
| pure-37Cl ceiling [W/kg] | **5.91482818e-23** | **5.91154080e-23** | **4.89984400e-23** | **4.89747164e-23** |

The power-envelope span is only **0.0556%** for GS98 and **0.0484%** for AGSS09met, much smaller than the corresponding total-SNU residual. B8 supplies `21.61176396` of the GS98 `22.66116076 SNU MeV` energy moment, so the power conclusion is high-energy dominated. Classification: Cl-37 neutrino-only W/kg gate PASS.

### First Ga/Cl Standard-Model power ledger
`research/sm_power_ledger.md` is authoritative for the first two-target ledger. Under the same pure-isotope and neutrino-only accounting, the largest currently validated value is 71Ga/GS98 at `1.03091848e-22 W/kg`; 37Cl/GS98 is lower by about a factor 1.74 despite its much higher capture-weighted Eν.

This is explicitly a **two-target benchmark, not a global cross-target Standard-Model ceiling**. A defensible G3 closure still requires target screening over additional physically relevant inverse transitions using matched primary response or measured-ft authority, thresholds and solar-spectrum overlap, pure/natural mass normalization, and integrated resonance strength/linewidth where applicable.

## Other active branches
- Many-body/spin: response formalism active; a single 1-meV magnon from a 1-MeV neutrino deposits only `1e-9` of incident energy. Sum-rule-preserving response toy remains open.
- Gravitational focusing: solar-limb weak-field benchmark `~547.741 AU`; transparent-Sun literature benchmark near `23.5 ± 0.1 AU`; finite-source/Liouville gain gate mandatory.
- Staggered metamaterial: at 1 MeV, `lambda≈1.23984e-12 m`; for `d=3 Å`, first Bragg angle `~0.118396 deg`; any gain must survive angle/energy integration at fixed mass column.

## Research gates
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS — CEvNS + tritium ft + Ga response + Cl pointwise/source-average anchors + matched historical B8/Cl audit |
| G1 static macroscopic coherence | PARTIAL NEGATIVE — naive N² opacity disfavored |
| G2 many-body deposited-energy channels | OPEN |
| G3 maximum SM deposited solar-neutrino power | PARTIAL PASS — Ga and Cl full folds + pure-isotope neutrino-only W/kg ceilings PASS; first two-target ledger frozen; broader cross-target screening still missing |
| G4 engineered resonance/polarization/periodicity | OPEN |
| G5 minimal BSM solution | LOCKED until G3 |
| G6 BSM constraints | LOCKED until G5 |
| G7 production/decay → inverse capture | PARTIAL PASS — measured-ft route validated |
| G8 resonance integrated-strength/bandwidth | OPEN |
| G9 finite gravitational focusing gain | OPEN |
| G10 staggered/multi-isotope fixed-mass-column gain | OPEN |

## Critical scope guards
1. Detector threshold ≠ total cross section.
2. Directional coherence ≠ integrated opacity.
3. Peak resonance ≠ flux-integrated capture.
4. Gravitational magnification is finite and multiplicative.
5. Projected atomic coverage ≠ neutrino opacity.
6. Exact time reversal and crossed weak processes must be classified correctly.
7. Never mix solar flux/spectrum/matter/oscillation/nuclear conventions silently.
8. BSM solution branch remains locked until G3 is quantitatively defensible across targets.
9. Green workflow ≠ scientific PASS until raw result and frozen gate are inspected.
10. Missing pointwise response must not be silently interpolated into authority when a source-average or uncertainty formulation is the correct observable.
11. Historical source-average cross sections validate only matched spectrum+response conventions; do not attribute a mixed-convention discrepancy to the spectrum alone.
12. Neutrino-sourced deposited-energy ceilings may credit at most incident `E_nu`; daughter decay or target nuclear-mass energy must be tracked separately and never counted as energy supplied by the neutrino.
13. A two-target maximum is not a global SM ceiling; additional targets must be screened under a common event-rate and W/kg normalization.

## Chronology
`0001` CEvNS/magnetic/coherence; `0002` production↔absorption/spin; `0003` inverse-transition seeds; `0004` gravity; `0005` staggered metamaterial; `0006` ft→capture; `0007–0012` B16 flux/spectra/matter/MSW; `0013` Ga response; `0014` full Ga fold; `0015` Cl pointwise fold/sensitivity; `0016` Cl source-average Be7 authority + mixed B8 audit; `0017` matched historical B8/Cl convention reclassification and CI repair; `0018` Ga-71 neutrino-only deposited-energy ceiling; `0019` Cl-37 neutrino-only deposited-energy ceiling + first Ga/Cl SM power ledger.

## Current maturity
**NMIR_READINESS: 38%**.

Readiness increases from 36% to 38% only because the Cl-37 W/kg gate is now hosted, raw-result inspected, reproducible, and incorporated into an explicit Ga/Cl ledger. Global G3 is not credited as closed.

## Exact next gate
1. Build a quantitative Standard-Model target-screening ledger for additional physically relevant inverse transitions. Rank event rate and neutrino-only W/kg using matched primary nuclear response or measured `ft` authority; include threshold/spectrum overlap and pure/natural-isotope mass normalization.
2. For resonant candidates, implement the G8 overlap/integrated-strength/linewidth bound before any ranking by peak cross section; no peak-only claims.
3. In parallel, implement the sum-rule-preserving spin-response toy, reproduce the transparent-Sun `~23.5 AU` benchmark with a finite-source/Liouville gain bound, and test staggered/multi-isotope stacks against the same atoms uniformly/randomly arranged at fixed mass column.
