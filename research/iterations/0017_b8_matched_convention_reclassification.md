# Iteration 0017 — B8/Cl matched-convention audit and reclassification

Date: 2026-09-06

## Motivation
Iteration 0016 correctly rejected the mixed `Ortiz-2000 B8 spectrum × Bahcall-1996 Cl pointwise response → historical 1.06e-42 cm2` comparison, but labeled the cause too narrowly as a spectral-convention mismatch. This iteration returns to the 1996 primary paper to separate spectrum evolution from nuclear-response evolution.

## Primary-source correction
Bahcall et al., *Standard Neutrino Spectrum from 8B Decay* (1996; arXiv:nucl-th/9601044, published Phys. Rev. C 54, 411) explicitly states:

1. Bahcall & Holstein (1986) obtained `sigma_Cl = (1.06 ± 0.10)e-42 cm2` using the then-current B(GT) information from Sextro et al.
2. Replacing only the B8 spectral shape by the 1996 best-fit spectrum while retaining the same older low-energy nuclear data gives `sigma_Cl = (1.08 ± 0.15)e-42 cm2`; the best estimate changes by only about 2%.
3. Using the newer A=37 nuclear data together with the 1996 spectrum gives `sigma_Cl = (1.14 ± 0.11)e-42 cm2`.
4. The paper's Table II supplies both the 1996 improved energy-dependent response and the older Bahcall-Ulrich response.

Therefore the historical `1.06e-42 cm2` value is **not a pure spectrum-convention target**. It bundles an older spectrum with an older nuclear-response convention. The iteration-0016 `+12.40%` mismatch must be classified more generally as a **mixed spectrum × response authority mismatch**, not as evidence that Ortiz-2000 spectral evolution alone accounts for the difference.

## New frozen matched input
`data/b8_bahcall_lisi1996_spectrum.csv` transcribes the central `lambda(E)` column of Table I on its 0.1-MeV grid. The table is a probability density per MeV; trapezoidal normalization is approximately unity.

`src/nmir/b8_historical_audit.py` folds that matched spectrum against either response column from `data/cl37_bahcall1996_response.csv`. Because Table II is sparse, this is deliberately classified as a tabulated/interpolated consistency check, not as a replacement for the paper's continuous internal calculation.

## Numerical consistency check
Using linear interpolation of the sparse Table-II points:

- 1996 spectrum × 1996 improved response column: `~1.15972e-42 cm2`, within ~1.73% of the paper's published `1.14e-42 cm2` full-response value.
- 1996 spectrum × Bahcall-Ulrich response column: `~1.07259e-42 cm2`, within ~0.69% of the paper's stated `1.08e-42 cm2` recalculation using the new spectrum with the older nuclear data.

The residual differences are consistent with using a sparse interpolation of representative response points rather than the authors' full continuous response calculation. Importantly, the matched audit reproduces the hierarchy and scale without any normalization retuning.

## Scientific classification
- Iteration-0016 rejection of the mixed Ortiz × historical-authority reproduction remains valid.
- Its causal label is corrected from `spectral-convention mismatch` to **spectrum-response convention mismatch**.
- Spectral evolution between Bahcall-Holstein and the 1996 best-fit spectrum changes the historical Cl source average by only ~2% when the nuclear response is held fixed.
- Nuclear-response updates account for an additional material shift (`1.08 -> 1.14e-42 cm2` in the primary 1996 comparison).
- The current Ortiz-2000 baseline may continue to be used for modern B16 solar folding, but historical source-average values must only validate matched spectrum+response pairs.

## Infrastructure
Added:
- `data/b8_bahcall_lisi1996_spectrum.csv`
- `src/nmir/b8_historical_audit.py`
- `tests/test_b8_historical_audit.py`

CI run from the new tests is tracked separately; scientific promotion requires successful CI, but the primary-source reclassification itself does not depend on CI outcome.

## Next gate
1. Consume CI for the matched-convention code/tests.
2. Freeze a final Cl uncertainty/convention envelope using the modern Ortiz+B16 working fold and matched historical audits without cross-convention validation abuse.
3. Move G3 to neutrino-only deposited-energy accounting for Ga/Cl and W/kg.

NMIR_READINESS: 34% pending CI validation; keep at 33% until CI passes.
