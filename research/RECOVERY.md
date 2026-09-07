# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-07
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Recovery protocol: `research/RECOVERY_MANUAL.md`
Funnel authority: `research/NMIR_FUNNEL.md`
Latest completed immutable record: `research/iterations/0072d_wagner_blue_identity_result.md`
Current readiness: `NMIR_READINESS: 89%`.

## Mandatory recovery order
Read `RECOVERY_MANUAL.md` completely, then this file, then `NMIR_FUNNEL.md`, newest numbered iterations plus prereg/amendments, commits newer than this reconciliation, and relevant queued/in-progress/newly-terminal Actions. Chat is never authority. Green CI alone is never scientific PASS.

## Frozen mission/accounting
NMIR is a discovery funnel, not a material scan. Keep state/focusing, microscopic interaction probability, detector visibility/amplification, and irreversible neutrino-supplied deposited energy separate.

`P_dep,nu = N_T integral dE mu(E,x) Phi(E) sigma_eff(E) E_dep,nu(E)`, with `0 <= E_dep,nu <= E_nu`.

Daughter decay, target preparation, stored free energy, pumping, mediator preparation and reset work are never neutrino-supplied power. Never multiply unvalidated gains.

## Stable broad guards
Closed in stated scopes unless a genuinely new assumption changes them: naive static `N^2`; geometry-only fixed-column gain; passive local density/phonon or spin/magnon free superextensive gain; extensive long-range-pair free gain; passive stable finite linear/nonlinear mediator free gain after field/free-energy accounting; linewidth narrowing as new integrated strength; metastable avalanche as neutrino-energy gain; bounded finite-range k-local higher-body free superextensive gain; actual-SM growing-coordination survivor absent in audited passive-SM scope.

## G2 detector chain
0049 transfer requirement: for 10-kg Ar40 and 10 accepted solar CEvNS/year, `eta=0.42207478` at 10 eV, `0.75683153` at 20 eV, impossible `2.35795954` at 40 eV. 0050/0051 close known-background and nuisance-aware budgets. Representative S=10/year ceilings: 3sigma/30% `4.274968302863348/year`; 5sigma/30% `1.0806120114381677/year`; 5sigma/50% `0.692094879071742/year`. 0058 requires `1.44e7–1.78e7` additional rejection at full acceptance. 0063 `BLOCKED_PUBLIC_ACHIEVEMENT_ANCHOR`; G2 `BLOCKED_NOT_ACTIONABLE` unless new same-configuration sub-keV measured rejection×bulk-NR acceptance appears.

## G3 passive-SM deposited-power chain
0047 `PASS_KLOCAL_EXTENSIVITY`. 0048 empirical/EFT stress strongly negative but not theorem: even 100× empirical extra-amplitude anchor gives `1.301537448e-5 W/kg`; bridge to 1 W/kg needs amplitude `28796.42286 = 28511.31×` anchor. 0059 `PASS_NO_UNIVERSAL_HARD_BOUND_FOUND / RESIDUAL_OPEN`; 0060 `PASS_NO_SM_GROWING_COORDINATION_SURVIVOR`; 0062 partial-wave route fails as coefficient-independent theorem and is too weak; 0065 `PASS_NO_COEFFICIENT_INDEPENDENT_OBSERVABLE_MAP / RESIDUAL_OPEN`. Absolute short-range/contact coefficient remains physically OPEN with no currently identified new coefficient-independent executable route.

## G8 RIOEC / Cu63
RIOEC entrance is electron antineutrino; ordinary fusion solar `nu_e` forbidden. Exact-state package: `63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)`, `E_R=162.496486 keV`, `B_reverse=2.85e-3...6.72e-2`. 0067 `PASS_SOURCE_TAIL_RECOMPUTED / RATE_FOLD_OPEN`, run/job `34081044588/101616231800`, artifact `10003691395`; `dPhi_anti-nu_e/dE(E_R)=3.528363521736758e-41 cm^-2 s^-1 MeV^-1`. 0068 `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`; no Cu63 rate or W/kg claimed. G8 `BLOCKED_NOT_ACTIONABLE` pending exact primary normalization authority.

## G9 focusing
0061 `PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY`, run/job `34071432319/101589393517`, artifact `10000583684`. Frozen 10-kpc Galactic CCSN transparent-Sun utility negligible after finite-source/alignment/duty accounting.

## BSM lock/unlock
0069 `PASS_UNLOCK_BSM_CONSTRAINT_LEDGER_ONLY`; not BSM-response PASS. 0070 generic vector+scalar+axial common ledger `BLOCKED_BSM_CONSTRAINT_NORMALIZATION`; gauge-complete `U(1)_{B-L}` chosen. 0071 `BLOCKED_B_MINUS_L_PRIMARY_CONTOUR_MATERIALIZATION`. BSM remains `UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY`; no NMIR B-L response/enhancement scan until a reproducible external envelope is frozen.

## 0072 Wagner primary-vector route
Parent prereg: `research/prereg/0072_b_minus_l_contour_materialization_contract.md`, commit `837a092a46d3b0d99f222c3777af8499f01c2062`.
0072a prospective vector amendment: `research/prereg/0072a_wagner_vector_extraction_amendment.md`, commit `02cccce1c2252f4e3e56094ae35e4e2c767820a2`.
Primary Wagner arXiv:1207.2442 source archive: 2,733,483 bytes, SHA256 `c1fd33d880b5810ede631284ddb91738d5df8e1816c3f47f4bef58a9eaa4e6e3`; vector `WEP_figure6.eps`: 581,517 bytes, SHA256 `4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882`.
Frozen conversion: `|g_BL|=2.70463357586823e-19*sqrt(|alpha_tilde|)`; `m_V[eV]=1.973269804e-7/lambda[m]`.

