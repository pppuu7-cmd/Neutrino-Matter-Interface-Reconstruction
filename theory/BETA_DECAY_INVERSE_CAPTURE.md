# NMIR — Reconstructing Neutrino Capture from Beta-Decay Data

## Key result

For an unpolarized nuclear transition, neutrino capture on a beta-decaying nucleus and the corresponding beta decay probe the same invariant weak matrix element. This gives NMIR a practical data-driven route: use measured beta-decay observables to infer inverse neutrino-capture strength instead of relying only on uncertain nuclear many-body calculations.

Consider a beta-decaying target `N` with

\[
\nu_e+N\to N'+e^-
\]

(or the charge-conjugate antineutrino/positron case). For a nucleus that already beta decays spontaneously, this capture can be thresholdless with respect to the incoming neutrino kinetic energy.

In the long-wavelength regime `p_nu R << 1`, the capture rate has the schematic form

\[
\sigma_{\rm NCB}v_\nu
=\frac{G_\beta^2}{\pi}
 p_eE_eF(Z,E_e)C_\nu(E_e,p_\nu),
\]

while the corresponding beta-decay rate contains the same nuclear shape factor in the crossed kinematic domain.

The measured comparative half-life gives

\[
ft_{1/2}=\frac{2\pi^3\ln2}{G_\beta^2\,\overline C_\beta}.
\]

Combining the two yields

\[
\sigma_{\rm NCB}v_\nu
=2\pi^2\ln2\,p_eE_eF(Z,E_e)
\frac{C_\nu(E_e,p_\nu)}{ft_{1/2}\,\overline C_\beta}.
\]

For superallowed/allowed cases in which the shape factor is effectively energy independent, this simplifies to

\[
\boxed{
\sigma_{\rm NCB}v_\nu
=2\pi^2\ln2\,
\frac{p_eE_eF(Z,E_e)}{ft_{1/2}}
}
\]

in the natural-unit convention of the source derivation.

## Why this is important for NMIR

This is close to the user's proposed algebraic intuition:

`known production process -> measured decay strength -> infer inverse capture`.

The crucial point is that the weak matrix element is not guessed. It is constrained by an observed decay lifetime / `ft` value.

## Search strategy

Construct a catalog of beta-decaying nuclei and rank candidates by:

1. low `ft` / large transition strength;
2. favorable Q value for the available neutrino spectrum;
3. allowed or superallowed transition class;
4. stable or manageable daughter state;
5. large outgoing charged-particle energy deposition;
6. target abundance / density / chemical realizability;
7. manageable radioactive self-background;
8. possible narrow two-body or bound-beta resonance when relevant.

For solar neutrinos, compute

\[
R_i/N_T=\int dE_\nu\,\Phi_i(E_\nu)\,\sigma_i(E_\nu),
\]

and deposited power

\[
P_i/N_T=\int dE_\nu\,\Phi_i(E_\nu)\,\sigma_i(E_\nu)E_{\rm dep}(E_\nu).
\]

A candidate may be excellent by event rate and poor by deposited power, or vice versa.

## Immediate normalization targets

1. Tritium / He-3 capture as a classic low-Q allowed case.
2. Free inverse beta decay on the proton as an independent precision benchmark (different threshold structure, but same production/inverse philosophy).
3. Historical Cl-37 solar-neutrino capture as a benchmark against established radiochemical calculations.
4. Ga capture as another low-energy solar benchmark.
5. Heavy beta-decaying candidates studied for relic-neutrino capture, noting that forbidden transitions may break the simple half-life↔capture mapping and require spectral-shape information.

## Strong caution

The simplified formula above is **not** to be used as a ready SI cross-section formula without an explicit unit/convention conversion and Coulomb/nuclear corrections. NMIR will implement it only after reproducing at least one published numerical benchmark exactly.

## Scientific opportunity

If this catalog can be automated, NMIR can scan thousands of known weak nuclear transitions using experimental decay data and ask an inverse-design question:

\[
\boxed{\text{Which known transition is intrinsically closest to a neutrino absorber?}}
\]

Only after that baseline is exhausted should engineered linewidths, polarization, lattice effects or BSM operators be invoked.
