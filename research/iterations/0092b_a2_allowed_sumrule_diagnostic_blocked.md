# Iteration 0092b-a2 — allowed-sum-rule diagnostic; total MeV envelope remains BLOCKED

Date: 2026-09-08
Classification: `BLOCKED_G9_0092B_A2_NUCLEAR_CHANNEL_AUTHORITY`

## Frozen parent
Preregistration: `research/prereg/0092b_a2_mev_interaction_envelope_authority.md`, frozen commit `4d0736b9ce5c1a44a467d81d63f0767805a3af1c`.
Validated composition parent: `research/iterations/0092b_a1_r3_model_s_composition_authority_pass.md`, record commit `684f8c47ea7b438fac3289665c6136340ffd05ef`.

This record does **not** evaluate the terminal 0092b `tau_total` and does not change the frozen 5–50 MeV threshold. It audits whether the required authority envelope can currently be closed without a result-selected solar-metal choice.

## Frozen columns used for diagnostics only
- `Sigma_H = 1.5217827389419937e12 g cm^-2`;
- `Sigma_He = 1.3518482663979014e12 g cm^-2`;
- `Sigma_Z = 5.8857354950716446e10 g cm^-2`;
- `N_H = 9.16438985041013e35 cm^-2`;
- `N_He = 2.035255134462346e35 cm^-2`;
- `N_N = 1.7659857664161126e36 cm^-2`.

## Authority audit
The frozen review authority remains Formaggio & Zeller, *From eV to EeV: Neutrino Cross Sections Across Energy Scales*, arXiv:1305.7513 / Rev. Mod. Phys. 84, 1307, which covers coherent scattering, neutrino capture, inverse beta decay and low-energy nuclear interactions:
- https://arxiv.org/abs/1305.7513

For inverse beta decay on free hydrogen, Vogel & Beacom give the dedicated low-energy treatment valid for `E_nu <= ~60 MeV`:
- https://doi.org/10.1103/PhysRevD.60.053003

For low-energy nuclear scattering, MARLEY 1.2.0 documents the allowed approximation in terms of Fermi and Gamow-Teller operators that are sums over the `A` nucleons. The same paper explicitly warns that forbidden nuclear transitions become increasingly important approaching / above the tens-of-MeV regime and identifies inclusion of forbidden transitions as a missing component of the old treatment:
- https://doi.org/10.1016/j.cpc.2021.108123

The current MARLEY 2.0 release (2026-08-01) removes the old rough allowed-only treatment for the supported `nu_e + 40Ar` channel and includes HF-CRPA forbidden nuclear matrix elements:
- https://www.marleygen.org/news_posts/v2_release.html

The associated 2026 calculation for `nu_e + 40Ar` reports that forbidden transitions are required in the refined inclusive calculation, although at energies appreciably below 100 MeV they do not fully compensate the change in allowed strength relative to the old MARLEY model:
- https://arxiv.org/abs/2604.26801

This is useful evidence that the allowed approximation is not a complete all-target removal envelope at the upper end of the frozen CCSN range. It is not a universal bound for all H/He/solar-metal nuclei.

## Allowed-transition sum-rule diagnostic
This subsection is deliberately **non-terminal**. It quantifies how much room exists before the parent `tau=0.1` threshold, but it may not be promoted to the total-channel PASS.

In the allowed approximation the charged-current Fermi and Gamow-Teller operators have the schematic forms

`O_F = sum_{n=1}^A t_±(n)`

and

`O_GT = sum_{n=1}^A sigma(n) t_±(n)`.

By completeness and the operator-norm triangle inequality,

`sum_f B_F <= g_V^2 A^2`,

`sum_f B_GT <= 3 g_A^2 A^2`.

Using the standard low-energy prefactor gives the diagnostic all-allowed envelope

`sigma_allowed <= (G_F^2 E^2 / pi) * (g_V^2 + 3 g_A^2) * A^2`.

