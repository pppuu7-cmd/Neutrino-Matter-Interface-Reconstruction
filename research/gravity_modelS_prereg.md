# NMIR G9 preregistration — full projected-mass Model-S lens

Date: 2026-09-06
Status: **PROSPECTIVE / FROZEN BEFORE IMPLEMENTATION**

## Question
Does a full radial solar density profile, projected into the lens plane without tuning to the published focal distance, reproduce the transparent-Sun ~23.5 AU focal scale and the quoted inner projected-mass scale?

This is an independent robustness check for G9. It does **not** yet assign a usable finite-source flux gain to any neutrino source and must not be composed with capture power.

## Frozen external authorities
1. Patla & Nemiroff, ApJ 685 (2008) 1297, arXiv:0711.4811: transparent-Sun minimum focal distance `23.5 +/- 0.1 AU`; rounded inner check near impact radius `0.024 R_sun` with enclosed/projected lens mass scale `0.0137 M_sun`.
2. Christensen-Dalsgaard et al., Science 272 (1996) 1286, Model S. Public Model-S limited-variable table is pinned through the RAMSES mirror:
   - repository: `ramses-organisation/ramses`
   - commit: `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`
   - path: `patch/global_star/modelS/data/cptrho.l5bi.d.15c`
   - Git blob SHA: `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`
   - columns used: `r/R`, `rho [g/cm^3]`.

Model S was calibrated to a photospheric radius about `6.96e10 cm`; this iteration freezes `R_model = 6.96e10 cm` and `M_model = 1.989e33 g` for the external normalization check.

## Frozen projection formula
For spherical density `rho(r)`, the mass inside a cylinder of projected radius `b` is

`M_2D(<b) = integral_0^R 4*pi*r^2*rho(r)*f(b,r) dr`,

where

- `f=1` for `r<=b`,
- `f=1-sqrt(1-(b/r)^2)` for `r>b`.

This is equivalent to integrating the surface density over the lens plane.

For an ultrarelativistic ray,

`alpha(b) = 4 G M_2D(<b)/(b c^2)`,

and the axis-crossing distance in the small-angle thin-lens control is

`F(b) = b/alpha = b^2 c^2/(4 G M_2D(<b))`.

## Frozen numerical procedure
- Parse all Model-S rows, sort by radius ascending, retain `0 <= r/R <= 1`.
- Integrate with trapezoidal quadrature on the native radial grid.
- Validate the projection implementation against the analytic uniform-sphere result
  `M_2D/M = 1-(1-(b/R)^2)^(3/2)`.
- Scan `b/R` on a combined logarithmic + linear grid covering `1e-4 ... 1`.
- Report total integrated mass, `M_2D(0.024R)/M_model`, `F(0.024R)`, minimum sampled `F`, and its impact parameter.

## Prospective gates
The result is **MODEL_S_ROBUSTNESS_PASS** only if all are true before looking at the result:
1. synthetic uniform-sphere projected-mass relative error <= `2e-3` over the test grid;
2. Model-S integrated mass is within `2%` of `1.989e33 g`;
3. `M_2D(0.024R)/M_model` is within `15%` of `0.0137`;
4. `F(0.024R)` is within `7%` of `23.5 AU`;
5. minimum sampled `F` lies within `7%` of `23.5 AU`.

If the full profile fails gates 3–5, that is a scientific discrepancy to diagnose; tolerances are not widened post hoc.

## Scope guards
- Model S (1996) is an independent solar-structure robustness model, not the exact BS05(OP) profile used by Patla & Nemiroff.
- Reproducing a focal scale does not prove a large finite-source magnification.
- The Sun cannot lens its own outward solar-neutrino flux in the distant-source geometry used here.
- Surface brightness is conserved; any total flux gain must come from image solid-angle/ray redistribution.
- No G9 gain enters the NMIR power ledger until an extended-source, receiver-integrated magnification is validated.
