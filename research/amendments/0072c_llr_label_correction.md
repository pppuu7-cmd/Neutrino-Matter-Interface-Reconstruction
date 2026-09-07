# NMIR 0072c pre-result amendment — LLR nomenclature correction

Date: 2026-09-07
Status: PRE-RESULT / nomenclature only. No 0072c curve-extraction result existed at this amendment.

The primary Wagner Figure-6 caption states that the **right** magenta LLR curve is derived from the earth-moon differential acceleration toward the Sun, while the **left** magenta LLR curve is the inverse-square-law constraint obtained from anomalous lunar-orbit precession.

Therefore the two frozen identity labels used by the implementation are corrected to:
- left magenta chain: `LLR_precession_inverse_square`;
- right magenta chain: `LLR_differential_acceleration`.

This corrects wording only. The preregistered left/right geometric assignment, source, path chaining algorithm, tolerances, multiplicity, exclusion sense, PASS/FAIL criteria and all other 0072c rules are unchanged.
