# NMIR preregistration amendment 0070a — explicit BSM coupling conventions

Date frozen: 2026-09-07
Parent: `research/prereg/0070_bsm_primary_constraints_ledger_contract.md`
Status: PROSPECTIVE CONVENTION FREEZE

## Purpose
Freeze concrete operator/coupling conventions before interpreting or transcribing any external exclusion contour into the 0070 machine-readable ledger. Source discovery is not a numerical NMIR-response calculation; no external limit may be merged across the conventions below without an explicit conversion.

## V — gauge-complete benchmark vector class
Primary vector benchmark is anomaly-free `U(1)_{B-L}` with a single gauge coupling `g_BL` and mediator mass `m_V`:

`L_int = g_BL V_mu J_{B-L}^mu`,

where `J_{B-L}` carries charge `-1` for leptons (including the neutrino chiral current in the low-energy theory) and `+1/3` for each quark, hence approximately `+1` per nucleon before nuclear form factors. Parameter plane: `(m_V, g_BL)`.

A phenomenological universal-vector model with independent `g_nu*g_f` is NOT silently identified with B-L. Results quoted only in a product convention remain a separate record unless an exact mapping is stated by the primary source.

## S — simplified Dirac-neutrino scalar class
Benchmark scalar is a real scalar `phi` with mass `m_S` and explicit Dirac-neutrino chirality-flipping coupling plus ordinary-matter Yukawa-like effective couplings:

`L_int = - y_nu phi (bar nu_R nu_L + h.c.) - y_e phi bar e e - sum_q y_q phi bar q q`.

For nuclear scattering the ledger records either the primary source's quark-level convention or its stated effective nucleon coupling `y_N`; no conversion through scalar nucleon form factors is performed unless the source gives the convention/input. Parameter records therefore keep `(m_S, y_nu, y_e, y_q/y_N)` or an explicitly quoted product such as `y_nu*y_N`.

This is a simplified low-energy model, not a claim of a unique gauge-complete UV completion. Constraints that assume Majorana neutrinos, a Higgs portal relation, universal mass-proportional Yukawas, invisible mediator decays, or a thermalized right-handed-neutrino sector are tagged `model_specific` and are not merged into a universal scalar contour.

## A — simplified axial/spin-dependent class
Benchmark axial mediator `A_mu` has mass `m_A` and

`L_int = g_nu^A A_mu bar nu_L gamma^mu nu_L + sum_q g_q^A A_mu bar q gamma^mu gamma5 q`.

At nucleon level `g_N^A = sum_q Delta q^(N) g_q^A` only when the primary source specifies the spin fractions/convention; otherwise retain the source's quark-level coupling. Parameter records keep `(m_A, g_nu^A, g_q^A)` or the exact product convention used by the source.

This is a simplified low-energy class. Anomaly cancellation, longitudinal-mode/unitarity completion and additional fermions are UV assumptions. Collider/cosmological/stellar limits depending on those additions are `model_specific` unless the same completion is frozen explicitly.

## Applicability rule
A constraint enters the common 0070 ledger only if its primary source supplies enough information to map it exactly onto one of the above records without selecting an unstated branching ratio, hidden-sector coupling, thermal history, anomaly-cancellation spectrum, or scalar nucleon form factor. Otherwise record the source as relevant authority but classification is `NOT_COMMONLY_NORMALIZABLE` for that class/constraint family.

## Frozen 0070 decision rule refinement
This amendment does not weaken the parent gate. `PASS_BSM_CONSTRAINT_LEDGER_FROZEN` requires a nonempty, primary-provenance constraint ledger for each benchmark class plus explicit flags for model-specific families. If an entire required class cannot obtain a cross-family externally constrained region under the frozen convention without additional post-hoc model assumptions, classify `BLOCKED_BSM_CONSTRAINT_NORMALIZATION` and do not open an NMIR BSM response scan.
