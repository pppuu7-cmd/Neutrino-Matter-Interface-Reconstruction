# G9 preregistration — transparent-Sun finite-source focusing

Date: 2026-09-06

## Funnel scope
F0 directional concentration / incident-flux enhancement, not microscopic absorption. F1 gravitational focusing. F3-F6 require extended transparent lens benchmark, finite source regularization, and Liouville/surface-brightness discipline before any F9 multiplication with capture.

## Frozen prospective gates
1. Reproduce the published transparent-Sun minimum focal-distance scale `23.5 +/- 0.1 AU` using the Patla–Nemiroff 2008 quoted critical interior point `b=0.024 R_sun`, projected enclosed mass `M_b=0.0137 M_sun`. Because those rounded inputs are quoted only to 2–3 significant figures, PASS tolerance is frozen at <=3% relative to 23.5 AU.
2. Implement an exactly finite on-axis uniform-disk point-lens control: `mu_fs(rho)=sqrt(rho^2+4)/rho`, `rho=theta_source/theta_E`. This is a finite-source/Liouville control, not a substitute for the extended-Sun caustic map.
3. Verify numerically that disk averaging of the point-source magnification agrees with the analytic finite-source result to <=1e-5 relative error.
4. Verify surface-brightness conservation explicitly: lensed flux gain equals image solid-angle gain; no intrinsic brightness gain is credited.
5. Do not compose any focusing gain with Li-7 or other capture W/kg until the source geometry and extended-lens magnification are physically specified.

## Authority
Primary benchmark: Patla & Nemiroff, ApJ 685 (2008) 1297, arXiv:0711.4811. Their paper reports `23.5 +/- 0.1 AU` and gives the independent rounded check `0.0137 M_sun` within `0.024 R_sun` -> approximately 23.5 AU.
