# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-06
Program: Neutrino–Matter Interface Reconstruction (NMIR)
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Recovery protocol: `research/RECOVERY_MANUAL.md`
Funnel authority: `research/NMIR_FUNNEL.md`
Latest immutable validated scientific record: `research/iterations/0054_cresst_lee_mitigation_evidence_gate.md`
Current readiness: `NMIR_READINESS: 83%`.

## Mandatory recovery order
Read `RECOVERY_MANUAL.md` completely, then this file, then `NMIR_FUNNEL.md`, then the newest numbered iteration/prereg files, recent commits newer than this reconciliation, and relevant queued/in-progress/newly-terminal GitHub Actions. Chat history is not authority. Do not duplicate running work. A green workflow is infrastructure success only until the raw scientific log/artifact is checked against the prospective contract.

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
- 0048 empirical/EFT absolute-strength stress: `PASS_EMPIRICAL_STRENGTH_STRONG_NEGATIVE`; even 100× the largest frozen empirical extra-amplitude anchor gives `1.301537448e-5 W/kg`; bridge to 1 W/kg requires extra amplitude `28796.42286 = 28511.31×` the empirical anchor. Evidence-distance result, not a universal coefficient theorem.

## G2 CEvNS / detector chain — validated through 0054
### 0041–0046 physics envelope
- 0041 Ar40 at 40 eV: exact source-opening threshold `E_nu,min=0.8628609380 MeV`.
- 0042 physical Be7 profile × Ar40: at 40 eV 31.104% source tail but only `4.906342834e-6` retained cross section and `3.973604373e-8 events/(kg day)`.
- 0043 continuous-A inverse-design law: `A_star=2E_nu^2/(3 m_u T_thr)`, equivalently `Tmax(A_star)≈3Tthr`; class-level envelope only.
- 0044 retained scientific FAIL: `M=A m_u` caused ~30% error at Ar40/Be7 40-eV endpoint; criterion was not relaxed.
- 0045 exact isotope masses + actual Z/N + full frozen solar source set over 23 nuclei PASS.
- 0046 `PASS_PHASE_DIAGRAM`; run/job `34052930672/101539642497`; artifact `9995368376`; SHA256 `046953d77896362afaaf5da0ff2015ddb36958196c0b921cc5e3f0ff4efe3951`; raw 29 tests PASS. Crossovers [eV]: Pb208→W184 3.9453125; W184→Xe132 4.4453125; Xe132→Mo100 6.3515625; Mo100→Se82 6.7265625; Se82→Ge74 12.5078125; Ge74→Ti48 12.9296875; Ti48→Ar40 12.9609375; Ar40→Pb208 15.5703125.

### 0049 — necessary detector-transfer rate requirement
Prereg commit `ab8610005f8e174fd6838f5491edab804f0a32ed`; scientific head `01186655d07883ce7d0a14f5d29c4ff16f207f1b`; run/job `34057771059/101552695624`; artifact `9996491115`; SHA256 `6154810eff9116c69407e2a89052817783c75fbe2eab3a246f2d2235d6528e86`.
For 10-kg Ar40 and goal 10 accepted solar CEvNS/year, necessary `eta=<epsilon_NR>*f_live`: 10 eV `0.42207478`; 20 eV `0.75683153`; 40 eV `2.35795954`, so 10/year at 40 eV is impossible at fixed 10 kg even for eta=1.
Effective kg for 10/year: Ar10 `4.22075`, Ar20 `7.56832`, Ar40 `23.5796`, Si10 `6.29724`, Ge10 `3.47811`, Se10 `3.33393`.

### 0050 — accepted-background inverse requirement
Prereg `15ad880cdcf0168eaa3fb1a1447bd35d4c251d9a`; head `488d23bfd6c4a84a750860e6fe1128807a4bf0eb`; run/job `34057997407/101553304948`; artifact `9996559867`; SHA256 `44a5dac90c92741a09bc25e531aa192a0c4ddb8064a0de30e8c5991a82cc66c5`.
Known-background one-year Asimov gate: for `S=10/year`, 3σ requires `B<=8.22524099/year`; 5σ `B<=1.71752668/year`. These are accepted analysis-indistinguishable backgrounds, not raw trigger/site rates.

