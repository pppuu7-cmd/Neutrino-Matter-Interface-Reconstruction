# Iteration 5 — Staggered-Layer Neutrino Metamaterial

Date: 2026-09-06 (Europe/Stockholm)

## User hypothesis

Construct many atomic layers with a lateral displacement from one layer to the next so that voids in one projected plane are covered by later planes. Test whether this can make a neutrino target effectively opaque or otherwise enhance capture.

## Immediate answer

The **materials geometry is physically realizable**. Ordinary close-packed crystals already use displaced ABAB (hcp) or ABCABC (fcc/ccp) planes, where atoms of the next plane occupy hollows of the previous one. Artificial multilayers can realize more general registries.

The **hard-sphere opacity interpretation is not valid for neutrinos**. Neutrinos do not need an open geometric channel between atomic electron clouds; their interaction probability is governed by weak/EM/BSM matrix elements and target response.

## New NMIR branch: SLNM

Staggered-Layer Neutrino Metamaterial (SLNM) asks whether layer registry can alter

\[
F(\mathbf q)=\sum_j e^{i\mathbf q\cdot\mathbf r_j}
\]

or the full dynamic response

\[
S_{ab}(\mathbf q,\omega)
\]

in a way that increases **flux-integrated interaction probability and deposited energy**, not merely a directional diffraction peak.

## Quantitative geometric sanity check

For one nucleus of radius `R_N` per square transverse cell of spacing `a`,

\[
f_{\rm geom}=\pi R_N^2/a^2.
\]

Using `R_N=5 fm`, `a=3 Angstrom`:

- `f_geom = 8.7266e-10` per layer;
- optimistic non-overlapping hard-disk layers for unity coverage: `~1.1459e9`.

This is only a geometric upper analogy. Actual MeV weak cross sections are vastly smaller than nuclear geometric cross sections, so projected coverage is not neutrino opacity.

## Structure-factor gate

For layer positions `(s_l, z_l)`:

\[
F(\mathbf q)=F_{\rm plane}(\mathbf q_\parallel)
\sum_l e^{i(\mathbf q_\parallel\cdot\mathbf s_l+q_z z_l)}.
\]

A staggered stack can therefore create constructive/destructive directions and move reciprocal-lattice peaks.

However, Aharonov, Avignone, Casher & Nussinov, Phys. Rev. Lett. 58, 1173 (1987), derive a Born-approximation sum rule for local crystal potentials in which the total force/effect scales linearly with the number of scatterers and no exotic total coherent enhancement occurs. Lipkin, Phys. Rev. Lett. 58, 1176 (1987), similarly emphasizes that N^2 coherent directional enhancements can be compensated by redistribution elsewhere.

A separate magnetic-neutrino crystal calculation (Augustin, Mueller & Greiner, Phys. Rev. D 41, 1683 (1990)) found a crystal enhancement scaling as `N^(1/3)` for a particular magnetic-scattering setup, but concluded it remained unobservable compared with ordinary weak interactions. This is a useful loophole/example to reproduce rather than assume that all registry effects are exactly zero.

## New promising variant

The strongest version is not a single-element shifted crystal, but a **multi-isotope staggered resonance stack**:

\[
A_1(Q_1),A_2(Q_2),\ldots,A_n(Q_n),
\]

with layer shifts, spacings, polarization and isotope choice optimized jointly. Different layers could overlap different solar-neutrino energies or different `(q,omega)` response sectors. This turns the design into a spectral-comb / response-engineering problem rather than a hard-sphere shadowing problem.

## Gates

| Gate | Test | Status |
|---|---|---|
| SL0 | Can staggered atomic planes exist? | PASS — AB/ABC stacking is ordinary solid-state physics |
| SL1 | Does staggering alone change incoherent optical depth at fixed mass column? | EXPECTED NO; formal test required |
| SL2 | Can registry produce large directional coherent gain? | YES in principle; toy `F(q)` code added |
| SL3 | Does angle/energy-integrated gain survive sum-rule constraints? | OPEN; prior literature strongly constrains |
| SL4 | Can solar-neutrino momenta match useful reciprocal-lattice/collective modes? | OPEN |
| SL5 | Can staggered multi-isotope layers increase flux-integrated capture/deposition? | OPEN — promoted variant |

## Code added

- `src/nmir/staggered_lattice.py`
- `tests/test_staggered_lattice.py`
- `theory/STAGGERED_LAYER_NEUTRINO_METAMATERIAL.md`

The toy code verifies both fully coherent and destructive-interference limits and includes the geometric nuclear-coverage sanity check.

## Next calculations

1. Convert solar-neutrino energies to accessible momentum-transfer ranges.
2. Compare those ranges with reciprocal-lattice scales `2pi/a` for Angstrom, nm, and moire superlattices.
3. Angularly integrate the toy structure factor and verify linear-N spectral-weight behavior for fixed scatterer count.
4. Add Debye-Waller disorder/temperature suppression.
5. Extend from elastic `F(q)` to an inelastic `S(q,omega)` stack.
6. Combine the staggered layer optimizer with the inverse-transition catalog: isotope per layer + shift + spacing + polarization.

## Scientific assessment

Naive projected atomic coverage: **very low promise for neutrino opacity**.

Registry/structure-factor engineering: **worth testing**.

Staggered multi-isotope resonant metamaterial: **high enough promise to retain as an NMIR branch**, especially when combined with the production↔absorption branch.
