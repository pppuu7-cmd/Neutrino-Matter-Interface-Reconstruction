# NMIR Discovery Funnel

Reconciled: 2026-09-07. Scientific authority is the repository, not chat. Recovery order is defined in `research/RECOVERY_MANUAL.md`; compact current state is `research/RECOVERY.md`.

## Mandatory funnel
Every idea passes, in order: F0 objective classification -> F1 channel -> F2 production/absorption where applicable -> F3 kinematics/spectral overlap -> F4 microscopic strength -> F5 collective/resonant enhancement -> F6 no-free-lunch/fundamental bounds -> F7 common quantitative score -> F8 external constraints -> F9 composition only after individual validation -> F10 outcome classification. Never multiply unvalidated gains.

## Frozen broad guards
Closed in stated scopes unless a genuinely new assumption is introduced: naive static N²; geometry-only staggered/fixed-column gain; passive local density/phonon free-energy gain; passive local spin/magnon superextensive gain; extensive-budget long-range pair free gain; passive stable finite linear mediator free gain; passive convex homogeneous nonlinear free gain; linewidth narrowing as new integrated resonance strength; metastable stored-energy avalanche as neutrino-energy gain.

## Highest-value OPEN gates
1. **G8 / F4-F7 — Cu63 primary RIOEC normalization/materialization gate (0068).** Iteration 0067 removed the thermal-solar high-energy-tail provenance blocker by prospectively recomputing `dPhi_anti-nu_e/dE(162.496486 keV)=3.528363521736758e-41 cm^-2 s^-1 MeV^-1` from Haxton-Lin Eq. (9) + BP98. The immediate remaining class-value question is whether the exact continuous-spectrum RIOEC normalization, line-shape convention, B(GT)->entrance-strength mapping, K-shell atomic factor and spin/unit conventions can be recovered unambiguously from primary Akhmedov-Lasserre-Maturi authority. No numerical rate fold until that package is prospectively frozen.
2. **G3 / F4-F6 — absolute short-range/contact-current physical residual.** 0059 found no universal hard coefficient bound; 0062 naive finite-l unitarity failed; 0065 found no coefficient-independent observable mapping. Further G3 work is admissible only with a genuinely new theorem/physical assumption.
3. **G2 / F7-F8 — measured scalable topology rejection × CEvNS-like bulk acceptance.** 0063 remains `BLOCKED_PUBLIC_ACHIEVEMENT_ANCHOR`; reopen only with genuinely new same-configuration sub-keV measured rejection × bulk-NR acceptance evidence.
4. **G9 new source classes.** 0061 closes the 10-kpc Galactic CCSN benchmark as physical focusing but strong-negative occurrence-weighted utility. Any different known-direction/persistent source requires a new prospective contract.
5. **BSM/light mediator.** Remains **LOCKED**. Iteration 0066 prospectively classified `FAIL_KEEP_BSM_LOCKED_OPEN_SM_ACTIONABLE` because reopened G8/Cu63 violated the unlock criterion requiring no quantitatively unbounded immediately actionable principal SM branch.

## G2 authoritative chain
0042 physical Be7 profile × Ar40 shows severe endpoint phase-space suppression. 0043 continuous-A inverse design is an envelope only. 0044 retained FAIL shows `M=A m_u` is inadequate near recoil endpoints. 0045 exact isotope masses/full-solar optimization PASS. 0046 `PASS_PHASE_DIAGRAM`, run/job `34052930672/101539642497`, artifact `9995368376`. 0049 detector-transfer rate requirements and 0050/0051 known/nuisance-aware background ceilings are closed. 0052 measured-threshold Si transfer fold, 0053 LEE scaling stress, 0054 mitigation audit, 0055–0057 time-information requirements and 0058 rejection×acceptance envelope are closed in stated scopes. 0063 remains `BLOCKED_PUBLIC_ACHIEVEMENT_ANCHOR`; no cross-detector multiplication allowed.

## G3 current state
0047 bounded finite-range k-local theorem: `PASS_KLOCAL_EXTENSIVITY`, run/job `34056195172/101548425397`, artifact `9996023078`. 0048 empirical/EFT strength stress is strongly negative but not a theorem: even 100× the largest frozen empirical extra-amplitude anchor gives `1.301537448e-5 W/kg`; bridge to 1 W/kg requires amplitude `28796.42286 = 28511.31×` empirical anchor. 0059: `PASS_NO_UNIVERSAL_HARD_BOUND_FOUND / RESIDUAL_OPEN`. 0060: `PASS_NO_SM_GROWING_COORDINATION_SURVIVOR` in audited passive-SM scope. 0062: `FAIL_UNITARITY_MODEL / HARD_LMAX_NOT_COEFFICIENT_INDEPENDENT; DIAGNOSTIC_BOUND_TOO_WEAK / RESIDUAL_OPEN`, run/job `34071960179/101590826472`, artifact `10000809024`. 0065 G3: `PASS_NO_COEFFICIENT_INDEPENDENT_OBSERVABLE_MAP / RESIDUAL_OPEN`. Absolute short-range/contact-current coefficient residual remains physically OPEN.