### 0051 — nuisance-aware accepted-background requirement
Prereg `3fb9b44309888e710ed748bac07f372162ecafad`; head `be3706d409b5018519be7b6dfcd0bc0581ed0135`; run/job `34058564427/101554849279`; artifact `9996725207`; SHA256 `148d4b3c877f52dc5813a4fe7247d20430aff45496105460b98714163766dfb8`; raw 5 tests PASS.
Profile-likelihood/Asimov Gaussian normalization nuisance `sigma_b=delta_B B` validated for `delta_B={0,0.10,0.30,0.50}`. For `S=10/year`, frozen ceilings used by 0053 include: 3σ/30% `4.274968302863348/year`; 5σ/30% `1.0806120114381677/year`; 5σ/50% `0.692094879071742/year`.

### 0052 — CRESST-III Si measured-threshold transfer fold
Prereg `72a089483f001fa4ee8383d8f8d0914ddc0ec134`. First run/job `34058821939/101555544155` retained as infrastructure FAIL after 5 passing tests because Be7 special flux mapping was evaluated after a generic lookup. Minimal repair `c2a359eecb4596bafd3291f4aa31cca97b544da9`; regression/scientific head `fb5cd82686006ba9c8134fac2b6dfbc9a879c079`; scientific inputs unchanged. Authoritative rerun/job `34058921851/101555813480`; artifact `9996833564`; SHA256 `67fd30cfca7e3321c4818a0a7d62343cbbdad2ca49e339dc12772ce6ad7df118`; raw 6 tests PASS; `PASS_CRESST_SI_TRANSFER_FOLD`.
Primary anchors: 0.35-g Si, threshold 10.0 eV, width 1.36 eV, trigger plateau 0.8053, cumulative trigger+cuts plateau 0.6591 above 14 eV. Full cumulative efficiency below 14 eV is not analytically published; NMIR uses the measured trigger turn-on and a labelled factorized all-cuts surrogate.
Si28 10-eV full-solar: ideal `4.3476963498860904e-3 events/(kg day)`; trigger fold `3.4252750501524354e-3`; surrogate `2.8034257861113496e-3`; surrogate retained `0.64480717`; effective mass for 10/year `9.766089763 kg`; actual 0.35-g module surrogate expectation `3.583829439e-4/year`, mass gap ~`2.79e4×`.

### 0053 — CRESST low-energy-excess scaling/rejection stress
Immutable authority: `research/iterations/0053_cresst_lee_scaling_gap.md`.
Prereg commit `018f6410c8bfa6bad9ebb321f621a75b785cd293`; scientific workflow head `567b7ffc2bad067c91f10023fbd2ff260ef24fbe`; run/job `34059182934/101556510236`; artifact `9996911051`; ZIP SHA256 `cc03b4c6264ba5c187eaf5c3b483b1e253f5d9811de950e0452eb4b795e0dc92`; raw `6 passed`; fail-closed benchmark `PASS_LEE_SCALING_GAP_STRESS`.
Frozen CRESST Si central LEE fit over 10–300 eV folded through the 0052 factorized surrogate gives corrected rate `2.232922324133041e6 events/(kg day)` and accepted stress rate `1.2567687196378214e6 events/(kg day)`, convergence residual `7.7346991e-9`.
Stress scaling unchanged per kg to `M10=9.766089763 kg` gives `4.482974815542e9 accepted events/year`.
Required total suppression/rejection relative to 0051 budgets:
- 3σ, delta_B=30%: `1.04865685496e9`;
- 5σ, delta_B=30%: `4.14855171707e9`;
- 5σ, delta_B=50%: `6.47739919930e9`.
This is explicitly a stress extrapolation, not a prediction of linear mass scaling and not a claim that all LEE events are known NR background.

### 0054 — CRESST LEE mitigation evidence audit
Immutable authority: `research/iterations/0054_cresst_lee_mitigation_evidence_gate.md`.
Prereg commit `c0052cf2c0f636cf4e176f987d233bbb3a4f4032`; evidence ledger `data/cresst_lee_mitigation_evidence.csv`; scientific workflow head `9b11f3bee1b70bdce87063eb66e16be25fcbf4f6`; hosted run/job `34059455141/101557243909`; artifact `9996995011`; ZIP SHA256 `baa710c01b2a548df0f32188627b53429b8f68f213c4cca5403586b81e5fd531`; raw `5 passed`; `PASS_LEE_MITIGATION_EVIDENCE_AUDIT`.
Scientific classification: `MECHANISM_SURVIVOR_QUANTITATIVE_GAP_OPEN`.
DoubleTES 2024 experimentally demonstrates topology discrimination: a diagonal absorber/bulk population is separable from single-TES near-sensor populations, with a conservative absorber cut requiring sensor energies within 35%. A separate absorber-band LEE remains and has measured above-ground decay time `10.2±1.1 d`. The paper reports significant near-threshold reduction but does not provide a public comparable pre/post rejection factor plus bulk acceptance over the 0053 10–300 eV window; data/code are on reasonable request.
The next-generation CRESST report foresees DoubleTES as baseline and uses ~10× and ~100× LEE reduction as projections/benchmarks (roughly ~450 d and ~900 d stable operation), not as already measured detector-wide suppression factors. Applying those projection-only factors to the frozen 0053 5σ/30% gap leaves residual required improvements `4.148551717e8` and `4.148551717e7`, respectively. SOS 6.7-eV results strengthen the threshold branch but are non-comparable as a measured 0053 LEE-suppression factor.

