# 0103P Pencil pathwise `B_perp(s)` interface preregistration

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103P`
Status: PREREGISTERED MODEL-CONDITIONAL GEOMETRY INTERFACE AUDIT

## Purpose

Test the final geometry step between a reproducible 3-D Pencil magnetic vector state and the one-dimensional transverse magnetic field required by the 0103 spin-flavor Hamiltonian.

This is a technical/model-conditional interface audit using the already validated `samples/mdwarf` regression model. It is not a Betelgeuse prediction and cannot close Betelgeuse field authority.

## Frozen external source

Repository: `pencil-code/pencil-code`
Commit: `1a672b5cb2983b3e286503a789dd36bf7d6d1141`
Sample: `samples/mdwarf`

Use the unmodified sample and the same official Pencil Python reader path validated by 0103S.

## Frozen ray

The stellar sphere in the sample has `r_ext = 1` in a Cartesian box spanning `[-1.5,1.5]^3`.

Freeze a central diameter ray:

- propagation coordinate: increasing `x`;
- ray direction: `n = (1,0,0)`;
- target transverse coordinates: exactly `y=0`, `z=0`;
- retained stellar interval: native x nodes satisfying `-1 <= x <= +1`.

No ray orientation, impact parameter, or interval may be changed after field values are inspected.

## Frozen interpolation rule

Because the even 32-point grid need not contain exact `y=0` or `z=0` nodes, evaluate each Cartesian magnetic component at `(x_i,0,0)` by bilinear interpolation in the `y-z` plane using the four native grid cells bracketing zero. Do not interpolate in `x`; retain the native interior `x_i` nodes.

For each component `Bc` at each retained x node:

1. find `j0,j1` such that `y[j0] <= 0 <= y[j1]`;
2. find `k0,k1` such that `z[k0] <= 0 <= z[k1]`;
3. use ordinary bilinear weights determined only by coordinate distances;
4. apply the same weights independently to `Bx`, `By`, `Bz`.

If zero is exactly a native coordinate on either axis, the corresponding interpolation collapses to that native plane.

## Frozen transverse-field definition

For `n=(1,0,0)`:

- `B_parallel(x_i) = Bx(x_i,0,0)`;
- `B_perp_vec(x_i) = (0, By, Bz)`;
- `B_perp(x_i) = sqrt(By^2 + Bz^2)`.

Also verify the basis-free identity

`B_perp = sqrt(max(0, |B|^2 - (B dot n)^2))`

to numerical tolerance.

## Gates

PASS requires:

1. exact external commit match;
2. the unmodified mdwarf sample produces a valid finite 3-D `bb` field;
3. zero is bracketed by both y and z coordinates;
4. at least two native x nodes lie in the stellar interval `[-1,+1]`;
5. all interpolated Cartesian components are finite;
6. all `B_perp` values are finite and non-negative;
7. at least one path node has strictly nonzero `B_perp`;
8. component and basis-free `B_perp` definitions agree with max absolute residual <= `1e-12` in code-field units;
9. interpolation weights in each transverse coordinate lie in `[0,1]` and sum consistently;
10. machine-readable output records the bracketing y/z coordinates, weights, retained x nodes, `B_perp min/max/RMS`, `B_parallel min/max/RMS`, and the hard scope marker `MODEL_CONDITIONAL_PATH_NOT_BETELGEUSE`.

## PASS ceiling

`PASS_0103P_PATHWISE_BPERP_INTERFACE_NONTERMINAL`

PASS would establish that NMIR has a preregistered, deterministic 3-D-vector-to-pathwise-`B_perp` geometry interface. It does not provide Betelgeuse's actual magnetic field. The Betelgeuse terminal ceiling remains:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.
