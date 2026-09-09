# 0105c — nuisance-orthogonal residual geometry pre-data result

Date recorded: 2026-09-10
Parent preregistration: `research/prereg/0105c_nuisance_orthogonal_residual_statistic.md`
Preregistration commit: `5a01d844cae4d84d09742eff64097a83a6f247c3`

## Scope

This record closes only the **pre-data mathematical implementation checkpoint** of 0105c. It does not open or classify an observed IceCube, COHERENT, JUNO, ICARUS or other neutrino residual.

The full Stage-A 0105c scientific classification remains locked pending authority pinning, experiment-specific null reproduction, exact residual realization and the prospectively required null-toy calibration.

## Implementation

NumPy dependency declaration:
- commit `070934e69f0f7ae3ccb852f6e88200eff16bb5de`.

Core implementation:
- `src/nmir/nuisance_orthogonal_residual_0105c.py`;
- commit `0910b521585518447a14b1667acf61de0c987bcb`.

Synthetic tests:
- `tests/test_nuisance_orthogonal_residual_0105c.py`;
- commit `147e3f7ab0dad2d8c7a9141f3d2c7731f317f127`.

The implementation evaluates the prospectively frozen weighted nuisance projector

`P_perp = I - N (N^T W N)^+ N^T W`,

ordered W-orthonormalization with nuisance-degenerate modes dropped rather than replaced, nuisance-cleaned operator Jacobians, relative-rank diagnostics and stacked cross-experiment identifiability rank.

## Hosted validation

Baseline CI run: `34413102499`
Job: `102671796831`
Head: `147e3f7ab0dad2d8c7a9141f3d2c7731f317f127`

Hosted result:
- full pytest: `660 passed in 62.00 s`;
- `python -m nmir.baseline`: success;
- workflow conclusion: success.

## Prospectively important synthetic result

A deliberately constructed two-parameter control verifies the distinction between ordinary fit combination and genuine nuisance-cleaned complementarity:

- experiment A has cleaned operator rank 1 because its nuisance tangent absorbs parameter direction 2;
- experiment B has cleaned operator rank 1 because its nuisance tangent absorbs parameter direction 1;
- the stacked cleaned Jacobian has rank 2.

Therefore two experiments can, in principle, recover a shared parameter vector that neither identifies alone **only when their surviving nuisance-orthogonal response directions are complementary**.

A second control verifies the converse: if the same shared direction lies entirely in the nuisance tangent space of every experiment, stacking does not rescue it; the stacked cleaned rank remains zero.

This is the mathematical criterion NMIR v2 will use before describing a common operator direction as reconstructed.

## Interpretation guard

The successful synthetic geometry establishes no observed anomaly and no BSM evidence. In particular it does not authorize:

- inspection of an observed Stage-A residual;
- a vector/scalar/magnetic/sterile preference;
- a combined IceCube+COHERENT likelihood;
- a discovery significance;
- replacement of the prospectively required experiment-specific full nuisance profiling by the local linear projector.

## Checkpoint status

`PASS_0105C_PREDATA_NUISANCE_ORTHOGONAL_GEOMETRY_IMPLEMENTATION_NONDISCOVERY`

This is an implementation checkpoint, not the later Stage-A residual classification defined in the 0105c preregistration.

## Remaining 0105c work

Before an observed residual can be opened:

1. complete the corresponding 0105a consumed-authority byte locks;
2. reproduce each experiment's authorized null/control fit;
3. instantiate the frozen <=5-mode basis on the exact public analysis bins and nuisance tangents without looking at observed residual structure;
4. freeze the experiment-specific residual parameterization and likelihood implementation;
5. implement and validate the prospectively required >=100,000-null-toy calibration path.
