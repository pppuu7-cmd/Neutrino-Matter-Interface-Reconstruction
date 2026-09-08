# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-08
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Protocol: `research/RECOVERY_MANUAL.md`
Funnel: `research/NMIR_FUNNEL.md`
Latest completed immutable scientific record: `research/iterations/0092b_a1_r3_model_s_composition_authority_pass.md`, record commit **`684f8c47ea7b438fac3289665c6136340ffd05ef`**.
Current prospectively frozen scientific gate: `research/prereg/0092b_a2_mev_interaction_envelope_authority.md`, frozen commit **`4d0736b9ce5c1a44a467d81d63f0767805a3af1c`**.
`NMIR_READINESS: 98%`.

## Mandatory recovery rule
Read `RECOVERY_MANUAL.md` -> this file -> `NMIR_FUNNEL.md` -> newest numbered iterations/preregs/amendments -> commits newer than this reconciliation -> relevant queued/in-progress/newly-terminal Actions. Repository + independently validated Actions artifacts are authority. Green workflow status alone is never scientific PASS.

## Frozen mission / accounting
Keep focusing/state control, microscopic interaction probability, detector visibility/amplification and irreversible neutrino-supplied deposited energy separate. Event gain != interaction gain != neutrino-energy gain. Stored/pump/preparation/reset energy is not neutrino-supplied power. Never multiply unvalidated gains.

## Stable non-BSM frontiers
- G2: 0063 `BLOCKED_NOT_ACTIONABLE` pending same-configuration measured sub-keV rejection x bulk-NR acceptance.
- G3: 0065 universal short-range/contact coefficient `OPEN_NOT_CURRENTLY_ACTIONABLE`.
- G8: 0068 `BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`.

## G9 authority chain — current front
Historical numerical failures/blocks remain immutable and are not retroactively promoted: 0075/0077/0089a/0089d/0090/0090a/0090b remain their recorded BLOCKED/FAIL classes. The independent successful path is:

- 0089b `PASS_G9_CONTINUOUS_PIECEWISE_LINEAR_PROJECTION_AUTHORITY`.
- 0089c `PASS_G9_CONTINUOUS_MAP_TURNING_ROOT_CERTIFICATION`.
- 0089e-r2 `PASS_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`.
- 0090c `PASS_G9_SOURCE_CENTRIC_EXACT_MEASURE_AUTHORITY`.
- 0090e-r1 `PASS_G9_RAY_CENTRIC_DUAL_DISK_SENTINEL_AUTHORITY`.
- 0090f **`PASS_G9_FULL_GRID_FINITE_NONZERO_SURVIVORS`**.
- 0091 **`BLOCKED_G9_REAL_SOURCE_AUTHORITY`**.
- 0092 **`PASS_G9_0092_MODEL_S_COLUMN_AUTHORITY`**.
- 0092a **`BLOCKED_G9_0092A_CROSS_SECTION_AUTHORITY_MIXED`**, containing a source-regime `SCIENTIFIC_FAIL_G9_TRANSPARENT_SUN_ASSUMPTION` at the 1.5-TeV NGC-1068 endpoint.
- 0092b-a1-r3 **`PASS_G9_0092B_MODEL_S_COMPOSITION_AUTHORITY`**.

### 0090f validated full-grid finite-source PASS
Prereg `fc277e3695ebeb2628d133b9385e7d7d2e12a5d5`; execution head `f0f2a857b9fb5dbeecdd7abe4788f0e826516025`; run/job `34270367643/102211319629`; artifact `10073678384`; ZIP SHA256 `1f55ba0d1c041d8711e12b63b02aaa6be820359f62c2541e2bd59b99532b8ff0`; inner JSON SHA256 `71831e971932c2d347e2f79c4c315c839ae853b2968d75545bb6a3b97ead6083`.

Frozen grid: 3 observers x 3 receiver radii x 25 source angular radii x 6 offsets = 1350 rows. All 1125 nonzero-offset rows satisfy the preregistered finite-nonzero survivor condition `theta>0`, `delta>0`, `mu>=2`. Global `mu_min=157.28015230029052`, `mu_max=2852164397.158548`. This is an abstract Model-S finite-source numerical survivor result only; no named-source realizability, duty cycle, detector/material gain or neutrino-power claim follows.

### 0091 named-source realizability BLOCKED
Prereg `4bf6979684c287e65a2f37b5ef0e092a787698a0`; immutable record `8bc8898f2193e9a4059b35f1ede3bf5597ca504a`; classification `BLOCKED_G9_REAL_SOURCE_AUTHORITY`.

Frozen candidates:
- NGC 1068: `BLOCKED_G9_NAMED_SOURCE_NEUTRINO_MORPHOLOGY_AUTHORITY`; observed neutrino source evidence exists, but no direct authoritative physical neutrino-emitting angular radius/centroid tight enough for the 0090f map without an EM/model proxy.
- TXS 0506+056: same morphology-authority blocker; also episodic.
- generic Galactic CCSN at 10 kpc: neutrinosphere angular size lies inside 0090f theta support, but the generic future event lacks a prospectively fixed sky direction tied to the <=100-m source-plane offset support; `BLOCKED_G9_NAMED_SOURCE_ALIGNMENT_AUTHORITY`.

