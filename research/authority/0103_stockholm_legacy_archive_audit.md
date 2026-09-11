# 0103 Stockholm legacy archive audit

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Status: `LEGACY_PUBLICATION_FIGURE_ARCHIVE_SURVIVES_VECTOR_STATE_NOT_RECOVERED`

## Purpose

Target surviving Stockholm Observatory web/FTP material associated with S. B. F. Dorch and the 2002-2004 Betelgeuse dynamo work, looking specifically for machine-readable simulation state rather than publications alone.

## Recovered public legacy traces

The old `ftp.astro.su.se` server remains publicly indexed and still exposes Dorch-era publication material. In addition, the surviving directory

`https://ftp.astro.su.se/peter/temp/`

contains PostScript files timestamped 2004-01-16:

- `Bfigure5.ps` — 5.0 MB
- `Bfigure6.ps` — 3.8 MB
- `Bfigure7a.ps` — 1.8 MB
- `Bfigure7b.ps` — 2.1 MB
- `Bfigure8a.ps` — 379 KB
- `Bfigure8b.ps` — 284 KB
- `color1.ps` — 460 KB

The names and timing are consistent with a live legacy figure-production archive from the period of the Dorch Betelgeuse dynamo work. This is useful provenance evidence that some research material survived on the historical server.

## What was not recovered

Targeted indexed searches did not recover a publicly exposed machine-readable nonlinear Betelgeuse magnetic vector state under obvious forms such as:

- Pencil `VAR*`/`var.dat` snapshots;
- `.dat`/`.bin` grid dumps;
- tar/gzip archives containing a run directory;
- a named 3-D `B(x,y,z)` snapshot with coordinate metadata;
- an archived exact Pencil run directory corresponding to the 2004 nonlinear model.

The exact predecessor hydrodynamic identifier `dst33gm06n03` remains known, but it refers to the earlier CO5BOLD/RHD flow input and not to the nonlinear 2004 magnetic state.

## Scope guard

The recovered PostScript files must not be rasterized or vector-graphics-parsed into a terminal magnetic field. Even if a figure encodes surface color values, it lacks the complete internal vector field, trajectory orientation and machine-readable state required to derive `B_perp(r)` without reconstruction assumptions.

Therefore the archive result is:

- historical/publication provenance: **strengthened**;
- evidence that legacy server material survives: **YES**;
- exact nonlinear 3-D magnetic vector snapshot: **NOT RECOVERED**;
- Betelgeuse pathwise field authority: **STILL BLOCKED**.

## Next acquisition route

The highest-information remaining archive route is no longer generic web search. It is targeted recovery through:

1. unindexed surviving Stockholm/University storage associated with the historical account/run;
2. author or institutional archive contact using exact publication/run context;
3. historical Pencil Code/SVN run directories or backup media from the 2003-2004 period;
4. any successor deposit that exposes full vector components plus grid, snapshot time and run provenance.

Until such a state is recovered, the terminal Betelgeuse-specific status remains

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.
