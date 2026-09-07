# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-07
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Protocol: `research/RECOVERY_MANUAL.md`
Funnel: `research/NMIR_FUNNEL.md`
Latest completed immutable record: `research/iterations/0075_g9_persistent_known_direction_solar_lens_admissibility.md`, commit `0f5d60d2d114c3676363420ff2ea85f2fa0e9c3a`.
Current prospective subgate: `research/prereg/0076_g9_global_multiimage_radial_kernel.md`, commit `05a3354dd2f8cdbba1f2dd04342161b515a10304`.
`NMIR_READINESS: 91%`.

## Mandatory recovery order
Read `RECOVERY_MANUAL.md` -> this file -> `NMIR_FUNNEL.md` -> newest numbered iterations/preregs -> commits newer than this reconciliation -> relevant queued/in-progress/newly-terminal Actions. Repository is scientific authority; chat is not. Green CI alone is not scientific PASS; inspect raw scientific log/artifact against the frozen prospective contract.

## Frozen mission / accounting
NMIR is a discovery funnel, not a material scan. Separate state/focusing, microscopic interaction probability, detector visibility/amplification and irreversible neutrino-supplied deposited energy. Daughter decay, target preparation, stored free energy, pumping, mediator preparation and reset work are never neutrino-supplied power. Event gain != interaction gain != neutrino-energy gain. Never multiply unvalidated gains.

## Stable broad guards
Closed in stated scopes unless a genuinely new assumption changes them: naive static `N^2`; geometry-only fixed-column gain; passive local density/phonon or spin/magnon free superextensive gain; extensive-budget long-range-pair free gain; passive stable finite linear/nonlinear mediator free gain after energy accounting; linewidth narrowing as new integrated strength; metastable avalanche as neutrino-energy gain; bounded finite-range k-local higher-body free superextensive gain; no actual-SM growing-coordination survivor in audited passive-SM scope.

## G2
0049 transfer requirement: 10-kg Ar40, 10 accepted solar CEvNS/year -> `eta=0.42207478` at 10 eV, `0.75683153` at 20 eV, impossible `2.35795954` at 40 eV. 0050/0051 close known-background and nuisance-aware budgets. Representative S=10/year ceilings: 3sigma/30% `4.274968302863348/year`; 5sigma/30% `1.0806120114381677/year`; 5sigma/50% `0.692094879071742/year`. 0058 needs `1.44e7–1.78e7` additional rejection at full acceptance. 0063 `BLOCKED_PUBLIC_ACHIEVEMENT_ANCHOR`; G2 `BLOCKED_NOT_ACTIONABLE` pending genuinely new same-configuration sub-keV measured rejection×bulk-NR acceptance.

## G3
0047 `PASS_KLOCAL_EXTENSIVITY`. 0048 empirical/EFT absolute-strength stress strongly negative but not theorem: 100× empirical extra-amplitude anchor gives `1.301537448e-5 W/kg`; bridge to 1 W/kg needs amplitude `28796.42286 = 28511.31×` anchor. 0059 no universal coefficient hard bound; 0060 no actual-SM growing-coordination survivor in audited passive scope; 0062 partial-wave route is not coefficient-independent and too weak; 0065 `PASS_NO_COEFFICIENT_INDEPENDENT_OBSERVABLE_MAP / RESIDUAL_OPEN`. Absolute short-range/contact coefficient remains physically OPEN with no currently identified executable coefficient-independent route. 0065 forbids repeating inclusive-response, GT/Ikeda or muon-capture information as a universal hard ceiling without a genuinely new operator theorem/assumption.

## G8
Exact Cu63 RIOEC state: `63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)`, `E_R=162.496486 keV`, `B_reverse=2.85e-3...6.72e-2`. 0067 `PASS_SOURCE_TAIL_RECOMPUTED / RATE_FOLD_OPEN`, run/job `34081044588/101616231800`, artifact `10003691395`, `dPhi_anti-nu_e/dE(E_R)=3.528363521736758e-41 cm^-2 s^-1 MeV^-1`. 0068 `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`; no Cu63 rate/Wkg claimed. Ordinary solar `nu_e` forbidden for RIOEC.

