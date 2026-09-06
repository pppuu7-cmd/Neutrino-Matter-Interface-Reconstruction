# NMIR 7Li inverse-capture screening seed

Status: next-target input freeze; no 7Li G3 authority yet.

## Direct production↔absorption anchor
ENSDF `7Be EC decay` gives for the ground-state branch:
- parent `7Be`, `Jpi=3/2-`;
- daughter `7Li` ground state, `Jpi=3/2-`;
- `Q_EC = 861.815(18) keV`;
- `T1/2 = 53.22(6) d`;
- branch `89.56(4)%`;
- `log ft = 3.324(1)`.

This directly anchors the crossed ground-state capture

`7Li(gs) + nu_e -> 7Be(gs) + e-`

with threshold near the EC Q value. Because the initial/final ground-state spins are both 3/2, no spin-degeneracy ambiguity is introduced by reversing this specific transition.

## Important excited-state guard
ENSDF also gives the `7Be(gs) -> 7Li*(477.612 keV)` EC branch (`10.44%`, `log ft=3.556`). That measured matrix element is **not automatically** the direct inverse of capture on a ground-state 7Li target into an excited 7Be state. Any use of the excited-state lithium-detector channel requires a separate mirror/isospin or direct weak-response authority and must not be inferred by naive crossing of different external nuclear states.

## Prospective validation plan
1. Use `log ft=3.324` with the already validated NMIR `ft -> capture` machinery to build the ground-state 7Li response.
2. Reproduce at least one published 7Li source-average capture cross section or historical matched-convention total before promotion.
3. Keep the excited-state response separate until its matrix element is independently frozen.
4. Fold the validated response with the same B16 GS98/AGSS09met spectra and MSW convention used by Ga/Cl/Se.
5. Report pure-7Li and natural-lithium rates and neutrino-only W/kg ceiling.

Historical context is only a cross-check: lithium detectors use `7Li + nu_e -> 7Be + e-` with a threshold near `0.86 MeV`; BP2000-era calculations quoted a total capture scale around `39.4 SNU` after then-current oscillation/flux assumptions. These values are not imported as modern NMIR authority.

## Files
- evaluated seed: `data/li7_be7_ec_seed.csv`
- reusable measured-ft code: `src/nmir/ft_capture.py`

**NMIR_READINESS remains 42%**: this file freezes the next input but closes no new scientific gate.
