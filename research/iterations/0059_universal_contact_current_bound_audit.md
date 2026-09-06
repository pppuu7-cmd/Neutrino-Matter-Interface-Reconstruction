# Iteration 0059 — universal renormalized contact/two-body-current bound audit

Date: 2026-09-07
Gate: G3 / F4-F6 absolute genuine two-/higher-body Standard-Model current residual
Scientific classification: `PASS_NO_UNIVERSAL_HARD_BOUND_FOUND / RESIDUAL_OPEN`

## Prospective authority
Contract: `research/prereg/0059_universal_contact_current_bound_audit.md`.
Preregistration commit: `5507f21e75e6e41df89a95029837b17952516d56`.
Frozen machine-readable evidence ledger: `data/g3_contact_bound_authority_0059.json`, created in commit `79447babca27e73c640f0b28de33b8db4d071b9d`.

This gate is a primary-authority theory audit rather than a result-dependent numerical calculation. Therefore no numerical benchmark artifact is used as scientific evidence. Baseline CI on the preregistration head completed successfully as run `34062348589`, but that green CI is infrastructure-only and is explicitly not the scientific PASS for this iteration.

## Frozen authority set and findings
### Gazit, Quaglioni, Navrátil — arXiv:0812.4444v2 / PRL 103, 102502
The paper states that the chiral low-energy constants `c_D` and `c_E` are constrained using A=3 binding energies and triton beta decay. This establishes the relevant contact strength as something calibrated from low-energy observables within a chosen EFT setup, not as a theory-derived regulator-independent universal maximum.

### Baroni et al. — arXiv:1509.07039v3 / PRC 93, 015501
Two-nucleon axial charge/current operators are derived through one loop; ultraviolet divergences, renormalization and contact terms are explicit parts of the construction. The source supplies operator structure and renormalization, but no finite universal cross-nucleus coefficient/operator-norm inequality satisfying the preregistered hard-bound definition.

### Krebs, Epelbaum, Meißner — arXiv:1610.03569 / Annals Phys. 378 (2017)
The complete axial-current derivation gives renormalized one-, two- and three-nucleon contributions. The authors show how unitary ambiguity is constrained by renormalizability and matching to nuclear forces. This is a consistency/matching statement; it does not furnish a regulator/renormalization-scheme-independent numerical hard ceiling on the short-range weak-current coefficient or operator norm.

### Krebs, Epelbaum — arXiv:2312.13932
The modern consistency analysis emphasizes that symmetry-preserving cutoff regularization must be used for nuclear forces and current operators. This reinforces the preregistered distinction between a properly renormalized EFT construction and a regulator-independent universal coefficient ceiling. No such finite ceiling is supplied.

### Gysbers et al. — arXiv:1903.00047 / Nature Physics 15 (2019)
Retained only as representative ab-initio empirical evidence-distance for actual many-body/two-body-current effects. In accordance with the preregistration, selected-nucleus corrections are not treated as global maxima.

## Prospective criterion check
A `PASS_UNIVERSAL_CONTACT_BOUND` required a finite theory-derived inequality/interval with explicit normalization, regulator/scheme independence after matching, cross-target applicability without refitting, and direct propagation through the 0048 amplitude-to-power bridge.

The frozen authority set supplies none of these as a universal hard bound. Instead it supplies EFT operator structure, renormalization/matching relations, fitted/calibrated LECs, regulator consistency requirements and selected-nucleus empirical corrections.

Therefore the preregistered outcome is:

`PASS_NO_UNIVERSAL_HARD_BOUND_FOUND / RESIDUAL_OPEN`.

## What this does and does not mean
This is a reproducible negative audit of the frozen primary authority set. It does **not** prove that no mathematically stronger universal Standard-Model bound could ever be derived. It also does not close the physical contact-current residual by assumption.

Iteration 0048 remains valid only as an evidence-distance stress: even 100x the largest frozen empirical extra-amplitude anchor gave `1.301537448e-5 W/kg`, and the bridge to `1 W/kg` required extra amplitude `28796.42286 = 28511.31x` the empirical anchor. 0059 does not promote that empirical scale to a theorem.

## Scientific consequence
The G3 contact-coefficient question is now epistemically classified: current frozen primary chiEFT authority does not provide the hard universal finite coefficient/operator-norm ceiling NMIR would need for a theorem-level all-target passive-SM closure. The residual remains OPEN honestly, rather than being hidden behind naturalness or fitted LEC ranges.

Because another pass over selected nuclei would not close this class, the next highest-value independent class-level gate is the genuinely long-range/growing-coordination Standard-Model residual outside the 0047 bounded-incidence theorem. That gate should first ask whether any actual SM weak/nuclear operator has the long-range/growing-coordination structure needed to evade the extensivity closure at fixed density, rather than assuming such an operator exists.

## Provenance
- Preregistration commit: `5507f21e75e6e41df89a95029837b17952516d56`.
- Evidence-ledger commit: `79447babca27e73c640f0b28de33b8db4d071b9d`.
- Baseline CI on prereg head: run `34062348589` — infrastructure success only, not scientific evidence.
- Scientific evidence is the frozen primary-source authority ledger above; no numerical artifact applies to this documentary theory audit.

## Exact next gate
Preregister G3/F5-F6 `genuinely long-range/growing-coordination SM operator existence and scaling audit`: enumerate the actual Standard-Model weak/nuclear current operators left outside 0047, freeze their range kernels and density scaling, and test whether any has site incidence or integrated pair strength that grows with N at fixed density after finite mediator mass/pion range/screening and cluster decomposition are enforced. If no actual SM operator satisfies the evasion assumptions, close that residual as a scoped no-go; otherwise carry the surviving operator to an absolute W/kg bound.
