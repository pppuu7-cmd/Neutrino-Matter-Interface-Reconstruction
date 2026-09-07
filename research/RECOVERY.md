# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-07
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Recovery protocol: `research/RECOVERY_MANUAL.md`
Funnel authority: `research/NMIR_FUNNEL.md`
Latest immutable scientific/architecture record: `research/iterations/0071_b_minus_l_primary_constraints_ledger.md`
Current prospective gate: `research/prereg/0072_b_minus_l_contour_materialization_contract.md`
Current readiness: `NMIR_READINESS: 89%`.

## Mandatory recovery order
Read `RECOVERY_MANUAL.md` completely, then this file, then `NMIR_FUNNEL.md`, newest numbered iterations and their prereg/amendments, commits newer than this reconciliation, and relevant queued/in-progress/newly-terminal Actions. Chat is never authority. Green CI alone is never scientific PASS.

## Frozen mission/accounting
NMIR is a discovery funnel, not a material scan. Keep state/focusing, microscopic interaction probability, detector visibility/amplification, and irreversible neutrino-supplied deposited energy separate.

`P_dep,nu = N_T integral dE mu(E,x) Phi(E) sigma_eff(E) E_dep,nu(E)`, with `0 <= E_dep,nu <= E_nu`.

Daughter decay, target preparation, stored free energy, pumping, mediator preparation and reset work are never neutrino-supplied power. Never multiply unvalidated gains.

## Stable baseline authority / broad guards
- Tritium measured-ft inverse capture: `sigma(v/c)≈7.785e-45 cm^2`, ~0.7% from published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fusion fluxes; pinned pp/hep/B8/CNO spectra; thermally broadened Be7; daytime adiabatic 3-flavour MSW for CC folds; CEvNS has no Pee factor.
- Charged-current validated target leader: pure 7Li/GS98 `1.06589117e-21 W/kg`, ~`9.38e20` below 1 W/kg; not an all-nucleus theorem.
- Frozen broad closures in stated scopes: naive static `N^2`; linewidth narrowing as new integrated strength; coordinate-local density/phonon and bounded-local spin/magnon free superextensive gain; extensive long-range-pair free gain; passive stable finite linear/nonlinear mediator free gain after field/free-energy accounting; fixed-column geometry-only gain; metastable avalanche as neutrino-energy gain; bounded finite-range k-local higher-body free superextensive gain; actual-SM growing-coordination survivor absent in audited passive-SM scope.

## G2 CEvNS / detector chain
0041–0046 close source-opening, Be7 profile suppression, continuous-A inverse design, exact-mass correction, real-nucleus full-solar optimization and target/threshold phase diagram. 0046 run/job `34052930672/101539642497`, artifact `9995368376`, raw 29 tests PASS.

0049: for 10-kg Ar40 and 10 accepted solar CEvNS/year, `eta=<epsilon_NR>*f_live=0.42207478` at 10 eV, `0.75683153` at 20 eV, and impossible `2.35795954` at 40 eV.

0050/0051 close known-background and nuisance-aware background budgets. Representative 0051 ceilings for S=10/year: 3σ/30% `4.274968302863348/year`; 5σ/30% `1.0806120114381677/year`; 5σ/50% `0.692094879071742/year`.

0052–0058 close measured-threshold Si transfer, LEE stress, mitigation/time-information and required rejection×acceptance envelopes; 0058 still requires `1.44e7–1.78e7` additional rejection at full signal acceptance.

0063: `BLOCKED_PUBLIC_ACHIEVEMENT_ANCHOR`; no public same-configuration sub-keV measured rejection × bulk-NR acceptance pair satisfying the frozen comparator. No cross-detector multiplication.

**G2 state:** `BLOCKED_NOT_ACTIONABLE` unless genuinely new same-configuration measured evidence appears.

## G3 passive-SM deposited-power chain
0047 bounded finite-range k-local current: `PASS_KLOCAL_EXTENSIVITY`, run/job `34056195172/101548425397`, artifact `9996023078`.

