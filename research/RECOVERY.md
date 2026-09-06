# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Recovery protocol: `research/RECOVERY_MANUAL.md`
Funnel authority: `research/NMIR_FUNNEL.md`
Latest immutable validated scientific record: `research/iterations/0047_finite_range_klocal_current_extensivity.md`
Current readiness: `NMIR_READINESS: 76%`.

## Mandatory recovery order
Read `RECOVERY_MANUAL.md` completely, then this file, then `NMIR_FUNNEL.md`, then the newest numbered iteration/prereg files, recent commits newer than this reconciliation, and relevant queued/in-progress/newly-terminal GitHub Actions. Chat history is not authority. Do not duplicate running work. A green workflow is not a scientific PASS without the scientific payload/log/artifact being inspected.

## Frozen accounting
NMIR is a discovery funnel, not a material scan. Keep separate state/focusing, microscopic interaction, detector visibility/amplification, and irreversible neutrino-supplied deposited energy.

`P_dep,nu = N_T integral dE mu(E,x) Phi(E) sigma_eff(E) E_dep,nu(E)`, with `0 <= E_dep,nu <= E_nu`.

Daughter decay, nuclear mass release, target preparation, stored medium free energy, external pumping, mediator preparation and reset work are never neutrino-supplied power. Never multiply unvalidated gains.

## Stable baseline authority
- Tritium measured-ft inverse capture: `sigma(v/c)≈7.785e-45 cm^2`, ~0.7% from published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; locally pinned pp/hep/B8/CNO spectra; thermally broadened Be7 profile; daytime adiabatic 3-flavour MSW for charged-current folds. CEvNS is active-flavour neutral current and has no Pee factor.
- Charged-current validated target leader remains pure 7Li/GS98: `1.06589117e-21 W/kg`, ~`9.38e20` below 1 W/kg. This is not an all-nucleus theorem.

## Broad frozen class closures
Do not reopen without a genuinely new assumption. Full derivations/provenance are in immutable numbered notes.
- 0024 leading-allowed passive envelope: strong-negative scoped.
- 0025 isolated-resonance area theorem: linewidth narrowing creates no integrated entrance strength.
- 0026 finite-q vector/axial envelope: strong-negative scoped.
- 0027 coordinate-local density f-sum: no free superextensive density/phonon energy gain.
- 0028 bounded-local spin first moment: no free superextensive local spin/magnon energy gain.
- 0031 extensive long-range-pair absolute budget -> extensive response.
- 0032/0038/0039 stable passive linear/nonlinear mediator energy-ledger closures.
- 0034 fixed-column geometry theorem and passive-mixture theorem.
- 0040 metastable avalanche: `DETECTION PASS-SURVIVOR / NEUTRINO-ENERGY-GAIN STRONG_NEGATIVE_SCOPED`; avalanche energy comes from stored free energy.
- 0047 bounded finite-range k-local two-/higher-body current class: `PASS_KLOCAL_EXTENSIVITY`; no free superextensive first-moment scaling at fixed support size, norm and site incidence. Absolute higher-body coefficient strength and genuinely long-range/growing-coordination operators remain OPEN.

## G2 CEvNS chain — validated through 0046
- 0041 Ar40 at 40 eV: exact source-opening threshold `E_nu,min=0.8628609380 MeV`.
- 0042 physical Be7 profile × Ar40: at 40 eV 31.104% source tail but only `4.906342834e-6` retained cross section and `3.973604373e-8 events/(kg day)`; endpoint suppression is severe.
- 0043 continuous-A inverse design law at fixed kg and approximate fixed QW/A: `A_star=2E_nu^2/(3 m_u T_thr)`, equivalently `Tmax(A_star)≈3T_thr`; class-level envelope only.
- 0044 retained scientific FAIL: `M=A m_u` caused ~30% error at Ar40/Be7 40-eV endpoint; criterion was not relaxed.
- 0045 exact-mass, actual-Z/N, full-solar 23-real-nucleus optimization PASS. Representative winners: Pb208 at 1,3,20,40 eV; Xe132 at 5 eV; Se82 at 10 eV. This is source/threshold matching, not interaction enhancement.
- 0046 `PASS_PHASE_DIAGRAM`; authoritative note `research/iterations/0046_cevns_target_threshold_phase_diagram.md`. Hosted run/job `34052930672/101539642497`; artifact `9995368376`; ZIP SHA256 `046953d77896362afaaf5da0ff2015ddb36958196c0b921cc5e3f0ff4efe3951`; raw log inspected, 29 tests PASS. Refined crossovers [eV]: Pb208→W184 3.9453125; W184→Xe132 4.4453125; Xe132→Mo100 6.3515625; Mo100→Se82 6.7265625; Se82→Ge74 12.5078125; Ge74→Ti48 12.9296875; Ti48→Ar40 12.9609375; Ar40→Pb208 15.5703125. All brackets width 0.015625 eV and independent topology checks PASS.

