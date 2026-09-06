# NMIR iteration 0030 — full Model-S projected transparent-Sun lens

Date: 2026-09-06
Classification: **MODEL_S_ROBUSTNESS_PASS / G9 PARTIAL**

## Funnel target
Strengthen G9 gravitational focusing beyond the iteration-0029 rounded interior-point check by projecting a full independent solar density profile into the lens plane with no tuning to the published focal distance.

## Prospective contract
`research/gravity_modelS_prereg.md`, commit `a237aa336b52ba57bca57b5e289d4ca3505f4586`, frozen before implementation and before seeing the Model-S projected-lens result.

## External authority and frozen input
- Transparent-Sun target: Patla & Nemiroff, ApJ 685 (2008) 1297, arXiv:0711.4811; published minimum focal distance `23.5 +/- 0.1 AU` and rounded interior scale near `b=0.024 R_sun`, projected mass fraction `~0.0137`.
- Independent density robustness profile: Christensen-Dalsgaard et al. Model S (Science 272, 1286, 1996), pinned through RAMSES mirror commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`, file `patch/global_star/modelS/data/cptrho.l5bi.d.15c`, Git blob SHA `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`.
- Frozen external normalization: `R_model=6.96e10 cm`, `M_model=1.989e33 g`.

## Projection
For a spherical density profile,

`M_2D(<b) = integral_0^R 4*pi*r^2*rho(r)*f(b,r) dr`,

with shell-cylinder fraction

- `f=1` for `r<=b`,
- `f=1-sqrt(1-(b/r)^2)` for `r>b`.

For an ultrarelativistic ray,

`alpha(b)=4 G M_2D(<b)/(b c^2)`,

`F(b)=b/alpha=b^2 c^2/(4 G M_2D(<b))`.

Implementation: `src/nmir/gravity_extended.py`; tests `tests/test_gravity_extended.py`; hosted benchmark `scripts/gravity_modelS_benchmark.py`; workflow `.github/workflows/gravity-models.yml`.

## Hosted authority
- run `34041004727`
- job `101507632178`
- head `ea85975f083b24b6cdd47fd3209ff5dfe190c41a`
- artifact `9991661778`
- artifact ZIP SHA256 `77b56826ee622042b57cfd658d2d4596d93b7f5c6f87aacf5e9b6a0592258d60`
- dedicated tests: `9 passed`
- pinned external Git blob verified exactly in raw output.

## Raw result
| diagnostic | result | frozen gate |
|---|---:|---:|
| uniform-sphere max projected-mass rel. error | `2.9062e-6` | `<=2e-3` |
| integrated Model-S mass | `1.9890968238e33 g` | within 2% |
| integrated-mass rel. error | `4.86796e-5` | `<=0.02` |
| `M_2D(0.024R)/M_model` | `0.01311330481` | within 15% of 0.0137 |
| rel. error to 0.0137 | `0.0428245` | `<=0.15` |
| `F(0.024R)` | `24.07378082 AU` | within 7% of 23.5 AU |
| rel. error | `0.0244162` | `<=0.07` |
| minimum sampled `F` | **`23.62935116 AU`** | within 7% of 23.5 AU |
| minimum rel. error | **`0.00550430`** | `<=0.07` |
| sampled minimum `b/R` | `1e-4` | diagnostic |
| profile points | `2402` | diagnostic |
| status | **MODEL_S_ROBUSTNESS_PASS** | all gates pass |

## Scientific interpretation
The published ~23.5 AU transparent-Sun focal scale is robust to replacing the paper's exact 2005 solar model with the independent 1996 Model-S density profile. The full projected profile yields `23.629 AU`, only ~0.55% above the published minimum, without fitting the focal distance.

The fact that the sampled minimum occurs at the smallest frozen impact parameter is consistent with the central finite projected surface-density limit: `M_2D(<b) ~ pi Sigma(0)b^2`, so `F(b)` approaches a finite central value rather than diverging. The result therefore supports the physical reality of the transparent-Sun short focal scale and rejects an interpretation in which the `0.024 R_sun` rounded check alone generated the result.

## Critical scope
This is **not** yet a usable neutrino-energy gain:
1. The geometry is for a distant source whose neutrinos pass through the Sun. The Sun cannot act as this lens for its own outward solar-neutrino flux.
2. Finite-source magnification and receiver aperture have not yet been integrated through the extended solar lens mapping.
3. Liouville/surface-brightness conservation remains mandatory.
4. No gravitational gain is multiplied into the Li-7 or other solar-capture power ledger.

## Next G9 decision
Before spending substantial effort on a full magnification map, distinguish source classes:
- solar neutrinos: transparent-Sun self-lensing geometry is inapplicable;
- distant astrophysical neutrinos: G9 is physically applicable but must be ranked against their much smaller incident energy flux and finite source/alignment duty cycle;
- solar neutrinos lensed by another body: a separate lens geometry is required.

This source-class separation should precede any F9 composition.
