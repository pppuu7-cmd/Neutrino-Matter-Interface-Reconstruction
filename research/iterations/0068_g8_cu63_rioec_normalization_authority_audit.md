# NMIR iteration 0068 — Cu63 RIOEC primary normalization/materialization audit

Date: 2026-09-07
Prospective contract: `research/prereg/0068_g8_cu63_rioec_normalization_contract.md`, commit `44abb5844e6bbcd358fd224052cf7bce92f2e881`.

## Classification
**`BLOCKED_RIOEC_NORMALIZATION_AUTHORITY`**.

This is an authority/materialization blocker, not a physical no-go and not a rate result.

## Recovery / duplication check
Mandatory recovery order was completed before new work: `RECOVERY_MANUAL.md` -> `RECOVERY.md` -> `NMIR_FUNNEL.md` -> iteration 0067 -> prereg 0068 -> recent commits -> relevant Actions. No scientific commits existed after the 0067 reconciliation. Baseline run `34084448539`, job `101625696458`, was newly terminal SUCCESS but is infrastructure evidence only and was not used as a scientific PASS.

## Primary authority audit
Primary authority: E. Akhmedov, T. Lasserre, L. Maturi, *Resonant Induced Orbital Electron Capture: Novel method for low-energy anti-nu_e detection*, arXiv:2608.25001v1 (submitted 2026-08-25).

The primary record directly establishes the physical channel-level statements required to keep RIOEC meaningful: the reaction is resonant, and for continuous-spectrum sources the effective response is governed by the spectral intensity of the electron-antineutrino flux at the resonance.

However, under the frozen 0068 acceptance rule the following exact implementation package must be independently materialized from primary authority before any Cu63 rate is computed:

1. continuous-spectrum cross-section/rate normalization;
2. line-shape convention and normalization;
3. exact `B(GT)`/nuclear-strength to entrance-strength mapping;
4. K-shell electron-wavefunction/atomic factor and normalization;
5. spin/statistical factors;
6. constants and unit chain to a rate per target atom;
7. target-number conversion to events/(kg s).

In this audit the accessible primary full formula chain could not be recovered in a form sufficient for an independent dimensionally unambiguous implementation. In particular, the exact normalization coefficient multiplying the resonant line, its atomic/spin factors, and the `B(GT)` mapping were not materialized from the primary source.

A secondary review exposes a Breit-Wigner-like expression and a continuous-source relation proportional to `B0 S(E_R)`. The prospective contract explicitly forbids using secondary summaries to fill any missing primary normalization factor, so that information is retained only as a non-authoritative cross-check and is not used numerically.

Machine-readable authority ledger: `data/g8_rioec_normalization_authority_0068.json`, commit `dfe1b11538079a7cb76c7c1aedba0c8c366ff50d`.

## Frozen inherited inputs intentionally not folded
- channel: `63Cu(g.s.,3/2-) + anti-nu_e + e_K -> 63Ni*(87.220 keV,5/2-)`;
- `E_R = 162.496486 keV`;
- `B_reverse = 2.85e-3 ... 6.72e-2`;
- 0067 source tail: `dPhi_anti-nu_e/dE(E_R) = 3.528363521736758e-41 cm^-2 s^-1 MeV^-1`.

No events/(kg s), events/(kg day), or W/kg are reported because doing so would require inserting an unmaterialized normalization factor after the source-tail result is already known.

## Interpretation
Iteration 0067 removed the source-spectrum blocker. Iteration 0068 shows that the remaining Cu63 RIOEC chain is now **primary-normalization-authority blocked** under NMIR's reproducibility standard. This does not establish that the physical rate is zero or small; it establishes that the rate cannot be claimed reproducibly from the presently materialized primary authority without guessing or importing secondary normalization factors.

This changes the BSM-unlock architecture relative to iteration 0066: the G8 branch is no longer an immediately actionable numerical SM calculation under the frozen rules. The formal unlock criterion must therefore be re-audited prospectively rather than silently changing BSM status.

## Next gate
Prospectively re-run the formal BSM unlock-readiness audit using the unchanged 0066 criteria, with G8 now classified `BLOCKED_NOT_ACTIONABLE` at primary normalization authority. Preserve:
- G3 absolute short-range/contact-current coefficient residual as explicitly OPEN but without a presently identified coefficient-independent theorem route;
- G2 same-configuration sub-keV measured rejection x bulk-NR acceptance as public-achievement blocked;
- G9 10-kpc CCSN solar-lens utility as strong-negative.

If and only if the unchanged unlock criteria pass, BSM may move to `UNLOCKED_FOR_CONSTRAINT_LEDGER_ONLY`; no enhancement scan is authorized.

## Readiness
0068 is a reproducible blocker classification, not closure of the physical G8 rate. `NMIR_READINESS` remains **89%**.
