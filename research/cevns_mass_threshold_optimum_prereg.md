# Prospective contract — CEvNS coherence-vs-threshold inverse mass optimum

Date frozen: 2026-09-06
Gate: G2 / F3-F7
Purpose: derive and numerically validate a class-level design rule for the target nuclear mass that balances CEvNS weak-charge coherence against recoil-threshold phase-space loss. This is an analytic precursor to the full solar-spectrum real-isotope optimization.

## Frozen approximation/scope
- Monoenergetic neutrino energy `E_nu`.
- Nuclear mass `M=A m_u` with `m_u=931.49410242 MeV`.
- Low-energy heavy-target limit `E_nu << M` for the analytic derivation.
- Weak charge per nucleon treated as fixed, `Q_W=q A`, so at fixed target mass the number of nuclei scales as `1/A` and the zero-threshold CEvNS rate scales as `A`.
- Frozen ideal differential CEvNS shape `d sigma/dT ∝ M [1-MT/(2E_nu^2)]`.
- No nuclear form factor, abundance, chemistry, detector efficiency or real-isotope stability claim is made in this gate.

## Analytic hypothesis frozen before numerical scan
Define

`A_max = 2 E_nu^2/(m_u T_thr)`

as the heavy-target-limit mass number whose recoil endpoint just equals threshold.
For `0<A<A_max`, the above-threshold rate per fixed detector mass should scale as

`R(A) ∝ A (1-A/A_max)^2`.

The unique interior maximum is therefore

`A_star = A_max/3 = 2 E_nu^2/(3 m_u T_thr)`

and equivalently `T_max(A_star) ≈ 3 T_thr`.

## Frozen benchmark points
Use `E_nu=0.86258 MeV` as a representative dominant-Be7-line energy and thresholds `40,20,10 eV`.
Analytic expected `A_star` values are approximately `13.31`, `26.63`, `53.25`.
Also test `E_nu=0.420 MeV, T=10 eV` (pp endpoint control, expected `A_star≈12.62`) and `E_nu=1.44 MeV, T=40 eV` (pep control, expected `A_star≈37.10`).

## Prospective numerical validation
For each benchmark:
1. compute the analytic `A_star`;
2. scan the same ideal differential CEvNS formula using exact recoil endpoint `T_max=2E^2/(M+2E)` and `M=A m_u`, with `Q_W=qA`, over a fine positive A grid;
3. require the numerical optimum to agree with analytic `A_star` within 1% when `A_star>=5`;
4. require the numerical optimum to satisfy exact `T_max/T_thr` within 1% of 3 for the same benchmark;
5. verify the objective tends to zero at the kinematic closure and is positive below it.

## Classification
PASS establishes a design heuristic/envelope, not a real material recommendation. The next gate must replace continuous A and fixed `Q_W/A` by real nuclei and fold the full physical solar spectra at fixed kg and threshold.
FAIL means the proposed simple inverse rule is not reliable even inside its stated low-energy approximation and must not guide target selection.
