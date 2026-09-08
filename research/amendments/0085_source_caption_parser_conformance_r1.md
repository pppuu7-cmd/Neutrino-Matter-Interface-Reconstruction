# NMIR 0085 source-caption parser conformance — r1

Date: 2026-09-08
Status: **INFRASTRUCTURE-ONLY FOLLOW-UP; SCIENTIFIC CONTRACT UNCHANGED**
Parent: `research/amendments/0085_source_caption_parser_conformance.md` and frozen preregistration `research/prereg/0085_wagner_identity_free_upper_envelope.md`.

## Follow-up cause
After the first caption-parser correction, regression runs still stopped before the scientific audit. The remaining cause is purely LaTeX syntax: the exact source phrase is inside math delimiters, so the normalized text is of the form

`$95 %$ cl upper bounds`

rather than a plain prose token sequence `95 % cl upper bounds`.

The `$...$` delimiters have no semantic content for the frozen source-authority question. They only mark TeX math mode. The r1 conformance implementation therefore removes `$` delimiters during text normalization before applying the already-frozen source phrase test.

The earlier synthetic fixture also briefly used an unnecessary `\,` before `\%`; that fixture was corrected to source-style spacing and never produced a scientific audit result.

## Permitted r1 implementation change
Only remove literal TeX math-mode delimiter `$` from normalized source text before applying the existing tests for:
- Figure 6 context;
- `95% CL upper bound(s)`;
- vector Yukawa semantics;
- B-L charge semantics.

No geometry, topology, clipping, interpolation, coupling conversion, side semantics, confidence interpretation, or PASS/BLOCKED/FAIL rule changes.

## Non-authoritative runs
- `34173898639`, job `101899394078`: regression failure before scientific audit due synthetic caption fixture/parser mismatch.
- `34173940771`, job `101899514932`: regression failure before scientific audit because `$` math delimiters remained between `%` and `CL`.

Both are infrastructure-only and produce no scientific 0085 classification.

`NMIR_READINESS` remains 97% pending a valid 0085 classification.