With `g_V=1`, `g_A=1.2756`,

`C_allowed = g_V^2 + 3 g_A^2 = 5.88146608`.

At the worst frozen endpoint `E=50 MeV`, with `G_F=1.1663788e-5 GeV^-2` and `1 GeV^-2 = 0.389379e-27 cm^2`,

`G_F^2 E^2 / pi = 4.215430137377298e-41 cm^2`.

For the **already composition-resolved H+He columns only**, the resulting diagnostic is

`tau_allowed_H+He <= 1.0345702243055577e-3`.

For the unresolved metal mass column, the algebraic relation for any chosen prospective nuclear domain is

`sum_j N_j A_j^2 <= A_max * Sigma_Z / m_u`.

If one merely illustrates the scale with `A_max=300`, the full H+He+metal allowed diagnostic would be

`tau_allowed_example(50 MeV) <= 3.670903980199914e-3`,

leaving a factor `~27.2` to the parent `0.1` threshold. **This A_max=300 illustration is not a frozen route-B authority and is not used for classification**, because the parent preregistration forbids selecting the metal domain after seeing the answer.

The diagnostic therefore says only that the allowed/coherent sector appears comfortably thin. It does not prove that the complete six-flavor removal probability is thin.

## Why the a2 PASS is not authorized
The frozen a2 contract requires every materially relevant low-energy channel to be included or dominated by a proved conservative envelope. Current recovered authority does not supply a single reproducible, composition-independent inequality that simultaneously dominates, for every physically admissible solar metal target over `5–50 MeV` and all six active flavor/antiflavor states:
- forbidden CC multipoles;
- forbidden/inelastic NC multipoles;
- Coulomb-enhanced final-state charged-lepton effects where relevant;
- target-specific nuclear thresholds and response strength;
- the unresolved full elemental/isotopic distribution inside `Sigma_Z`.

The 2026 MARLEY update strengthens rather than removes this concern: modern tens-of-MeV calculations explicitly restore forbidden nuclear responses and remain target-specific (`40Ar` in the cited implementation), so it cannot be promoted to a universal solar-metal upper envelope.

No post-hoc safety multiplier may be invented to bridge this authority gap. In particular, the `~27` allowed-sector margin does not authorize choosing an arbitrary factor smaller than 27 and calling the result a PASS.

## Classification
Under the preregistered taxonomy the present authority state is therefore

**`BLOCKED_G9_0092B_A2_NUCLEAR_CHANNEL_AUTHORITY`**.

The metal-mixture question remains coupled to the same blocker, but `NUCLEAR_CHANNEL_AUTHORITY` is the primary classification because even an exact elemental mixture would still require target-valid complete CC/NC response envelopes.

This is an external-authority blocker, not evidence that CCSN-MeV neutrinos are opaque. The available allowed-sector diagnostic strongly favors thinness, but terminal `PASS_G9_CCSN_MEV_SOLAR_TRANSMISSION_THIN` is not authorized.

## Next admissible repair
Only one of the following can repair this gate without weakening it:
1. a prospectively frozen set of target-specific complete 5–50 MeV CC+NC response authorities spanning the actual deep-solar elemental/isotopic mixture, plus electron/free-H channels; or
2. a prospectively derived and externally auditable operator/sum-rule inequality that provably dominates allowed **and forbidden** weak nuclear responses over an independently fixed physical nuclear domain, including charged-current Coulomb effects.

A convenient representative O/Fe nucleus, a photospheric metal mix, an allowed-only MARLEY table, or a post-result safety factor is forbidden.

## Consequence for 100% readiness
This record terminally identifies the present 0092b-a2 blocker but does not itself make the CCSN branch physically actionable. The remaining research-closure front is therefore: repair or retain this external-authority block under an explicit terminal policy, then separately close the already-known 0091 prospective CCSN alignment/actionability blocker.

No detector/material/BSM gain or neutrino-supplied power claim is authorized.
