# NMIR 0059 preregistration — universal renormalized contact/two-body-current bound audit

Date: 2026-09-07
Gate: G3 / F4-F6 absolute genuine two-/higher-body Standard-Model current residual
Status at preregistration: OPEN

## Question
Do primary Standard-Model/chiral-EFT authorities imply a regulator- and renormalization-scheme-independent hard upper bound on the renormalized short-range/contact contribution to low-energy nuclear weak currents that can be propagated as a universal coefficient/operator-norm ceiling across nuclei, rather than only a power-counting/naturalness expectation or a fitted low-energy-constant range?

## Scope
This gate addresses the residual explicitly left open by iterations 0047–0048. It does not revisit the already closed bounded-finite-range extensivity theorem and does not infer a universal maximum from selected nuclei. It also does not cover genuinely long-range/growing-coordination operators outside 0047.

## Frozen authority classes to inspect
Use primary or authoritative theory sources covering all of the following before classification:
1. chiral-EFT electroweak/axial current derivations through the first non-vanishing two-body contact terms, including regulator/renormalization dependence;
2. the relation of the axial contact current to fitted LECs such as `c_D`/equivalent conventions and the fact that those LECs are calibrated jointly with nuclear forces/observables;
3. explicit demonstrations of cutoff/regulator or scheme dependence and the role of counterterms/renormalization;
4. representative ab-initio/empirical calculations showing actual two-body-current corrections, used only as evidence-distance anchors and not universal maxima.

Preferred source families, to be frozen by DOI/arXiv/primary URL in the iteration evidence ledger: Krebs/Epelbaum/Meißner electroweak-current derivations; Baroni et al. axial-current derivations; Gazit/Quaglioni/Navrátil or equivalent `c_D` calibration work; modern ab-initio axial-current calculations such as Gysbers et al. where appropriate. A source may be replaced only if inaccessible, and the replacement must be primary and equivalent in scope.

## Definitions
A **hard universal bound** must be all of:
- an inequality or finite allowed interval derived from the theory/renormalization structure itself, not a naturalness prior;
- stated in a convention that can be mapped with explicit units/normalization;
- regulator/cutoff/scheme independent after the required matching/renormalization;
- applicable across the target class without fitting a new free coefficient separately to each nucleus;
- strong enough to propagate through the frozen 0048 amplitude-to-power bridge without importing an empirical selected-nucleus maximum as the theorem.

The following do **not** count as a hard universal bound:
- `O(1)` naturalness assumptions;
- truncation-error bands or power-counting order estimates;
- finite fitted intervals for a LEC tied to a chosen regulator/Hamiltonian/data set unless a scheme-independent theorem maps them to a universal current norm;
- observed percent-level corrections in selected nuclei;
- absence of known large corrections.

## Prospective classifications
### PASS_UNIVERSAL_CONTACT_BOUND
Only if the frozen authorities provide a genuine hard universal bound satisfying every definition above. Record the exact inequality, units/conventions, regulator mapping, target scope, and propagate it through the 0048 power bridge.

### PASS_NO_UNIVERSAL_HARD_BOUND_FOUND / RESIDUAL_OPEN
If the authorities instead show that the relevant contact strength is a renormalized/fitted LEC whose numerical value is regulator/scheme/Hamiltonian dependent and no regulator-independent universal finite coefficient/operator-norm inequality is supplied. This is a reproducible negative audit, not a theorem that no such bound can ever be derived. Preserve the G3 residual OPEN and use 0048 only as evidence-distance.

### BLOCKED_AUTHORITY_GAP
If the source set cannot establish the renormalization status cleanly enough to distinguish the two outcomes.

## Acceptance discipline
No post-hoc naturalness ceiling may be promoted to a theorem. No selected-nucleus correction may be treated as the global maximum. If classification is `PASS_NO_UNIVERSAL_HARD_BOUND_FOUND`, NMIR readiness may increase only for closing the audit question, while the physical coefficient residual remains explicitly OPEN.

## Exact next action
- On `PASS_UNIVERSAL_CONTACT_BOUND`: implement the bound with tests and propagate to a universal passive-SM W/kg ceiling.
- On `PASS_NO_UNIVERSAL_HARD_BOUND_FOUND`: document the theory limitation, keep the residual OPEN, and move to the next independent class-level survivor (genuinely long-range/growing-coordination SM residual or G9/G8 depending recoverable authority).
- On `BLOCKED_AUTHORITY_GAP`: stop this branch without inventing a coefficient and move to another independently testable gate.