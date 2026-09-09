# 0105e-a1 — stable numerical evaluation of the range-information kernel

Date: 2026-09-10
Parent gate: NMIR-V2-0105E
Amendment type: NUMERICAL CONDITIONING ONLY

## Trigger

The first full-CI run of 0105e (`34417731115`, head `174033d9b06df68f4a9f33736de5b525d1354d19`) failed exactly one invariant test while 679 tests passed.

The failed invariant was the preregistered reciprocal symmetry

`K(x) = K(1/x)`, `x=mX/q`.

At `x=1e-4` versus `x=1e4`, the implementation returned

- `3.999999840000003e-16`;
- `3.9999997825623963e-16`.

The relative mismatch was above the frozen `5e-9` tolerance.

## Diagnosis

The analytic kernel is

`K = 4 f^2 (1-f)^2`,

`f=x^2/(1+x^2)`.

This is exactly equivalent to

`K(x)=4 x^4/(1+x^2)^4`.

The original implementation first computed `f` using the authoritative 0105b bridge and then formed `1-f`. For `x >> 1`, `f -> 1` and the subtraction `1-f` loses significant digits by catastrophic cancellation. The asymmetry observed in CI is therefore a finite-precision implementation artifact, not a change in the physical kernel.

## Frozen correction

Do **not** loosen the symmetry tolerance and do **not** change the physical formula.

For the direct `mX,q` / `x=mX/q` range kernel, evaluate the same analytic expression in a reciprocal-stable form:

- for `x <= 1`: `K = 4 x^4/(1+x^2)^4`;
- for `x > 1`, let `y=1/x` and evaluate `K = 4 y^4/(1+y^2)^4`.

This preserves the exact reciprocal symmetry by construction while avoiding subtraction of nearly equal floating-point numbers.

`range_information_kernel_from_f(f)` remains the literal `4 f^2(1-f)^2` helper for callers that already possess a trustworthy `f`; its endpoint semantics are unchanged.

## Non-scientific-change guard

This amendment changes only numerical evaluation. It must not alter:

- the definition of `f`;
- the definition of `eta=ln(mX)`;
- the location or value of the maximum (`mX=q`, `K=1/4`);
- light/heavy fourth-power asymptotics;
- any preregistered tolerance;
- any observed-data or likelihood rule.

0105e remains NONDISCOVERY and consumes no observed event data.