## G9
0061 `PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY`, run/job `34071432319/101589393517`, artifact `10000583684`; frozen 10-kpc Galactic CCSN transparent-Sun utility negligible after finite-source/alignment/duty accounting. Its immutable scope explicitly did not close persistent/known-direction sources.

### 0075 persistent/known-direction class — CLOSED BLOCKED
Prospective contract commit `60dfd94c269e8d5b3a23f73043c779099cd15783`. Corrected implementation head `844ca8fcd5bfd46649a48bc37df39eb8a44c6c98`; hosted run/job `34149433817/101828380178`; artifact `10028826311`; artifact ZIP SHA256 `1c60e0ce3756250d82632df8b407202df98cd1bfe74774216950e8c4a0864ed8`. Artifact metadata digest and independently downloaded ZIP hash matched exactly, and the raw JSON artifact was inspected directly.

Classification: **`BLOCKED_G9_PERSISTENT_GEOMETRY`**. Exact reason: `local focal branch turned before requested support`. No `mu>=2` survivor, no strong-negative utility map, and no grid point was claimed. Repository raw-result copy `data/g9_persistent_lens_0075.json`, commit `576c0ce88195686743d1c4d0651ae322a14e0f92`; immutable iteration commit `0f5d60d2d114c3676363420ff2ea85f2fa0e9c3a`.

The blocker is sharply localized: the pinned Model-S lens equation exists globally in impact parameter, but the 0061 local one-ring monotone solver cannot be continued through a radial turn without a validated multi-image segmentation/no-double-counting rule. Stale run `34149348350` is non-authoritative regardless of status.

### 0076 global multi-image radial kernel — RUNNING
Prospectively frozen before any 0076 numerical result at commit `05a3354dd2f8cdbba1f2dd04342161b515a10304`. This is a geometry/method validation gate only; it is forbidden to inspect/classify the old 0075 utility map.

Frozen method: full validated impact domain `1e-4<=b/Rsun<=1`; observer-distance controls generated by `b/Rsun=0.020,0.024,0.030`; discover/refine all signed-map roots; insert roots so narrow caustic intervals cannot be missed; solve disjoint global preimages of `|y|<=r` for `r=1e0...1e9 cm`; sum each impact annulus once. PASS requires root recovery within `1e-10`, nonnegative monotone cumulative area <= `pi R_sun^2`, local exact one-ring reproduction within `0.5%`, and base-vs-once-bisected-grid cumulative area agreement within `0.5%`.

Implementation: `src/nmir/g9_global_kernel.py` commit `554c2b806ab4d22efa1c3dd18e60e268c8f8ff48`; tests commit `3004a5a6f7fbf45fa639d0104e8958849cb51ec4`; benchmark commit `448540cd0af75550f4a211c3ae66cf5fad0d5025`; workflow commit `e6bf01e281d5f4f70c54e6ca74c23f27c3bdf776`. Hosted run/job `34149715242/101829231239` is in progress at this reconciliation; dedicated regression tests have completed successfully and the fail-closed scientific benchmark is running. Do not duplicate it. No scientific classification until its raw artifact is terminal and inspected.

## BSM architecture
0069 `PASS_UNLOCK_BSM_CONSTRAINT_LEDGER_ONLY`; this is not BSM-response PASS. 0070 generic vector+scalar+axial constraint composition `BLOCKED_BSM_CONSTRAINT_NORMALIZATION`; gauge-complete `U(1)_{B-L}` selected. 0071 `BLOCKED_B_MINUS_L_PRIMARY_CONTOUR_MATERIALIZATION`. No NMIR B-L response/enhancement scan until reproducible external constraints are frozen.

