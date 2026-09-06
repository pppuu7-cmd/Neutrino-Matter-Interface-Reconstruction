# NMIR iteration 0034 — staggered-layer / fixed-column theorem gate

Date: 2026-09-06
Classification: **G10_GEOMETRY_ONLY_STRONG_NEGATIVE / FIXED_COLUMN_MIXTURE_THEOREM_PASS**

## Prospective contract
`research/structured_column_prereg.md`, commit `868d71658cbbc41a6582136f9d88ae40c108fbe2`.

## Question
Can a material whose successive atomic layers are transversely staggered so that projected geometric holes disappear increase total neutrino capture at fixed material column, assuming the layering itself does not change the microscopic weak cross sections?

## T1 — exact layer-order/offset invariance
For independent passive events,

`tau_j(E)=Ncol_j sigma_j(E)`,

`S(E)=product_j exp(-tau_j)=exp(-sum_j tau_j)`,

hence

`A(E)=1-exp(-sum_j tau_j)`.

The result contains no layer-order or transverse-offset variable. Permutation regression tests pass to machine precision.

## T2 — fixed-mass mixture theorem
For mass fractions `w_i>=0`, `sum w_i=1`, and `kappa_i=sigma_i/m_i`,

`tau/Sigma_mass = sum_i w_i kappa_i <= max_i kappa_i`.

Therefore a passive isotope mixture/layering at fixed mass column cannot beat the best pure component once the microscopic cross sections are fixed. Random-mixture regression tests satisfy the bound.

## T3 — tilt cannot increase total captured power of a fixed slab
For `c=cos(theta)`, the projected beam-intercept area falls as `c`, while optical depth grows as `tau/c`:

`C(c)=c[1-exp(-tau/c)]`.

Hosted scans over `tau=1e-12...100` and `c=1e-4...1` confirm

`C(c)<=C(1)`.

The thin limit approaches angular invariance; at finite optical depth tilt is worse for total captured power.

## T4 — projected atomic coverage stress
To avoid understating the idea, use an absurdly generous microscopic weak cross section:
- A=300, Z_f=119, E_nu=20 MeV operator-norm allowed cross section;
- multiply by the frozen finite-q factor 128;
- multiply by the iteration-0033 full one-body subleading amplitude stress `(1+r_1b)^2`.

Result:
- allowed operator-norm sigma = `2.3002005233545382e-35 cm^2`;
- finite-q stressed sigma = `2.944256669893809e-33 cm^2`;
- one-body-subleading stressed sigma = `2.4740960790061117e-32 cm^2`;
- effective interaction radius = `8.87428442927202e-19 m`;
- ideal square lattice spacing = `2 Angstrom`, cell area `4.0e-16 cm^2`;
- optical depth per ideal dense atomic layer = `6.185240197515279e-17`;
- layers needed for `tau~1` = `1.61675208733481e16`;
- corresponding idealized thickness = `3.2335041747e6 m` (~3234 km).

This is not a realistic absorber design; it is a deliberate stress test showing that optical-style geometric coverage of atoms is unrelated to neutrino opacity even after using a vastly overgenerous weak cross section.

## Hosted validation
Workflow run `34043114890`, job `101513298058`, artifact `9992278460`.
Raw log inspected:
- `6 passed in 0.04s`;
- benchmark emitted the values above;
- workflow conclusion SUCCESS.

## Scientific scope
This theorem closes only geometry-only rearrangement at fixed microscopic response. It does NOT close any structure that changes `sigma(E,q)` itself through:
- coherent many-body response;
- a real nuclear/atomic resonance;
- polarization/spin response;
- active pumping;
- BSM operators.

Density/spin coherent energy-gain claims must still pass the already-closed sum-rule gates; resonance and active/BSM mechanisms remain their own funnel branches.

## Conclusion
The staggered-layer idea is physically realizable as a geometry, but eliminating ordinary line-of-sight atomic gaps does not create neutrino opacity. For independent weak interactions, capture is controlled by integrated interaction column, not visual/projected atomic coverage.
