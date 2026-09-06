# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Recovery protocol: `research/RECOVERY_MANUAL.md`
Funnel authority: `research/NMIR_FUNNEL.md`
Latest immutable validated scientific record: `research/iterations/0050_detector_background_requirement.md`
Current readiness: `NMIR_READINESS: 79%`.

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
- 0047 bounded finite-range k-local two-/higher-body current class: `PASS_KLOCAL_EXTENSIVITY`; no free superextensive first-moment scaling at fixed support size, norm and site incidence.
- 0048 empirical/EFT absolute-strength stress: `PASS_EMPIRICAL_STRENGTH_STRONG_NEGATIVE`; even 100× the largest frozen empirical extra-amplitude anchor gives only `1.301537448e-5 W/kg`, while the exact bridge to 1 W/kg requires extra amplitude `28796.42286`, or `28511.31×` the empirical anchor. This is an evidence-distance result, not a universal coefficient theorem.

## G2 CEvNS chain — validated through 0050
- 0041 Ar40 at 40 eV: exact source-opening threshold `E_nu,min=0.8628609380 MeV`.
- 0042 physical Be7 profile × Ar40: at 40 eV 31.104% source tail but only `4.906342834e-6` retained cross section and `3.973604373e-8 events/(kg day)`; endpoint suppression is severe.
- 0043 continuous-A inverse design law at fixed kg and approximate fixed QW/A: `A_star=2E_nu^2/(3 m_u T_thr)`, equivalently `Tmax(A_star)≈3T_thr`; class-level envelope only.
- 0044 retained scientific FAIL: `M=A m_u` caused ~30% error at Ar40/Be7 40-eV endpoint; criterion was not relaxed.
- 0045 exact-mass, actual-Z/N, full-solar 23-real-nucleus optimization PASS. Representative winners: Pb208 at 1,3,20,40 eV; Xe132 at 5 eV; Se82 at 10 eV. This is source/threshold matching, not interaction enhancement.
- 0046 `PASS_PHASE_DIAGRAM`; hosted run/job `34052930672/101539642497`; artifact `9995368376`; ZIP SHA256 `046953d77896362afaaf5da0ff2015ddb36958196c0b921cc5e3f0ff4efe3951`; raw 29 tests PASS. Crossovers [eV]: Pb208→W184 3.9453125; W184→Xe132 4.4453125; Xe132→Mo100 6.3515625; Mo100→Se82 6.7265625; Se82→Ge74 12.5078125; Ge74→Ti48 12.9296875; Ti48→Ar40 12.9609375; Ar40→Pb208 15.5703125.

### 0049 — necessary detector-transfer rate requirement
Immutable authority: `research/iterations/0049_detector_transfer_rate_requirement.md`.
Prospective contract commit `ab8610005f8e174fd6838f5491edab804f0a32ed`; scientific head `01186655d07883ce7d0a14f5d29c4ff16f207f1b`; hosted run/job `34057771059/101552695624`; artifact `9996491115`; ZIP SHA256 `6154810eff9116c69407e2a89052817783c75fbe2eab3a246f2d2235d6528e86`; raw 4 tests PASS and benchmark inspected.

For 10-kg Ar40 and goal 10 accepted solar CEvNS events/year, factorized necessary `eta=<epsilon_NR>*f_live` requirements are:
- 10 eV: ideal `23.6924840/year`, `eta_required=0.42207478` -> `RATE_FEASIBLE_TRANSFER_TARGET`.
- 20 eV: ideal `13.2129801/year`, `eta_required=0.75683153` -> `RATE_FEASIBLE_TRANSFER_TARGET`.
- 40 eV: ideal `4.24095487/year`, `eta_required=2.35795954` -> `RATE_IMPOSSIBLE_AT_FIXED_MASS` for 10/year at 10 kg.

Effective kg for 10 events/year: Ar10 `4.22075`, Ar20 `7.56832`, Ar40 `23.5796`, Si10 `6.29724`, Ge10 `3.47811`, Se10 `3.33393`. Ar10 needs only `1.265997×` the effective mass of ideal Se10.

### 0050 — accepted-background inverse requirement
Immutable authority: `research/iterations/0050_detector_background_requirement.md`.
Prospective contract commit `15ad880cdcf0168eaa3fb1a1447bd35d4c251d9a`; scientific head `488d23bfd6c4a84a750860e6fe1128807a4bf0eb`; hosted run/job `34057997407/101553304948`; artifact `9996559867`; ZIP SHA256 `44a5dac90c92741a09bc25e531aa192a0c4ddb8064a0de30e8c5991a82cc66c5`; raw 4 tests PASS; inversion residual `9.8809849e-15`.

Known-background, one-year Asimov counting requirement:
`Z_A=sqrt(2[(S+B)ln(1+S/B)-S])`.

For `S=10 accepted/year`:
- 3σ requires `B <= 8.22524099 accepted indistinguishable events/year`;
- 5σ requires `B <= 1.71752668/year`.

For Ar40, 10 kg, 10 eV, eta=0.50 (`S=11.8462420/year`):
- 3σ: `Bmax=12.0986684/year = 1.20986684/(kg year)`;
- 5σ: `Bmax=2.75655475/year = 0.275655475/(kg year)`.

