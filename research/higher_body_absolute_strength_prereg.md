# NMIR prereg — empirical/EFT absolute-strength stress envelope for genuine higher-body SM currents

Date: 2026-09-06
Status: prospective; frozen before implementation/result inspection.

## Question
After iteration 0047 closed free superextensive scaling for bounded finite-range k-local currents, can the *absolute amplitude* of genuine two-/higher-body Standard-Model nuclear currents plausibly bridge the remaining passive-solar deposited-power gap?

This is NOT a universal operator-norm theorem. It is an evidence-anchored stress envelope using primary weak-transition data and chiral-EFT authorities, with deliberately large multiplicative safety factors.

## Frozen baseline
Use the iteration-0026 leading finite-q passive envelope

`P_leading = 1.2056895107775174e-9 W/kg`

and iteration-0033 conservative omitted one-body amplitude ratio

`r_1b = 1.8988146448649366`.

All amplitudes below are normalized to the same leading-current amplitude used in 0026/0033. Total stress power is

`P_stress(r_2b) = P_leading * (1 + r_1b + r_2b)^2`.

No resonance, gravity, detector avalanche, structure, BSM or daughter-energy gain may be multiplied into this gate.

## Primary empirical anchors frozen before calculation
1. King et al., Phys. Rev. C 102, 025501 (2020), DOI 10.1103/PhysRevC.102.025501: two-body axial-current contributions are typically 2–3% in A<=10 weak transitions and 20–30% in selected impulse-suppressed 8Li/8B/8He channels.
2. Warburton, Towner, Brown, Phys. Rev. C 49, 824 (1994), DOI 10.1103/PhysRevC.49.824: axial-charge enhancement factor `epsilon_exp = 1.61 +/- 0.03` at A~16, corresponding to extra amplitude `r_extra≈0.61` relative to the impulse term in that channel.
3. Warburton, Phys. Rev. Lett. 66, 1823 (1991) / Phys. Rev. C 44, 233 (1991): fitted rank-zero axial-charge enhancement `epsilon_MEC = 2.01 +/- 0.05` in A=205–212, corresponding to the largest frozen empirical extra-amplitude anchor `r_emp = 1.01`.
4. Krebs, Eur. Phys. J. A 56, 234 (2020), DOI 10.1140/epja/s10050-020-00230-9: complete chiral-EFT nuclear-current hierarchy through N3LO; this motivates an EFT hierarchy but is NOT used as a hard universal coefficient bound.

The 2.01 heavy-nucleus enhancement is deliberately taken as the dominant empirical anchor even though it is channel-specific and historically larger than modern ordinary-GT two-body corrections.

## Frozen safety ladder
Set `r_emp = 1.01` and evaluate the genuine higher-body extra-amplitude stress values

`r_2b = S * r_emp`, for `S = {1, 3, 10, 100, 1000}`.

The `S=1000` point is intentionally absurdly conservative and is a stress diagnostic, not an EFT claim.

Also compute the exact amplitude bridge required for `P_stress=1 W/kg`:

`r_bridge_total = sqrt(1/P_leading) - 1 - r_1b`.

Report `r_bridge_total/r_emp`.

## Prospective classifications
- `PASS_EMPIRICAL_STRENGTH_STRONG_NEGATIVE` if even `S=100` remains below `1e-3 W/kg` AND the exact bridge exceeds `1e4 * r_emp`.
- `PARTIAL_EMPIRICAL_STRENGTH_NEGATIVE` if `S=100` remains below 1 W/kg but either stronger condition fails.
- `FAIL_EMPIRICAL_ENVELOPE_NOT_SMALL` if `S=100` reaches/exceeds 1 W/kg.

`S=1000` is reported but does not define PASS because it is intentionally far beyond any frozen empirical anchor.

## Scope / anti-overclaim
A PASS means: known weak-transition two-body-current amplitudes, even inflated by two orders of magnitude over the largest frozen empirical extra-amplitude anchor, remain far too small to rescue passive solar-neutrino power in the already-deliberately-loose 0026 envelope.

A PASS does NOT prove that every mathematically possible higher-body SM contact/operator coefficient is universally bounded by the empirical anchor. Unknown renormalized contact terms, genuinely long-range/growing-coordination operators, breakdown-scale configurations, and BSM currents remain outside this statement unless separately bounded.

## Required implementation evidence
- deterministic module under `src/nmir/`;
- dedicated tests;
- machine-readable benchmark JSON;
- hosted fail-closed workflow;
- raw log/artifact inspection before scientific classification;
- immutable numbered iteration note and RECOVERY.md reconciliation.
