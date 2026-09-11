# 0103 Betelgeuse dataset-identifier search

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Status: `PUBLICLY_INDEXED_PATHWISE_VECTOR_DATA_NOT_RECOVERED`

## New concrete lead

A dedicated source search recovered a specific historical model identifier from the predecessor Dorch & Freytag Betelgeuse dynamo work (`astro-ph/0208523`):

- model identifier: `dst33gm06n03`;
- grid: `127^3`;
- input flow sequence: 120 snapshots;
- covered simulated interval: 7.5 years.

This is much more useful than an unspecific statement that 'simulation data existed', because future archive/contact searches can target an exact identifier.

## Critical scope guard

`dst33gm06n03` is the **prescribed hydrodynamic flow input** used in the earlier kinematic dynamo study. It must not be silently equated with the nonlinear Pencil-Code magnetic state published by Dorch (2004). Recovering this RHD flow sequence alone would therefore still not supply the terminal 0103 `B(x,y,z)` magnetic snapshot.

The 2002 work does show that the associated dynamo calculation produced a three-dimensional magnetic geometry, including volume renderings and a depth-dependent qualitative topology. But publication figures are not a machine-readable vector field and cannot be converted into `B_perp(r)` without uncontrolled reconstruction.

## Indexed archive search performed

Exact-identifier searches for `dst33gm06n03` were performed broadly and specifically against common public/research-code locations, including searches scoped to Zenodo, CDS/VizieR and GitHub. No public machine-readable dataset entry was recovered by those indexed searches.

This is an **absence-of-recovery statement**, not proof that the files no longer exist or were never archived. They may survive in author/institution storage or under a different identifier.

## Additional reproducibility lead

The CO5BOLD documentation contains explicit Betelgeuse-style full-star parameter-file examples and historical model file naming conventions (for example later `st35...` models). Bernd Freytag's current Uppsala research page still links CO5BOLD materials and Betelgeuse-like simulation movies. These are useful provenance/contact leads but do not expose the required magnetic vector snapshot.

## Consequence for 0103

The authority status is unchanged:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`.

The next highest-information acquisition route is now narrower:

1. target author/institution archives using the exact `dst33gm06n03` identifier for the historical RHD branch;
2. separately target Dorch's 2004 nonlinear Pencil-Code run state or any successor archived magnetic `B(x,y,z)` output;
3. accept only data with vector components, coordinates/grid metadata, snapshot identity/time, and enough provenance to define a neutrino ray prospectively;
4. do not substitute CO5BOLD hydrodynamic snapshots, simulation movies, raster figures, or surface field amplitudes for a magnetic vector state.
