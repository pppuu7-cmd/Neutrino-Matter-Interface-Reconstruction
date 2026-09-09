# 0105 — prior-art / novelty audit for NMIR v2 BSM residual reconstruction

Date: 2026-09-10
State: `NOVELTY_NARROWED_BEFORE_DATA_SCAN`
Parent: `research/prereg/0105_v2_model_agnostic_bsm_residual_reconstruction.md`

## Purpose

Prevent NMIR v2 from claiming novelty for ideas already established in the neutrino-NSI literature. This audit was performed before any 0105 result-dependent residual scan.

## Prior art that removes weak novelty claims

The following concepts are **not** novel NMIR claims:

1. **Using CEvNS to constrain neutrino NSI / light vector mediators.**
   - Liao & Marfatia, *COHERENT constraints on nonstandard neutrino interactions*, Phys. Lett. B 775 (2017) 54–57, DOI `10.1016/j.physletb.2017.10.046`, explicitly considered vector mediators lighter than ~50 MeV and related COHERENT constraints to effective matter-propagation NSI.
   - Denton, Farzan & Shoemaker, JHEP 07 (2018) 037, DOI `10.1007/JHEP07(2018)037`, analyzed arbitrary mediator mass after COHERENT and the relation to oscillation NSI/LMA-Dark.

2. **Combining oscillation and coherent-scattering information.**
   - Coloma, Esteban, Gonzalez-Garcia & Maltoni, JHEP 02 (2020) 023, performed a global fit to oscillation + COHERENT timing/energy data for neutral-current NSI.
   - Dutta et al., JHEP 09 (2020) 106, explicitly developed a global strategy combining scattering and oscillation information to break generalized NSI degeneracies.
   - Coloma et al., JHEP 08 (2023) 032, performed a broad global analysis of neutrino oscillation + CEvNS constraints with vector/axial interactions and multiple flavour coefficients.

3. **Model-independent/generalized matter potentials in IceCube DeepCore.**
   - IceCube Collaboration, Phys. Rev. D 104, 072006 (2021), constrained individual NSI couplings and a generalized matter-potential parametrization using three years of DeepCore data.

4. **The statement that finite-q CEvNS can distinguish light-mediator behavior from a heavy/contact limit.**
   This is established phenomenology, not an NMIR discovery.

Therefore the 0105b propagator bridge is a required correctness/reproducibility control, not itself a publication-level novelty claim.

## What remains potentially distinctive

A targeted literature search did not establish, by itself, that the following exact workflow has already been executed across the same public neutrino authorities:

`experiment-specific null reproduction`
`-> low-complexity data residual without choosing a BSM family from the observed shape`
`-> nuisance-orthogonal residual certification`
`-> microscopic operator identification across propagation and finite-q scattering`
`-> freeze operator + parameters + sign/shape/support prediction`
`-> validate on a genuinely held-out later neutrino dataset`.

This audit does **not** claim that no publication anywhere has elements of this workflow. It only means novelty cannot be assigned to ordinary NSI global fitting; the defensible NMIR target is the full prospective reconstruction/prediction architecture and, ultimately, any genuinely new residual/operator it discovers.

## Strong novelty guard

NMIR v2 must not advertise any of the following as the scientific jump:

- “first combination of oscillation and CEvNS”;
- “first mapping between matter NSI and scattering NSI”;
- “first light-mediator CEvNS test”;
- “first generalized matter-potential analysis”;
- “new interaction” merely because a multi-dataset BSM fit is better than a single-dataset fit.

A high-impact claim requires at least one of:

1. a statistically robust residual not explained by the authorized SM+nuisance model;
2. a previously unrecognized cross-experiment consistency relation or operator direction that survives existing global analyses and other laboratory/astrophysical constraints;
3. a prospective prediction that is later confirmed by an independent dataset;
4. a rigorous new no-go/identifiability theorem that changes how BSM neutrino interactions can be reconstructed.

## Immediate consequence for 0105

The research priority changes from “perform an IceCube+COHERENT light-mediator fit” to:

1. reproduce each experiment independently;
2. construct a residual statistic that is protected against nuisance-template directions;
3. test whether any surviving residual is common across regimes without choosing the operator from held-out data;
4. audit external constraints before promoting a surviving mediator region;
5. preserve future SBN / IceCube Upgrade / richer JUNO authority as prospective validation where possible.

Classification:

`PASS_0105_PRIOR_ART_AUDIT_NOVELTY_SCOPE_NARROWED_NONDISCOVERY`
