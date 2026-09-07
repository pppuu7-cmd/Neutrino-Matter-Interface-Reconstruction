# NMIR preregistration 0065 — G8 63Cu crossed-B(GT) loophole audit

Date frozen: 2026-09-07
Status at freeze: PROSPECTIVE FOLLOW-UP / iteration 0064 retained immutable
Parent authority: iteration 0064 classified G8 thermal-solar RIOEC as `BLOCKED_ENTRANCE_STRENGTH`. A subsequently identified independent 2025 peer-reviewed shell-model study reports target-specific B(GT) values for the exact crossed nuclear transition `63Ni*(87.2 keV, 5/2-) -> 63Cu(g.s., 3/2-)`. This follow-up tests whether that evidence is sufficient to reopen G8 without weakening the 0064 provenance rules.

## Scientific question
Does the independently calculated crossed transition strength for the 87.2-keV state, combined with independent evaluated nuclear/atomic data, provide a complete enough `63Cu(g.s.) + anti-nu_e + e_K -> 63Ni*(87.2 keV)` RIOEC entrance package to replace the generic `|M|^2=0.1` assumption and justify a prospective target-specific spectral fold?

## Frozen required package
A PASS requires all of the following to be independently recoverable and mutually consistent:
1. exact channel/spins: `63Cu(g.s., 3/2-) -> 63Ni*(87.2 keV, 5/2-)`, an allowed GT transition;
2. atomic-mass / beta-Q authority sufficient to fix `Q_epsilon = M(63Cu)-M(63Ni)`;
3. evaluated daughter excitation `E_x`;
4. daughter-atom K-vacancy binding/excitation energy `E_b` and a physical K-vacancy natural width (or equivalent daughter-system width authority);
5. target-specific weak normalization for the exact crossed transition from experiment or an explicit evaluated calculation. A theoretical B(GT) ensemble is admissible only if its convention and reverse-transition mapping can be stated; its model spread must be propagated rather than collapsed to a convenient central value;
6. consistency check that the reconstructed `E_R=-Q_epsilon+E_x+E_b` agrees with the independently published 63Cu RIOEC resonance at the stated uncertainty/order, without using that published resonance as an input;
7. no linewidth-as-strength substitution and no generic log(ft) assumption.

## Reverse-transition convention gate
For the standard reduced transition probability definition
`B(GT;i->f)=|<f||sigma tau||i>|^2/(2J_i+1)`,
the reverse B(GT) must be obtained by the spin statistical factor, not assumed equal. The audit must explicitly track whether the RIOEC formalism uses reduced matrix-element squared or B(GT), and convert consistently before any rate fold.

## Prospective classifications
- `PASS_G8_CU63_PROVENANCE_REOPENED`: all package components above are independently frozen; next action is a new preregistered thermal-solar anti-nu_e spectral fold with the full B(GT) model envelope.
- `PARTIAL_PASS_CU63_STRENGTH_ONLY`: exact crossed weak strength is independently grounded but one or more atomic/Q/width components needed by the frozen package remain unavailable or ambiguous.
- `FAIL_CROSSED_MAPPING`: the 2025 B(GT) values cannot consistently normalize the inverse RIOEC transition under detailed balance/convention matching.
- `BLOCKED_CU63_PACKAGE`: evidence remains insufficient; iteration 0064 blocker stands.

## Guards
- 0064 is never rewritten or reclassified retroactively; 0065 may only supersede its current frontier if new evidence passes this stricter follow-up.
- The 2026 RIOEC paper's generic `|M|^2=0.1` is not an input to the entrance strength.
- The RIOEC paper's quoted `E_R=162.5 keV` is comparator-only, not an input to reconstructed resonance energy.
- Source spectrum is not folded in this gate; 0064 already established the physical thermal-solar anti-nu_e source class. Numerical events/kg/s or W/kg remain forbidden until provenance PASS.
- Model spread is evidence uncertainty, not a tunable optimization parameter.

## Next action on PASS
Freeze the primary/evaluated evidence ledger, record immutable iteration 0065, then preregister a `63Cu` thermal-solar anti-nu_e spectral fold using a materialized Vitagliano-Redondo-Raffelt spectrum and the full allowed weak-strength envelope.
