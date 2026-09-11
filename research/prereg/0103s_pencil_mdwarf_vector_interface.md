# 0103S Pencil `mdwarf` vector-field interface preregistration

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103S`
Status: PREREGISTERED MODEL-CONDITIONAL INTERFACE AUDIT

## Scientific scope guard

`0103S` is deliberately **not** the Betelgeuse-specific 0103 terminal branch. It is a separate reproducible MHD surrogate/interface benchmark intended only to test whether NMIR can ingest a genuine three-dimensional star-in-a-box magnetic vector field without inventing a radial `B(r)` law.

A PASS must never be described as:

- recovery of the Dorch 2004 Betelgeuse simulation;
- a prediction for Betelgeuse;
- empirical authority for Betelgeuse's internal magnetic field;
- closure of `BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.

## Frozen external source

Repository: `pencil-code/pencil-code`
Commit: `1a672b5cb2983b3e286503a789dd36bf7d6d1141`
Sample: `samples/mdwarf`

The frozen sample is a fully-convective star-in-a-box MHD test. Its repository configuration uses a `32^3` grid for the regression run, magnetic module enabled, non-periodic box, spherical star-in-a-box geometry, initial magnetic vector-potential noise and resistive MHD evolution. The sample is part of Pencil Code's own standard auto-test list.

The sample's `32^3` regression grid is an **interface/reproducibility fixture only**. The README recommendation of `128^3` or more is acknowledged; no scientific dynamo-convergence claim may be made from the small regression run.

## Frozen run protocol

On a clean Ubuntu GitHub-hosted runner:

1. clone the exact Pencil Code commit above;
2. set `PENCIL_HOME` and prepend `$PENCIL_HOME/bin` to `PATH`;
3. enter `samples/mdwarf`;
4. create a local `data/` directory;
5. execute the documented Pencil sequence `pc_setupsrc`, `pc_build`, `pc_start`, `pc_run` under a hard workflow timeout;
6. inspect the resulting latest `var.dat` with the Pencil Python reader from the same pinned commit;
7. request/derive `bb = curl(aa)` through the official reader rather than reconstructing a magnetic field with NMIR-specific finite differences.

If current compiler/toolchain incompatibility prevents execution, classify the run as infrastructure/code-compatibility BLOCKED/FAIL and do not modify the frozen physical setup after seeing the failure merely to obtain a green result.

## Frozen extraction gates

A PASS requires all of the following:

1. pinned external commit identity matches exactly;
2. sample build completes without changing its physical run parameters;
3. `pc_start` and `pc_run` complete;
4. at least one valid full-state Pencil VAR snapshot is produced;
5. Pencil Python reader returns finite coordinate arrays and a finite three-component magnetic field `bb`;
6. `bb.shape[0] == 3` and each spatial dimension is nonzero;
7. at least one `abs(B)` value is strictly nonzero;
8. no NaN/Inf occurs in `bb`;
9. the result record reports snapshot time, `bb` shape, min/max/RMS `|B|`, coordinate extents and the exact external commit;
10. no Betelgeuse label is attached to the field.

## Optional numerical integrity metric

If the official reader and grid geometry make it straightforward, record a discrete `div(B)` diagnostic. It is descriptive unless a divergence tolerance is preregistered separately; failure to define a coordinate-appropriate divergence operator must not be patched post-result.

## PASS ceiling

`PASS_0103S_PENCIL_MDWARF_VECTOR_INTERFACE_NONTERMINAL`

A PASS proves only that a reproducible full 3-D MHD magnetic vector state can enter the NMIR spin-flavor field interface from a pinned external model. The Betelgeuse-specific terminal ceiling remains:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.