## G8 current state
0025/0035 establish integrated-strength and channel-identity guards. Ordinary solar pp/CNO/B8 `nu_e` flux is forbidden for RIOEC; entrance is electron antineutrino. 0064 was `BLOCKED_ENTRANCE_STRENGTH` on the evidence then audited.

A concurrent prospective follow-up later established `PASS_G8_CU63_PROVENANCE_REOPENED` for `63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)`, with `E_R=162.496486 keV` and mandatory reverse-strength envelope `B_reverse=2.85e-3...6.72e-2` (~23.58× spread).

### 0067 source-tail result
Prospective contract `research/prereg/0067_g8_cu63_thermal_tail_rate_gate.md`, commit `e42cd8ccd8a321cfa850b87b0fbd8d11bed30956`.

Authoritative run/job `34081044588/101616231800`, artifact `10003691395`, artifact ZIP SHA256 `22cc917e5ac275fb509d78b69565736a0d73f433f45461bb20d4d0e01232bfb9`. Raw log inspected directly. The first attempt `34081007772` was infrastructure-only failure due NumPy 2.4 `np.trapz` removal; the rerun changed only API compatibility.

Classification: **`PASS_SOURCE_TAIL_RECOMPUTED / RATE_FOLD_OPEN`**.

Validated source numbers:
- `dPhi_anti-nu_e/dE(162.496486 keV)=3.528363521736758e-41 cm^-2 s^-1 MeV^-1`;
- 5-keV sanity-check flux density `3.765698986767552e7 cm^-2 s^-1 MeV^-1`;
- 6000->12000 grid relative change `5.832844895924436e-8`;
- BP98 source blob SHA256 `6bd3c2d9cde15b74cf1fcebe1620566e2b3d832c09e65fc36d5422a6ef0bf198`.

Frozen ledger `data/g8_cu63_thermal_tail_0067.json`; immutable note `research/iterations/0067_g8_cu63_thermal_tail_source_recomputation.md`.

This removes the source-tail blocker but is not yet a rate claim.

### 0068 current prospective gate
`research/prereg/0068_g8_cu63_rioec_normalization_contract.md`, commit `44abb5844e6bbcd358fd224052cf7bce92f2e881`.

Recover from primary RIOEC authority the exact continuous-spectrum cross-section/rate formula, line-shape normalization, B(GT)->entrance-strength relation, K-shell atomic factor, spin/statistical factors, constants and unit conventions. If any essential piece is unavailable, classify `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`; do not fill gaps from secondary summaries. On PASS, freeze a separate prospective numerical-fold contract before computing the Cu63 rate.

## G9 current state
0061 `PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY`, prereg `4396de3ae532b574f76e3a34d935b08e51746868`; run/job `34071432319/101589393517`; artifact `10000583684`. At `b/Rsun=0.024`, focus `24.073780819657056 AU`; 21-km source at 10 kpc projects to `0.2451 mm`; 1/10/100-m receiver alignment probabilities only `~1.93e-26,1.93e-24,1.93e-22`; impossible full-solar-disk collection still leaves expected multiplier ~`1.00000000934`.

## BSM lock
0066 classification: **`FAIL_KEEP_BSM_LOCKED_OPEN_SM_ACTIONABLE`**. Frozen unlock criterion failed because Cu63 G8 remained a principal passive-SM branch that was quantitatively unbounded and actionable. BSM stays LOCKED while 0068 is actionable.

## F10 snapshot
- Ideal full-solar CEvNS target/threshold phase diagram: PASS-SURVIVOR for detection physics; no neutrino-energy amplification.
- Metastable avalanche: PASS-SURVIVOR for detection / STRONG_NEGATIVE_SCOPED for harvesting.
- G2 detector chain: requirements strongly constrained; public achievement anchor BLOCKED.
- Bounded finite-range k-local higher-body collective scaling: STRONG_NEGATIVE_SCOPED for free superextensive gain.
- G3 universal-contact routes: three independent attempted ceilings retired; absolute coefficient residual OPEN.
- Actual-SM long-range/growing-coordination: no survivor in audited passive-SM scope.
- Geometry-only structured matter at fixed mass column: STRONG_NEGATIVE_SCOPED.
- G8 Cu63: exact-state F4 provenance PASS; 162.5-keV thermal-solar source tail RECOMPUTED; exact primary RIOEC normalization OPEN under 0068.
- G9 10-kpc Galactic CCSN solar-lens utility: physical focusing PASS / occurrence-weighted utility STRONG NEGATIVE.
- BSM: LOCKED after 0066 FAIL.

## Exact next gate
Execute 0068. Materialize the exact primary RIOEC continuous-spectrum normalization package. Only if `PASS_RIOEC_NORMALIZATION_MATERIALIZED` may a new prospective numerical-fold contract be frozen and the validated 0067 source tail folded with the complete Cu63 strength envelope to events/(kg s), events/(kg day), and neutrino-supplied W/kg.

`NMIR_READINESS: 89%`.
