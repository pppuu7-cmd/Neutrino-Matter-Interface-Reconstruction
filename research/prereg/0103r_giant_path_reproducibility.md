# NMIR-0103R — pathwise magnetic-geometry reproducibility

Status: PREREGISTERED BEFORE RESULT

## Scope
Independent engineering audit of the already demonstrated `B(x,y,z) -> B_perp(s)` interface. This audit is deliberately synthetic and cannot close Betelgeuse authority.

## Frozen fixture
A deterministic analytic 3-D vector field is sampled on fixed Cartesian grids. A non-grid-aligned target `(y,z)` is evaluated with fixed bilinear interpolation along the x-directed ray. RNG seed 103 is used only for independent algebraic projection checks.

## Frozen gates
1. all field/path values finite;
2. interpolation weights valid and sum to one;
3. `B_perp = sqrt(max(0, |B|^2-(B·n)^2))` agrees with `|B x n|` to <= 1e-12 for the extracted ray;
4. the same identity agrees to <= 1e-12 for 64 deterministic random unit directions/vectors;
5. reversing the ray direction changes the sign of `B_parallel` but leaves `B_perp` invariant after path reversal, <= 1e-12;
6. interpolation evaluated exactly at grid nodes reproduces the original field to <= 1e-14;
7. path coordinate is strictly monotonic;
8. two independent executions in one process produce identical canonical SHA256 summaries;
9. explicit scope guard remains `ENGINEERING_ONLY_NOT_BETELGEUSE`.

No stellar physics parameter, normalization, or empirical Betelgeuse claim is permitted in this audit.