0091 is not a physical no-go. It exposed solar-matter transmission as a separate compatibility gate.

### 0092 validated Model-S solar-column PASS
Parent prereg `29ad32defe3d18983bb26f6e1e58005bc3d95e9e`; execution head `cf2093e46acd2770bdead2963a8444d5cb4f4d71`; run/job `34274667136/102224608870`; artifact `10075203769`.

Official Christensen-Dalsgaard Model-S file was fetched directly during hosted execution. Exact file SHA256 `65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc`. Independent artifact validation: ZIP SHA256 `21037786abe3cd62d9b6baf1ee2a4414c5dc9d5de92ca12cf26eef9a33e2d396`; inner JSON SHA256 `23fe3a1d43b4483225c30184e818e16beb61e3fe3c02b847152fcb623a7f24e9`.

For the frozen `b/Rsun=0.024` ray:
- `Sigma = 2.9324883602905845e12 g cm^-2`;
- `N_N = 1.7659857664161126e36 cm^-2`;
- coarse/fine relative difference `3.2685418524731032e-12` vs frozen `1e-4` requirement;
- linear-vs-log-rho sensitivity `2.5699089258994556e-6`.

Classification `PASS_G9_0092_MODEL_S_COLUMN_AUTHORITY`. This validates the solar chord column only, not transmission at any energy.

Immutable note: `research/iterations/0092_g9_model_s_solar_column_authority_pass.md`, record commit `dab1a5c0ea08c4d2dcbcdc53947027b9d18be21c`.

### 0092a validated mixed cross-section/transmission result
Prereg `c6820c20ad96ea189d5bb15439f5155bbdeaaf82`; execution head `b8396e9f1440cbb80e9ee8e664e61fde00615603`; run/job `34276868882/102231933804`; artifact `10076044489`; dedicated tests `2 passed`.

Independent artifact validation:
- ZIP SHA256 `8b7fa8fc988327de2a4242edcb04a273fc9bbf939967d99ca7ea233194218557`;
- inner `g9_0092a_cross_section_authority.json` SHA256 `ead1e74ae32410b0bcf307632606b2f77cbabd10d056ab5cd311068d56227bfe`.

Frozen direct high-energy authority: FASER nu_mu charged-current coefficient `(0.5 +/- 0.2)e-38 cm^2 GeV^-1` over 520–1760 GeV. The preregistered conservative central-minus-1sigma sentinel at 1.5 TeV is `0.3e-38 cm^2 GeV^-1`, hence

`sigma_CC_lower = 4.5e-36 cm^2`,

`tau_CC_lower = N_N*sigma = 7.946935948872507`,

`T0 <= exp(-tau) = 3.5374439669189366e-4`.

Therefore the exact NGC-1068 low-end source/ray regime is **`SCIENTIFIC_FAIL_G9_TRANSPARENT_SUN_ASSUMPTION`** even under this conservative CC-only lower sentinel. This invalidates the transparent/unattenuated-Sun approximation for that 1.5-TeV reference ray; it does not invalidate gravitational focusing geometry generally.

The overall 0092a gate remains mixed BLOCKED:
- NGC 1068 1.5 TeV: scientific transparent-Sun FAIL;
- TXS 290 TeV: `BLOCKED_G9_0092A_HIGH_ENERGY_AUTHORITY` pending an exact numerical cross-section authority under the frozen contract;
- CCSN 5–50 MeV: initially `BLOCKED_G9_0092A_MEV_TOTAL_CROSS_SECTION_AUTHORITY` pending chord composition + complete low-energy interaction accounting.

### 0092b-a1 validated Model-S composition PASS
Parent prereg `66341d7eb7322e958a52dc30fb24d4e2b3e44647`; prospective composition amendment `8e7466013f0e978be9c036ec9ca10f4aa005cb66`.

Two earlier hosted candidates are immutable infrastructure failures only:
- r1 `34277408907/102233717306`: blank-record header parser assumption;
- r2 `34277513371/102234063162`: whitespace parser incompatible with official fixed-width `1p5e16.9` format.

Neither produced a scientific composition result and neither altered the gate.

Authoritative r3 execution head `e1c2e584f7d5b80ce00f7b8c34c2c8011573e5a8`; run/job `34277614693/102234398138`; artifact `10076333882`; dedicated tests `3 passed`.

Independent validation:
- artifact ZIP SHA256 `bf9a7dcdfab0bf05d7ca936c61bba54f2cd39841cd380316bf4a421da71aa4ec`;
- result JSON SHA256 `1edda4508f0ce73ffc025adce7c0a867c301cd301a8e65a0509ac75d70df2291`;
- limited Model-S SHA256 `65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc`;
- extensive GONG Model-S SHA256 `a30c31b9f6af2e5918f49d3808c0dade54f9946133b679b86949fc73625c2393`;
- official GONG format PDF SHA256 `9614e18f6eed3f7121352539651c502ae84b7b13bb308b091a66157b45a597b5`.

