# Preregistration 0092b-a2 — CCSN-MeV total interaction-envelope authority

Date frozen: 2026-09-08
Parent transmission gate: `research/prereg/0092b_g9_ccsn_mev_solar_transmission_authority.md`.
Validated composition parent: `research/iterations/0092b_a1_r3_model_s_composition_authority_pass.md`, record commit `684f8c47ea7b438fac3289665c6136340ffd05ef`.

## Question
Can a reproducible, MeV-valid Standard-Model interaction ledger provide a conservative upper bound on the *total removal/scattering optical depth* for every active CCSN neutrino/antineutrino flavor over `5–50 MeV` through the validated Model-S H/He/Z chord, without choosing a favorable metal mixture after seeing the result?

This is an authority/envelope gate. It must be completed before evaluating a terminal 0092b `tau_total`. No cross-section result selected after this prereg may change the frozen energy grid, composition columns or parent thresholds.

## Frozen parent columns
Use only the validated 0092b-a1 fine results:
- `Sigma_H = 1.5217827389419937e12 g cm^-2`;
- `Sigma_He = 1.3518482663979014e12 g cm^-2`;
- `Sigma_Z = 5.8857354950716446e10 g cm^-2`;
- `N_H = 9.16438985041013e35 H nuclei cm^-2`;
- `N_He = 2.035255134462346e35 He nuclei cm^-2`;
- total nucleon column remains `N_N = 1.7659857664161126e36 cm^-2`.

Do not recompute or retune composition in this gate.

## Frozen energy/flavor coverage
Exact sentinel energies: `E = {5, 10, 20, 30, 40, 50} MeV`.
The authority ledger must cover all active flavors and antiflavors relevant to a generic CCSN burst: `nu_e`, `anti-nu_e`, `nu_mu`, `anti-nu_mu`, `nu_tau`, `anti-nu_tau`.

A formula/table with a narrower valid energy range may not be extrapolated outside it. The terminal upper envelope at each energy is the maximum over the six frozen flavor states after summing non-double-counted removal channels for that flavor.

## Frozen primary/review authority hierarchy
Start from the cross-section review:
- J. A. Formaggio and G. P. Zeller, Rev. Mod. Phys. 84, 1307 (2012), arXiv:1305.7513, which explicitly covers coherent scattering, neutrino capture, inverse beta decay and low-energy nuclear interactions.

Channel-specific primary/review authority may supersede the review only when its formula/table and validity range are explicit and its source provenance is immutable. At minimum audit:
1. `anti-nu_e + p -> e+ + n` on H (IBD), using a MeV-valid Vogel-Beacom / Strumia-Vissani class authority rather than a DIS approximation;
2. neutrino-electron elastic scattering for all six flavor states;
3. CEvNS / coherent NC scattering on He and metals, with finite-size form factor set to `F(q)=1` when used as an upper bound;
4. incoherent NC/CC interactions on He/metals where they are not already dominated by a proved conservative envelope;
5. any free-nucleon CC/NC channel applicable to the actual H/He/Z target ledger.

## Frozen metal rule
0092b-a1 intentionally did not select a representative metal nucleus. 0092b-a2 therefore has only two admissible routes, chosen and documented before any terminal `tau` calculation:

A. obtain a reproducible Model-S-compatible radial elemental/isotopic metal distribution and freeze it prospectively; or

B. prove a composition-independent conservative metal upper envelope from the total validated `Sigma_Z`, using a prospectively fixed physically admissible nuclear domain and a cross-section inequality that dominates every included metal species/channel in that domain.

No solar photospheric mixture and no single representative O/Fe nucleus may be inserted after seeing the optical depth.

## Frozen formula/units requirements
Every accepted channel authority must record:
- reaction/target;
- formula or table interpolation rule;
- units;
- energy validity interval;
- flavor/antiflavor applicability;
- whether it is a central prediction, measured result, lower bound, or conservative upper bound;
- exact citation/URL and, for downloaded numerical/source assets, SHA256.

Use `1 GeV^-2 = 0.389379...e-27 cm^2` only if an analytical Fermi-theory formula is frozen with exact constants in the implementation.

## Frozen numerical classification
This subgate does **not** require the final total optical depth unless and until all channel/envelope authorities are complete.

- `PASS_G9_0092B_A2_MEV_INTERACTION_ENVELOPE_AUTHORITY` only if the six-flavor, 5–50 MeV total-removal upper envelope is fully specified with no unresolved target/channel gap and no double counting.
- `BLOCKED_G9_0092B_A2_METAL_ENVELOPE_AUTHORITY` if the unresolved metal mixture cannot be bounded conservatively under route A or B.
- `BLOCKED_G9_0092B_A2_NUCLEAR_CHANNEL_AUTHORITY` if He/metal CC/NC channels cannot be shown included or dominated by the frozen envelope.
- `BLOCKED_G9_0092B_A2_FLAVOR_COVERAGE` if any frozen flavor/antiflavor state lacks a valid upper envelope over the full interval.
- `INFRASTRUCTURE_FAIL_G9_0092B_A2` only for tool/download/execution failure.

A PASS authorizes a separate exact 0092b optical-depth calculation using the already frozen parent threshold `tau_total_upper <= 0.1`. A BLOCKED result may not be repaired by dropping the offending channel or choosing a favorable metal species.

## Guards
No DIS extrapolation to MeV. No detector cross section substituted for total solar-removal cross section. No post-result metal nucleus. No EM/source-morphology proxy. No detector/material/BSM gain multiplication. No changing the parent `0.1` thinness threshold.
