# 0103G Pencil giant star-in-a-box vector-field interface preregistration

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103G`
Status: PREREGISTERED MODEL-CONDITIONAL GIANT-STAR INTERFACE AUDIT

## Scope

0103G is a deliberately separate model-conditional benchmark using the public Pencil Code sample `samples/star-in-a-box-giant-Kprof`. Its purpose is to test a reproducible **giant-star MHD** vector-field interface closer in geometry/class to the Dorch red-supergiant problem than the 0103S `mdwarf` regression fixture.

0103G is **not Betelgeuse authority** and cannot replace the missing Dorch (2004) nonlinear state.

## Frozen external source

Repository: `pencil-code/pencil-code`
Commit: `1a672b5cb2983b3e286503a789dd36bf7d6d1141`
Sample: `samples/star-in-a-box-giant-Kprof`

Frozen repository configuration includes:

- `64 x 64 x 64` grid;
- MPI decomposition `2 x 2 x 2` (8 ranks);
- non-periodic `2.2^3` Cartesian box from `-1.1` to `+1.1` on each axis;
- `lsphere_in_a_box = T`, `Rstar=1`;
- initial condition module `star_in_a_box_poly`;
- gravity potential `RGB-1Msun-11.7`;
- magnetic module enabled;
- magnetic vector-potential initialization `gaussian-noise-rprof`, amplitude `1e-4`;
- constant magnetic diffusivity `eta=2e-3`;
- rotation rate `Omega=1`;
- run length `nt=10` with the unmodified sample settings.

No parameter above may be changed after observing results to make a gate pass.

## Frozen execution

1. Clone the exact external commit.
2. Enter the frozen giant sample without editing `start.in`, `run.in`, `src/Makefile.local` or `src/cparam.local`.
3. Run the normal `pc_setupsrc`, `pc_build`, `pc_start`, `pc_run` sequence.
4. Read the native final `VAR` snapshot with the Python reader from the same external commit.
5. Derive the full Cartesian `bb = curl(aa)` using the official Pencil reader.
6. Record all three components, coordinates, snapshot time and `|B|` statistics.

If an MPI launcher refuses 8 ranks solely because the hosted runner advertises fewer physical slots, that is infrastructure-only. A later rerun may set the launcher to oversubscribe while preserving all scientific/sample parameters; such a rerun must be explicitly identified.

## Gates

PASS requires:

1. exact external commit match;
2. source setup/build success without sample-parameter edits;
3. start/run success for the frozen 10-step sample;
4. valid native full-state snapshot;
5. `bb` has shape `[3, nz, ny, nx]` with all spatial dimensions nonzero;
6. every `bb` entry is finite;
7. at least one field component is nonzero;
8. finite coordinate arrays are recovered for x/y/z;
9. output records snapshot time, grid shape, coordinate extents, `|B| min/max/RMS`;
10. result carries the hard scope marker `MODEL_CONDITIONAL_GIANT_NOT_BETELGEUSE` and `betelgeuse_authority_closed=false`.

## PASS ceiling

`PASS_0103G_PENCIL_GIANT_VECTOR_INTERFACE_NONTERMINAL`

PASS would demonstrate that NMIR can ingest a reproducible 3-D MHD vector field from an explicit public giant-star star-in-a-box calculation. It would not establish Betelgeuse's true internal field and would not lift

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.
