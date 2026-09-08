# 0089e-r2 — G9 mesh-free narrow-preimage replica

Date: 2026-09-08

## Prospective authority
Frozen preregistration: `research/prereg/0089e_g9_mesh_free_narrow_preimage_replica.md`, commit `da8e7c5664cf0980b3490926036231bea9270fcb`.

The r1 scientific command exceeded the original 45-minute workflow timeout before producing a scientific artifact and was classified as infrastructure failure. The only r2 execution change was workflow timeout `45 -> 180` minutes at commit `466f6fee04f6052e4c758cb613290f33610373e8`; H0-H4 scientific code, precision levels, topology controls, radii, formulas and thresholds were unchanged.

## Authoritative hosted execution
- head: `466f6fee04f6052e4c758cb613290f33610373e8`
- run: `34227872401`
- job: `102066360966`
- artifact: `10061342281` (`nmir-g9-0089e-mesh-free-narrow-preimage-replica`)
- artifact ZIP SHA256: `d76b3937a9ea0fcced50769c8098642b96e1345dd1f5b77bbd1754f53c104bb3`
- raw JSON SHA256: `010a9f55c11c9bb7c7020293f2ebef9ce3e00b4dc8401ade700a417c327ba56e`
- dedicated tests: `4 passed in 0.22s`
- exact scientific command completed after about 113 minutes.

ZIP and inner JSON hashes were independently recomputed after artifact download and match the hosted log/artifact digest.

## Frozen H0-H4 results
H0 PASS:
- pinned Model-S blob SHA1 `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`
- all three preregistered toys PASS (`monotone_linear`, `narrow_linear`, `one_turn_quadratic`).

H1 PASS:
- maximum `|x_60-x_90| = 1.6093783306292206e-62`, threshold `2e-15`;
- maximum root residual / frozen residual limit ratio `8.450346354645747e-4 < 1`;
- 60- and 90-digit topologies identical.

H2 PASS:
- all area invariants PASS;
- maximum 60-vs-90 relative area difference `6.149719436396269e-54`, threshold `5e-7`.

H3 PASS:
- existing double-precision branch construction and independent 90-digit mesh-free replica agree in interval topology/parent identity;
- maximum endpoint absolute x difference `4.4593495562850194e-13`, threshold `2e-11`;
- maximum area relative difference `6.431489360829985e-5`, threshold `0.005`.

H4 PASS, inherited one-ring guard at `x0=0.024`:
- radius 100 cm: relative error `5.907334718856089e-10`;
- radius 1000 cm: `4.375807481078149e-11`;
- radius 10000 cm: `6.7827105540637515e-12`;
all far below the frozen `0.5%` criterion.

## Classification
`PASS_G9_MESH_FREE_NARROW_PREIMAGE_REPLICA`

The narrow accepted preimages that defeated the fixed global midpoint meshes in 0089d are independently reproducible by a scan-free 60/90-digit construction. Thus 0089d remains terminally `BLOCKED_G9_CONTINUOUS_MAP_MONOTONE_KERNEL` for its fixed-mesh method, but the narrow-preimage geometry itself is no longer unresolved.

This PASS authorizes only a **separately prospectively preregistered** finite-source/alignment/persistent-source gate using the certified continuous-map branch geometry. It does not retroactively promote 0089d, does not change Model-S physics, and does not authorize BSM response/enhancement.
