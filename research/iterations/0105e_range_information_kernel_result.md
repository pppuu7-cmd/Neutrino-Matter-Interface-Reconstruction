# 0105e result — finite-range information kernel

Date: 2026-09-10
Gate ID: NMIR-V2-0105E
Final state: `PASS_0105E_RANGE_INFORMATION_KERNEL_PREFLIGHT_NONDISCOVERY`

## Scope

This closes only the pre-data local information-geometry control frozen in `research/prereg/0105e_range_information_kernel_preflight.md`. It uses no observed event residuals and makes no experimental BSM sensitivity or significance claim.

## Result

With

`f = mX^2/(mX^2+q^2)`, `eta=ln(mX)`,

the common fixed-absolute-covariance range kernel is

`K_range = 4 f^2 (1-f)^2`.

Equivalently, with `x=mX/q`,

`K_range(x)=4 x^4/(1+x^2)^4`.

The frozen invariants are satisfied:

- `K_range >= 0`;
- endpoint limits vanish;
- the unique interior maximum is at `x=1`, i.e. `mX=q`;
- `K_range(1)=1/4`;
- reciprocal symmetry `K_range(x)=K_range(1/x)`;
- light limit `K_range ~ 4 x^4`;
- heavy/contact limit `K_range ~ 4 x^-4`.

For the composition coordinate `rho=gp/gn`, the corresponding fixed-absolute-covariance amplitude factor is `f^2`, so the light limit suppresses local composition information as `x^4`, while the contact limit does not suppress composition amplitude even though range information vanishes.

## First CI failure and conditioning audit

Initial run:

- run: `34417731115`
- head: `174033d9b06df68f4a9f33736de5b525d1354d19`
- result: FAILURE
- pytest: `1 failed, 679 passed`

The only failure was reciprocal symmetry at `x=1e-4` versus `x=1e4`. The original implementation computed `f` and then `1-f`; for `x>>1`, `f->1` and the subtraction loses significant digits. The analytic kernel itself remained exactly reciprocal.

Amendment `research/amendments/0105e_a1_stable_range_kernel_evaluation.md` froze the correction before implementation: retain all tolerances and physics, but evaluate the mathematically equivalent reciprocal-stable form using `y=min(x,1/x)`.

Implementation commit:

`6cdaf47f4383d6492b92468f19ff79a51872a7e4`

## Successful hosted authority

Corrected full CI:

- run: `34418049698`
- job: `102687214931`
- head: `6cdaf47f4383d6492b92468f19ff79a51872a7e4`
- result: SUCCESS
- pytest: `685 passed`
- `python -m nmir.baseline`: SUCCESS

No tolerance, physical formula, gate domain, or acceptance criterion was loosened.

## Scientific interpretation

0105e supplies a prospective design principle for mediator-range tomography: under the frozen local covariance convention, a momentum-transfer bin carries the largest local derivative information about `ln(mX)` when `q` is near `mX`. Therefore a multi-q recoil spectrum should be evaluated for **q-support coverage**, rather than selecting a mediator-mass window after residuals are observed.

This is not an experiment-independent sensitivity law. Actual covariance, nuisance projection and likelihood semantics remain authoritative in the later experiment-specific stage.

## Discovery guard

This PASS is NONDISCOVERY. It does not establish that a mediator exists, does not fit `mX`, and does not authorize observed residual execution.
