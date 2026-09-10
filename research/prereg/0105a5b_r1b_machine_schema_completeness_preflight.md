# 0105a5b R1b — DeepCore B4RITM machine-schema completeness audit preflight

Date frozen: 2026-09-10
Parent: `0105a5b` and verified-document extraction `0105a5b R1`
Scope: byte-first schema and structural-authority audit only; no oscillation fit and no residual.

## Purpose

Determine, before any standard-3nu optimization, exactly which parts of the frozen 0105a5b null model are natively reconstructible from the byte-locked B4RITM CSV release and which require separately pinned external computational authority.

This gate must not infer missing response functions from observed data.

## Exact byte authority

Before parsing any CSV, all nine Saved Original CSV payloads must be fetched through Dataverse `?format=original` and match the 0105a4d SHA256 ledger exactly:

- `data.csv` `68bdc3db7404d497a0c439fb2d95ab0b7ed9942ac4ed6dde236e761413360cfd`
- `hs_numu_cc.csv` `115faa79d37e36da7a170f26003aa10fed8b4f74cc4f05c8bc80a14c4c66c80a`
- `hs_nu_nc_nue_cc.csv` `b0dad7154fd0f1ca0b76c04f47bcdfd56de5689ac882238a1b5e9e4033e248be`
- `hs_nutau_cc.csv` `811ee4547e60a8e1ebe9037f6b6c48a2c4720b20daa49298af888aa384479f11`
- `mc_mu.csv` `b4efdd740b85bbfe5a8365d5f82284946620af3d355de795bb5bf9606958f28c`
- `mc_nue_cc.csv` `a968f274726dc4b316c6eb9d93901dacda13dc92528d1081887fd473a958cf8b`
- `mc_numu_cc.csv` `a3bc53223d8e6f9b9e43e36d277550976631315f5a00771dff2c588120410724`
- `mc_nu_nc.csv` `aab94b5e0e285135471d5eb7b27db3f818f40c423ed95f27af6d3ba06becf355`
- `mc_nutau_cc.csv` `7e8596016ae4a9fca8e2d805c132f3b89ac9a6eacfb1ea828a7347f6c0184f07`

Any mismatch blocks parsing.

## Frozen schema expectations from verified release docs

`data.csv` must contain at least:
`count`, `pid`, `reco_coszen`, `reco_energy`.

Every neutrino MC file must contain at least:
`reco_energy`, `reco_coszen`, `pid`, `pdg`, `true_energy`, `true_coszen`, `weight`, `type`, `interaction`, `MaCCQE_linear`, `MaCCQE_quad`, `MaCCRES_linear`, `MaCCRES_quad`, `Q2`, `W`, `x`, `y`.

`mc_mu.csv` must contain at least:
`count`, `abs_uncertainty`, `pid`, `reco_coszen`, `reco_energy`.

Every detector hypersurface file must contain at least:
`reco_energy`, `reco_coszen`, `pid`, `deltam31`, `intercept`, and one slope column for each of the five detector directions used by the verified notebook:
`dom_eff`, `hole_ice_p0`, `hole_ice_p1`, `bulk_ice_abs`, `bulk_ice_scatter`.

The verified readme spells the final scattering label as `bulk_ice_scat` while the verified executable notebook uses `bulk_ice_scatter`. R1b resolves only the machine-column identity; it must record this documentation alias explicitly rather than silently renaming it.

## Structural checks

Without constructing an observed-minus-expected residual, record:

- exact column lists and row counts for all nine CSVs;
- data row count, unique reconstructed coordinates and sum of `count`;
- whether the data define exactly 10 energy × 10 coszen × 2 PID = 200 unique analysis cells;
- whether every analysis coordinate in `data.csv` is unique;
- MC event row counts and presence of the frozen physics/reweight columns;
- muon-template row count, coordinate coverage, finite/nonnegative count and uncertainty fields;
- hypersurface row counts, distinct `deltam31` support values, analysis-coordinate coverage per `deltam31`, and detector-slope column identities.

Do not calculate an oscillated expectation, chi-square, nuisance best fit, or residual.

## Frozen nuisance-authority classification

For each of the 18 frozen nuisance directions, classify one of:

- `NATIVE_RELEASE_RESPONSE`: exact response is directly encoded in the byte-locked release;
- `NATIVE_RELEASE_PRIMITIVE_EXTERNAL_FORMULA`: release contains the event primitive, but a collaboration-publication formula/model is required;
- `EXTERNAL_COMPUTATIONAL_AUTHORITY_REQUIRED`: response is not encoded and requires an external program/table/parameterization to be pinned before R2/R3;
- `MISSING_AUTHORITY_BLOCKER`: neither release nor already frozen collaboration authority identifies a reproducible path.

Do not promote mere presence of `Q2/W/x/y` to an exact DIS-CSMS response unless the release provides the mapping. Do not promote `true_energy/true_coszen/pdg` to exact atmospheric-flux variations unless the Honda baseline and MCEq/Barr response construction are independently pinned. Do not treat the simplified two-flavor notebook as the publication's custom 3-flavor propagation engine.

## PASS semantics

`PASS_0105A5B_R1B_MACHINE_SCHEMA_AUDIT_NONDISCOVERY` requires exact byte identity, all frozen minimum schema fields, exact 200-cell observed bin structure and a complete per-nuisance authority classification.

This PASS does **not** mean the full 18-nuisance likelihood is executable. If any direction is `EXTERNAL_COMPUTATIONAL_AUTHORITY_REQUIRED`, the next gate must pin those dependencies before R2/R3. If any direction is `MISSING_AUTHORITY_BLOCKER`, terminal full-0105a5b reproduction remains BLOCKED unless a new external authority is prospectively admitted.

`observed_residual_execution_allowed = false` throughout.
