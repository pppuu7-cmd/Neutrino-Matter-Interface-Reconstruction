# 0102 NSI parameter-authority and medium-transfer audit

Date: 2026-09-10
Status: RESEARCH NOTE — DOES NOT CREATE A TERMINAL PARAMETER LOCK
Benchmark: `NMIR-BENCHMARK-0102`
Parent preregistration: `research/prereg/0102_known_model_benchmark_nsi_preflight.md`

## Question

What external NSI parameter authority can be used in the stellar NMIR propagation problem without silently transferring an Earth-effective matter coefficient into a medium with a different neutron/electron composition?

## Frozen NMIR interface

The already-preregistered 0102 propagation term is

`A_CC [diag(1,0,0) + epsilon]`

with dimensionless Hermitian `epsilon`, and the source profile inherited from 0100 supplies the stellar `rho(r), Ye(r)` pair.

The terminal question is therefore not merely whether a published NSI interval exists. The authority must also specify what charged-fermion current the coefficient multiplies so that the effective matter coefficient in the stellar medium is defined.

## Finding 1 — IceCube confirms the Hamiltonian convention, but its epsilon^Earth is medium-effective

Relevant publication:
- IceCube Collaboration, *All-flavor constraints on nonstandard neutrino interactions and generalized matter potential with three years of IceCube DeepCore data*, Phys. Rev. D 104, 072006 (2021).
- DOI: `10.1103/PhysRevD.104.072006`.

IceCube writes the matter Hamiltonian in the same conventional form used by NMIR: an ordinary charged-current electron term plus a Hermitian NSI matrix multiplying `V_CC = sqrt(2) G_F N_e`. It also subtracts the common `epsilon_mumu I` component because an identity contribution does not affect oscillation probabilities. This is an independent convention cross-check for the 0102 mathematical preflight.

However, its reported coefficients are effective Earth-matter quantities. In the notation used there,

`epsilon^Earth_ab ≈ epsilon^e_ab + epsilon^p_ab + Y_n^Earth epsilon^n_ab`.

Equivalently in the up/down-quark basis,

`epsilon^Earth_ab = epsilon^e_ab + (2+Y_n^Earth) epsilon^u_ab + (1+2Y_n^Earth) epsilon^d_ab`.

Therefore an `epsilon^Earth` numerical value cannot be inserted unchanged into a stellar profile unless the underlying electron/proton/neutron or electron/up/down couplings are specified and the stellar composition mapping is performed.

**Decision:** IceCube is excellent convention and Earth-effective cross-check authority, but it is not by itself a composition-transferable terminal authority for a stellar NMIR run.

## Finding 2 — fundamental charged-fermion NSI removes the ambiguity

Primary candidate publication:
- Pilar Coloma, M. C. Gonzalez-Garcia, Michele Maltoni, João Paulo Pinheiro, Salvador Urrea, *Global constraints on non-standard neutrino interactions with quarks and electrons*, JHEP 08 (2023) 032.
- DOI: `10.1007/JHEP08(2023)032`.
- arXiv: `2305.07698`.

This analysis parameterizes neutral-current NSI at the charged-fermion level and combines oscillation and CEvNS information. For vector interactions in electrically neutral matter, the propagation coefficient is

`epsilon_eff_ab(r) = epsilon^{e,V}_ab + [2+Y_n(r)] epsilon^{u,V}_ab + [1+2Y_n(r)] epsilon^{d,V}_ab`,

where `Y_n(r)=N_n(r)/N_e(r)`.

This equation exposes the medium-transfer requirement explicitly.

## Finding 3 — electron-only vector NSI is the cleanest terminal branch for the existing NMIR source authority

For an electron-only vector interaction,

`epsilon^{u,V} = epsilon^{d,V} = 0`,

so

`epsilon_eff_ab(r) = epsilon^{e,V}_ab`.

The NSI matrix is then independent of `Y_n(r)` and multiplies the already-authorized electron-density potential `V_CC(r) = sqrt(2) G_F N_e(r)`. This maps directly onto the frozen 0102 `A_CC * epsilon` implementation without inferring a new stellar neutron profile.

This is a stronger interface match than importing Earth-effective coefficients.

**Recommended 0102 terminal model class:** contact/heavy-mediator, electron-only, vector neutral-current NSI, with real coefficients unless a separately pinned authority and preregistration expands the phase convention.

## Published electron-vector authority ranges