Official GONG header is `nn=2482, iconst=15, ivar=25, ivers=210`. Under the prospectively frozen official-format semantics, `var(6)=X`, `var(17)=Z` for v210, and `Y=1-X-Z`. The validated 0092 limited file remains density authority; GONG supplies composition fractions only.

At `b/Rsun=0.024`: `X=0.35554806874807887`, `Y=0.6241438995900526`, `Z=0.02030803166186854`.

Fine component columns:
- `Sigma_H=1.5217827389419937e12 g cm^-2`, `N_H=9.16438985041013e35 cm^-2`;
- `Sigma_He=1.3518482663979014e12 g cm^-2`, `N_He=2.035255134462346e35 cm^-2`;
- `Sigma_Z=5.8857354950716446e10 g cm^-2`.

Component sum `2.9324883602906113e12 g cm^-2` closes to the independent 0092 total with relative error `9.157911456241502e-15`. Coarse/fine discrepancies are `1.287e-11`, `7.508e-12`, `2.913e-12` for H/He/Z, all far below the frozen `1e-4` gate.

Classification **`PASS_G9_0092B_MODEL_S_COMPOSITION_AUTHORITY`**. This closes deep-solar H/He/Z chord composition authority only. No representative metal nucleus was chosen and no 5–50 MeV total optical depth has yet been certified.

Immutable record: `research/iterations/0092b_a1_r3_model_s_composition_authority_pass.md`, commit `684f8c47ea7b438fac3289665c6136340ffd05ef`.

## Current frozen gate — 0092b-a2 MeV interaction-envelope authority
Prereg commit `4d0736b9ce5c1a44a467d81d63f0767805a3af1c`.

The remaining 0092b blocker is no longer deep-solar composition. The new gate freezes exact energies `{5,10,20,30,40,50} MeV`, all six active neutrino/antineutrino flavor states, and requires a non-double-counted total-removal upper envelope covering at minimum IBD on H where applicable, neutrino-electron scattering, CEvNS/coherent NC, and relevant incoherent CC/NC nuclear interactions.

The unresolved metal mixture must be handled prospectively either by a Model-S-compatible elemental/isotopic radial distribution or by a proved composition-independent conservative metal envelope based only on the validated `Sigma_Z`. No representative O/Fe nucleus may be selected post-result. Formaggio-Zeller is the review anchor; MeV-valid channel-specific primary authority may supersede it. High-energy DIS remains forbidden.

A 0092b-a2 PASS authorizes a separate terminal optical-depth calculation under the already frozen parent thinness criterion `tau_total_upper<=0.1`; it does not itself establish transmission thinness.

## BSM / B-L authority
0069 unlocks only the constraints ledger. BSM response/enhancement remains **LOCKED** pending reproducible external-envelope completeness + formal unlock. 0084b Shin-Yun and 0085 Wagner remain PASS. 0074a/0074b detector response benchmarks remain PASS; 0074c combined-likelihood numerical benchmark remains BLOCKED. 0087/0087a are partial topology authority only; 0087c Cerdeño, 0087d COHERENT mass support, 0087e finite-mass fifth-force, 0087f BBN tail and 0087g restricted-below-1-eV completeness remain BLOCKED.

## Exact next action
Do not recompute composition and do not reopen 0092a. Execute 0092b-a2 as an authority ledger first: freeze MeV-valid formulas/tables, flavor applicability and exact provenance; resolve the metal-mixture upper-envelope issue prospectively; only after a reproducible `PASS_G9_0092B_A2_MEV_INTERACTION_ENVELOPE_AUTHORITY` may a separate terminal 0092b optical-depth calculation evaluate the pre-existing `tau_total_upper<=0.1` criterion.

A separate exact 290-TeV TXS cross-section gate remains allowed but lower priority because TXS is already named-source morphology BLOCKED in 0091.

## Critical guards
No raster/manual contour reading. No generic dark-photon contour promoted to B-L absent exact mapping. No Majorana/Dirac union/intersection. No T/L union. No finite-mass extrapolation of 0079a. No arbitrary Yukawa threshold. No Wagner statistical-combination claim. No COHERENT benchmark interpolation. No lowering blocked-family criteria. No blocked-family-as-null assumption. No BSM response scan before dedicated completeness PASS and formal unlock. No post-hoc promotion of failed/blocked G9 numerics. No result-selected G9 nodes/orders/intervals/tolerances. No EM/PSF source size promoted to physical neutrino morphology. No DIS extrapolation into MeV solar propagation. No photospheric abundance promoted to the deep solar chord. No post-result representative metal nucleus. No claim that TeV opacity kills the CCSN MeV branch.