## G2 exact next gate
Build a factorized technology budget for the remaining detector gap while enforcing independence. Candidate factors: intrinsic LEE reduction per kg, DoubleTES/topology classification, time-domain likelihood separation from the measured LEE decay against steady solar flux, segmentation/coincidence/veto rejection, and retained CEvNS signal acceptance. Quantify what combinations are mathematically required to reach the 0051 5σ budget, mark which factors have direct experimental anchors, and never multiply projected or correlated factors as if independent. A high-value subgate is to derive the maximum discrimination obtainable from time dependence alone under a frozen exponential-LEE + constant-solar model; this can establish whether waiting/time-likelihood can retire more than the 10–100 projection factors.

## G3 passive-SM deposited-power status
Leading/allowed, finite-q, one-body, local density/spin, passive mediator, finite-range k-local collective scaling and empirical/EFT absolute higher-body amplitude stress are strong-negative/closed in exact stated scopes.
Remaining residuals: whether a defensible universal renormalized SM contact-coefficient bound exists without pretending EFT naturalness is a theorem; and genuinely long-range/growing-coordination SM operators. If primary theory supplies no hard bound, retain the residual honestly.

## Other OPEN survivors
- G8 target-specific thermal-solar anti-nu_e RIOEC OPEN/BLOCKED until a primary thermal-solar anti-nu_e spectral density and independently evaluated entrance strength/width are frozen; ordinary solar nu_e flux is forbidden for this entrance channel.
- G9 transparent-Sun focal scale robust/partial; distant-source physical flux × finite-source/alignment/duty-cycle utility OPEN. Solar-neutrino self-lensing is inapplicable.
- G10 geometry-only staggered/fixed-column and passive mixing gains closed; only genuinely structure-induced microscopic-response changes could reopen under a new hypothesis.
- BSM/light mediator remains LOCKED pending formal unlock audit.

## Research-gate snapshot
| Gate | Status |
|---|---|
| G0 weak/capture normalization | PARTIAL PASS |
| G1 static macroscopic coherence | PARTIAL NEGATIVE |
| G2 many-body/detection | **STRONG PARTIAL PASS — ideal CEvNS phase diagram, rate/nuisance requirements, measured-threshold Si transfer, empirical LEE stress and DoubleTES mechanism audit CLOSED; quantitative scalable LEE suppression/discrimination OPEN** |
| G3 maximum passive-SM deposited power | **STRONG PARTIAL PASS — finite-range k-local scaling CLOSED; empirical/EFT strength stress strongly negative; universal contact + genuine long-range/growing-coordination residual OPEN** |
| G4 engineered resonance/polarization/periodicity | PARTIAL |
| G5/G6 BSM | LOCKED pending unlock audit |
| G7 production↔absorption | PARTIAL PASS |
| G8 resonance integrated strength | PARTIAL PASS; target-specific thermal anti-nu RIOEC OPEN/BLOCKED |
| G9 gravity | PARTIAL PASS; distant-source utility OPEN |
| G10 fixed-column geometry/composition | STRONG NEGATIVE in frozen geometry-only scope |

## Critical guards
Event/detection gain != interaction gain != neutrino-energy gain. Peak resonance != integrated capture. Directional coherence != integrated opacity. Gravitational gain must satisfy source geometry, finite-source/Liouville and receiver integration. A few-target maximum is not a global SM ceiling. Selected-nucleus two-body corrections are not universal maxima. Empirical amplitude anchors are evidence-distance constraints, not mathematical coefficient bounds. Metastable amplification requires stored-energy/reset accounting. Accepted-background requirements are not raw site background requirements. A low measured threshold or measured trigger turn-on is not automatically a full recoil-dependent all-cuts efficiency. A demonstrated topology handle is not a measured rejection factor. Projection factors are not measured suppression. Frozen criteria are never weakened after results. No F9 multiplication of unvalidated gains.