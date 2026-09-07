# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-07
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Protocol: `research/RECOVERY_MANUAL.md`
Funnel: `research/NMIR_FUNNEL.md`
Latest completed immutable record: `research/iterations/0076_g9_global_multiimage_radial_kernel.md`, commit `073c6a8daabcfe07703d2befc1975c9b29bce1a2`.
Current prospective subgate: `research/prereg/0077_g9_turning_point_monotone_kernel.md`, commit `71c21236b1da1817d122567286c938ca6efcce6c`.
`NMIR_READINESS: 91%`.

## Mandatory recovery order
Read `RECOVERY_MANUAL.md` -> this file -> `NMIR_FUNNEL.md` -> newest numbered iterations/preregs -> commits newer than this reconciliation -> relevant queued/in-progress/newly-terminal Actions. Repository is scientific authority; chat is not. Green CI alone is not scientific PASS.

## Frozen mission / accounting
NMIR is a discovery funnel, not a material scan. Separate focusing/state control, microscopic interaction probability, detector visibility/amplification and irreversible neutrino-supplied deposited energy. Daughter decay, target preparation, stored free energy, pumping, mediator preparation and reset work are never neutrino-supplied power. Event gain != interaction gain != neutrino-energy gain. Never multiply unvalidated gains.

## Stable broad guards
Closed in stated scopes unless a genuinely new assumption changes them: naive static `N^2`; geometry-only fixed-column gain; passive local density/phonon or spin/magnon free superextensive gain; extensive-budget long-range-pair free gain; passive stable finite linear/nonlinear mediator free gain after energy accounting; linewidth narrowing as new integrated strength; metastable avalanche as neutrino-energy gain; bounded finite-range k-local higher-body free superextensive gain; no actual-SM growing-coordination survivor in audited passive-SM scope.

## G2
0049 transfer requirement: 10-kg Ar40, 10 accepted solar CEvNS/year -> `eta=0.42207478` at 10 eV, `0.75683153` at 20 eV, impossible `2.35795954` at 40 eV. 0050/0051 close known-background and nuisance-aware budgets. Representative S=10/year ceilings: 3sigma/30% `4.274968302863348/year`; 5sigma/30% `1.0806120114381677/year`; 5sigma/50% `0.692094879071742/year`. 0058 needs `1.44e7–1.78e7` additional rejection at full acceptance. 0063 `BLOCKED_PUBLIC_ACHIEVEMENT_ANCHOR`; G2 `BLOCKED_NOT_ACTIONABLE` pending genuinely new same-configuration sub-keV measured rejection×bulk-NR acceptance.

## G3
0047 `PASS_KLOCAL_EXTENSIVITY`. 0048 empirical/EFT absolute-strength stress strongly negative but not theorem: 100× empirical extra-amplitude anchor gives `1.301537448e-5 W/kg`; bridge to 1 W/kg needs amplitude `28796.42286 = 28511.31×` anchor. 0059 no universal coefficient hard bound; 0060 no actual-SM growing-coordination survivor in audited passive scope; 0062 partial-wave route is not coefficient-independent and too weak; 0065 `PASS_NO_COEFFICIENT_INDEPENDENT_OBSERVABLE_MAP / RESIDUAL_OPEN`. Absolute short-range/contact coefficient remains physically OPEN with no currently identified executable coefficient-independent route.

## G8
Exact Cu63 RIOEC state: `63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)`, `E_R=162.496486 keV`, `B_reverse=2.85e-3...6.72e-2`. 0067 `PASS_SOURCE_TAIL_RECOMPUTED / RATE_FOLD_OPEN`, run/job `34081044588/101616231800`, artifact `10003691395`, `dPhi_anti-nu_e/dE(E_R)=3.528363521736758e-41 cm^-2 s^-1 MeV^-1`. 0068 `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`; no Cu63 rate/Wkg claimed.

## G9
0061 `PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY`, run/job `34071432319/101589393517`, artifact `10000583684`; 10-kpc Galactic CCSN transparent-Sun utility negligible after finite-source/alignment/duty accounting. Persistent/known-direction sources explicitly remained out of scope.

0075 contract commit `60dfd94c269e8d5b3a23f73043c779099cd15783`; run/job `34149433817/101828380178`; artifact `10028826311`; ZIP SHA256 `1c60e0ce3756250d82632df8b407202df98cd1bfe74774216950e8c4a0864ed8`. Classification `BLOCKED_G9_PERSISTENT_GEOMETRY`: the local one-ring branch turns before the requested blur support. Immutable commit `0f5d60d2d114c3676363420ff2ea85f2fa0e9c3a`.

