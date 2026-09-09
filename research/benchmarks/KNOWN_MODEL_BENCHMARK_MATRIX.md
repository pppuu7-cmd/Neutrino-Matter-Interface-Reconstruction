# NMIR known-model benchmark matrix

Date frozen: 2026-09-09
Purpose: apply the NMIR reconstruction/funnel discipline to established neutrino models before deciding whether a new model is needed.

## Rule of use
A model is not called "true" because it passes this matrix. PASS means only that the model survives the explicitly frozen gate being tested. FAIL is scoped to the tested claim. BLOCKED means the required external authority/input is unavailable or insufficient and is not to be relabeled as a physics failure.

No gate may be weakened for a later custom NMIR model merely because an established model fails it. Any model-specific contract must be preregistered before its terminal calculation.

## Common benchmark axes
Every benchmark must report the following axes separately:

1. **MATHEMATICAL_CONSISTENCY**
   - finite parameters and observables;
   - required Hermiticity/unitarity/positivity/conservation properties;
   - numerical invariants.
2. **KNOWN_LIMIT_RECOVERY**
   - recover analytically known limits or a simpler parent theory;
   - independent formula-vs-numerical checks where possible.
3. **PARAMETER_AUTHORITY**
   - provenance of externally fitted constants/ranges;
   - no silent parameter tuning after results.
4. **SOURCE_PROPAGATION_AUTHORITY**
   - source/environment profiles required by the model must be traceable;
   - density/composition/electron-density profiles are not inferred from unrelated quantities without authority.
5. **INTERACTION_TRANSPORT_AUTHORITY**
   - absorptive/scattering/nuclear-response claims require their own authority;
   - coherent flavor evolution cannot be used to close nuclear opacity.
6. **G9_GEOMETRY_DEPENDENCY**
   - identify whether the model changes the already-certified lens geometry, only changes flavor composition/weights, or requires a new ray calculation.
7. **DISTINGUISHING_PREDICTION**
   - record what observable could distinguish the model from the control;
   - absence of a distinguishing observable is not automatically a physics failure but limits model-selection value.
8. **REPRODUCIBILITY / PROVENANCE**
   - preregistration commit, code commit, run/job/artifact IDs and hashes for terminal numerical claims.

## Prospectively frozen benchmark order
The order below is fixed before executing benchmark 0100. Detailed contracts for each future model must still be preregistered before execution.

| ID | Model / scenario | Role | State |
|---|---|---|---|
| 0100 | Standard three-flavor massive-neutrino oscillation phenomenology + MSW matter potential | control / known-limit calibration | ACTIVE |
| 0101 | 3+1 sterile-neutrino extension | BSM extension | PLANNED |
| 0102 | neutral-current-like neutrino non-standard interactions (NSI) in matter | BSM matter-potential deformation | PLANNED |
| 0103 | neutrino magnetic-moment / spin-flavor extension | BSM electromagnetic channel | PLANNED |
| 0104 | light-mediator neutrino interaction benchmark | BSM interaction/transport deformation | PLANNED |

The list is representative, not exhaustive. Adding later models is allowed, but results from 0100–0104 must not be erased or have their gates rewritten.

## Decision rule for a custom model
A custom NMIR model is justified only after the known-model matrix exposes a reproducible unmet design region, for example a set of requirements that no benchmarked model can satisfy simultaneously. The custom model's design specification must be derived from that failure/block matrix and frozen before fitting or terminal tests.

A custom model must not be created merely to obtain novelty or to replace an established model that already closes the required observable sector.

## Global interpretation guard
The v2 G9 Betelgeuse engineering branch and the known-model benchmark are separate layers. A spacecraft power-authority block does not make a neutrino model scientifically false, and a flavor-model PASS does not establish spacecraft feasibility, detector event gain, deposited-energy gain, or useful power.