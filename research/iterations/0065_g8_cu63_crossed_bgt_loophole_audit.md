# NMIR iteration 0065 — 63Cu crossed-B(GT) RIOEC loophole audit

Date: 2026-09-07
Classification: **PASS_G8_CU63_PROVENANCE_REOPENED**

## Why this iteration exists
Iteration 0064 correctly froze the then-audited G8 state as `BLOCKED_ENTRANCE_STRENGTH`: the 2026 RIOEC candidate paper used a generic squared nuclear matrix element of 0.1 and the audited target set did not contain a complete exact-state entrance package.

After 0064 was recorded, a new independent authority was identified: Xin-Xu Wang et al., *Astrophys. J.* 984, 8 (2025), arXiv:2503.14835v2, explicitly calculated B(GT) for the exact crossed transition `63Ni*(87.2 keV, 5/2-) -> 63Cu(g.s., 3/2-)` using several shell-model Hamiltonians. 0064 remains immutable; 0065 prospectively tests whether this additional evidence is sufficient to reopen the 63Cu branch.

Prospective contract:
- `research/prereg/0065_g8_cu63_crossed_bgt_loophole_audit.md`
- prereg commit `3e52add9f3881f96b8409fb7474af564f114a395`.

Frozen evidence ledger:
- `data/g8_cu63_crossed_bgt_authority_0065.json`
- ledger commit `4d64aa7a95f1f794af303c467aa81fd9752fa2a2`.

## Independent target package
### Nuclear states and Q
- NNDC/ENSDF: `63Cu` ground state `Jpi=3/2-`.
- NNDC/ENSDF adopted `63Ni` first excited state: `E_x=87.220 keV`, `Jpi=5/2-`.
- NIST/ENSDF-backed direct beta-endpoint metrology: `63Ni -> 63Cu` beta-minus endpoint `Q_beta=66.945 +/- 0.004 keV`.
- Therefore for the inverse atomic-mass convention used by RIOEC, `Q_epsilon=M(63Cu)-M(63Ni)=-66.945 keV` at this precision level.

### Atomic daughter vacancy
NIST X-ray transition-energy authority places the Ni K edge around 8.33 keV. The frozen comparator value is `E_b=8331.486 eV`; the NIST search exposes multiple evaluated/measurement columns around 8.331--8.347 keV, so any precision fold must preserve this small source-column ambiguity rather than pretend a sub-eV atomic-mass reconstruction.

Independent reference-data calculations give a Ni K-vacancy natural width near `Gamma_K=1.39 eV` (recommended; HFR about 1.36 eV). The 87.2-keV nuclear level lifetime is about `1.61 us`, corresponding to a nuclear natural width only `~4.1e-10 eV`, so the atomic vacancy dominates the natural width by many orders of magnitude.

## Exact-state weak strength
Wang et al. explicitly state that beta-minus rates from the two low-lying excited states had not been measured and calculate the GT strengths in the large-scale shell model. For

`63Ni*(87.2 keV, 5/2-) -> 63Cu(g.s., 3/2-)`

they report:
- SM fpd6pn: `B(GT)=3.56e-3`;
- SM GXPF1J: `1.90e-3`;
- SM jun45: `4.48e-2`;
- prior SM fpd6npn: `6.83e-3`.

This is an independently evaluated exact-state weak normalization, not the generic `|M|^2=0.1` used for preliminary ranking in the 2026 RIOEC proposal.

Under the standard definition

`B(GT;i->f)=|<f||sigma tau||i>|^2/(2J_i+1)`,

the crossed/reverse strength obeys

`B_reverse=[(2J_Ni+1)/(2J_Cu+1)] B_forward=(6/4) B_forward`.

Therefore the admissible model envelope for the inverse nuclear transition is

`B_reverse = 2.85e-3 ... 6.72e-2`,

a factor `23.58` spread. This spread is a mandatory theory uncertainty; it may not be optimized away.

## Independent resonance reconstruction
Using only the independent inputs above,

`E_R = -Q_epsilon + E_x + E_b`

becomes

`E_R = 66.945 + 87.220 + 8.331486 = 162.496486 keV`.

The 2026 RIOEC proposal independently quotes `162.5(6) keV` for the 63Cu candidate. The agreement is essentially exact at the relevant precision and is a successful out-of-sample consistency check because the quoted RIOEC resonance was comparator-only, not an input.

## F10 result
**PASS_G8_CU63_PROVENANCE_REOPENED.**

The strict 0065 package criteria are satisfied: exact states, Q, daughter K-vacancy energy/width and an independently calculated exact crossed weak strength are all recoverable. The target-strength part of the 0064 blocker is therefore no longer absolute for `63Cu`; 0064 remains a correct record of the narrower evidence audit available at that iteration.

This PASS does **not** claim useful thermal-solar event rates. The `63Cu` resonance is at 162.5 keV, far above the ~eV-keV thermal-solar spectral maximum, so spectral overlap may be catastrophically small. That is now the next quantitative gate.

## Next gate
Prospectively materialize or recompute the Standard-Model thermal-solar electron-antineutrino differential spectrum through the high-energy tail needed at `E_R≈162.5 keV`, then fold it with the full `B_reverse=2.85e-3...6.72e-2` model envelope and the target atomic factors. If the primary spectrum authority is not valid/recoverable at 162.5 keV, classify the numerical branch `BLOCKED_HIGH_ENERGY_TAIL` rather than extrapolate a plotted spectrum. If recoverable, calculate events/kg/s and the neutrino-supplied deposited-power ceiling with all external/stored energy excluded.

## Readiness
A previously blocked exact-state F4 target package has been reopened with new independent evidence. `NMIR_READINESS` advances provisionally from 87% to **88%**, subject to recovery/funnel reconciliation.
