# 0103G Pencil giant star-in-a-box vector-field interface result

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103G`
Status: `PASS_0103G_PENCIL_GIANT_VECTOR_INTERFACE_NONTERMINAL`

Preregistration: `research/prereg/0103g_pencil_giant_vector_interface.md`
Workflow: `.github/workflows/0103g-pencil-giant-vector-interface.yml`
External repository: `pencil-code/pencil-code`
External commit: `1a672b5cb2983b3e286503a789dd36bf7d6d1141`

## Infrastructure history

The scientific/sample configuration remained unchanged through all attempts.

1. First run failed before execution because the hosted image lacked OpenMPI (`mpirun`, `mpif.h`).
2. Second run installed OpenMPI only; the sample compiled successfully but `pc_start` stopped because the hosted runner exposed only four hardware slots while the frozen sample requires eight MPI ranks.
3. The preregistration had explicitly allowed MPI oversubscription for exactly this infrastructure case. The authoritative run therefore added only `OMPI_MCA_rmaps_base_oversubscribe=1`; none of the four frozen sample files or physical parameters changed.

Frozen file SHA256 values, reverified in the authoritative run:

- `start.in`: `3ea3aef5acc7de73816887125bc128ef2cce9ae056f9f5f3ddd45d53f8bc8cf4`
- `run.in`: `72773e7f385cc3c092e3a2163312c46431949d6b3bb26f54fe61fc22cc645680`
- `src/Makefile.local`: `a278904dfda275f3fbe778699f9bfcc5b1c9d0c803459061bfcbe53af3584c8d`
- `src/cparam.local`: `89528b76c9e6c424fe64543bf685aad7364924cd891c797403ff315faade69b6`

## Authoritative execution

- NMIR head commit: `67223a3f96ce63f72f81c4b1be46488d9ea194d2`
- workflow run: `34651257225`
- job: `103433701596`
- conclusion: `success`
- evidence artifact ID: `10284082560`
- evidence artifact ZIP SHA256: `a2cba02a11777af297f7bdb9f91f74ff28d09fb07656f03ed2361a197b2a3d02`
- compiler: GNU Fortran 13.3.0
- MPI: Open MPI 4.1.6

## Frozen giant-star sample execution

The exact pinned public Pencil sample executed successfully with:

- grid `64 x 64 x 64`;
- Cartesian box `[-1.1,+1.1]^3`;
- 8 MPI ranks (`2 x 2 x 2` decomposition);
- `RGB-1Msun-11.7` gravity potential;
- magnetic module active;
- initial vector-potential noise from the frozen sample;
- constant resistivity and all other sample parameters unchanged;
- exactly 10 time steps.

The simulation wrote the final snapshot at

`t = 0.10545807208801390`

in the model's code units.

## Official reader extraction

The pinned Pencil Python reader derived `bb=curl(aa)` from the native final `var.dat` state.

Machine-readable result:

- `bb_shape = [3,64,64,64]`;
- `x,y,z` each span `[-1.1,+1.1]` with 64 points;
- all coordinates finite: `true`;
- all magnetic-vector components finite: `true`;
- nonzero magnetic field present: `true`;
- `|B|_min = 0.0`;
- `|B|_max = 0.006793491973397675`;
- RMS `|B| = 0.0008310479354408083`.

All preregistered gates passed.

The Pencil reader emitted its standard equidistant-grid warning when deriving curl without a separate grid object. This frozen sample uses a uniform Cartesian grid, so the warning does not introduce an unregistered interpolation or geometry change.

## Scientific meaning

0103G independently confirms on a public **giant-star sphere-in-a-box MHD** sample that NMIR can reproduce the complete chain from pinned external model source through native multi-rank Pencil state to a finite, nonzero, three-component 3-D magnetic vector field.

Together with 0103S and 0103P, the technical machinery now has three separate positive checks:

1. native Pencil 3-D magnetic-vector ingestion on `mdwarf` — PASS;
2. deterministic vector-to-pathwise `B_perp(s)` projection on a prospectively frozen ray — PASS;
3. native 3-D vector ingestion on an MPI giant-star model — PASS.

Thus the principal 0103 uncertainty is no longer a software, representation, MPI, vector-extraction, or path-projection problem.

## Strict scope guard

The public `star-in-a-box-giant-Kprof` sample is a model-conditional giant-star fixture using an `RGB-1Msun-11.7` potential. It is not Betelgeuse and is not the Dorch (2004) nonlinear red-supergiant calculation.

Therefore this PASS does not change the Betelgeuse terminal status:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.
