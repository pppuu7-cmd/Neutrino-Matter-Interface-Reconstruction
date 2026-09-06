# NMIR prereg — inverse background requirement for accepted solar-CEvNS counts

Date: 2026-09-06
Status: prospective; frozen before implementation/result inspection.

## Question
Once an accepted solar-CEvNS signal rate is feasible (iteration 0049), how low must the *indistinguishable accepted background* be to reach nominal counting-only 3σ or 5σ discovery significance in one year?

This gate derives a necessary background target. It does not claim any current detector already meets it.

## Frozen statistical metric
Use the standard Asimov median discovery significance for a Poisson counting experiment with known background expectation B:

`Z_A(S,B) = sqrt( 2 * [ (S+B) ln(1+S/B) - S ] )`, for `S>0`, `B>0`.

For each signal scenario and target Z, solve uniquely for the largest `B_max` satisfying `Z_A(S,B_max)=Z`.

Background normalization uncertainty is deliberately excluded here and must tighten the requirement in a later nuisance-aware gate.

## Frozen signal scenarios
A. Design yield: `S=10 accepted events/year`.
B. Ar40, 10 kg, 10 eV, `eta=0.50`, using iteration-0049 ideal `23.6924840370675/year`: `S=11.84624201853375/year`.
C. Ar40, 10 kg, 20 eV, `eta=0.75`, using iteration-0049 ideal `13.212980112/year`: `S=9.909735084/year`.

Evaluate `Z={3,5}`.

Also report `B_max/S` and the equivalent mean indistinguishable-background rate per kg-year for the 10-kg Ar scenarios.

## Prospective validation
- numerical inversion must reproduce Z to relative error <=1e-10;
- `B_max(5σ) < B_max(3σ)` for every scenario;
- `B_max` must increase monotonically with S at fixed Z;
- invalid nonpositive S/Z/B inputs fail closed.

Classification: `PASS_BACKGROUND_REQUIREMENT_MAP` if all validation conditions pass. Otherwise `FAIL_BACKGROUND_REQUIREMENT_MAP`.

## Scope guards
- This is a counting-only, known-background requirement, not an experimental sensitivity claim.
- It applies to the *accepted, analysis-indistinguishable* background after all recoil/ER/neutron/topological selections, not raw environmental triggers.
- Site-specific SBC neutron rates are not imported as universal backgrounds.
- Background systematics, spectral information, time dependence, directional information and multi-bin likelihoods remain outside this gate.
- Detector signal amplification remains detector gain, not weak-interaction or neutrino-energy gain.

## Required evidence
Deterministic module, dedicated tests, JSON benchmark, fail-closed hosted workflow, raw log/artifact inspection, immutable numbered iteration and RECOVERY reconciliation.
