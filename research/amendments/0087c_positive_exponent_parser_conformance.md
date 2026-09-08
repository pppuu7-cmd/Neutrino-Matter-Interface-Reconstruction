# NMIR amendment 0087c — positive-exponent parser conformance

Date: 2026-09-08

The first hosted 0087c run `34180384404`, job `101918098909`, stopped in the dedicated regression tests before any source audit. Test `test_direct_signed_power_only` showed that the implementation rejected source text `10^2` because `direct_power()` required an explicit `+` or `-` after normalization.

This is **INFRASTRUCTURE_FAIL_PARSER_CONFORMANCE**, not a scientific Cerdeño classification. No source-derived 0087c numerical result was produced or inspected.

The frozen preregistration requires signed numerical major tick anchors but does not require an explicit plus glyph for a positive exponent. Standard source-native `10^2` therefore has exponent `+2` and must be admissible. The implementation may be corrected so that:

- a caret-form positive exponent such as `10^2` is accepted;
- explicit signed forms such as `10^-2`, `10^+2`, Unicode superscript-minus forms remain accepted;
- an ambiguous ordinary token such as `102` or whitespace-separated ordinary text `10 2` is **not** reinterpreted as a power of ten;
- split exponent reconstruction may accept a digits-only smaller superscript fragment when its source-native font-size/vertical/adjacency geometry establishes exponent placement; no missing minus may be synthesized.

No scientific tolerance, x-band, anchor count, span criterion, residual threshold, frame tolerance, source bytes, target interval, threat rule, PASS/BLOCKED/FAIL consequence or guard is changed.