### 0072b PASS axis calibration
`PASS_WAGNER_AXIS_CALIBRATION`. Transform:
`log10(lambda/m)=3.0018224354393763*x_eps - 7.051566622680237`;
`log10(|alpha_tilde|)=1.650456736852946*y_eps - 12.69366318007594`.
Frozen max residual 0.002 decades; observed x max `0.0012151893845810946`, y max `0.0008843296043608007`; side agreement exact within tolerance. This subgate accepts calibration only, not a contour.

### 0072c PARTIAL PASS named vector curves
Hosted raw evidence in later 0072d run reproduces `PARTIAL_PASS_WAGNER_VECTOR_CURVES`. Four source identities are unambiguous and physically transformed with round-trip max EPS error `8.881784197001252e-16`: `Princeton`, `Moscow`, `LLR_precession_inverse_square`, `LLR_differential_acceleration`. Blue family has four connected chains rather than the expected three semantic traces; no EW/EW94/EW99 name was promoted at 0072c.

### 0072d scientific FAIL blue identity
Prospective contract: `research/prereg/0072d_wagner_blue_identity_resolution.md`, commit `2014d3d7f8a027fe4065965b6d1a8dc5131e4075`. Pre-result overlap correction: `research/amendments/0072d_overlap_logic_correction.md`, commit `73fcfa69c0b5ab28098f85e55c739cf6bb0980cd`. Resolver commit `70f0ceef559c6fa67b422e3a6a413b2346f642ae`.
Classification: **`SCIENTIFIC_FAIL_WAGNER_BLUE_IDENTITY`**. Pairwise source-order rule fails because blue chains cross: chain 0 vs 3 has `y0-y3=-2.925...+1.15` on x `[2.154,5.361]`; chain 1 vs 3 has `-0.6579787...+0.9835333` on `[2.349,3.678]`. No unique global top/bottom candidate, therefore EW/EW94/EW99 semantic identities are not assigned and no post-hoc shape/label-proximity rescue is allowed.

Authoritative hosted run/job: `34112933849 / 101713070731`. Raw log inspected. Persisted result: `data/wagner_blue_identity_0072d.json`, bot commit `590ed0850984446f9cecb0e3d6e05a19cda95d46`. Artifact `10015072386`, ZIP SHA256 `ce4db4c90c234e79b60d019f3e8b9326bf81860a9ec365e75400fd40d58ea8ce`. Immutable iteration commit `d2fe40f5890879671ab7a686194cfc1b990d5920`.
Raw JSON SHA256s from hosted log: axis calibration `f3f84f388f03d952a7c7274c2d5bf7e1a947b0ab8664926a08d2a6b5cd07e9e3`; named curves `7ee5dcbb644ed16fee2b596b91ec8f1ce43a040c39cbfb3ffb9202158a8748a3`; blue identity `64c3c2a24cb22922f7872662ca0c9977c9728ec24bc7aecc2cd7c67b299462ee`.

0072d does not invalidate 0072b calibration or the four unambiguous 0072c curves. It retires only the frozen Wagner-blue semantic-resolution route.

Latest baseline CI on 0072d head: run `34113035477`, completed success; infrastructure evidence only.

## Current funnel state
- G2: `BLOCKED_NOT_ACTIONABLE`.
- G3: strong partial negative/structural closure; absolute contact coefficient OPEN_NOT_CURRENTLY_ACTIONABLE.
- G8: target/source provenance PASS, primary normalization BLOCKED.
- G9: physical focusing PASS, frozen utility strong-negative.
- BSM: `UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY`; Wagner route is partial primary materialization plus blue-identity scientific FAIL; no global B-L envelope yet.

## Exact next funnel gate
Follow the frozen 0072d decision tree: switch to the independent same-convention direct-detection route using De Romeri–Papoulias–Ternes, JHEP 05 (2024) 165 / arXiv:2402.05506, anchored to primary PandaX-4T solar-neutrino electron-recoil information. Before any result-dependent reproduction, prospectively freeze exact experimental bins/exposure/background treatment, B-L scattering convention, solar flux, detector response and likelihood/statistic. The new route must reproduce a primary published benchmark/SM spectrum before emitting a B-L contour. Raster/manual contour digitization remains forbidden. Cosmology/stellar primary source archives remain parallel 0072 targets.

## Critical guards
Event/detection gain != interaction gain != neutrino-energy gain. Peak resonance != integrated capture. A fitted EFT LEC range is not regulator-independent authority. A per-partial-wave unitarity bound does not justify universal hard `lmax~kR`. Inclusive response agreement does not isolate arbitrary contact strength with interference. Metastable amplification requires stored-energy/reset accounting. Low threshold is not full efficiency. Cross-detector rejection×acceptance multiplication forbidden. Ordinary solar `nu_e` forbidden for RIOEC. Raster/manual contour reading forbidden. Frozen criteria never weakened. No F9 multiplication of unvalidated gains.
