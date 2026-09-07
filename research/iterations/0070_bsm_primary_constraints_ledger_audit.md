# NMIR iteration 0070 — primary BSM constraints-ledger normalization audit

Date: 2026-09-07
Prospective contract: `research/prereg/0070_bsm_primary_constraints_ledger_contract.md`
Convention freeze amendment: `research/prereg/0070a_bsm_coupling_conventions_amendment.md`, commit `502a21da07e258285ec3223a1b5271da7c6aae74`.
Machine-readable ledger: `data/bsm_primary_constraints_audit_0070.json`, commit `ae1d1731201f91386746232e38068eef9c20f79a`.

## Classification
**`BLOCKED_BSM_CONSTRAINT_NORMALIZATION`**.

This is not a BSM mechanism failure and not evidence against light mediators. It means the frozen 0070 request for one common primary constraints ledger spanning vector, scalar and axial/spin-dependent classes cannot be fulfilled without adding model assumptions that are not common to those classes.

## Primary laboratory anchor
De Romeri, Papoulias and Ternes, JCAP 05 (2025) 012, DOI `10.1088/1475-7516/2025/05/012`, arXiv `2411.11749`, is a primary reanalysis of XENONnT/PandaX-4T CEvNS plus electron-recoil data. It explicitly defines light scalar/vector/axial interactions and states its simplifying universal-coupling convention

`g_a = sqrt(g_nu_a g_q_a) = sqrt(g_nu_a g_l_a)`.

It also treats `U(1)_{B-L}` separately because its charge assignment differs from the phenomenological universal-vector case. Scalar/vector nuclear coefficients require specified hadronic conventions, while the axial response is spin dependent.

This primary source is sufficient to demonstrate that low-energy laboratory constraints are meaningful only after the coupling convention is frozen; it does not justify replacing independent couplings by one universal `g_a` outside that benchmark.

## Why the full 0070 ledger blocks
The same primary analysis states that the astrophysical and cosmological regions shown for low-mass mediators are strongly model dependent and require tailored analyses. It also notes that axial limits change when the quark and lepton couplings are not assumed equal.

Under 0070a the scalar class keeps independent `(y_nu, y_e, y_q/y_N)` and the axial class keeps independent `(g_nu^A, g_q^A)` unless a primary source fixes a relation. Therefore:

- collider/fixed-target visible versus invisible searches require mediator branching ratios/additional couplings;
- stellar/SN production, free streaming and trapping depend on the full coupling pattern;
- BBN/CMB/free-streaming constraints depend on thermal history, mediator population and, for scalar neutrino couplings, the neutrino-chirality/extra-state content;
- fifth-force/equivalence-principle constraints act on ordinary-matter charges, so mapping them to a neutrino-matter product requires an additional relation between matter and neutrino couplings;
- axial simplified models additionally require a UV completion for anomaly cancellation/longitudinal behavior if collider/cosmology constraints are to be transported globally.

A 2026 primary generalized-neutrino-interaction study (Phys. Rev. D 113, 095019; DOI `10.1103/t3s4-8kvh`) independently reinforces the normalization warning: different common GNI parametrizations need explicit conversion before constraints can be compared.

## Scientific consequence
The generic three-class ledger fails the frozen acceptance criterion, because an entire class-wide common normalization cannot be constructed without post-hoc model assumptions. No external contour is silently recast into an incompatible coupling plane.

However, one subclass is immediately actionable without violating this result: anomaly-free `U(1)_{B-L}` has a fixed matter/neutrino charge relation and a single gauge coupling `g_BL`. That makes a dedicated `(m_V,g_BL)` primary constraint ledger a well-posed next gate.

## BSM state after 0070
BSM remains **`UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY`**. No NMIR BSM response or enhancement scan is allowed yet. The 0070 block is a normalization/architecture result, not permission to optimize a mediator.

## Exact next gate
Prospectively freeze iteration 0071: a gauge-complete `U(1)_{B-L}` primary constraints ledger in `(m_V,g_BL)` only. Require laboratory neutrino-scattering/CEvNS, collider/fixed-target where applicable, stellar/SN, cosmological and fifth-force families, all in the same B-L charge convention or explicitly marked non-applicable. Only if a surviving parameter region is frozen may a later prospective B-L NMIR response gate be considered.

## Readiness
No readiness increase: this iteration identifies a class-normalization blocker and a cleaner benchmark route, but does not yet bound a BSM response.
