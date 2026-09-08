# NMIR 0085 post-run source-caption parser conformance correction

Date: 2026-09-08
Status: **INFRASTRUCTURE/PARSER CORRECTION ONLY; FROZEN 0085 SCIENTIFIC CONTRACT UNCHANGED**
Parent preregistration: `research/prereg/0085_wagner_identity_free_upper_envelope.md`.
Affected run: `34173707219`, job `101898844487`, artifact `10036532329`.

## Why the provisional BLOCKED string is not scientific authority
The hosted audit completed and produced a machine-readable result with:
- exact EPS SHA match;
- exact corrected topology: 4 blue + 1 red + 1 orange + 2 magenta = 8 retained components;
- all components x-monotonic;
- all transformed values finite and positive;
- EPS transform round-trip maximum absolute residual `8.881784197001252e-16`;
- name/order invariance maximum `0.0` decade;
- fine-grid shared-point reproduction maximum `0.0` decade;
- non-empty clipped support.

The only failing prerequisite was `source_text_authority.upper_bounds_95cl = false`. Inspection of the audit's own exact-TeX evidence shows the Wagner source caption contains:

`the left panel shows $95 %$ cl upper bounds on the strength of a vector yukawa interaction coupled to ... b-l`

and the body independently says the left panel shows `$95 %$ cl limits` on the Yukawa magnitude for `b-l` charge.

The executable implementation searched for singular/literal forms such as `95% cl upper bound` after normalizing TeX into a spaced form. It therefore rejected the exact source phrase solely because it is `95 %` with whitespace and `upper bounds` in the plural.

Under the frozen 0085 contract, parser/test/source-text extraction failures are infrastructure failures. Run `34173707219` is therefore retained as **INFRASTRUCTURE_FAIL_SOURCE_CAPTION_PARSER_CONFORMANCE**; its provisional `BLOCKED_WAGNER_IDENTITY_FREE_B_L_UPPER_ENVELOPE` string is not promoted to scientific authority.

## Frozen conformance repair
Permitted implementation changes only:
1. recognize `95%` and `95 %` equivalently after TeX whitespace normalization;
2. recognize both singular `upper bound` and plural `upper bounds`;
3. require the already-extracted Figure-6 context flag in the final source-authority conjunction, as the prereg explicitly requires Figure-6 left-panel authority;
4. add regression coverage for the exact source-style caption wording.

No curve membership, topology, calibration, coupling conversion, clipping, interpolation, grid, side semantics, PASS/BLOCKED/FAIL criteria, or statistical interpretation may change.

## Immutable provenance
- run `34173707219`
- job `101898844487`
- head `02caf4622f5be639ab0bbf145fae01bfeb95e771`
- artifact `10036532329`
- GitHub ZIP digest `sha256:3e30868869e340a2bca1867d92a8863a325f9c718860d9b814acc1df2eb41ae5`
- independently downloaded ZIP SHA256 `3e30868869e340a2bca1867d92a8863a325f9c718860d9b814acc1df2eb41ae5`
- raw JSON SHA256 `6dccff400ca6e463226fe5d9032974e0b0b89b8f71288153fa243380d69a5890`

`NMIR_READINESS` remains 97% until a valid 0085 scientific classification is obtained.
