# NMIR Recovery / Source-of-Truth State

Last reconciled: 2026-09-08
Repository: `pppuu7-cmd/Neutrino-Matter-Interface-Reconstruction`
Protocol: `research/RECOVERY_MANUAL.md`
Funnel: `research/NMIR_FUNNEL.md`
Latest completed immutable scientific record: `research/iterations/0092a_g9_cross_section_authority_mixed_blocked.md`, record commit **`975838ae5150e9e4295e3e902f1946d659492c93`**.
Current prospectively frozen scientific gate: `research/prereg/0092b_g9_ccsn_mev_solar_transmission_authority.md`, frozen commit **`66341d7eb7322e958a52dc30fb24d4e2b3e44647`**.
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
- CCSN 5–50 MeV: `BLOCKED_G9_0092A_MEV_TOTAL_CROSS_SECTION_AUTHORITY` because a conservative total optical-depth upper bound requires prospectively frozen chord composition + coherent/incoherent low-energy channel accounting. No DIS extrapolation or post-result composition choice is allowed.

Immutable note: `research/iterations/0092a_g9_cross_section_authority_mixed_blocked.md`, record commit `975838ae5150e9e4295e3e902f1946d659492c93`.

## Current frozen gate — 0092b CCSN-MeV solar transmission
Prereg commit `66341d7eb7322e958a52dc30fb24d4e2b3e44647`.

Question: can an authority-backed conservative total Standard-Model interaction optical-depth upper bound over the frozen `5–50 MeV` CCSN interval prove the exact Model-S reference chord thin (`tau_total<=0.1`)?

0092b freezes the validated 0092 density/column, requires a reproducible chord-composition authority or a prospectively derived composition-independent upper bound, and audits at minimum neutrino-electron scattering, NC nuclear/nucleon scattering, CC channels and CEvNS. High-energy DIS is forbidden. A photospheric composition may not be promoted to the deep chord composition.

PASS would establish only solar transmission compatibility for the CCSN-MeV ray; 0091's prospective alignment blocker would remain. BLOCKED may not be repaired by choosing a convenient abundance mix after seeing a result.

## BSM / B-L authority
0069 unlocks only the constraints ledger. BSM response/enhancement remains **LOCKED** pending reproducible external-envelope completeness + formal unlock. 0084b Shin-Yun and 0085 Wagner remain PASS. 0074a/0074b detector response benchmarks remain PASS; 0074c combined-likelihood numerical benchmark remains BLOCKED. 0087/0087a are partial topology authority only; 0087c Cerdeño, 0087d COHERENT mass support, 0087e finite-mass fifth-force, 0087f BBN tail and 0087g restricted-below-1-eV completeness remain BLOCKED.

## Exact next action
Do not reopen 0092a thresholds. Execute 0092b only after locating and freezing a reproducible deep-solar/chord composition authority or prospectively deriving a rigorous composition-independent upper bound, then freeze the low-energy channel/cross-section ledger before evaluating `tau_total`. Independently, a later exact 290-TeV TXS cross-section gate is allowed but lower priority because TXS remains named-source morphology BLOCKED in 0091.

## Critical guards
No raster/manual contour reading. No generic dark-photon contour promoted to B-L absent exact mapping. No Majorana/Dirac union/intersection. No T/L union. No finite-mass extrapolation of 0079a. No arbitrary Yukawa threshold. No Wagner statistical-combination claim. No COHERENT benchmark interpolation. No lowering blocked-family criteria. No blocked-family-as-null assumption. No BSM response scan before dedicated completeness PASS and formal unlock. No post-hoc promotion of failed/blocked G9 numerics. No result-selected G9 nodes/orders/intervals/tolerances. No EM/PSF source size promoted to physical neutrino morphology. No DIS extrapolation into MeV solar propagation. No claim that TeV opacity kills the CCSN MeV branch.
