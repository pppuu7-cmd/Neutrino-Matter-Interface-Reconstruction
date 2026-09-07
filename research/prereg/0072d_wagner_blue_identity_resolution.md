# NMIR 0072d preregistration — Wagner blue-chain identity resolution

Date frozen: 2026-09-07
Parent result: 0072c `PARTIAL_PASS_WAGNER_VECTOR_CURVES`.
Status at freeze: four blue vector chains are already structurally materialized, but none is named. The 0072c result is immutable and is not reclassified retroactively.

## New primary-source fact motivating this follow-up
Direct inspection of primary Wagner et al. Figure 6 (not a secondary digitization) shows four blue trace/label instances in the left panel: `EW99` once, `EW94` twice (one short-/intermediate-range trace and one separate long-range trace), and `EW` once. The figure caption names three Eot-Wash experiment families, but does not state that each family must be represented by exactly one connected vector path. Therefore the four-chain topology found by 0072c is source-consistent if and only if two disconnected chains can be assigned to EW94 without inventing a bridge between them.

No numerical coordinate has been read manually from the raster/PDF to make this assignment. Primary Figure 6 is used only for semantic label multiplicity and vertical identity order.

## Frozen inputs
- `data/wagner_named_curves_0072c.json` — primary vector geometry transformed using the already-PASS 0072b axes.
- `data/wagner_blue_chains_0072d.json` — structural summary only.
- Primary source: Wagner et al., arXiv:1207.2442v1, Figure 6 and its caption.

## Frozen identity algorithm
1. Require exactly four unresolved blue connected chains from 0072c and no dropped blue fragment.
2. Find the subset of exactly three blue chains having a non-empty common EPS-x interval. This is the short/intermediate-range triple. If more than one distinct triple qualifies, classification is identity FAIL.
3. Sample 101 equally spaced x positions across that common interval and linearly interpolate each chain only within its own connected path. No gap crossing is allowed.
4. Require the pointwise vertical ordering to be identical at all 101 samples with no crossing/tie closer than `1e-6` EPS-y. Assign within this triple, from highest y (weakest upper bound) to lowest y (strongest): `EW99`, `EW94_short`, `EW`.
5. The fourth chain is a candidate `EW94_long`. It must have a non-empty common x interval with the assigned `EW` chain. Across 101 equally spaced x samples in that overlap, require `y(EW94_long) > y(EW)` at every sample by at least `1e-6` EPS-y. This is the source-consistent long-range ordering shown by Figure 6.
6. Preserve `EW94_short` and `EW94_long` as two disconnected components carrying the same experiment-family label. **Never merge their vertices or interpolate across their gap.**
7. All physical coordinates remain exactly those already transformed under 0072b; 0072d changes semantic labels only and must not refit axes or alter points.

## Classification
- `PASS_WAGNER_BLUE_IDENTITIES_RESOLVED` if all frozen conditions hold. Combined with the already-resolved Princeton, Moscow and two LLR chains, this completes the seven published constraint identities while preserving eight connected path components because EW94 has two components.
- `SCIENTIFIC_FAIL_WAGNER_BLUE_IDENTITY` if triple uniqueness, stable ordering, or long-range EW94/EW ordering fails.
- `INFRASTRUCTURE_FAIL` only if the frozen input cannot be read or the deterministic calculation cannot execute.

## Consequence on PASS
Write a machine-readable identity ledger and a new immutable 0072d result. The Wagner family then counts as a primary machine-readable contour-family PASS for 0072, but **not** as a global B-L allowed-region PASS. Continue with independent direct-detection and cosmology/stellar primary families. Do not fill the EW94 disconnected gap and do not perform an NMIR BSM enhancement scan yet.
