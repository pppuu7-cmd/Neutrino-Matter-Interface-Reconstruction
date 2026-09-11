# 0103S Pencil `mdwarf` vector-field interface result

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103S`
Status: `PASS_0103S_PENCIL_MDWARF_VECTOR_INTERFACE_NONTERMINAL`

Preregistration: `research/prereg/0103s_pencil_mdwarf_vector_interface.md`
Workflow: `.github/workflows/0103s-pencil-mdwarf-vector-interface.yml`
External repository: `pencil-code/pencil-code`
External commit: `1a672b5cb2983b3e286503a789dd36bf7d6d1141`

## Authoritative execution

The first execution (`34650530711`) successfully compiled and ran the frozen MHD sample but failed only at the postprocessing import stage because the GitHub-hosted Python environment lacked `matplotlib`. That run is infrastructure-only and is not the scientific/interface authority.

The rerun changed **only** postprocessing dependencies (`matplotlib` and `lazy_loader`); no physical sample parameter, field initialization, grid, gate or extraction rule was altered.

Authoritative run:

- NMIR head commit: `c49b2dddffd79ac0bfa6e50af8dfab016eb8b23c`
- workflow run: `34650666488`
- job: `103431814298`
- conclusion: `success`
- evidence artifact ID: `10283931487`
- evidence artifact ZIP SHA256: `3711dc174eb4d9eb8e8dd4ff09f0e9a65f8be6aee7c84bd7ae7f896ef4403482`
- compiler: GNU Fortran 13.3.0

## Frozen sample execution

The exact pinned Pencil sample compiled and ran without modification of its physical configuration:

- grid: `32 x 32 x 32`;
- Cartesian box extents: `[-1.5, 1.5]` on each axis;
- magnetic module active;
- 41 timesteps completed;
- final snapshot time: `t = 0.58838927699252963` in the sample's code units;
- native snapshots `VAR0`, `VAR1`, `VAR2`, and `var.dat` were written.

The live Pencil diagnostics independently showed a nonzero magnetic field throughout the short regression evolution. At the final reported timescale the native diagnostic was approximately `brms = 4.520e-06`, `bmax = 4.710e-05` in code units.

## Official reader extraction

The pinned Pencil Python reader was applied to the native `var.dat` and asked to derive `bb` from the stored magnetic vector potential through its built-in curl implementation.

Machine-readable extraction result:

- `bb_shape = [3, 32, 32, 32]`;
- all components finite: `true`;
- at least one component nonzero: `true`;
- extracted snapshot time: `0.5883892774581909`;
- `|B|_min = 0.0`;
- `|B|_max = 4.687900321192166e-05`;
- RMS `|B| = 4.490911276462364e-06`;
- coordinates: `x,y,z in [-1.5,1.5]`, 32 points each.

All preregistered vector-interface gates passed.

The reader emitted a warning that, because a full Pencil grid object was not passed to the curl helper, it assumed an equidistant grid. That assumption is consistent with this frozen Cartesian sample and with its reported uniform coordinate arrays. No post-result numerical correction was introduced.

## Scientific meaning

This result establishes a concrete technical fact that was previously only assumed:

> NMIR can ingest a native, reproducibly generated Pencil Code full-state snapshot and obtain a finite, nonzero, full three-component three-dimensional magnetic field without imposing a hand-written radial magnetic-field law.

Therefore the generic **MHD-vector-field ingestion interface is operational**.

This materially narrows the remaining 0103 problem: the obstacle is no longer whether NMIR can technically consume a 3-D Pencil magnetic state. It is whether the **specific Betelgeuse-like nonlinear state** used in Dorch (2004), or another prospectively admissible Betelgeuse-specific vector authority, can be recovered.

## Strict scope guard

The `mdwarf` field is a regression/model-conditional fully-convective-star fixture. It is not Betelgeuse, not a red-supergiant reconstruction, and not the Dorch 2004 nonlinear run.

Consequently this PASS does **not** alter the Betelgeuse terminal classification:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.

It does justify a separate next-stage model-conditional giant-star benchmark if prospectively preregistered, while the original-author/archive acquisition route is pursued independently.
