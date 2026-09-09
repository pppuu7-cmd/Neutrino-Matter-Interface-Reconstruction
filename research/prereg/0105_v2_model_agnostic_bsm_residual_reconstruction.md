# 0105 — NMIR v2 model-agnostic BSM residual reconstruction and cross-regime operator bridge

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105
State: ACTIVE_PREREGISTRATION_ONLY
Parent controls: `research/benchmarks/KNOWN_MODEL_BENCHMARK_MATRIX.md`, benchmarks 0100–0104

## Scope expansion and immutability rule

This gate starts a new NMIR v2 discovery layer. It does **not** reopen, weaken, reinterpret, or overwrite any NMIR v1 classification. NMIR v1 remains closed under its frozen 0095 contract.

The scientific objective is no longer to choose a preferred BSM model and fit it after inspecting residuals. The objective is to ask whether mutually orthogonal neutrino experiments require a reproducible low-complexity residual beyond the frozen Standard-Model/three-flavor control, and, only if such a residual survives, whether the residuals admit a **single common microscopic operator** whose parameters predict a held-out observable.

The known-model controls 0102 (NSI), 0103 (magnetic spin/flavor), and 0104 (light vector-like mediator) are fixed benchmark families. They may diagnose a recovered residual, but none may be selected post hoc as the winner merely because it fits best.

## Discovery architecture

The frozen architecture is

`CONTROL -> RESIDUAL -> COMMON OPERATOR -> FREEZE -> HELD-OUT PREDICTION`.

A result cannot skip a stage.

### Stage A — per-experiment residual test

For each admitted authority dataset `i`, construct

`R_i = D_i - M_i(SM + authorized nuisance)`

using that experiment's own likelihood/statistical semantics and nuisance model whenever publicly recoverable.

A residual is scientifically admissible only if it is:

1. non-null under a prospectively fixed statistic;
2. structured in energy/baseline/recoil/flavor rather than a normalization-only offset unless normalization is itself the frozen target;
3. robust to the experiment's authorized nuisance treatment;
4. reproducible from immutable public inputs;
5. obtained without increasing residual-basis complexity after seeing the result.

No experiment-level confidence level is translated into a different experiment's statistic. A green workflow is not a residual PASS.

### Stage B — cross-regime common-operator test

Propagation and scattering residuals remain separate until a microscopic operator maps both.

A model-agnostic propagation term `Delta H(E,rho,Ye,...)` by itself is **not** allowed to predict CEvNS. Promotion requires an explicit low-energy interaction Lagrangian/operator, charge/flavor convention, and one shared parameter vector `theta_shared` that generates both the zero-momentum forward potential and finite-momentum scattering amplitude.

At least two physically distinct regimes are required for promotion, e.g.

- coherent propagation / matter effect (`q -> 0`), and
- finite-`q` neutrino scattering such as CEvNS.

Separate experiment-specific BSM fudge factors are forbidden.

### Stage C — prospective held-out test

Before inspecting the held-out result used for confirmation, freeze:

- the selected operator family;
- all shared BSM parameters or their predictive posterior;
- nuisance treatment inherited from the held-out experiment;
- the predicted **sign, shape and support** of the effect in the held-out observable;
- a quantitative acceptance/failure rule.

A later result counts only if it tests this frozen prediction. A merely compatible exclusion contour is not a discovery confirmation.

## Authority roles frozen at preregistration

These roles describe data-access/statistical suitability, not experimental quality.

### Current calibration / discovery-candidate authorities

1. **IceCube DeepCore 7.5-year public sterile/oscillation authority** — propagation/matter-sector control where the exact released likelihood/response semantics can be pinned under the relevant gate.
2. **COHERENT public CEvNS releases** — finite-`q` scattering control/candidate authority where signal, background, response and nuisance information are sufficient for an independent likelihood reproduction.
3. **JUNO first 59.1-day 2026 result** — high-value precision constraint/cross-check, but not promoted here to the primary residual-discovery likelihood unless collaboration-level posterior/likelihood/nuisance authority is immutably recovered. Public source-data points from figures alone cannot substitute for the collaboration likelihood.
4. **ICARUS first 2026 disappearance result** — already-public control/constraint, not a blind future confirmation dataset.

### Prospective validation authorities

The following are reserved as prospective validation opportunities to the extent that their relevant result has not been inspected/frozen into the discovery fit:

- a future joint SBND+ICARUS SBN oscillation result/data release;
- observed IceCube Upgrade oscillation/matter-effect data after commissioning and public statistical authority;
- a future JUNO release with sufficient collaboration-level likelihood/posterior/nuisance information;
- a future independent CEvNS dataset with reproducible recoil-response likelihood.

A dataset loses held-out status as soon as its result-dependent information is used to choose the operator, basis complexity, parameter domain, statistic, or acceptance threshold.

## Minimal residual basis rule

0105 does not yet authorize a data fit. Before any Stage-A numerical residual scan, a child preregistration must freeze the exact basis and coefficient bounds separately for propagation and scattering.

The default design target is the lowest-complexity basis capable of representing:

- an energy-independent matter-potential deformation;
- one smooth energy-dependent deformation;
- one finite-`q` scattering deformation.

Adding basis functions after seeing residual structure requires a new numbered amendment and cannot be back-promoted to the original blind gate.

## Benchmark cross-regime invariant: single neutral vector mediator

This is a **control identity**, not an assumption that Nature uses a vector mediator.

For a neutral vector field `X_mu` with schematic interaction

`L_int ⊃ X_mu [ g_nu^(alpha beta) nu_bar_alpha gamma^mu P_L nu_beta + sum_f g_f f_bar gamma^mu f ]`,

the static forward coefficient for matter fermion `f` is

