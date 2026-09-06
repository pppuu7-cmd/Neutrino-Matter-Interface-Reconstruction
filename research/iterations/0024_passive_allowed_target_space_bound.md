# NMIR iteration 0024 — passive allowed-current target-space upper bound

Date: 2026-09-06
Status: scientific PASS / **STRONG NEGATIVE (scoped)**
Readiness after promotion: `NMIR_READINESS: 47%` (audit estimate)

## Motivation
Four individually validated passive targets (71Ga, 37Cl, 82Se, 7Li) still leave an enormous gap to macroscopic neutrino-supplied power. Instead of continuing isotope-by-isotope indefinitely, iteration 0024 asks whether the entire leading **allowed one-body charged-current** target class can be bounded from above.

This is intentionally narrower than global Standard Model nuclear response: forbidden multipoles, resonant line capture, engineered collective media, focusing and BSM interactions are excluded and remain separate gates.

## Preregistered construction
The acceptance criteria and stress domain were committed before hosted output in `research/passive_allowed_bound_prereg.md` (commit `88bf3a6718122a354f6bada3ad2fb43d58371392`).

For the attractive point-Coulomb factor

`F_pc = x/(1-exp(-x))`, `x=2*pi*alpha*Z_f*E/p`,

`exp(x)>=1+x` implies `F_pc<=1+x`, hence

`p E F_pc <= (1+2*pi*alpha*Z_f) E^2`.

A correlation-independent one-body operator-norm cap was deliberately chosen rather than a realistic nuclear model:

`S_F <= A^2`, `S_GT <= 3 A^2`,

so

`S_allowed <= A^2 (1+3 g_A^2)`.

This massively over-allocates allowed weak strength compared with physical Fermi/GT sum-rule systematics.

The maximization domain was also deliberately biased toward large power:
- `A<=300`;
- daughter `Z_f<=119`;
- zero reaction threshold and zero excitation energy;
- all admitted solar-neutrino energies up to `20 MeV`;
- artificial incident neutrino **energy** flux `<=2000 W/m^2`, exceeding total electromagnetic solar irradiance and vastly exceeding the real solar-neutrino energy flux;
- target nuclei/kg increased by a further 2% safety factor.

Finally, a separate `x10^6` omitted-physics stress multiplier was preregistered. It is not part of the analytic theorem and is not an uncertainty estimate; it is an intentionally extreme robustness diagnostic.

Prospective classification:
- `STRONG_NEGATIVE_SCOPED` if the x1e6 stressed value remains below `1e-3 W/kg`;
- `NEGATIVE_SCOPED` if the analytic value is below 1 W/kg but the first condition fails;
- `NO_NEGATIVE_BOUND` if the analytic envelope reaches 1 W/kg.

## Hosted result
Implementation commits:
- analytic code `3d4a8b74cdd3f86396bc0435c9dae2700aed4673`;
- regression tests `65c922e5ea9fee816fe299a8514cc089c7f43b45`;
- JSON benchmark `7c422c78ecf978925529ce256d0eeef0d5641767`;
- hosted workflow head `5cdb30148ce7a928fdb00424723f065e54a5f104`.

Hosted scientific run:
- workflow `NMIR passive allowed bound`;
- run `34038214660`;
- job `101500085408`;
- artifact `9990839187`;
- artifact ZIP SHA256 `f9e544b9aa5372f8e286e8214f2eba422f35cc8e02468501babc99cfcbbc8642`.

Six dedicated regression tests passed. Same-head baseline CI run `34038214654` also completed successfully.

Raw JSON, inspected before classification:

| quantity | result |
|---|---:|
| analytic allowed-current envelope | `9.419449302949355e-12 W/kg` |
| deficit to 1 W/kg | `1.061633188775576e11` |
| preregistered omitted-physics stress | `1e6` |
| x1e6 stressed diagnostic | `9.419449302949354e-6 W/kg` |
| stressed deficit to 1 W/kg | `1.061633188775576e5` |
| classification | **STRONG_NEGATIVE_SCOPED** |

The analytic envelope is about `8.84e9` times above the current validated Li7/GS98 target result (`1.0659e-21 W/kg`), confirming that it is genuinely an envelope rather than a fitted extrapolation of the four-target ledger.

## Scientific interpretation
Within the stated domain, ordinary leading allowed one-body charged-current nuclear capture cannot supply macroscopic power from the solar-neutrino field. The result remains far below 1 W/kg even after simultaneously granting impossible/over-generous nuclear strength, zero thresholds, a 20-MeV endpoint, a 2000-W/m2 neutrino energy flux, and then multiplying the final answer by another million as a non-theorem stress diagnostic.

This is substantially stronger than an isotope ranking, but it is **not yet a global passive-SM no-go theorem**. The remaining loopholes that must be bounded independently are:
1. first-forbidden/higher multipole charged-current strength at solar energies;
2. resonant capture, where peak cross section cannot be used without integrated strength × linewidth × solar-spectrum overlap (G8);
3. collective/engineered channels already assigned to G2/G4/G10;
4. finite gravitational focusing (G9), which can only multiply incident phase-space density within Liouville/finite-source limits.

## Gate update
- G3: PARTIAL PASS strengthened — four validated targets + class-level leading-allowed negative bound.
- G8: OPEN and now higher priority.
- Forbidden-multipole envelope: OPEN and required before global passive nuclear no-go.
- G5/G6 BSM remain locked.

`NMIR_READINESS: 47%`.
