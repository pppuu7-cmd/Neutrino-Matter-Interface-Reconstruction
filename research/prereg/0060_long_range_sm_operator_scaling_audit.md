# NMIR 0060 preregistration — genuinely long-range/growing-coordination Standard-Model operator audit

Date: 2026-09-07
Gate: G3 / F5-F6 residual outside bounded finite-range k-local closure
Status at preregistration: OPEN

## Question
Does any actual Standard-Model neutrino/nuclear weak operator relevant to passive matter possess genuinely long-range or growing-coordination structure at fixed density that escapes the 0047 bounded-incidence extensivity theorem and can support superextensive integrated weak response without importing external/stored energy?

## Scope
This gate does not revisit 0047 for finite-range bounded-incidence operators and does not revisit the 0059 contact-coefficient audit. It asks whether the mathematical evasion assumptions themselves are physically realized by a Standard-Model weak/nuclear operator. BSM mediators remain excluded.

## Frozen operator classes to inspect
Before classification, cover at least:
1. direct electroweak W/Z exchange and its low-energy four-fermion limit;
2. pion-range and multi-pion components of nuclear electroweak currents in chiral EFT;
3. electromagnetic long-range kernels only insofar as a Standard-Model neutrino electromagnetic property is nonzero, with its actual SM suppression kept explicit;
4. collective nuclear/matter correlations mediated by finite-range interactions, with fixed-density cluster decomposition/saturation distinguished from a true interaction kernel whose integrated strength grows with system size;
5. any massless-SM-field contribution that could couple neutrinos to matter in the relevant channel without being merely ordinary external-state radiation or a BSM effective moment.

## Frozen scaling test
For a pair/range kernel `K(r)` at fixed number density `rho`, define the per-site integrated coordination measure

`I(R) = rho * integral_{r0}^{R} 4 pi r^2 |K(r)| dr`.

A candidate counts as genuinely growing-coordination only if, after the physically required mediator mass/range, screening, saturation and operator normalization are included, `I(R)` diverges or grows parametrically with system radius `R` in the thermodynamic limit and the corresponding response is not already limited by an extensive absolute energy/sum-rule budget.

Finite-range Yukawa kernels with nonzero mass, exponentially decaying pion-range kernels, and screened kernels are expected to saturate but this expectation is not a PASS until checked against frozen primary authorities and the analytic scaling criterion.

## Prospective classifications
### PASS_NO_SM_GROWING_COORDINATION_SURVIVOR
Only if every frozen actual SM operator class either has finite interaction range/screening causing `I(R)` to saturate, is already inside an extensive sum-rule/energy-budget closure, or has a neutrino coupling too structurally different to supply the hypothesized passive nuclear/matter gain. Record exact scopes; do not call it a universal QFT theorem.

### PASS_SM_LONG_RANGE_SURVIVOR
If a concrete SM operator has a physical unscreened long-range kernel for the relevant neutrino-matter response such that `I(R)` genuinely grows at fixed density and is not already closed by an extensive budget. Freeze that operator and carry it alone to an absolute response/W/kg gate; no generic gain multiplication.

### BLOCKED_AUTHORITY_GAP
If the operator inventory or range structure cannot be established from primary/authoritative sources without guesswork.

## Acceptance guards
- A mathematical all-to-all toy model is not evidence that the SM realizes it.
- Finite pion range is not called long-range merely because it exceeds a nucleon size.
- Ordinary macroscopic electromagnetic fields are not neutrino coupling enhancement unless the actual neutrino electromagnetic vertex is included.
- Standard-Model neutrino magnetic moments, if considered, must use the SM value/structure and are not a BSM free parameter.
- Correlation length and interaction range are distinct; critical correlations do not automatically create a new microscopic weak operator or neutrino-supplied energy.
- No naturalness, target scan, or F9 gain multiplication is allowed.

## Scientific-vs-infrastructure failure
This is primarily an analytic/authority audit. A documentary classification may be scientific without a numerical artifact if the primary-source ledger and analytic kernel integrals are fully recoverable. Any supporting code/workflow is infrastructure/reproducibility support, not the source of the physical operator inventory.

## Exact next action
- On `PASS_NO_SM_GROWING_COORDINATION_SURVIVOR`: mark the 0047 long-range/growing-coordination loophole closed in the audited SM scope and move to the next independent survivor, likely G9 distant-source focusing utility or G8 if its source/entrance-strength blocker is resolved.
- On `PASS_SM_LONG_RANGE_SURVIVOR`: preregister an operator-specific absolute response and W/kg calculation.
- On `BLOCKED_AUTHORITY_GAP`: preserve the residual OPEN and move to an independently testable survivor without inventing a kernel.
