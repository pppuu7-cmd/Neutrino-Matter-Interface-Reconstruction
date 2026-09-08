# Iteration 0092b-a1 r2 — GONG fixed-width parser infrastructure failure

Date: 2026-09-08
Classification: `INFRASTRUCTURE_FAIL_G9_0092B_A1`

Execution head: `8ceb503050c5d70b59d889390ce25da67747cc38`.
Run/job: `34277513371 / 102234063162`.
Artifact: `10076294046`.

The r1 blank-record issue was repaired and dedicated tests again passed (`3 passed`). Official files again fetched with exactly the same hashes:
- limited Model-S `65ecb920ed81b6b41f733cb8ab6f8c30941f7c743b0b6fec831de30e9a7322cc`;
- GONG Model-S `a30c31b9f6af2e5918f49d3808c0dade54f9946133b679b86949fc73625c2393`;
- format PDF `9614e18f6eed3f7121352539651c502ae84b7b13bb308b091a66157b45a597b5`.

The scientific composition calculation still did not begin. The second parser assumed whitespace-delimited floating fields after locating the correct integer record. The official format specification states `1p5e16.9`, and the raw Model-S file contains adjacent fixed-width signed exponent fields that need not have whitespace between them. `numpy.fromstring(..., sep=' ')` therefore raised before payload construction.

This is an implementation/parser failure, not composition authority/numerics evidence. No H/He/Z result JSON was created, so no scientific PASS/BLOCKED/FAIL classification is permitted.

Raw upload ZIP digest: `9136eaf7528fdf586fe4ae4c62e295fd06891045401b483e11f35cdbfbefdaf1`. The artifact contains only the three official source files.

Permitted repair: parse every post-header numeric record according to the already-frozen official fixed-width format (five 16-character E fields per line), preserving all scientific sources, formulas, resolutions and thresholds unchanged.