`C_f(0) = g_nu^(alpha beta) g_f / m_X^2`,

while the finite-spacelike-momentum coefficient is

`C_f(q^2) = g_nu^(alpha beta) g_f / (m_X^2 + |q|^2)`

under the benchmark sign/propagator convention.

Therefore

`r_f(q) = C_f(q^2) / C_f(0) = m_X^2 / (m_X^2 + |q|^2)`.

For the idealized single-`q` benchmark and `0 < r < 1`,

`m_X^2 = [r/(1-r)] |q|^2`.

This relation is a cross-regime consistency test: forward propagation measures the zero-momentum effective coefficient while a recoil spectrum probes finite momentum transfer. In a realistic CEvNS calculation the test must integrate over recoil-dependent `q`, nuclear form factors, isotope composition, flux and detector response. Nuclear coherent charges (`Z g_p + N g_n`, or the declared quark-level equivalent) must be explicit.

Heavy-mediator limit: `m_X^2 >> |q|^2` gives a contact interaction and generally preserves the coupling/mass degeneracy.

Finite-range regime: `m_X ~ |q|` can imprint a recoil-shape dependence capable, in principle, of breaking that degeneracy.

Very-light regime: nonlocal/range validity and macroscopic-medium assumptions must be re-audited; the local forward-potential approximation of 0104 is not automatically valid.

## Hypothesis-family separation

The following families must remain separate through model selection:

- vector mediator / vector NSI;
- scalar mediator;
- magnetic-moment / spin-flavor interaction;
- sterile-only mixing;
- generic phenomenological residual with no microscopic identification.

A scalar response may not inherit the vector forward/scattering bridge. A magnetic interaction may not be relabeled as density-dependent NSI. Sterile mixing may not absorb arbitrary matter-interaction coefficients unless a dedicated combined model is prospectively preregistered.

## Null-model and nuisance guard

The primary null is the experiment-appropriate Standard Model + authorized three-flavor oscillation model with frozen nuisance semantics.

A 3+1 sterile component may enter a null/alternative only where the 0101 authority contract and a child preregistration explicitly authorize it. Sterile freedom cannot be introduced after observing a residual merely to absorb or expose another BSM effect.

Nuisance parameters must not be shared across experiments unless they represent a genuinely common physical quantity with a justified covariance model.

## Statistical guard

- Do not sum experiment-specific `Delta chi^2` values unless they arise from commensurate likelihoods under a justified joint statistical model.
- Do not invent a shared confidence label from heterogeneous 90%/95% contours.
- Do not use generic Wilks thresholds at a coupling boundary or where mediator mass is non-identifiable under the null without validation.
- Prefer experiment-supplied constructions; otherwise use prospectively defined Monte Carlo/toy calibration when feasible.
- Global look-elsewhere effects from scanning mass, operator family, flavor texture or residual basis must be accounted for before a discovery-level claim.
- A posterior predictive cross-check is not independent confirmation if the same data chose the model.

## Mandatory promotion ladder

Allowed classifications are deliberately conservative:

1. `PASS_0105_RESIDUAL_PROTOCOL_PREFLIGHT_NONTERMINAL`
2. `BLOCKED_0105_AUTHORITY_INCOMPLETE`
3. `FAIL_0105_NULL_ADEQUATE`
4. `PASS_0105_STRUCTURED_RESIDUAL_NONDISCOVERY`
5. `FAIL_0105_NO_COMMON_OPERATOR`
6. `PASS_0105_SHARED_OPERATOR_IDENTIFIED_NONDISCOVERY`
7. `PASS_0105_HELDOUT_PREDICTION_FROZEN`
8. `PASS_0105_INDEPENDENT_PREDICTION_CONFIRMED_DISCOVERY_CANDIDATE`

The final label is still only a **discovery candidate** inside NMIR. A claim of a new fundamental interaction requires the relevant experimental significance, systematic closure, collaboration-quality validation, and independent replication appropriate to particle physics.

## Fail-closed conditions

0105 must stop or remain BLOCKED if any of the following holds:

- only plot digitization is available where the required likelihood/nuisance authority is not public;
- the apparent residual disappears under an authorized nuisance treatment;
- no immutable machine-readable source can reproduce the claimed effect;
- a common operator requires experiment-specific BSM couplings not implied by source composition/flavor physics;
- the operator family or residual basis was chosen after viewing held-out results;
- finite-`q` transport is inferred from the 0104 forward-only preflight;
- a future validation result has already influenced the frozen prediction;
- discovery significance depends on an unvalidated asymptotic threshold.

## Immediate child gates authorized by this preregistration

No result-dependent BSM fit is authorized yet. The next actions are authority and mathematics only:

1. `0105a` — immutable cross-experiment authority audit: JUNO, IceCube/DeepCore, COHERENT, ICARUS/SBN; identify exactly what machine-readable likelihood/response/nuisance objects exist.
2. `0105b` — analytic + unit-tested forward/finite-`q` vector-mediator bridge, including heavy/contact and finite-range limits, with no data fit.
3. `0105c` — prospectively freeze the lowest-complexity Stage-A residual basis and toy-calibrated model-selection statistic before opening a residual scan.
4. Only after 0105a–c PASS: authorize a result-dependent Stage-A scan.

## Scientific target

The high-value outcome is not a numerically better fit in one experiment. It is a reproducible statement of the form:

> a low-complexity residual appears independently in physically different neutrino regimes; one common microscopic operator maps both with the same shared parameters; those parameters were frozen before a later experiment; and the later experiment observed the predicted sign/shape/support.

That is the minimum NMIR v2 architecture capable of turning a methodological framework into a credible search for a genuinely new neutrino–matter interaction.