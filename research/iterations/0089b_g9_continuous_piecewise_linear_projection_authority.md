# NMIR iteration 0089b — G9 continuous piecewise-linear projection authority

Date: 2026-09-08
Classification: **PASS_G9_CONTINUOUS_PIECEWISE_LINEAR_PROJECTION_AUTHORITY**
NMIR readiness after this iteration: **98%**.

## Scope
This iteration validates only an analytic projection of the same frozen continuously linearly interpolated Model-S density field. It removes the moving-point trapezoidal source-knot cusp mechanism that blocked 0089a. It does **not** certify turning roots, accepted areas, a multiimage kernel, finite-source effects, alignment duty cycle or persistent-source utility.

## Prospective authority
Scientific preregistration: `research/prereg/0089b_g9_continuous_piecewise_linear_projection_authority.md`, frozen commit `5d99cd6cd4d3a5f1f9defecfbd7f4036c93b8636`.

Implementation/reference-conformance amendments were frozen before their corresponding retries and did not modify scientific thresholds:
- V1 observability: `011fd76e317a61b725b86126a1308ebb61bf5d7a`;
- V1 mass theta-reference identity repair: `2300db976ba40d7d2bc7c4d87316baecc0162b38`;
- high-x derivative conformance diagnostic: `0460ed7026167db314959c51509b7b6a9fd04328`;
- endpoint-centered t-space production derivative stability repair: `a0ee082787ab15fab1a5677b40f5c3af501ee29a`.

Frozen scientific criteria remained:
- V1 independent 80-digit Model-S replica: mass relative error `<=1e-10`, derivative relative error `<=1e-9`;
- V2 all positive source knots: smallest-offset scaled derivative-continuity error `<=2e-5` plus the prospectively frozen convergence semantics;
- V3 continuous-vs-frozen-discrete compatibility on the frozen 3001-point grid: max symmetric relative mass and focal-distance differences each `<=0.005`.

## Provenance
- Model-S source commit: `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`.
- Model-S git blob SHA1: `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`.
- `R_sun = 6.96e10 cm` and the same physical constants/parser semantics as the frozen G9 chain.
- Production evaluator: `src/nmir/g9_continuous_projection.py` at hosted head `e4891230d6fcbdf379dbcda0571d6fc4ca90f5c3`.
- Production uses exact closed-form source-interval primitives and no numerical quadrature.

## Pre-PASS implementation diagnosis
The high-x diagnostic was separately validated before the final production repair:
- run/job `34212969375/102018040810`;
- artifact `10050562702`;
- artifact ZIP SHA256 `3ce57426e607ab3258381b9a653732d656a1b4f8b84e0f4ddc35ad1ffeb04fcc`;
- inner JSON SHA256 `74b235e0ac5160ef7538a11f85db99322a52b7a06cf2e67f454559aceb7cdf4b`;
- two independent 100-digit theta-space/t-space derivative references at `x=0.99999825` agreed to symmetric relative `3.08298265610274e-97`;
- the prior production formula missed them by `3.6792373931063796e-08` and had a diagnosed active-shell cancellation ratio `7784.261664298522`.

This authorized only the algebraically equivalent endpoint-centered t-space stability repair. No scientific tolerance changed.

## Authoritative hosted result
- run/job: **`34213225896 / 102018855558`**;
- hosted head: **`e4891230d6fcbdf379dbcda0571d6fc4ca90f5c3`**;
- dedicated regression suite: **`7 passed in 0.15s`**;
- artifact: **`10050706570`**, `nmir-g9-0089b-continuous-projection-authority`;
- independently downloaded artifact ZIP SHA256: **`2303e2c8280365e0d0e3f8b38364a2a7f45e911da5aad4d84cf9e4f6c9360ed9`**;
- independently extracted `g9_0089b_result.json` SHA256: **`e35ba20581d433daf9d85685a805fb85299f2ab58bda34987346928d4782070c`**.

Green CI was not used as scientific authority: the raw job log was read and the ZIP/inner JSON were independently hash-verified before this classification.

## Scientific results
### V0 — algebra/reference controls
- external-antiderivative max relative discrepancy: `2.0279853818144804e-81`;
- toy five-point derivative max relative discrepancy: `2.0506983119669857e-10`.

### V1 — independent high-precision Model-S authority
47 frozen points passed:
- max mass relative discrepancy: **`4.510003732611039e-13`** at `x=1e-4`, far below `1e-10`;
- max derivative relative discrepancy: **`6.5184329458976905e-12`** at `x=0.99999825`, far below `1e-9`.

### V2 — source-knot derivative continuity
All **2400** positive source knots passed. Maximum smallest-offset scaled error:

**`1.5255834512405636e-05`** at knot `x=0.0013911`, below the frozen `2e-5` criterion.

Thus the continuously projected piecewise-linear density does not inherit the derivative-undefined/source-knot orientation pathology of the moving-point trapezoidal map in the tested authority scope.

### V3 — compatibility with the previously frozen discrete map
On **3001** frozen grid points:
- max mass symmetric relative difference: **`0.004580294256676816`** at `x=1e-4`;
- max focal-distance symmetric relative difference: **`0.004580294256676684`** at `x=1e-4`;
- RMS mass difference: `0.0015515340692085458`;
- RMS focal-distance difference: `0.0015515340692085484`.

Both maxima remain below the prospectively frozen **0.005** compatibility ceiling.

## Interpretation
0089b establishes a reproducible continuous-map authority compatible with the inherited discrete map at the frozen 0.5% scale while eliminating its knot-derivative discontinuity mechanism. This is a numerical/model-representation result, not evidence for useful gravitational focusing by itself.

The PASS authorizes only a separately preregistered turning-root certification using this continuous map. No root count, root location, accepted area, focusing gain or persistent-source metric is inferred here.

## Next action
Prospectively freeze a root-certification-only gate for the accepted continuous map before evaluating any new signed-map derivative signs or root positions. Any later kernel/area calculation requires another post-root PASS preregistration.

BSM response/enhancement remains **LOCKED**.