For Ar40, 10 kg, 20 eV, eta=0.75 (`S=9.909735084/year`):
- 3σ: `Bmax=8.05522456/year = 0.805522456/(kg year)`;
- 5σ: `Bmax=1.67341796/year = 0.167341796/(kg year)`.

These are accepted analysis-indistinguishable background targets, not raw trigger/environmental rates. Background normalization uncertainty is excluded and is the exact next statistical gate.

G2 next practical steps: (1) nuisance-aware background-normalization uncertainty; (2) full recoil-dependent `epsilon_NR(T,state)` and threshold distribution; (3) calibrated detector-specific backgrounds/false triggers; (4) mass scaling and live/reset dynamics; (5) stored-energy preparation/reset accounting for metastable architectures. Evidence ledger: `research/metastable_detector_evidence_ledger.md`.

## G3 passive-SM deposited-power status
Leading/allowed, finite-q, one-body, local density/spin, passive mediator, finite-range k-local collective scaling and an empirical/EFT absolute higher-body amplitude stress are all strong-negative/closed in their exact stated scopes.

### 0047 authority
Prereg commit `1e669c71a10784120d831c5c57560129146df333`; scientific head `21e42755ed237074601f45a48a401a52586c0de2`; hosted run/job `34056195172/101548425397`; artifact `9996023078`; ZIP SHA256 `7203aaec5cb567c1ac8cac3ca661198f5d8673bf132497bc3eb4b7edd5b402cb`; raw 4 tests PASS, 72 support-enumeration cases, 24 explicit matrix cases. Classification `PASS_KLOCAL_EXTENSIVITY`.

### 0048 authority
Prospective contract commit `3c1e9c6ae65d9f34f4c6d7e3bc6bbb1c128f9091`; scientific head `e5d5de4cdd607dc0f02dd03c28b2167598382700`; hosted run/job `34057567878/101552145767`; artifact `9996427850`; ZIP SHA256 `88a259c70bd5b95c380bed1351dd183b7aadf20c77dea8cf0e44382936fd3340`; raw 5 tests PASS; raw benchmark/artifact inspected.

Frozen largest empirical extra-amplitude anchor `r_emp=1.01`. Stress ladder powers [W/kg] for S={1,3,10,100,1000}: `1.84215e-8`, `4.23810e-8`, `2.03724e-7`, `1.30154e-5`, `1.23699e-3`. Exact bridge `r_bridge=28796.4228567 = 28511.31*r_emp`. Classification `PASS_EMPIRICAL_STRENGTH_STRONG_NEGATIVE`.

Remaining G3 residuals: whether a defensible universal renormalized SM contact-coefficient bound exists without pretending EFT naturalness is a theorem; and genuinely long-range/growing-coordination SM operators. If primary theory does not supply a hard bound, retain the residual honestly rather than inventing one.

## Other OPEN survivors
- G8 target-specific thermal-solar anti-nu_e RIOEC remains OPEN/BLOCKED until primary thermal-solar anti-nu_e spectral density and independently evaluated entrance strength/width are frozen; ordinary solar nu_e flux is forbidden for this entrance channel.
- G9 transparent-Sun focal scale robust/partial; distant-source physical flux × finite-source/alignment/duty-cycle utility remains OPEN. Solar-neutrino self-lensing is inapplicable.
- G10 geometry-only staggered/fixed-column and passive mixing gains closed; only genuinely structure-induced microscopic-response changes could reopen under a new hypothesis.
- BSM/light mediator remains LOCKED pending formal unlock audit; 0047–0048 substantially narrow passive-SM nuclear residuals but do not alone authorize unlock.

## Research-gate snapshot
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body/detection | **STRONG PARTIAL PASS — ideal CEvNS phase diagram, rate-transfer and known-background requirements CLOSED; nuisance/full detector transfer OPEN** |
| G3 maximum passive-SM deposited power | **STRONG PARTIAL PASS — finite-range k-local scaling CLOSED; empirical/EFT absolute-strength stress strongly negative; universal contact + genuine long-range/growing-coordination residual OPEN** |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5/G6 BSM | LOCKED pending unlock audit |
| G7 production↔absorption | PARTIAL PASS |
| G8 resonance integrated strength | PARTIAL PASS; target-specific thermal anti-nu RIOEC OPEN/BLOCKED |
| G9 gravity | PARTIAL PASS; distant-source utility OPEN |
| G10 fixed-column geometry/composition | STRONG NEGATIVE in frozen geometry-only scope |

## Critical guards
Event/detection gain != interaction gain != neutrino-energy gain. Peak resonance != integrated capture. Directional coherence != integrated opacity. Gravitational gain must satisfy source geometry, finite-source/Liouville and receiver integration. A few-target maximum is not a global SM ceiling. Selected-nucleus two-body corrections are not universal maxima. Empirical amplitude anchors are evidence-distance constraints, not mathematical coefficient bounds. Metastable amplification requires stored-energy/reset accounting. Accepted-background requirements are not raw site background requirements. Frozen criteria are never weakened after results. No F9 multiplication of unvalidated gains.
