# NMIR iteration 0067 — Cu63 thermal-solar anti-nu_e source-tail recomputation

Date: 2026-09-07
Prospective contract: `research/prereg/0067_g8_cu63_thermal_tail_rate_gate.md`, commit `e42cd8ccd8a321cfa850b87b0fbd8d11bed30956`.

## Result scope
This iteration closes the **source-side F3 provenance/materialization sub-gate** required by 0067. It does **not** yet classify the full RIOEC rate as strong-negative or survivor, because the exact primary RIOEC rate normalization must still be frozen independently before a result-dependent rate calculation.

Classification for this substantive sub-result: **PASS_SOURCE_TAIL_RECOMPUTED / RATE_FOLD_OPEN**.

## Primary model and implementation
The source calculation implements the ordinary-Compton thermal antineutrino emissivity of Haxton & Lin Eq. (9), using the BP98 radial Standard Solar Model table for `T(r), rho(r), X(r)`, electron density `n_e = N_A rho (1+X)/2`, the Haxton-Lin Fermi blocking correction `n'_e/n_e`, radial volume integration over the Sun, and dilution to 1 AU.

Primary authority identifies ordinary Compton production as dominating the thermal high-energy tail above approximately 5 keV. No plotted-spectrum extrapolation and no ordinary solar `nu_e` substitution are used.

Implementation commit: `704c55c09e36c3e62d67af7e355d649f1171eb79`.

The first hosted run `34081007772` failed before a physics result because NumPy 2.4 removed `np.trapz`. The only repair was `np.trapz -> np.trapezoid`, commit `a7eb05109ee3a5e6a119d20bf6a19a6215705748`; formulas, inputs and acceptance criteria were unchanged.

## Authoritative hosted result
Run/job: `34081044588 / 101616231800`.
Artifact: `10003691395`.
Artifact ZIP SHA256: `22cc917e5ac275fb509d78b69565736a0d73f433f45461bb20d4d0e01232bfb9`.

Raw log was inspected directly. Machine-readable output:

- `status = PASS_SOURCE_TAIL_RECOMPUTED`;
- `Ebar = 0.162496486 MeV`;
- `dPhi_anti-nu_e/dE(162.496486 keV) = 3.528363521736758e-41 cm^-2 s^-1 MeV^-1`;
- 5-keV sanity-check differential flux `= 3.765698986767552e7 cm^-2 s^-1 MeV^-1`;
- 6000->12000 kernel-grid relative change at 162.5 keV `= 5.832844895924436e-8`;
- Fermi-blocking ratio range `0.9652620161900424 ... 0.9989419936712352`;
- BP98 source blob SHA256 `6bd3c2d9cde15b74cf1fcebe1620566e2b3d832c09e65fc36d5422a6ef0bf198`.

Frozen machine-readable ledger: `data/g8_cu63_thermal_tail_0067.json`.

## Interpretation
The source-side blocker is removed: the Standard-Model thermal-solar electron-antineutrino differential tail at the exact Cu63 resonance can be computed under primary authority rather than extrapolated by eye. The resulting differential flux is extraordinarily small, but the project does not convert that observation into a final RIOEC rate claim until the exact rate normalization/integrated-strength formula is prospectively frozen from primary RIOEC authority.

## Next gate
Freeze a primary-source RIOEC normalization contract: exact resonance line shape/integrated cross-section formula, atomic K-shell factor, spin conventions, B(GT) convention, units and target-number normalization. Only after that freeze may the full `B_reverse=2.85e-3...6.72e-2` envelope be folded with the validated source tail to events/(kg s), events/(kg day) and neutrino-supplied W/kg.

## Readiness
This closes a real source-provenance gate and removes the 0067 high-energy-tail blocker. `NMIR_READINESS` increases from 88% to **89%**. The full G8 rate gate remains open.
