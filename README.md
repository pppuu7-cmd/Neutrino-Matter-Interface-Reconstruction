# NMIR — Neutrino–Matter Interface Reconstruction

NMIR is a model-agnostic research program for reconstructing and optimizing the physical interface between neutrinos and organized matter.

## Central question

> What is the strongest neutrino↔matter coupling, energy-transfer channel, or state-control mechanism allowed by known physics and current observations, and what additional microphysics would be required to exceed it?

NMIR does **not** assume that a useful neutrino absorber exists. A rigorous no-go/upper-bound result is an acceptable scientific outcome.

## Core decomposition

We separate three physically different tasks:

1. **State control** — flavor/spin conversion without necessarily depositing energy.
2. **Scattering/detection** — producing an observable recoil or excitation.
3. **Energy capture** — irreversible/inelastic deposition of a non-negligible fraction of the incident neutrino energy.

A mechanism is never promoted from (1) or (2) to (3) without an explicit energy-transfer calculation.

## Model-independent interface

At low energy, candidate microscopic couplings are mapped onto medium response functions,

\[
\Gamma_\nu \sim \int d^3q\,d\omega\; L_{ab}(q,\omega)\,S^{ab}(q,\omega),
\]

where the leptonic tensor/operator kernel `L_ab` contains the neutrino interaction and `S_ab` (or equivalently the retarded susceptibility `chi_ab`) contains the many-body material physics.

The inverse problem is

\[
S_{\rm target}(q,\omega)=\arg\max_{S\in\mathcal A}\; P_{\rm dep}[S]
\]

subject to causality, unitarity, sum rules, conservation laws, material stability, and laboratory/astrophysical/cosmological constraints.

## Initial operator basis

NMIR begins with:

- Standard Model charged-current and neutral-current weak interactions;
- coherent elastic neutrino–nucleus scattering (CEvNS);
- electron scattering;
- neutrino magnetic/electric dipole moments and electromagnetic form factors;
- matter potentials and spin-polarized media;
- general low-energy non-standard interactions (NSI);
- light scalar/vector/tensor mediator hypotheses only after the Standard-Model ceiling is quantified.

## First research gates

- **G0 — normalization/reproducibility:** reproduce standard weak-interaction scales and known limiting formulas.
- **G1 — static-coherence gate:** determine what ordinary nuclear/material coherence can and cannot enhance.
- **G2 — response-function gate:** derive energy deposition in terms of density, spin, current, phonon/magnon/quasiparticle response.
- **G3 — Standard-Model ceiling:** maximize solar-neutrino deposited power over physically admissible passive media.
- **G4 — engineered-medium scan:** polarization, periodic media, resonances, superconductors, magnetic systems, low-threshold collective modes.
- **G5 — BSM residual:** identify what coupling structure would be required if the SM ceiling is parametrically too small.
- **G6 — global consistency:** confront any BSM region with CEvNS, electron recoil, oscillations, stellar cooling, supernova, BBN/CMB and other applicable bounds.

## Non-negotiable scientific rules

- Repository state, equations, scripts and generated results are authoritative; chat text is not.
- Distinguish amplitude coherence from total-rate enhancement.
- Distinguish lower threshold from larger total cross section.
- Distinguish elastic momentum transfer from useful energy absorption.
- Do not infer a new energy source: neutrinos carry an incident energy flux; NMIR studies possible coupling/capture of that flux.
- Negative gates and no-go results are retained, not hidden.
- Any numerical claim intended for a paper must have a script, inputs, units, assumptions and a reproducibility test.

## Current status

**2026-09-06 — Iteration 0 / program initialization.**

Research maturity estimate: **~5%**. The problem has been defined, but the operator inventory, response taxonomy, constraint database and benchmark calculations are only beginning.

See `research/RECOVERY.md` for the source-of-truth research state and `research/ROADMAP.md` for the staged program.