0048 empirical/EFT stress is strongly negative but not a theorem: even 100× the largest empirical extra-amplitude anchor gives `1.301537448e-5 W/kg`; bridge to 1 W/kg requires amplitude `28796.42286 = 28511.31×` empirical anchor.

0059: `PASS_NO_UNIVERSAL_HARD_BOUND_FOUND / RESIDUAL_OPEN`.
0060: `PASS_NO_SM_GROWING_COORDINATION_SURVIVOR` in audited passive-SM scope.
0062: `FAIL_UNITARITY_MODEL / HARD_LMAX_NOT_COEFFICIENT_INDEPENDENT; DIAGNOSTIC_BOUND_TOO_WEAK / RESIDUAL_OPEN`, run/job `34071960179/101590826472`, artifact `10000809024`; finite-l diagnostic `520819.2495826213 W/kg`, floor-control `130204.81239565533 W/kg`.
0065: `PASS_NO_COEFFICIENT_INDEPENDENT_OBSERVABLE_MAP / RESIDUAL_OPEN`.

**Remaining G3 residual:** absolute short-range/contact-current coefficient remains physically OPEN. 0059/0062/0065 retire three distinct universal-ceiling routes. No currently identified new coefficient-independent theorem/input route is executable; do not count this as closure.

## G8 RIOEC / Cu63
Channel guard: RIOEC entrance is electron antineutrino; ordinary pp/CNO/B8 solar `nu_e` flux is forbidden. Integrated resonance strength/source-profile guards remain frozen.

Exact-state Cu63 target package authority:
- `63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)`;
- `E_R=162.496486 keV`;
- reverse-strength envelope `B_reverse=2.85e-3...6.72e-2` (~23.58× spread).

0067 source-tail gate: prereg `e42cd8ccd8a321cfa850b87b0fbd8d11bed30956`; authoritative run/job `34081044588/101616231800`; artifact `10003691395`; ZIP SHA256 `22cc917e5ac275fb509d78b69565736a0d73f433f45461bb20d4d0e01232bfb9`; classification `PASS_SOURCE_TAIL_RECOMPUTED / RATE_FOLD_OPEN`.
Validated source numbers from Haxton-Lin ordinary-Compton Eq. (9)+BP98: `dPhi_anti-nu_e/dE(162.496486 keV)=3.528363521736758e-41 cm^-2 s^-1 MeV^-1`; 5-keV sanity value `3.765698986767552e7`; 6000->12000 relative change `5.832844895924436e-8`; BP98 blob SHA256 `6bd3c2d9cde15b74cf1fcebe1620566e2b3d832c09e65fc36d5422a6ef0bf198`.

0068 primary normalization/materialization gate: prereg commit `44abb5844e6bbcd358fd224052cf7bce92f2e881`; ledger commit `dfe1b11538079a7cb76c7c1aedba0c8c366ff50d`; immutable note commit `0a7d726dbb599d78831f91a888c1947a6c6d542c`; classification **`BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`**.

**G8 state:** `BLOCKED_NOT_ACTIONABLE` at primary normalization authority. This is not a physical no-go.

## G9 distant-source focusing
0061: `PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY`, run/job `34071432319/101589393517`, artifact `10000583684`. At `b/Rsun=0.024`, focus `24.073780819657056 AU`; 21-km source at 10 kpc projects to `0.2451 mm`; 1/10/100-m alignment probabilities `~1.93e-26,1.93e-24,1.93e-22`; impossible full-solar-disk collection still yields expected multiplier only `~1.00000000934`.

## BSM lock/unlock and constraint authority
0066: `FAIL_KEEP_BSM_LOCKED_OPEN_SM_ACTIONABLE` because G8/Cu63 was then immediately actionable.

0069 re-applied the unchanged criterion after 0068 changed G8 to an authority blocker and classified **`PASS_UNLOCK_BSM_CONSTRAINT_LEDGER_ONLY`**. BSM response/enhancement scans remain forbidden until constraints are frozen.

