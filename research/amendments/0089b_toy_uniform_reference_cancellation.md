# NMIR amendment 0089b — uniform-sphere toy reference cancellation repair

Date: 2026-09-08
Parent scientific preregistration: `5d99cd6cd4d3a5f1f9defecfbd7f4036c93b8636`.

The first hosted 0089b attempt stopped in V0 regression tests before the Model-S scientific audit was executed and before any `g9_0089b_result.json` existed. Four tests passed; the constant-density toy comparison failed only at the very small-x reference evaluation because the existing helper evaluates `1-(1-x^2)^(3/2)` by direct subtraction in binary64. At `x=1e-4` this reference suffers cancellation; the observed relative mismatch was `3.824015833274657e-09`, while no Model-S value or V1-V3 result was produced.

Implementation-only repair frozen before rerun:
- leave `src/nmir/g9_continuous_projection.py`, all analytic formulas, Model-S bytes, V1-V3 points and all scientific criteria unchanged;
- replace only the constant-density *test reference* by the algebraically identical stable evaluation `-expm1(1.5*log1p(-x*x))`;
- retain the same toy test tolerance.

This amendment cannot convert any Model-S scientific result because none was evaluated in the failed run.