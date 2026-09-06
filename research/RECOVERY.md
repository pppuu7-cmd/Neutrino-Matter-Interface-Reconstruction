# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-07
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Recovery protocol: `research/RECOVERY_MANUAL.md`
Funnel authority: `research/NMIR_FUNNEL.md`
Latest immutable validated scientific record: `research/iterations/0058_required_topology_performance_envelope.md`
Current readiness: `NMIR_READINESS: 84%`.

## Mandatory recovery order
Read `RECOVERY_MANUAL.md` completely, then this file, then `NMIR_FUNNEL.md`, then newest numbered iteration/prereg files, recent commits newer than this reconciliation, and relevant queued/in-progress/newly-terminal Actions. Chat history is not authority. Do not duplicate running work. Green CI is not scientific evidence until the dedicated result/log/artifact is checked against the prospective contract.

## Frozen accounting
NMIR is a discovery funnel, not a material scan. Keep state/focusing, microscopic interaction probability, detector visibility/amplification, and irreversible neutrino-supplied deposited energy separate.

`P_dep,nu = N_T integral dE mu(E,x) Phi(E) sigma_eff(E) E_dep,nu(E)`, with `0 <= E_dep,nu <= E_nu`.

Daughter decay, target preparation, stored medium free energy, external pumping, mediator preparation and reset work are never neutrino-supplied power. Never multiply unvalidated gains.

## Stable baseline authority
- Tritium measured-ft inverse capture: `sigma(v/c)≈7.785e-45 cm^2`, ~0.7% from published `7.84e-45`.
- Solar authority: B16 GS98/AGSS09met fluxes; locally pinned pp/hep/B8/CNO spectra; thermally broadened Be7 profile; daytime adiabatic 3-flavour MSW for charged-current folds. CEvNS is active-flavour neutral current and has no Pee factor.
- Charged-current validated target leader: pure 7Li/GS98 `1.06589117e-21 W/kg`, ~`9.38e20` below 1 W/kg. This is not an all-nucleus theorem.

## Broad frozen class closures
Do not reopen without a genuinely new assumption; exact scopes are in immutable iteration notes.
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
- 0048 empirical/EFT absolute-strength stress: `PASS_EMPIRICAL_STRENGTH_STRONG_NEGATIVE`; even 100× the largest frozen empirical extra-amplitude anchor gives `1.301537448e-5 W/kg`; bridge to 1 W/kg requires extra amplitude `28796.42286 = 28511.31×` empirical anchor. Evidence-distance result, not a universal coefficient theorem.

## G2 CEvNS / detector chain — validated through 0058
### 0041–0046 physics envelope
- 0041 Ar40 at 40 eV: exact source-opening threshold `E_nu,min=0.8628609380 MeV`.
- 0042 physical Be7 profile × Ar40: at 40 eV 31.104% source tail but only `4.906342834e-6` retained cross section and `3.973604373e-8 events/(kg day)`.
- 0043 continuous-A inverse-design law: `A_star=2E_nu^2/(3 m_u T_thr)`, equivalently `Tmax(A_star)≈3Tthr`; class-level envelope only.
- 0044 retained scientific FAIL: `M=A m_u` caused ~30% error at Ar40/Be7 40-eV endpoint; criterion was not relaxed.
- 0045 exact isotope masses + actual Z/N + full frozen solar source set over 23 nuclei PASS.
- 0046 `PASS_PHASE_DIAGRAM`; run/job `34052930672/101539642497`; artifact `9995368376`; SHA256 `046953d77896362afaaf5da0ff2015ddb36958196c0b921cc5e3f0ff4efe3951`; raw 29 tests PASS. Crossovers [eV]: Pb208→W184 3.9453125; W184→Xe132 4.4453125; Xe132→Mo100 6.3515625; Mo100→Se82 6.7265625; Se82→Ge74 12.5078125; Ge74→Ti48 12.9296875; Ti48→Ar40 12.9609375; Ar40→Pb208 15.5703125.

### 0049–0051 rate and accepted-background requirements
- 0049 `PASS_DETECTOR_TRANSFER_RATE_REQUIREMENT`: for 10-kg Ar40 and 10 accepted CEvNS/year, required `eta=<epsilon_NR>*f_live` is `0.42207478` at 10 eV, `0.75683153` at 20 eV, and impossible `2.35795954` at 40 eV. Run/job `34057771059/101552695624`, artifact `9996491115`.
- 0050 known-background one-year Asimov: for `S=10/year`, 3σ requires `B<=8.22524099/year`; 5σ `B<=1.71752668/year`. Run/job `34057997407/101553304948`, artifact `9996559867`.
- 0051 nuisance-aware profile-likelihood map: representative frozen ceilings for `S=10/year`: 3σ/30% `4.274968302863348/year`; 5σ/30% `1.0806120114381677/year`; 5σ/50% `0.692094879071742/year`. Run/job `34058564427/101554849279`, artifact `9996725207`.

