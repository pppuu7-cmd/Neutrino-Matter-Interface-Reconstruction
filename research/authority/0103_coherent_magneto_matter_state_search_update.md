# 0103 coherent Betelgeuse magneto-matter state search — update

Date: 2026-09-12
Status: `PUBLIC_INDEXED_COHERENT_MAGNETO_MATTER_STATE_NOT_RECOVERED`
Benchmark: `NMIR-BENCHMARK-0103`

## Target

Recover a machine-readable Betelgeuse or defensibly Betelgeuse-like MHD state in which the vector magnetic field and matter variables are co-registered in one snapshot/state, with enough metadata to define coordinates, units, composition/electron-density semantics and a deterministic neutrino ray.

## Search result

Targeted indexed searches were repeated for Dorch 2004, Pencil Code, Betelgeuse MHD snapshot/data/archive terms, the historical model identifier `dst33gm06n03`, and public data/archive terminology. The search recovered publications, documentation and figure-level material, but no indexed downloadable full-state dataset satisfying the terminal contract.

The following distinctions remain critical:

1. Dorch 2004 establishes a full 3-D nonlinear MHD star-in-a-box simulation of a red supergiant with Betelgeuse-like parameters using the Pencil Code. It establishes that relevant numerical states existed, not that a machine-readable full state is publicly indexed today.
2. The historical identifier `dst33gm06n03` belongs to the earlier Freytag hydrodynamic flow sequence used as input for a kinematic dynamo study. The published description states a `127^3` grid and 120 flow snapshots spanning 7.5 years. This is hydrodynamic input, not the nonlinear Dorch 2004 magnetic state, and by itself cannot supply terminal `B_perp(s)`.
3. Current public Pencil Code infrastructure contains reproducible star-in-a-box giant and mdwarf examples, useful for interface regression, but these cannot silently substitute for the historical Betelgeuse-specific nonlinear state.

## Scientific consequence

No terminal Betelgeuse probability may be computed from surface-field numbers, figures, arbitrary radial laws, or a mixed magnetic/matter model assembled from unrelated simulations.

After 0103M PASS, the technical pipeline is ready for a coherent state. The remaining narrow blocker is external data authority/provenance:

`BLOCKED_0103_BETELGEUSE_COHERENT_MAGNETO_MATTER_STATE_AUTHORITY`

This is an external-data limitation, not a physics FAIL. The author/institutional archive route remains scientifically legitimate; absence from indexed web search is not evidence that the original numerical state no longer exists.