For the global oscillation analysis including NSI effects in neutrino-electron elastic scattering, Coloma et al. report the following 90% CL, 1-d.o.f., two-sided marginalized intervals for vector NSI with electrons, after marginalizing over all other NSI and oscillation parameters:

| coefficient | 90% CL marginalized interval |
|---|---:|
| `epsilon^{e,V}_ee` | `[-0.13, +0.10]` |
| `epsilon^{e,V}_mumu` | `[-0.20, +0.10]` |
| `epsilon^{e,V}_tautau` | `[-0.17, +0.093]` |
| `epsilon^{e,V}_emu` | `[-0.097, +0.011]` |
| `epsilon^{e,V}_etau` | `[-0.18, +0.080]` |
| `epsilon^{e,V}_mutau` | `[-0.0063, +0.016]` |

The publication states that this branch applies to interactions induced by mediators with masses of order `>= 10 MeV`, i.e. the contact-like regime relevant to a conventional propagation potential.

### Statistical guard

These values are **one-dimensional marginalized intervals**, not a six-dimensional joint confidence box.

It is prohibited to take arbitrary endpoints from these six rows, form one simultaneous epsilon matrix, and call that point or hyper-rectangle a 90% CL region. Such a construction would destroy the correlation/profile-likelihood semantics that the NMIR funnel is specifically designed to preserve.

The intervals may presently be used only as:
- axis-wise authority information;
- sanity/scale checks;
- prospectively declared one-parameter stress tests if explicitly labelled non-joint.

They are not yet sufficient for `research/locks/0102_nsi_parameter_terminal_lock.json`.

## Why the IceCube generalized-matter best fit is not used as the stellar terminal point

The 2021 IceCube generalized matter-potential analysis reports a simultaneous best-fit in its Earth-effective epsilon basis. That is attractive statistically because it avoids combining unrelated one-dimensional intervals. But the numerical coefficients already include the composition weighting appropriate to Earth.

Using that same matrix in the stellar `rho(r),Ye(r)` profile would implicitly assume that the star has the same charged-fermion composition mapping as Earth. The NMIR source contract does not authorize that assumption.

Therefore the Earth-effective GMP best fit remains a cross-check, not the terminal stellar fixture.

## Required terminal-authority routes

A legitimate 0102 terminal lock can be created by any one of the following prospectively completed routes.

### Route A — released joint likelihood/profile in the electron-only vector basis

Preferred. Pin a public immutable likelihood, profile grid, chain, or equivalent object from which a reproducible electron-only vector point/region can be selected while preserving correlations.

### Route B — published/reproducible simultaneous best fit in the electron-only vector basis

Acceptable for a benchmark fixture if the exact operator convention, coefficient values, analysis branch, and provenance are immutable and no confidence-region claim beyond the published result is fabricated.

### Route C — one-operator-at-a-time benchmark

If no transferable joint object is public, amend/preregister 0102 before terminal execution to test a finite set of one-operator electron-vector slices. Each slice must set all other NSI coefficients exactly to zero and use an authority actually valid under that one-operator condition, rather than a marginalized interval derived while other operators floated.

A one-at-a-time endpoint stress test based only on marginalized intervals may still be useful, but must remain explicitly non-statistical and cannot close PARAMETER_AUTHORITY as a confidence-region claim.

## Current decision

Terminal status remains

`BLOCKED_0102_NSI_PARAMETER_AUTHORITY_UNPINNED`.

No physics failure is inferred. The audit has reduced the problem to a sharper requirement:

> The 0102 authority must be specified at the charged-fermion/operator level or be proven composition-transferable to the stellar medium. Earth-effective epsilon values alone are insufficient.

## Methodological consequence for future custom NMIR models

Add a general **MEDIUM_TRANSFER_AUTHORITY** question to any future matter-coupled model:

1. Is the fitted parameter fundamental/operator-level or already effective for a particular medium?
2. If effective, what density/composition ratios were absorbed into it?
3. Does the target environment supply those same ratios from a pinned source model?
4. If not, can the coefficient be unfolded to operator-level couplings without introducing an unpinned assumption?

A model that passes mathematical consistency but fails this transfer check is `BLOCKED` on authority; it is not automatically scientifically false.

## Next deterministic task

Search for a public joint/profile-likelihood or reproducible best-fit object for the 2023 electron-vector NSI analysis. If none exists, identify a published one-operator electron-vector authority suitable for prospective Route C and freeze its exact operator convention before any terminal 0102 computation.
