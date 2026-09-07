# NMIR Iteration 0081 — B-L BBN observational semantics

Date: 2026-09-08
Classification: **PASS_COSMOLOGY_B_L_BBN_OBSERVATIONAL_SEMANTICS**
Prospective contract: `research/prereg/0081_bl_bbn_observational_semantics.md`, frozen commit `c2ece0e25d2cef9c24d16833bc5703ccc94d08f1`.

## Scope
This gate audits only exact primary Esseili–Kribs TeX for the present-observation BBN helium criterion governing the published Majorana/Dirac BBN figures. It does not inspect vector path/color identity, calibrate axes, extract geometry, combine with CMB contours, or perform any BSM response scan.

## Primary authority
- source: `https://export.arxiv.org/e-print/2308.07955v2`
- source SHA256: `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`
- primary TeX: `neff_arXiv_v2.tex`
- TeX SHA256: `f77b577688b3609c574985b05fc9a213709c958ded60a511478357f1f881d678`

The primary source states a conservative BBN bound `Delta Y_p = 0.008` at `95% C.L.` and defines
`Delta Y_p = Y_p|_BSM - Y_p|_SM`.
Thus the recovered convention is signed BSM-minus-SM, not an absolute-value definition. Figure 7 is the Majorana BBN figure; Figure 8 explicitly states that it is the same as Figure 7 for the Dirac case. All frozen semantic checks pass.

## Authoritative hosted evidence
- head commit: `5873dafc291bcb5579b10aec70dd7ade1851b119`
- run/job: `34164891666 / 101873875465`
- artifact: `10033820001`, 2641 bytes
- raw JSON SHA256: `cbdceeabcd7f55094096028be481c26cdf18493018401c0c6092f2ac56a2b33c`
- artifact ZIP SHA256: `d33e63b8716ad3af82650653734395e333f52744138f2340824b85343927f705`
- GitHub artifact metadata digest: `sha256:d33e63b8716ad3af82650653734395e333f52744138f2340824b85343927f705`
- independently downloaded ZIP SHA256: `d33e63b8716ad3af82650653734395e333f52744138f2340824b85343927f705`
- independently downloaded inner JSON SHA256: `cbdceeabcd7f55094096028be481c26cdf18493018401c0c6092f2ac56a2b33c`
- dedicated regression tests: `6 passed`.

Raw job log was inspected directly before accepting the PASS. Green workflow status alone was not used as scientific authority.

## Fail-closed implementation history
Run/job `34164735098 / 101873432383` is permanently classified `IMPLEMENTATION_INVALID_EXACT_SOURCE_TEX_PARSER_FALSE_NEGATIVE`: its raw saved primary context itself contained `Delta Y_p=0.008 at 95% C.L.` and the signed BSM-minus-SM definition, but the parser returned null CL/sign fields. No scientific criterion was relaxed.

Run/job `34164808383 / 101873639242` is permanently `IMPLEMENTATION_INVALID_REGRESSION_TEST_FAILURE_BEFORE_SCIENTIFIC_AUDIT`: the new exact-source-style fixture exposed missing TeX math-delimiter handling; the scientific audit was skipped and no artifact was produced. The frozen contract again remained unchanged.

Parser/test corrections culminated in commit `5873dafc291bcb5579b10aec70dd7ade1851b119`; they only repaired exact-source TeX recognition.

## Scientific consequence
0081 validates the observational semantics needed to interpret the BBN figures, but it does **not** itself materialize an excluded polygon. Majorana and Dirac remain separate scenario-conditioned branches per 0080e. No CMB threshold may replace the BBN threshold, and no CMB+BBN combination is authorized by this gate.

## Next action
Prospectively freeze a separate 0081a BBN vector-asset axis-calibration and semantic-identity gate before any vector path/color inspection or excluded-region extraction.

`NMIR_READINESS` remains **94%**: this is a reproducible semantics gate, but it does not yet add an independently materialized excluded region to the external envelope.