### 0052 — measured-threshold CRESST-III Si transfer fold
Prereg `72a089483f001fa4ee8383d8f8d0914ddc0ec134`. First run `34058821939` retained as infrastructure FAIL; minimal repair left scientific inputs unchanged. Authoritative rerun/job `34058921851/101555813480`; artifact `9996833564`; SHA256 `67fd30cfca7e3321c4818a0a7d62343cbbdad2ca49e339dc12772ce6ad7df118`; raw 6 tests PASS; `PASS_CRESST_SI_TRANSFER_FOLD`.
Si28 10-eV full-solar: ideal `4.3476963498860904e-3 events/(kg day)`; trigger fold `3.4252750501524354e-3`; factorized all-cuts surrogate `2.8034257861113496e-3`; surrogate retained `0.64480717`; effective mass for 10/year `9.766089763 kg`; current 0.35-g module mass gap ~`2.79e4×`.

### 0053 — CRESST LEE scaling/rejection stress
Run/job `34059182934/101556510236`; artifact `9996911051`; ZIP SHA256 `cc03b4c6264ba5c187eaf5c3b483b1e253f5d9811de950e0452eb4b795e0dc92`; raw 6 tests PASS; `PASS_LEE_SCALING_GAP_STRESS`.
Frozen CRESST Si central LEE fit 10–300 eV folded through the 0052 surrogate gives accepted stress rate `1.2567687196378214e6 events/(kg day)`. Stress scaling unchanged per kg to `M10=9.766089763 kg` gives `4.482974815542e9 accepted events/year`. Required total reduction/rejection: `1.04865685496e9` (3σ,30%), `4.14855171707e9` (5σ,30%), `6.47739919930e9` (5σ,50%). Technology stress extrapolation only, not a future-background prediction.

### 0054 — LEE mitigation evidence audit
Run/job `34059455141/101557243909`; artifact `9996995011`; `PASS_LEE_MITIGATION_EVIDENCE_AUDIT / MECHANISM_SURVIVOR_QUANTITATIVE_GAP_OPEN`.
DoubleTES demonstrates topology discrimination, but no public comparable detector-wide pre/post rejection × bulk-acceptance pair is frozen for the 0053 10–300 eV window. 10×/100× next-generation LEE reductions remain projection/benchmark scenarios, not measured achieved factors.

### 0055 — waiting-time requirement map
Run/job `34059603535/101557649153`; artifact `9997041670`; `PASS_WAITING_TIME_REQUIREMENT_MAP / WAITING_ONLY_OPERATIONALLY_INSUFFICIENT`.
Under deliberately optimistic `R_proj(t)=10^(t/450 d)`, the 0053 5σ/30% gap closes only after `11.8496 y`; at 3 y the stress factor is `272.27013`, leaving `1.5236896e7` independent improvement.

### 0056 — finite-horizon mitigation budget
Run/job `34060855059/101560998357`; artifact `9997410337`; `PASS_FINITE_HORIZON_MITIGATION_BUDGET`.
At 3 y, authority-capped 100× leaves `4.148551717e7` residual rejection; stress continuation 272.27× leaves `1.523689618e7` at perfect signal acceptance. Signal loss is explicitly charged.

### 0057 — exact unbinned time-likelihood information bound
Immutable authority: `research/iterations/0057_time_likelihood_information_bound.md`.
Scientific head `66008c2478e3145175b165e7481ad84f9862f073`; run/job `34061194530/101561925452`; artifact `9997513698`; SHA256 `b907eff49815716ce1a026af68453cab0808f9cdd098e330d58ff18e9357d796`; raw 6 tests PASS; `PASS_TIME_LIKELIHOOD_BOUND / TIME_SHAPE_USEFUL_BUT_INSUFFICIENT`.
For 3-y `S=30`, authority-capped branch requires exact `R_time,5σ=1.77570304169906e7`; stress branch `1.4440370654436817e7`. Time shape improves over count-only by factors `4.9568×` and `6.0728×`, but remains far from sufficient. This full likelihood requirement is not multiplied by 0056 waiting factors.

### 0058 — required measured topology-performance envelope
Immutable authority: `research/iterations/0058_required_topology_performance_envelope.md`.
Preregistration commit `447dedd4d39414b1dbc113b6f291f9490d31f2d1`; scientific workflow head `7ee2d1598d49146a98d39d71a2b7c4cb18b1d234`; hosted run/job `34061477253/101562663106`; artifact `9997604078`; SHA256 `ff0ad8d14663358cb8d3136570c2297ecfdce21895e500b05a71f93d133274fa`. Dedicated pytest and fail-closed benchmark steps completed successfully; downloaded machine-readable artifact inspected directly.
Classification: `PASS_REQUIRED_TOPOLOGY_PERFORMANCE_ENVELOPE / PUBLIC_ACHIEVEMENT_ANCHOR_OPEN`.
At `epsilon_S=1`, the exact 0057 requirements are recovered: `1.77570304169906e7` and `1.4440370654436817e7`. Fixed-exposure topology requirements rise sharply with signal loss: at `epsilon_S=0.5`, `1.1095483713662188e8` and `9.407539776651382e7`; at `epsilon_S=0.3`, `5.248261401309289e8` and `4.58373974654573e8`. Signal-restored exposure obeys exactly `R_base/epsilon_S`. All frozen acceptance-grid requirements remain >`1e6`.
This is a detector-performance requirement map, not achieved DoubleTES performance and not an extra factor to multiply with 0056/0057.