### 0072 Wagner primary-vector route
Primary Wagner `WEP_figure6.eps` hash-pinned. 0072b `PASS_WAGNER_AXIS_CALIBRATION`; 0072c `PARTIAL_PASS_WAGNER_VECTOR_CURVES` accepts Princeton, Moscow and two LLR curves. 0072d `SCIENTIFIC_FAIL_WAGNER_BLUE_IDENTITY`: blue EW-family chains cross under preregistered identity rule, so no post-hoc semantic rescue. Hosted run/job `34112933849/101713070731`; artifact `10015072386`; ZIP SHA256 `ce4db4c90c234e79b60d019f3e8b9326bf81860a9ec365e75400fd40d58ea8ce`; immutable commit `d2fe40f5890879671ab7a686194cfc1b990d5920`.

### 0073 PandaX route
0073a `PARTIAL_PASS_VECTOR_DATA_EFFICIENCY_ONLY`: exact 30 observed 1-keV bins sum to 1058 and 301-point primary efficiency accepted. Hosted run/job `34119097740/101732725133`; artifact `10017450789`; ZIP SHA256 `8d58850fca7067c84bc439b4efb1809ee321b9e574f6ae652798dc01ea971e14`; immutable commit `a83158d84b603796a81103fc36e5c2fd70204d3e`.
0073b `BLOCKED_PRIMARY_LIKELIHOOD_INPUTS`: public-primary routes do not supply four separately normalized minor-background templates required by the nuisance model. Full-profile PandaX B-L route retired; no proportional decomposition.

## 0074 COHERENT B-L likelihood materialization
Official COHERENT packages hash-pinned: Ar Analysis A Zenodo `10.5281/zenodo.3903810` v1.0 and CsI first observation `10.5281/zenodo.1228631` v1.0. Hosted materialization run/job `34130108479/101767911241`; artifact `10021726721`; ZIP SHA256 `10f96287ec55907b851e2f9b9d6ee1f6046665cd8492e9a36107ef791e2f3220`; exact per-file manifest commit `52e281e8dd858ea53240b4d527f2f5ca00030d83`.

0074a `PASS_COHERENT_AR_SM_NORMALIZATION_BENCHMARK`: run/job `34135884676/101786622645`, artifact `10023995784`, independent `134.21440238243503` events vs frozen `128±17`.

0074b `PASS_COHERENT_CSI_SM_RESPONSE_BENCHMARK`: run/job `34140558778/101801362484`, artifact `10025718339`, `152.8442722589695` events vs frozen `173±48`, exact released `6<=PE<30` support.

0074c contract commit `80d8ffaae102d8c5a3ba731dc1e8ae3b7e4d9d41` required a same-analysis non-circular numerical combined-likelihood benchmark with tolerance before minimization. Primary paper/releases pin supports, templates, nuisances and detector least-squares formulas but provide no exact combined SM/background `chi2_min`, complete profiled nuisance vector or official likelihood reference point adequate for a pre-result tolerance. Classification **`BLOCKED_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY`**. Machine-readable audit commit `17c41bf043015a3cf11dd5d33033f8ba3bc5451c`; immutable iteration commit `0aba4bdd59c31086b472b6b77e49c28af16e1ee1`. No likelihood minimization and no `(m_V,g_BL)` point evaluated.

## Current funnel state
- G9 0075 is closed BLOCKED on local geometry; 0076 global multi-image method gate is running and is the highest-value executable route.
- G3 absolute contact coefficient `OPEN_NOT_CURRENTLY_ACTIONABLE`.
- G2 `BLOCKED_NOT_ACTIONABLE`.
- G8 `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`.
- BSM constraints-only; no global B-L envelope and no B-L response scan.

## Exact next gate
Do not duplicate 0076. Inspect run/job `34149715242/101829231239` when terminal, inspect the raw `nmir-g9-0076-result` artifact and hash, and classify strictly against prereg commit `05a3354dd2f8cdbba1f2dd04342161b515a10304`. PASS may only authorize a separately preregistered future finite-source persistent-source convolution. BLOCKED/FAIL closes at the exact geometry/validation failure without tolerance relaxation.

## Critical guards
Raster/manual contour reading forbidden. No Asimov substitution for a required primary observed-data likelihood. No proportional splitting of grouped backgrounds. No cross-analysis response/template substitution without explicit identity provenance. No post-result tolerance relaxation. No F9 multiplication of unvalidated gains.