G2 next practical survivor gate is the **real metastable detector transfer ledger**: measured nucleation/trigger efficiency versus recoil, threshold distribution and stability, dark counts/backgrounds, reset/dead time/live fraction, stored-energy preparation/reset cost. Keep detector gain separate from neutrino deposited-energy gain.

## G3 passive-SM deposited-power status
Leading/allowed, finite-q, one-body, local density/spin, passive mediator and now finite-range k-local collective-scaling loopholes are bounded/closed in their stated scopes.

0047 authority: prereg commit `1e669c71a10784120d831c5c57560129146df333`; scientific head `21e42755ed237074601f45a48a401a52586c0de2`; hosted run/job `34056195172/101548425397`; artifact `9996023078`; ZIP SHA256 `7203aaec5cb567c1ac8cac3ca661198f5d8673bf132497bc3eb4b7edd5b402cb`; raw log: 4 tests PASS, 72 support-enumeration cases, 24 explicit matrix cases, max count/bound 0.75, max local nested/bound 0.7822716656, max measured m1/global-bound 0.00200549056, bound/site exactly 240 for N=6..64. Classification `PASS_KLOCAL_EXTENSIVITY`.

Exact next G3 funnel gate: **absolute genuine two-/higher-body Standard-Model current strength envelope**. Prospectively freeze chiral-EFT/power-counting and empirical two-body-current primary authorities, derive/benchmark an absolute coefficient/operator-norm envelope, then propagate that envelope through the frozen solar spectra into the common neutrino-only W/kg score. Do not infer small absolute strength merely from extensivity.

## Other OPEN survivors
- G8 target-specific thermal-solar anti-nu_e RIOEC remains OPEN/BLOCKED until a primary thermal-solar anti-nu_e spectral density and independently evaluated entrance strength/width are frozen; ordinary solar nu_e flux is forbidden for this entrance channel.
- G9 transparent-Sun focal scale is robust/partial; distant-source physical flux × finite source/alignment/duty-cycle utility remains OPEN. Solar-neutrino self-lensing is inapplicable.
- G10 geometry-only staggered/fixed-column and passive mixing gains are closed; only genuinely structure-induced microscopic-response changes could reopen under a new hypothesis.
- BSM/light mediator remains LOCKED until principal passive-SM residuals are substantially bounded.

## Research-gate snapshot
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body/detection | **PARTIAL PASS — ideal CEvNS phase diagram CLOSED; real metastable detector ledger OPEN** |
| G3 maximum passive-SM deposited power | **PARTIAL PASS — finite-range k-local collective scaling CLOSED; absolute higher-body strength + genuine long-range/growing-coordination residual OPEN** |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5/G6 BSM | LOCKED |
| G7 production↔absorption | PARTIAL PASS |
| G8 resonance integrated strength | PARTIAL PASS; target-specific thermal anti-nu RIOEC OPEN/BLOCKED |
| G9 gravity | PARTIAL PASS; distant-source utility OPEN |
| G10 fixed-column geometry/composition | STRONG NEGATIVE in frozen geometry-only scope |

## Critical guards
Event/detection gain != interaction gain != neutrino-energy gain. Peak resonance != integrated capture. Directional coherence != integrated opacity. Gravitational gain must satisfy source geometry, finite-source/Liouville and receiver integration. A few-target maximum is not a global SM ceiling. Selected-nucleus two-body corrections are not universal maxima. Metastable amplification requires stored-energy/reset accounting. Frozen criteria are never weakened after results. No F9 multiplication of unvalidated gains.
