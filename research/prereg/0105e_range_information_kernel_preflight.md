# 0105e — finite-range information-kernel preflight

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105E
State: ACTIVE_PREREGISTRATION_ONLY
Parent: `research/prereg/0105_v2_model_agnostic_bsm_residual_reconstruction.md`
Dependencies: 0105b vector-mediator bridge; 0105c nuisance-cleaned geometry; 0105d composition/range algebraic identifiability.

## Purpose

Separate **algebraic identifiability** from **statistical certifiability** before any observed BSM residual is inspected. 0105d shows when the signed coefficient map can be inverted. 0105e asks where the finite-range scale is actually informative under a local small-signal coefficient model.

This is a pre-data information-geometry control. It is not evidence for a mediator, not a measured sensitivity curve, and not a replacement for an experiment-specific likelihood.

## Frozen coefficient model

For target/bin `j`, write the normalized BSM coefficient

`R_j(rho,mX,q_j) = B_j(rho) f(mX,q_j)`

with

`B_j(rho) = (Z_j rho + N_j)/(Yp rho + Yn)`

and

`f(mX,q) = mX^2/(mX^2 + q^2)`.

Let the range coordinate be

`eta = ln(mX)`.

Then

`d f / d eta = 2 f (1-f)`

and

`d R_j / d eta = 2 f (1-f) B_j`.

## Frozen fixed-absolute-covariance information kernel

For a local Gaussian coefficient model with positive-definite covariance `C` that is treated as fixed with respect to the infinitesimal BSM coefficient perturbation,

`I_eta = (dR/deta)^T C^{-1} (dR/deta)`.

For a common-q block, the entire mediator-range dependence factors as

`I_eta = K_range(f) * [B^T C^{-1} B]`

where

`K_range(f) = 4 f^2 (1-f)^2`.

The gate must verify prospectively:

1. `K_range >= 0` for `0 <= f <= 1`;
2. `K_range = 0` at both endpoints `f=0` and `f=1`;
3. the unique interior maximum occurs at `f=1/2`;
4. `f=1/2` is equivalent to `mX=q` for positive `mX,q`;
5. `K_range(1/2)=1/4`;
6. light limit `mX/q=x<<1`: `K_range ~ 4 x^4`;
7. heavy/contact limit `mX/q=x>>1`: `K_range ~ 4 x^-4`.

Thus coefficient-level information about the finite range is intrinsically concentrated near momentum transfers `q ~ mX`; it is not uniform across mediator mass.

## Composition-information scaling

At fixed `mX,q`,

`d R_j / d rho = f dB_j/d rho`.

For the same fixed absolute covariance convention,

`I_rho = f^2 * [B_rho'^T C^{-1} B_rho']`.

Therefore the light-mediator limit suppresses local composition information as

`I_rho ~ (mX/q)^4`.

In the heavy/contact limit `f -> 1`, this particular amplitude suppression disappears, even though range information itself vanishes. This cleanly separates two statements:

- target composition can remain informative in the contact limit;
- mediator **range** cannot be inferred once the response becomes contact-like.

## Error-model guard

The fourth-power asymptotics above are frozen only for the local fixed-absolute-covariance coefficient model. They must **not** be advertised as an experiment-independent sensitivity law. If an uncertainty model scales with the BSM coefficient itself, or if covariance/nuisance projections vary with the BSM parameters, the practical scaling can change.

For the later observed analysis, 0105c nuisance projection and each experiment's actual likelihood/covariance take authority over this toy kernel.

## Multi-q consequence

A recoil spectrum supplies multiple momentum transfers. The prospective range-tomography strategy is therefore not to choose a mass window after seeing residuals, but to evaluate whether the frozen q-support spans the kernel around candidate `mX` values. Bins with `q << mX` and `q >> mX` can constrain normalization/composition while bins with `q ~ mX` carry the largest local derivative with respect to `ln mX` under this control model.

No observed bin may be selected because it gives a favorable BSM residual.

## Frozen tests

The implementation must test:

1. exact equivalence of direct `x=mX/q` and `f` forms;
2. non-negativity and endpoint zeros;
3. maximum `K_range=1/4` at `x=1`;
4. symmetry `K_range(x)=K_range(1/x)` for positive `x`;
5. fourth-power light/heavy asymptotics numerically away from floating endpoints;
6. composition amplitude factor `f^2` tends to `x^4` for `x<<1` and to one for `x>>1`;
7. invalid non-positive `mX` or `q` fails closed;
8. no function consumes observed event data or returns a likelihood/significance.

## Allowed result

If all frozen invariants pass full repository CI:

`PASS_0105E_RANGE_INFORMATION_KERNEL_PREFLIGHT_NONDISCOVERY`

Otherwise:

`FAIL_0105E_RANGE_INFORMATION_KERNEL_INVARIANT`.