0070 classification: **`BLOCKED_BSM_CONSTRAINT_NORMALIZATION`**. A generic vector+scalar+axial common ledger cannot be built without post-hoc coupling/branching/thermal-history/UV assumptions. Anomaly-free `U(1)_{B-L}` remains the clean actionable gauge-complete benchmark.

0071 prereg commit `80d93debb2a20e35d6e06fa3000591f82ffbd1a8`; machine-readable primary-family ledger commit `70a282743c9b9b0d6c1ab495ee45eed61e2f0e99`; immutable iteration commit `805140c678211c5ebc1e586eb031e2e6f2ab96f1`.

0071 classification: **`BLOCKED_B_MINUS_L_PRIMARY_CONTOUR_MATERIALIZATION`**.
- All required primary B-L constraint families were identified in compatible model language: CEvNS/neutrino scattering, neutrino-electron/direct detection, collider context, stellar/SN, cosmology and fifth force.
- Representative authorities include Cadeddu et al. JHEP 01 (2021) 116; De Romeri et al. JHEP 05 (2024) 165; Hong-Shin-Yun PRD 103 (2021) 123031; Esseili-Kribs JCAP 05 (2024) 110; and MICROSCOPE-derived long-range B-L analyses.
- The blocker is numerical reproducibility: several controlling constraints are published primarily as graphical contours without a common machine-readable table. 0071 forbids reading values by eye from uncalibrated plots.
- No global surviving region and no full-interval exclusion is therefore claimed.

BSM remains **`UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY`**. No B-L NMIR response/enhancement scan is allowed.

## Current prospective gate — 0072
`research/prereg/0072_b_minus_l_contour_materialization_contract.md`, prereg commit `837a092a46d3b0d99f222c3777af8499f01c2062`.

Materialize controlling primary B-L contours by auditable routes only: author/publisher numerical data or public code first; otherwise calibrated vector-path extraction from PDF/XML/SVG; otherwise independent likelihood reproduction under the exact primary B-L convention. Manual raster plot reading is forbidden.

Priority order: fifth-force low-mass region; BBN/CMB + stellar/SN eV–MeV region; CEvNS/neutrino-electron/direct-detection keV–GeV region. Only after enough validated contours cover the full frozen `1e-6 eV–10 GeV` interval may a global allowed region be frozen.

## Research-gate snapshot
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body/detection | **BLOCKED_NOT_ACTIONABLE through 0063** |
| G3 maximum passive-SM deposited power | **STRONG PARTIAL PASS; absolute contact coefficient OPEN_NOT_CURRENTLY_ACTIONABLE** |
| G4 engineered resonance/polarization/periodicity | broad passive guards CLOSED in stated scopes |
| G5/G6 BSM | **UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY; generic normalization BLOCKED via 0070; B-L contour materialization prospective 0072** |
| G7 production↔absorption | PARTIAL PASS |
| G8 RIOEC | **Cu63 target/source provenance PASS; normalization authority BLOCKED via 0068** |
| G9 gravity | **physical focusing PASS; 10-kpc CCSN utility STRONG NEGATIVE** |
| G10 fixed-column geometry/composition | STRONG NEGATIVE in frozen scope |

## Exact next funnel gate
**Execute 0072 first.** Reproducibly materialize primary `U(1)_{B-L}` constraints in `(m_V,g_BL)` without manual plot reading. No NMIR BSM enhancement calculation until a global external allowed region is immutable and a separate response contract is prospectively frozen.

## Critical guards
Event/detection gain != interaction gain != neutrino-energy gain. Peak resonance != integrated capture. Selected-nucleus two-body corrections are not universal maxima. A fitted EFT LEC range is not regulator-independent authority. A per-partial-wave unitarity bound does not justify a hard universal `lmax≈kR`. Inclusive response agreement does not isolate arbitrary contact strength when interference is allowed. Metastable amplification requires stored-energy/reset accounting. Low threshold is not full efficiency. Cross-detector rejection × acceptance multiplication is forbidden. Ordinary solar `nu_e` is forbidden for RIOEC. Frozen criteria are never weakened after results. No F9 multiplication of unvalidated gains.