### 0076 global scan-grid multi-image kernel — CLOSED SCIENTIFIC FAIL
Prospective contract commit `05a3354dd2f8cdbba1f2dd04342161b515a10304`. Hosted run/job `34149715242/101829231239`, head `e6bf01e281d5f4f70c54e6ca74c23f27c3bdf776`; artifact `10029092681`, 2640 bytes; artifact ZIP SHA256 `759f9b79acf8d4a990190c63389571e912b2c7afa619cec055ed13094a68f26c`; raw result SHA256 `66a99ff6abc86aaae465568086c6e6efb1b277dbab95ce58bfc1508bdb735340`. Raw decoded job log was inspected directly; dedicated tests `5 passed in 0.03s`.

Classification: **`SCIENTIFIC_FAIL_G9_GLOBAL_MULTIIMAGE_KERNEL`**. Root recovery, root uniqueness and area invariants pass. Frozen 0.5% grid-refinement criterion fails badly: max base-vs-bisected relative difference `0.7391843634769288`. Frozen local-authority containment also fails at `b0/Rsun=0.024`, receiver radius 100 m: global `mu=59368342.34353704` vs exact one-ring `69875418.96262653`, relative error `0.1503687101283685`, `global_contains_one_ring=false`. The 1 m and 10 m controls reproduce the local annulus accurately, localizing the defect to missed narrow `|y|<=r` preimages near radial extrema/caustics, not the signed-map physics. Repository result commit `55cd9fdae2f11e9a09a3c1e8327f3be1b09752b8`; immutable iteration commit `073c6a8daabcfe07703d2befc1975c9b29bce1a2`.

No tolerance was relaxed, no 0075 utility number was reused, and 0076 is not a physical no-go.

### 0077 turning-point / monotone-segment kernel — FROZEN, NOT YET RUN
Prospective contract commit `71c21236b1da1817d122567286c938ca6efcce6c`. This is a genuinely new numerical geometry method, not a post-hoc patch: explicitly bracket/refine radial turning points of the signed mapping, partition the full aperture into monotone segments, validate each segment at 9 interior controls, and solve `y=0,+r,-r` per segment. Same Model-S, same domain/control distances/radii; no source/detector/BSM input.

Frozen criteria retain the 0.5% exact-one-ring containment and base-vs-bisected-grid agreement and add 0.5% nominal-vs-half derivative-step agreement. Any unresolved derivative reversal is BLOCKED, not repaired by result-selected nodes. PASS alone may authorize a separately preregistered finite-source persistent-source convolution.

Implementation is not yet authoritative; a connector write attempt for `src/nmir/g9_turning_kernel.py` was blocked before repository mutation. This is not a scientific failure and no run exists yet.

## BSM architecture
0069 `PASS_UNLOCK_BSM_CONSTRAINT_LEDGER_ONLY`; no BSM-response PASS. 0072 Wagner route partially materialized but blue EW-family semantic identity failed. 0073 PandaX full-profile route blocked by missing separately normalized minor-background templates. 0074 official COHERENT packages hash-pinned; 0074a Ar SM benchmark PASS (`134.21440238243503` vs `128±17`), 0074b CsI SM response PASS (`152.8442722589695` vs `173±48`), 0074c `BLOCKED_COMBINED_LIKELIHOOD_BENCHMARK_AUTHORITY`. No global B-L envelope and no B-L response/enhancement scan.

## Current funnel state
- G9: 0076 is a scientific method FAIL; 0077 is the highest-value executable/frozen gate, pending implementation/run.
- G3 absolute contact coefficient `OPEN_NOT_CURRENTLY_ACTIONABLE`.
- G2 `BLOCKED_NOT_ACTIONABLE`.
- G8 `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`.
- BSM constraints-only; no global B-L envelope.

## Exact next gate
Implement 0077 exactly as frozen at commit `71c21236b1da1817d122567286c938ca6efcce6c`, with tests, machine-readable benchmark and fail-closed hosted workflow. Do not alter the 0.5% criteria. If implementation can be committed, run it once, inspect raw log/artifact/hash, and classify strictly as PASS/BLOCKED/SCIENTIFIC_FAIL. Only PASS may reopen finite-source persistent-source convolution.

## Critical guards
No raster/manual contour reading. No Asimov substitution for required primary observed-data likelihoods. No proportional splitting of grouped backgrounds. No cross-analysis response/template substitution without explicit identity provenance. No post-result tolerance relaxation. No F9 multiplication of unvalidated gains.
