# 0103 Dorch nonlinear Betelgeuse archive acquisition contract

Date: 2026-09-12
Benchmark: `NMIR-BENCHMARK-0103`
Status: `ACTIONABLE_EXTERNAL_DATA_ACQUISITION_ROUTE`

## Why this contract exists

The remaining terminal blocker is not a missing scalar field strength. NMIR needs a path-resolved **vector** magnetic state from the nonlinear 2004 Betelgeuse-like Pencil Code calculation, with enough numerical metadata to derive `B_perp(r)` prospectively.

A generic request for “the data behind the paper” is too ambiguous. This document freezes the minimum useful acquisition payload before any new archive material is obtained.

## Publication/run anchors

Target publication:

S. B. F. Dorch, *Magnetic activity in late-type giant stars: Numerical MHD simulations of non-linear dynamo action in Betelgeuse*, A&A 423, 1101–1107 (2004), DOI `10.1051/0004-6361:20040435`, arXiv `astro-ph/0403321`.

Published numerical anchors useful for identifying the correct run/state:

- full nonlinear MHD `star-in-a-box` Pencil Code calculation;
- stellar model parameters `R = 640 R_sun`, `M = 5 M_sun`;
- results in the paper use a `128^3` uniform grid;
- nominal spatial resolution `Delta x = 15 R_sun`;
- chosen surface rotation velocity `5 km/s`;
- Figure 8 surface magnetic map is from a nonlinear snapshot at `t = 695 yr`;
- Figure 7 magnetic power spectrum is from `t = 732 yr`.

The first preferred recovery target is therefore the full numerical state used at or nearest `t=695 yr`; the `t=732 yr` state is a second high-value target.

## Minimum acceptable payload — Tier A

Any one of the following is sufficient to begin a terminally eligible field-authority audit:

1. a native Pencil Code full-state snapshot (`VAR*`, `var.dat`, or historical equivalent) plus the corresponding run metadata needed to read it; or
2. a machine-readable array containing the three magnetic-vector components `Bx, By, Bz` on the full 3-D grid plus coordinate arrays and units; or
3. a machine-readable three-component vector potential `Ax, Ay, Az` on the full grid plus coordinates, units and enough boundary/grid metadata to reconstruct `B=curl(A)` using the original Pencil convention.

## Required metadata

The payload must identify, directly or through recoverable run files:

- snapshot time or iteration;
- grid dimensions and coordinate ordering;
- physical/code-unit conversion for length and magnetic field;
- box extents and stellar radius in box coordinates;
- vector-component convention;
- boundary-condition convention;
- Pencil Code revision/version if available;
- enough run/configuration files (`start.in`, `run.in`, local Makefile/cparam or historical equivalents) to associate the snapshot with the published nonlinear model.

Strongly preferred accompanying fields:

- density `rho` or `lnrho` on the same grid;
- temperature/entropy on the same grid;
- velocity vector;
- any snapshot/run log identifying saturation epoch.

These are useful for co-registration and provenance but the vector magnetic state itself is the critical requirement.

## Acceptance gates after receipt

Before any spin-flavor propagation is run, the recovered payload must pass a separate preregistered audit requiring:

1. immutable byte hashes for every supplied file;
2. an unambiguous association with the nonlinear Betelgeuse-like calculation of the 2004 paper;
3. a finite three-component vector field on a 3-D coordinate grid;
4. nonzero field support;
5. declared units or a reproducible unit conversion;
6. a frozen snapshot identity/time;
7. a frozen neutrino-ray definition selected **before** examining conversion probabilities;
8. a frozen interpolation/regridding rule;
9. explicit separation between the model field and empirical Betelgeuse observations.

If only figures, movies, surface maps, scalar RMS/max histories, or a 1-D radial average are recovered, the terminal field-authority gate remains blocked.

## Current acquisition route

The original author, Bertil Dorch, has a current University of Southern Denmark institutional profile and remains professionally active with stated research interests including stellar/solar magnetism, MHD, dynamos, computational astrophysics and Betelgeuse. Therefore direct author/institutional archive recovery is currently an actionable route rather than a hypothetical one.

The request should specifically ask whether any of the following survive in personal/institutional backups:

- the nonlinear 2004 Pencil run directory;
- full `VAR`/snapshot state around `t=695 yr` or `t=732 yr`;
- raw `A(x,y,z)` or `B(x,y,z)` arrays;
- historical code revision/configuration files;
- an archive/tape/disk location from which the run could be restored.

## Classification consequence

Until that acquisition route is exhausted or succeeds, NMIR should **not** close 0103 as permanently data-limited.

Current status remains:

`BLOCKED_0103_BETELGEUSE_PATHWISE_VECTOR_FIELD_AUTHORITY`

with an explicit actionable external acquisition path.
