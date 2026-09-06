# Staggered-Layer Neutrino Metamaterial (SLNM)

## Motivation

Consider a material made from many atomic planes whose lateral registry is shifted from layer to layer so that, in geometric projection, voids in one plane are covered by atoms in later planes. Ordinary close-packed crystals already realize AB or ABC stacking; artificial epitaxial and moire multilayers generalize the idea.

The NMIR question is not whether such a projected covering can be drawn, but whether layer registry can increase the **neutrino interaction probability or deposited energy** relative to a target with the same mass column.

## Critical distinction: geometric opacity is not weak-interaction opacity

For photons, geometric/electronic opacity can correlate with projected atomic coverage. For MeV neutrinos, an atom is not a hard absorbing disk. In the dilute incoherent limit,

\[
\tau(E_\nu)=\sum_j n_j\sigma_j(E_\nu)L_j,
\]

so rearranging the same number of independent scatterers at fixed column density does not change the leading optical depth.

A staggered lattice can matter only through physics beyond independent-site counting, e.g.

1. coherent elastic interference;
2. inelastic collective modes;
3. engineered vector/axial response functions;
4. resonance matching to nuclear/atomic transitions;
5. externally driven nonequilibrium order.

## Elastic lattice amplitude

For identical scattering centers at positions `r_j`, the elastic amplitude contains

\[
F(\mathbf q)=\sum_{j=1}^{N}e^{i\mathbf q\cdot\mathbf r_j},
\qquad
I(\mathbf q)\propto |F(\mathbf q)|^2.
\]

For a stack of planes with spacing `d` and lateral shift `s_l`,

\[
F(\mathbf q)=F_{\rm plane}(\mathbf q_\parallel)
\sum_{l=0}^{N_L-1}
\exp\{i[\mathbf q_\parallel\cdot\mathbf s_l+q_zld]\}.
\]

Therefore layer shifts can move Bragg/coherent peaks, create destructive directions, or sharpen selected momentum transfers.

However, published sum-rule results for neutrino scattering from local crystal potentials in the Born approximation show that the total force/integrated effect is linear in the number of scatterers, despite coherent directional peaks. NMIR therefore treats any `N^2` directional enhancement as spectral/angular redistribution until an explicit loophole is demonstrated.

## A useful geometric sanity check

Suppose a lattice cell has transverse area `a^2` and one nucleus of radius `R_N`. A purely geometric projected nuclear covering estimate per layer is

\[
f_{\rm geom}\sim \pi R_N^2/a^2.
\]

For `R_N ~ 5 fm` and `a ~ 3 Angstrom`, this is only about `9e-10` per layer. But this is still vastly larger than the actual weak interaction probability: a typical MeV-scale weak cross section is many orders of magnitude below the nuclear geometric cross section. Thus even complete projected nuclear covering would not imply neutrino absorption.

## SLNM gates

### SL0 — realizability

AB/ABC and more complicated staggered registries are physically realizable. PASS in principle.

### SL1 — independent-site column-density gate

At fixed composition and mass column, simple staggering must reproduce the same incoherent optical depth. Any claimed gain must identify a coherent, resonant, or many-body term.

### SL2 — angular redistribution gate

Compute `|F(q)|^2` for aligned vs staggered stacks. Directional peaks are allowed, but the angle/energy-integrated strength must be checked against sum rules.

### SL3 — solar-neutrino kinematics gate

Evaluate whether the momentum transfers accessible for pp, Be-7, pep, B-8 and CNO solar neutrinos can match reciprocal-lattice vectors or collective-mode momenta of realizable structures.

### SL4 — inelastic/deposited-energy gate

Replace the static structure factor by `S_ab(q,w)` and ask whether the staggered registry moves spectral weight into channels with both enhanced rate and substantial `w/E_nu`.

### SL5 — resonance-stack gate

Test stacks in which successive layers contain different isotopes/transition energies. The goal is not geometric shadowing but a broad spectral comb that overlaps multiple solar-neutrino components.

## Most promising variant

A simple one-isotope shifted crystal is unlikely to increase total opacity parametrically. A more interesting NMIR design is a **staggered multi-isotope resonant stack**:

\[
\text{layer }1:A_1(Q_1),\quad
\text{layer }2:A_2(Q_2),\quad\ldots
\]

with registry, polarization and spacing jointly optimized so that different layers cover different regions of `(E_nu,q,w)` response space.

The inverse problem becomes

\[
\{s_l,d_l,A_l\}^*=\arg\max P_{\rm dep}
\]

subject to fixed total mass, stability, sum rules, nuclear transition data, and realistic fabrication constraints.

## Status

Branch opened in NMIR iteration 5. The naive hard-sphere opacity interpretation is not accepted; the structure-factor / multi-isotope / inelastic variants remain open.
