# 0105c — nuisance-orthogonal low-complexity residual statistic

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105C
State: ACTIVE_PREREGISTRATION_ONLY
Parent: `research/prereg/0105_v2_model_agnostic_bsm_residual_reconstruction.md`

## Purpose

Freeze a data-independent Stage-A residual construction before inspecting any 0105 result-dependent residual. The purpose is to prevent flux normalization, spectral tilt, detector response, background morphing or other authorized nuisance directions from being rediscovered and mislabeled as BSM structure.

This gate defines an **identifiability diagnostic plus a profile-likelihood test**. The local linear projection below does not replace the experiment's full nonlinear nuisance profiling.

## Per-experiment null geometry

For experiment `i`, let the expected reconstructed-bin vector under the authorized null be

`mu_i(eta)`

with nuisance vector `eta`. At a null-only reference point fixed without BSM residual information, define the nuisance tangent matrix

`N_i[:,a] = d mu_i / d eta_a`.

Let `W_i` be the positive-semidefinite local information metric implied by the experiment-authorized likelihood/covariance at the same null reference. If a simple covariance representation is valid, `W_i = V_i^+`; for a Poisson likelihood the expected Fisher metric may be used. The exact construction must be frozen in an experiment-specific child record before opening observed residuals.

Define the nuisance-orthogonal projector

`Pperp_i = I - N_i (N_i^T W_i N_i)^+ N_i^T W_i`,

where `+` denotes the Moore-Penrose pseudoinverse.

The projection is used only to construct/diagnose residual directions. The final statistic must still profile the full authorized nuisance model.

## Frozen raw smooth basis

Observed counts are forbidden when constructing the raw basis or choosing its complexity.

### Atmospheric propagation sample (IceCube/DeepCore class)

Use normalized analysis coordinates

`x = affine(log E_rec) in [-1,1]`,
`z = affine(cos zenith_rec) in [-1,1]`.

The maximum raw basis is the five nonconstant tensor-Legendre modes of total degree <=2:

1. `P1(x)`
2. `P1(z)`
3. `P2(x)`
4. `P1(x) P1(z)`
5. `P2(z)`

If the public analysis has additional categorical channels/topologies, the same physical mode is evaluated in each channel through the experiment's forward prediction; no new channel-specific free residual coefficient is introduced in 0105c.

### CEvNS scattering sample (COHERENT class)

Use normalized reconstructed recoil/energy coordinate

`t = affine(T_rec) in [-1,1]`

and, only where prompt/delayed time information is part of the collaboration likelihood, normalized time coordinate `u`.

The maximum raw basis is:

1. `P1(t)`
2. `P2(t)`
3. `P3(t)`
4. `P1(t) P1(u)` when a physical timing axis is present;
5. `P2(t) P1(u)` when a physical timing axis is present.

No residual basis function may be added on a pure background-discriminator or detector-quality axis (for example an analysis variable used only to separate nuclear/electron recoils) unless a later preregistration proves that a neutrino BSM signal has an independent physical dependence on that axis.

The constant mode is deliberately omitted because overall signal/background/flux normalizations belong to the authorized nuisance model.

## Projection and rank rule

Each raw mode `b_k` is mapped to `Pperp_i b_k` using only the null expectation/nuisance model, never the observed residual.

Modes are W-orthonormalized in the prospectively fixed order above. A mode whose projected W-norm is `< 1e-8` times its raw W-norm is declared nuisance-degenerate and dropped. It is **not replaced** by a higher-order mode after data are viewed.

The surviving number of coefficients is therefore `K_i <= 5` and is determined before opening the residual result.

## Residual alternative

The residual coefficients `a_k` are signed and enter the reconstructed expectation through the smallest representation compatible with positivity and the experiment's likelihood semantics. The experiment-specific child gate must freeze whether this is an additive count deformation, multiplicative log-rate deformation, or a forward-model perturbation before observed residuals are evaluated.

No mediator mass, NSI epsilon, sterile parameter, magnetic moment or other BSM parameter appears in Stage A. Those belong to Stage B after a residual is established.

## Test statistic

For each experiment separately,

`T_i = 2 [ log L_i(a_hat, eta_hat) - log L_i(a=0, eta_hat0) ]`.

All authorized nuisance parameters are re-profiled in both hypotheses.

Because nonlinear nuisance structure, low counts and effective rank can invalidate a naive chi-square law, the primary Stage-A p-value is calibrated by a parametric bootstrap/toy ensemble generated from the full authorized null including its auxiliary-constraint semantics. Every toy is subjected to the identical fit/profiling procedure.

Minimum ordinary Stage-A calibration: `100,000` valid null toys unless an exact experiment-supplied calibration is available. Failed fits are retained in an audit ledger and may not simply be discarded if doing so can bias the tail.

A tail extrapolation is forbidden for the ordinary residual classification unless separately preregistered and validated on independent toys.

## Frozen Stage-A classification threshold

A per-experiment result may receive

`PASS_0105C_STRUCTURED_RESIDUAL_NONDISCOVERY`

only if all of the following hold:

1. the corresponding null/control analysis was reproduced prospectively within its own frozen tolerance;
2. the residual basis/rank was fixed without observed residual information;
3. the bootstrap p-value satisfies `p <= 0.0027` (a two-sided Gaussian-equivalent 3-sigma screening scale, used only as a non-discovery anomaly threshold);
4. the fitted deformation remains physical under the experiment's forward model;
5. the result survives the full authorized nuisance profiling;
6. no single documented data-quality/systematic failure accounts for the residual.

If `p > 0.0027`, classify

`FAIL_0105C_NULL_ADEQUATE_AT_SCREENING_LEVEL`.

Neither result is a BSM discovery.

## Multiple-experiment guard

Per-experiment p-values are not multiplied, summed or converted into a fabricated shared confidence level.

A later common-operator gate may build a genuine joint likelihood only if independence/shared covariance assumptions are explicitly justified. Otherwise experiments remain separate predicates.

Selection of which experiments proceed to Stage B must follow the preregistered authority roles; it may not be based on choosing whichever public dataset fluctuates most strongly.

## Operator-identifiability condition for Stage B

For a proposed shared microscopic operator with parameter vector `theta`, let `S_i = d mu_i / d theta` be its local response in experiment `i` and define the nuisance-cleaned response

`Sperp_i = Pperp_i S_i`.

A parameter direction lying in the null space of the stacked nuisance-cleaned Jacobian

`S_stack = [Sperp_1; Sperp_2; ...]`

is not cross-experiment identifiable and may not be advertised as reconstructed.

The numerical rank/condition threshold for a specific operator must be frozen in its Stage-B child preregistration before result inspection.

## Anti-overfit / anti-discovery guards

- No increase in polynomial order after seeing observed residuals.
- No knot placement, localized bump basis or neural anomaly detector in 0105c.
- No basis chosen from residual principal components.
- No sharing nuisance parameters merely to increase significance.
- No dropping an authorized systematic because it overlaps the residual.
- No 5-sigma/fundamental-discovery language from this Stage-A test.
- A 3-sigma screening residual that fails held-out prediction remains an anomaly/failure, not evidence for a new interaction.

## Allowed pre-data work

Before observed Stage-A residuals are opened, 0105c may implement and unit-test:

- weighted nuisance projectors;
- W-orthonormalization/rank logic;
- synthetic Poisson/Gaussian toy calibration;
- identifiability diagnostics on synthetic matrices;
- experiment-specific null/control reproduction.

No observed BSM residual coefficient may be reported until 0105a immutable authority locks and the corresponding null reproduction pass.