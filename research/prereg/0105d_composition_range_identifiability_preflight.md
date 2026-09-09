# 0105d — composition / finite-range identifiability preflight

Date frozen: 2026-09-10
Gate ID: NMIR-V2-0105D
State: ACTIVE_PREREGISTRATION_ONLY
Parent: `research/prereg/0105_v2_model_agnostic_bsm_residual_reconstruction.md`
Dependencies: 0105b mathematical vector-mediator bridge; 0105c nuisance-cleaned identifiability geometry.

## Purpose

Before any observed BSM residual is inspected, derive and unit-test a coefficient-level sufficient condition under which one propagation coefficient plus two composition-distinct finite-q nuclear targets can identify both a vector mediator's proton/neutron coupling ratio and its finite-range scale.

This is an identifiability/control gate, not evidence for a mediator and not a novelty claim for multi-target NSI phenomenology.

## Frozen coefficient convention

Let

`rho = gp/gn`

and

`lambda = mX^2 > 0`.

For a propagation medium with known proton/neutron number-density weights `(Yp, Yn)`, define the common forward charge factor

`A(rho) = Yp rho + Yn`.

For nuclear target `j` with proton/neutron counts `(Zj, Nj)`, define

`Aj(rho) = Zj rho + Nj`.

After dividing out the same overall `g_nu * g_n` normalization and known experiment-specific dimensional constants, the signed coefficient ratio between finite-q scattering and forward propagation is

`Rj = [Aj(rho)/A(rho)] * lambda/(lambda + qj^2)`.

This normalized coefficient relation is a mathematical control. An observed event-rate analysis must later derive signed coefficient information through the full SM-interference, flux, nuclear, detector and nuisance model; rates may possess additional discrete degeneracies.

## Equal-q sufficient identifiability lemma

For two targets observed at the same prospectively specified `q>0`,

`R1/R2 = A1(rho)/A2(rho)`.

Let

`k = R1/R2`.

Provided the denominator is nonzero,

`rho = (N1 - k N2)/(k Z2 - Z1)`.

The target composition determinant is

`Delta12 = Z1 N2 - Z2 N1`.

If `Delta12 != 0`, the two target charge vectors are not proportional and the ratio map is generically sensitive to `rho` rather than merely repeating the same composition measurement.

After `rho` is recovered, define

`f = R1 * A(rho)/A1(rho)`.

In the physical finite-range branch `0 < f < 1`,

`lambda = q^2 f/(1-f)`

and

`mX = q sqrt[f/(1-f)]`.

Thus one propagation coefficient plus two composition-distinct finite-q coefficients is locally sufficient to separate composition ratio from mediator range under the frozen signed-coefficient model.

## Non-identifiable / ill-conditioned limits

The implementation and tests must preserve these fail/limiting cases:

1. `q=0`: `f=1` independently of mediator mass, so finite-range mass information is absent.
2. `Delta12=0`: composition vectors are proportional, so the target ratio cannot identify `rho`.
3. `A(rho)=0`: the chosen normalized ratio to the forward coefficient is singular; this coordinate chart cannot be used.
4. `Aj(rho)=0`: a target coefficient crosses zero and ratio inversion requires a different local representation.
5. `f<=0` or `f>=1`: no positive finite mediator mass exists under this benchmark branch.
6. Heavy/contact limit `mX^2 >> q^2`: inversion is mathematically possible away from the endpoint but becomes progressively ill-conditioned because `f -> 1`.
7. Very-light limit `mX^2 << q^2`: coefficient suppression can become extreme and practical identifiability depends on experimental sensitivity; algebraic invertibility alone is not a sensitivity claim.

## Prospectively frozen real-composition scale controls

Use only nuclear-composition identities, not observed CEvNS residuals:

- Ar-40: `(Z,N)=(18,22)`;
- Cs-133: `(55,78)`;
- I-127: `(53,74)`.

The tests must verify that Ar-40 versus Cs-133 and Ar-40 versus I-127 have nonzero composition determinants. This establishes only that these compositions are algebraically nonparallel.

The real CsI detector response is a mixture and must later be treated as such; the single-isotope identities above are pre-data composition controls, not a replacement for the full CsI likelihood.

## Frozen synthetic tests

1. Forward construction followed by equal-q inversion round-trips `rho` and `mX` for at least five signed synthetic `rho` values that avoid charge zeros.
2. Round-trip spans at least four decades in `mX/q` excluding numerically singular endpoints.
3. Proportional target compositions are rejected as non-identifying.
4. `q<=0` is rejected by the mass inversion path.
5. `f<=0` and `f>=1` are rejected.
6. Ar/Cs and Ar/I composition determinants are nonzero.
7. Swapping target order preserves recovered `rho` and `mX`.
8. Multiplying both normalized coefficients by a common unknown scale is **not** allowed to preserve the mass inversion; the test must document that an absolute propagation-to-scattering normalization is required after composition ratio is found.
9. No function returns a likelihood, p-value, event-rate discovery statistic or observed BSM preference.

## Relation to 0105c

This coefficient-level lemma is necessary but not sufficient for observed reconstruction. In a real experiment, the derivatives of the forward model with respect to `(rho,mX,overall coupling,...)` must first survive each experiment's nuisance projector and then satisfy the prospectively frozen stacked-rank/condition test of 0105c.

Therefore a nonzero composition determinant cannot override a nuisance degeneracy.

## Interpretation guard / prior art

Multi-target CEvNS complementarity and oscillation+CEvNS NSI constraints are established prior art. 0105d must not be advertised as their first discovery.

The scientific role of 0105d is narrower: give NMIR v2 an explicit, testable algebraic criterion for deciding whether a proposed cross-regime authority set can in principle separate mediator composition from range before spending compute on observed residuals.

## Allowed result

If all frozen synthetic/algebraic invariants pass:

`PASS_0105D_COMPOSITION_RANGE_IDENTIFIABILITY_PREFLIGHT_NONDISCOVERY`

Otherwise:

`FAIL_0105D_COMPOSITION_RANGE_IDENTIFIABILITY_INVARIANT`.
