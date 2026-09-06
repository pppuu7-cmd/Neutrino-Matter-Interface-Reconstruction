# NMIR Literature / Constraint Ledger

Purpose: provenance ledger for formulas, experimental baselines, known enhancement mechanisms and exclusion gates. Entries are seeds, not a complete review.

## Electromagnetic neutrino properties

### Giunti, Kouzakov, Li, Studenikin (2024)
**Neutrino Electromagnetic Properties** — arXiv:2411.03122

Use in NMIR:
- general electromagnetic form factors;
- magnetic/electric moments, millicharge, effective charge radius;
- Dirac/Majorana distinctions;
- experimental-bound map.

Status: REVIEW/INPUT.

## CEvNS baseline and coherence

### Hoferichter, Menéndez, Schwenk (2020)
**Coherent elastic neutrino-nucleus scattering: EFT analysis and nuclear responses** — Phys. Rev. D 102, 074018.

Use in NMIR:
- EFT/nuclear-response organization;
- departure from ideal `Q_W^2` coherence;
- precision nuclear matching.

### Liao, Marfatia, Zhang (2024)
**Testing for coherence and nonstandard neutrino interactions in COHERENT data** — Phys. Rev. D 110, 055040.

Use in NMIR:
- empirical confirmation of neutron-number-squared coherent scaling in current COHERENT data;
- NSI constraint gate.

### Detailed nuclear structure calculations for CEvNS (2025)
Phys. Rev. D 111, 033003.

Use in NMIR:
- precision Standard-Model CEvNS baseline;
- nuclear-form-factor uncertainty budget.

### Reactor CEvNS / BSM constraints (2025)
Phys. Rev. D 112, 015007.

Use in NMIR:
- reactor-scale CEvNS constraints;
- weak mixing angle, electromagnetic-property, NSI and light-mediator constraint ledger.

## Condensed-matter / dynamic-response formalism

### Donchenko, Kouzakov, Studenikin (2021)
**Neutrino magnetic moments in low-energy neutrino scattering on condensed matter systems** — arXiv:2111.03331.

Use in NMIR:
- dynamic structure factor formalism;
- collective target effects in low-energy neutrino scattering;
- explicit superfluid-He benchmark.

Important caution: improved low-energy visibility or a spectral enhancement does not by itself imply a parametrically larger total neutrino opacity or useful energy capture.

### Raffelt & Seckel (1993)
**A Self-Consistent Approach to Neutral-Current Processes in Supernova Cores** — astro-ph/9312019.

Use in NMIR:
- separation of the weak probe from vector/axial medium structure functions;
- common response-function treatment of neutrino scattering, emission and absorption;
- production↔absorption duality in a many-body medium.

### Lykasov, Pethick, Schwenk (2008)
**Unified approach to structure factors and neutrino processes in nucleon matter** — arXiv:0808.0330.

Use in NMIR:
- density/spin response functions;
- scattering, pair bremsstrahlung and absorption from a common response formalism;
- many-body correlation gate.

### Shin, Rrapaj, Holt, Reddy (2023)
**Chiral EFT calculation of neutrino reactions in warm neutron-rich matter** — arXiv:2306.05280.

Use in NMIR:
- charged-current absorption from dynamical response functions;
- demonstration that correlations redistribute spectral strength and can enhance or suppress absorption depending on energy/channel.

## Production ↔ absorption / inverse weak reactions

### Tomalak, Liu, Li (2026)
**Theory of inverse beta decay for reactor antineutrinos** — Phys. Rev. D, accepted 15 June 2026.

Reaction:
`anti-nu_e + p -> e+ + n (+ gamma)`.

Use in NMIR:
- modern precision inverse-beta benchmark;
- explicit example that a beta-production amplitude has a measurable inverse absorption channel;
- recoil, weak magnetism, nucleon structure and radiative-correction requirements.

### Tomalak (2026)
**Radiative corrections to inverse beta decay: Precision analysis for reactor neutrinos** — Phys. Rev. Lett., accepted 27 May 2026.

Use in NMIR:
- precision normalization/uncertainty gate for inverse beta decay.

## Recoilless / resonant neutrino absorption

### Visscher (1959)
**Neutrino Detection by Resonance Absorption in Crystals at Low Temperatures** — Phys. Rev. 116, 1581.

Use in NMIR:
- historical direct realization of the production↔inverse-absorption idea;
- electron-capture source plus inverse resonant absorption;
- recoil-free crystal concept analogous to Mössbauer spectroscopy.

### Kells & Schiffer (1983)
**Possibility of observing recoilless resonant neutrino absorption** — Phys. Rev. C 28, 2162.

Use in NMIR:
- low-Q two-body electron-capture / bound-state-beta candidates;
- resonance-linewidth and recoilless-absorption design space.

### Potzel (2010)
**Mössbauer Antineutrinos: Recoilless Resonant Emission and Absorption of Electron Antineutrinos** — arXiv:1012.5000.

Use in NMIR:
- explicit failure modes of the H-3/He-3 realization;
- lattice expansion/contraction, phononless fraction and solid-state line broadening;
- Ho-163/Dy-163 alternative candidate.

Important caution: resonant peak enhancement is not equivalent to broadband opacity. Track integrated line strength and source/absorber spectral overlap.

## Electroweak resonance proof-of-principle

### IceCube Glashow-resonance observation (Nature result; IceCube data release 2021)
Reaction:
`anti-nu_e + e- -> W-` near 6.3 PeV.

Use in NMIR:
- empirical proof that a neutrino interaction cross section can become dramatically resonant at a precisely matched center-of-mass energy;
- high-energy proof-of-principle only, not a solar-neutrino energy-harvesting candidate.

## Working constraints / claims that require provenance before use

The following must **not** be used as paper claims until a primary source and convention are frozen:

- exact numerical laboratory/astrophysical limits on `mu_nu`, millicharge or charge radius;
- solar-neutrino component fluxes and spectra;
- supernova energy-loss/trapping bounds for any new mediator;
- stellar-cooling bounds;
- BBN/CMB bounds;
- material-specific dynamic structure factors;
- any claimed macroscopic coherence enhancement beyond nuclear CEvNS;
- any claimed resonant neutrino cross section unless the source/absorber linewidth, recoil-free fraction and integrated spectral strength are specified.

## Literature tasks

- [ ] Build a dated table of current magnetic-moment bounds by source and flavor assumption.
- [ ] Build a solar-neutrino spectral/flux input file with a frozen solar-model source.
- [x] Seed charged-current capture / inverse-beta literature.
- [x] Seed recoilless-resonant neutrino absorption literature and known failure modes.
- [ ] Build a machine-readable catalog of beta/electron-capture/bound-beta inverse transition candidates.
- [ ] Add polarized-matter / axial-potential literature.
- [ ] Add periodic-density / parametric-resonance literature.
- [ ] Add neutrino scattering in superconductors, superfluids, magnetic systems and semiconductors.
- [ ] Add sum-rule/no-go literature relevant to macroscopic coherent neutrino scattering.
- [ ] Build light-mediator exclusion surfaces in `(m_X, g_nu, g_m)` with source provenance.
