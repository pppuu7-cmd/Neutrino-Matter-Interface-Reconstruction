# NMIR iteration 0071 — gauge-complete U(1)_{B-L} primary constraints ledger

Date: 2026-09-07
Prospective contract: `research/prereg/0071_b_minus_l_primary_constraints_contract.md`, frozen commit `80d93debb2a20e35d6e06fa3000591f82ffbd1a8`.
Machine-readable ledger: `data/b_minus_l_primary_constraints_0071.json`, commit `70a282743c9b9b0d6c1ab495ee45eed61e2f0e99`.

## Classification
**`BLOCKED_B_MINUS_L_PRIMARY_CONTOUR_MATERIALIZATION`**.

This is not a physics exclusion of gauged B-L and not permission for an NMIR BSM response scan. It means the frozen 0071 acceptance condition — a reproducible allowed/excluded region over `1e-6 eV <= m_V <= 10 GeV` with all applicable primary constraint families represented in one `(m_V,g_BL)` convention — cannot yet be satisfied without an additional reproducible contour-materialization step.

## Recovery and CI check
Recovery order was followed before new work. Repository reconciliation head was `8ab17f7574509baa96723755a44ae890305f6058`; no newer commit existed before this iteration. Baseline CI run `34092808036` had newly reached `completed/success`, but this is infrastructure evidence only and was not used as scientific PASS evidence.

## Primary-family audit
The mandatory families are all represented by relevant B-L authority:

1. **CEvNS / low-energy neutrino scattering:** Cadeddu et al., JHEP 01 (2021) 116, arXiv:2008.05022, explicitly analyze universal, B-L and L_mu-L_tau vector models using COHERENT CsI and Ar and derive B-L mass-coupling constraints.
2. **Neutrino-electron / direct detection:** De Romeri, Papoulias and Ternes, JHEP 05 (2024) 165, arXiv:2402.05506, derive anomaly-free B-L limits from solar-neutrino electron recoils in XENONnT, LZ and PandaX-4T.
3. **Collider:** Queiroz et al., Phys. Rev. D 111, 095021 (2025), arXiv:2501.00610, explicitly show how B-L dilepton limits depend on invisible branching fraction. Their quoted TeV-scale mass limits are outside the frozen 0071 upper mass of 10 GeV, so they are not silently transported into the audited interval.
4. **Stellar/SN:** Hong, Shin and Yun, Phys. Rev. D 103, 123031 (2021), arXiv:2012.05427, derive young-neutron-star cooling constraints for a B-L gauge boson, with approximately `g/e' <~ 1e-13` below O(0.1 MeV) under their cooling assumptions. Cerdeno et al., arXiv:2106.11660, provide B-L SN1987A diffusion-time constraints including medium effects and explicitly discuss their model/simulation dependence.
5. **Cosmology:** Esseili and Kribs, JCAP 05 (2024) 110, arXiv:2308.07955, calculate BBN/CMB `Delta N_eff` constraints for gauged B-L over roughly 1 eV–100 MeV, with right-handed-neutrino/anomaly-cancellation and Dirac/Majorana assumptions stated.
6. **Fifth force / long range:** Fayet, Phys. Rev. D 99, 055043 (2019), with the related MICROSCOPE B-L analysis arXiv:1712.00856, provides long-range B-L force limits. These are naturally reported in long-range-force/epsilon conventions, so a conversion to the exact 0071 `g_BL` convention must be frozen rather than guessed.

## Why the gate blocks
The scientific issue is now data materialization rather than model naming. Several dominant primary constraints are published as curves in mass-coupling figures without a common machine-readable table. The 0071 prereg explicitly forbids reading numerical values by eye from an uncalibrated plot. Combining such curves anyway would make the apparent surviving B-L region non-reproducible and would allow hidden convention errors near contour crossings.

The correct next operation is therefore not an enhancement calculation and not a manual plot trace. It is a new prospective contour-materialization gate that freezes one of three admissible routes per source: author-provided numerical table/code; calibrated vector-path extraction from publication PDF/XML/SVG; or independent likelihood reproduction under the exact published B-L convention.

## Scientific consequence
All five required constraint families exist in primary literature, so 0071 does **not** fail for lack of external constraints. But the global allowed region has not yet been frozen numerically. Therefore:

- `PASS_B_MINUS_L_CONSTRAINT_LEDGER_FROZEN` is not granted;
- `SCIENTIFIC_FAIL_B_MINUS_L_NO_SURVIVING_REGION` is not granted;
- BSM remains `UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY`;
- no NMIR B-L response/enhancement scan is allowed.

## Exact next gate
Prospectively freeze iteration 0072: reproducible B-L contour materialization. Prioritize the constraints that can control the `1e-6 eV–10 GeV` interval: long-range/fifth-force at the low-mass end, cosmology/stellar in the eV–MeV region, and low-energy neutrino/direct-detection constraints in the keV–GeV region. Recover numerical tables/code first; otherwise use calibrated vector extraction or independent likelihood reproduction. Only after a global numerical allowed region is immutable may a B-L response bound be opened.

## Readiness
No readiness increase. 0071 identifies the exact external-data blocker but does not yet bound the surviving B-L response.
