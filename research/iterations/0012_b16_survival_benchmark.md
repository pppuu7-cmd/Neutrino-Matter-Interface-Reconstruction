# Iteration 0012 — validated B16 production-averaged solar survival benchmark

Date: 2026-09-06

## Inputs preserved

- Frozen oscillation convention: `sin^2(theta12)=0.307`, `sin^2(theta13)=0.0220`, `Delta m21^2=7.53e-5 eV^2`, normal ordering, day-side adiabatic MSW, Earth regeneration OFF.
- Exact B16-GS98 and B16-AGSS09met electron-density/production distributions from iteration 0011.
- No retuning was allowed after seeing real B16 survival values.

## Prospective kernel validation

CI run `34014950750`, job `101437007287`, head `9a2cdc3e8ba6a35043ca50e4f7f632d89b65763f` completed SUCCESS with `64 passed in 0.16s`.

The tests were frozen before the real B16 benchmark and include:

1. zero-density agreement with the phase-averaged three-flavour vacuum limit;
2. asymptotic high-density adiabatic limit;
3. physical low/high-energy ordering;
4. native-grid production averaging.

Classification: **MSW numerical-kernel PASS within the explicitly frozen approximation**.

## Exact B16 component benchmark

Hosted run `34015021346`, job `101437186911`, head `0ab9de14afba809a4258e3fdd3c9925c834c44b9` completed SUCCESS and exact-verified the B16 inputs before averaging.

Artifact:

- ID `9983624802`;
- ZIP SHA256 `09cd10d0530723646dce465f3b965796624cc03ce1070a81556f374ebb7b5d50`.

### B16_GS98

| Component | E (MeV) | P_ee |
|---|---:|---:|
| pp | 0.300 | 0.5441859844 |
| Be7 | 0.384 | 0.5401270522 |
| Be7 | 0.862 | 0.5269716156 |
| pep | 1.442 | 0.5168705126 |
| N13 | 0.700 | 0.5328862475 |
| O15 | 1.000 | 0.5206085576 |
| F17 | 1.000 | 0.5203080977 |
| B8 | 5.000 | 0.3934493208 |
| B8 | 10.000 | 0.3270173973 |
| hep | 10.000 | 0.3870522826 |

### B16_AGSS09met

| Component | E (MeV) | P_ee |
|---|---:|---:|
| pp | 0.300 | 0.5441453692 |
| Be7 | 0.384 | 0.5400820090 |
| Be7 | 0.862 | 0.5268636988 |
| pep | 1.442 | 0.5167008279 |
| N13 | 0.700 | 0.5331722524 |
| O15 | 1.000 | 0.5205585129 |
| F17 | 1.000 | 0.5202542230 |
| B8 | 5.000 | 0.3931246897 |
| B8 | 10.000 | 0.3268237245 |
| hep | 10.000 | 0.3858005360 |

## Physical cross-check

The benchmark reproduces the standard qualitative and quantitative LMA-MSW transition without parameter retuning: low-energy pp is about `0.544`, Be7 about `0.527` at 0.862 MeV, and the B8 10-MeV checkpoint is about `0.327`. PDG 2025 shows the standard survival curve decreasing from roughly `0.55` at low energy to roughly `0.31` at high energy; its tabulated phenomenology also quotes pp and Be7 survival probabilities around `0.57±0.09` and `0.53±0.05`, respectively.

The two B16 metallicity branches change these representative survival checkpoints only at the `~1e-4` to `~1e-3` absolute level. This is useful: the large GS98/AGSS09 flux differences in some components should not be confused with comparably large oscillation-probability differences.

Classification: **component-resolved day-side B16 survival benchmark PASS within the frozen approximation**.

## Scope / non-claims

- This is not yet the full spectrum-folded Ga-71 or Cl-37 prediction.
- Earth regeneration remains excluded by design in the first benchmark.
- Small three-flavour corrections beyond the standard decoupled solar approximation are not yet included.
- The representative-energy checkpoints are diagnostics; continuum components must be integrated over their frozen spectra for capture rates.

## Gate update

- G3 solar input stack: flux PASS; spectra PASS; matter/production PASS; day-side MSW kernel + B16 component benchmark PASS.
- Next missing dominant G3 object: nuclear capture response and full energy folding for Ga-71, then Cl-37.
- G5/BSM remains LOCKED.

## Readiness

`NMIR_READINESS: 27%`

Increase `26% -> 27%` is credited to the newly closed prospective-MSW + exact-B16 component-survival benchmark gate, not to code volume.

## Exact next gate

1. Freeze a primary/authoritative Ga-71 solar-neutrino capture response or component cross-section representation.
2. Fold frozen solar spectra × B16 flux × component-specific production-averaged `P_ee(E)` × Ga response.
3. Reproduce a published Ga total/component SNU benchmark without retuning.
4. Repeat for Cl-37.
5. Convert validated capture/deposition to W/kg and advance the quantitative Standard-Model ceiling.
