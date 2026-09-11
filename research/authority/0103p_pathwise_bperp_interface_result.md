# 0103P Pencil pathwise `B_perp(s)` interface result

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103P`
Status: `PASS_0103P_PATHWISE_BPERP_INTERFACE_NONTERMINAL`

Preregistration: `research/prereg/0103p_pencil_pathwise_bperp_interface.md`
Workflow: `.github/workflows/0103p-pencil-pathwise-bperp-interface.yml`
External repository: `pencil-code/pencil-code`
External commit: `1a672b5cb2983b3e286503a789dd36bf7d6d1141`

## Authoritative execution

- NMIR head commit: `a822441202e07c84e49abd40a872c9e2d4422196`
- workflow run: `34651140105`
- job: `103433327546`
- conclusion: `success`
- evidence artifact ID: `10283632757`
- evidence artifact ZIP SHA256: `54134a37bee28308ae282025288e7e1b4aa8d58757c98a532fc61e19f53973a6`

All preregistered gates passed.

## Frozen geometry

The audit used the already validated unmodified `samples/mdwarf` MHD state and froze the ray before seeing the path result:

- propagation direction `n=(1,0,0)`;
- target transverse coordinates `y=z=0`;
- stellar interval restricted to native x nodes satisfying `-1 <= x <= +1`;
- no interpolation in x;
- bilinear interpolation only in the y-z plane.

The even grid brackets zero by

- `y=[-0.04838705062866211,+0.04838705062866211]`, weights `[0.5,0.5]`;
- `z=[-0.04838705062866211,+0.04838705062866211]`, weights `[0.5,0.5]`.

Twenty native x nodes were retained along the stellar diameter.

## Pathwise result

Snapshot time:

`t = 0.5883892774581909`

Transverse field:

- `B_perp_min = 1.0703093388848252e-06`
- `B_perp_max = 1.4364693974972633e-05`
- `B_perp_rms = 6.8443609176478045e-06`

Parallel field:

- `B_parallel_min = -9.804290848155403e-06`
- `B_parallel_max = 4.381053218774913e-06`
- `B_parallel_rms = 3.72274516588295e-06`

All values above are in the frozen sample's code-field units.

The component definition

`B_perp = sqrt(By^2+Bz^2)`

agreed with the basis-free identity

`B_perp = sqrt(max(0, |B|^2-(B dot n)^2))`

with maximum absolute residual

`1.6940658945086007e-21`.

## Retained x nodes

`[-0.9193547964096069, -0.8225806355476379, -0.7258064150810242, -0.6290323138237, -0.5322580337524414, -0.4354839324951172, -0.33870959281921387, -0.24193549156188965, -0.14516127109527588, -0.04838705062866211, 0.04838705062866211, 0.14516127109527588, 0.2419353723526001, 0.3387094736099243, 0.4354839324951172, 0.5322580337524414, 0.6290321350097656, 0.725806474685669, 0.8225805759429932, 0.9193549156188965]`

## Scientific meaning

0103P closes a technical ambiguity that was previously still open: NMIR now has a preregistered deterministic map from an authentic native Pencil 3-D vector state to the one-dimensional transverse field required by the spin-flavor Hamiltonian. The ray, interpolation and transverse projection were fixed before the numerical result was inspected.

Together with 0103S, the demonstrated chain is now:

`native Pencil VAR -> official-reader B(x,y,z) -> frozen ray/interpolation -> pathwise B_perp(s)`.

Therefore the remaining 0103 Betelgeuse bottleneck is not a missing numerical geometry/interface method. It is the absence of a Betelgeuse-specific machine-readable vector-field authority and its physical co-registration with the propagation medium.

## Strict scope guard

This result uses the public `mdwarf` regression fixture. It is not Betelgeuse and is not the nonlinear Dorch (2004) run.

Accordingly this PASS does **not** alter the terminal Betelgeuse status:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.