## G2 current state
**STRONG PARTIAL PASS / PUBLIC_ACHIEVEMENT_ANCHOR_OPEN.** Ideal CEvNS phase space, rate requirements, nuisance-aware background budgets, measured-threshold Si transfer, LEE stress, mitigation evidence, waiting/time-information accounting, and the topology rejection×acceptance requirement envelope are now closed. Further algebraic requirement maps are low value. The next G2 closure requires a genuinely measured comparable underground rejection × CEvNS-like bulk-event acceptance anchor; none is currently frozen.

## G3 passive-SM deposited-power status
Leading/allowed, finite-q, one-body, local density/spin, passive mediator, finite-range k-local collective scaling and empirical/EFT absolute higher-body amplitude stress are strong-negative/closed in exact stated scopes.
Remaining residuals: whether a defensible universal renormalized Standard-Model/chiral-EFT contact or two-/higher-body-current coefficient bound exists without pretending EFT naturalness is a theorem; and genuinely long-range/growing-coordination SM operators. If primary theory supplies no hard bound, retain the residual honestly.

## Other OPEN survivors
- G8 target-specific thermal-solar anti-nu_e RIOEC OPEN/BLOCKED until a primary thermal-solar anti-nu_e spectral density and independently evaluated entrance strength/width are frozen; ordinary solar nu_e flux is forbidden for this entrance channel.
- G9 transparent-Sun focal scale robust/partial; distant-source physical flux × finite-source/alignment/duty-cycle utility OPEN. Solar-neutrino self-lensing is inapplicable.
- G10 geometry-only staggered/fixed-column and passive mixing gains closed; only genuinely structure-induced microscopic-response changes could reopen under a new hypothesis.
- BSM/light mediator remains LOCKED pending formal unlock audit.

## Exact next funnel gate
**G3 / F4-F6 universal-contact residual audit.** Before any result-dependent calculation, freeze a prospective evidence contract specifying primary chiral-EFT/SM current authorities, what would constitute a true regulator/renormalization-scheme-independent hard coefficient/operator bound versus only naturalness/power-counting evidence, and how either outcome propagates to the 0048 power bridge. PASS may be either (a) a defensible universal bound with explicit scope and units, or (b) a reproducible negative audit establishing that no such hard universal bound follows from the frozen authorities, in which case the residual remains OPEN rather than being guessed closed. Do not start another material/isotope scan.

## Research-gate snapshot
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body/detection | **STRONG PARTIAL PASS — through 0058 requirement envelope CLOSED; measured scalable underground rejection×acceptance anchor OPEN** |
| G3 maximum passive-SM deposited power | **STRONG PARTIAL PASS — finite-range k-local scaling CLOSED; empirical/EFT strength stress strongly negative; universal contact + genuine long-range/growing-coordination residual OPEN** |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5/G6 BSM | LOCKED pending unlock audit |
| G7 production↔absorption | PARTIAL PASS |
| G8 resonance integrated strength | PARTIAL PASS; target-specific thermal anti-nu RIOEC OPEN/BLOCKED |
| G9 gravity | PARTIAL PASS; distant-source utility OPEN |
| G10 fixed-column geometry/composition | STRONG NEGATIVE in frozen geometry-only scope |

## Critical guards
Event/detection gain != interaction gain != neutrino-energy gain. Peak resonance != integrated capture. Directional coherence != integrated opacity. Gravitational gain must satisfy source geometry, finite-source/Liouville and receiver integration. A few-target maximum is not a global SM ceiling. Selected-nucleus two-body corrections are not universal maxima. Empirical amplitude anchors are evidence-distance constraints, not mathematical coefficient bounds. Metastable amplification requires stored-energy/reset accounting. Accepted-background requirements are not raw site background requirements. A low measured threshold or trigger turn-on is not automatically a full recoil-dependent all-cuts efficiency. A demonstrated topology handle is not a measured rejection factor. Projection factors are not measured suppression. Signal loss is never free background rejection. Alternative time scenarios are never multiplied. Time-likelihood rejection is not an independent waiting multiplier. The 0058 topology requirement already includes 0057 time information. Frozen criteria are never weakened after results. No F9 multiplication of unvalidated gains.