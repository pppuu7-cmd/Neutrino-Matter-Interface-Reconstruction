# 0105a5b R1 — verified DeepCore release-document extraction result

Date: 2026-09-10
Parent gate: `0105a5b`
Classification: **`PASS_0105A5B_R1_VERIFIED_DOC_EXTRACTION_NONDISCOVERY`**

This is a byte-first documentation extraction result only. It is not the terminal 0105a5b null-reproduction result, not a residual analysis, and not evidence for or against BSM physics.

## Hosted provenance

- Frozen 0105a5b preregistration: `1b666e4d3621727b2ce707c28f9494ae853ef817`
- R1 extraction implementation: `9163dc53c10789aa06f89bf3fcb9b127d0be902d`
- R1 tests: `9fc71739b37af50635731c943fc9cac951e29609`
- R1 workflow head: `50636920ac3868623a948df9f36df6f0302b3e78`
- Workflow run/job: `34429098726/102720565219`
- Artifact: `10133772067`, `nmir-v2-0105a5b-r1-deepcore-release-semantics`
- Artifact digest: `sha256:21d2a3c2675af76775704cbabc3825d7faa68f00a5f2fb3d6e0edbe1b4f45ea6`
- Inner extraction-manifest SHA256: `fb9f1f03cd63a8dca1554a9903366188fb5668783b9ba7c06c3062391da5fcdc`

Both consumed documentation assets were completely hashed before either was decoded or parsed:

- `readme.md`, file id `11674676`: SHA256 `0f8e7bbc6059d18376843370e36e98a0cfa69fbc4bd767df694c6d65f861149f`;
- `example.ipynb`, file id `11674675`: SHA256 `900acac6e74cced45e0b894017340b7aa0a64ccb615365b865cc7b4ae87be1a3`.

Both SHA256, provider MD5 and byte-size identities matched the frozen 0105a4d authority ledger. No event CSV was opened in this R1 extraction.

## Verified release semantics obtained

The byte-locked release documentation specifies:

- `data.csv` contains observed count plus `pid`, `reco_coszen`, `reco_energy` in the analysis binning;
- four neutrino MC files contain event-level reconstructed variables, `pdg`, `true_energy`, `true_coszen`, generator `weight`, reaction `type` and `interaction`;
- non-DIS CC events carry `MaCCQE_linear`, `MaCCQE_quad`, `MaCCRES_linear`, `MaCCRES_quad` reweighting coefficients;
- DIS events carry `Q2`, `W`, `x`, `y` kinematic variables;
- `mc_mu.csv` carries atmospheric-muon bin counts and absolute uncertainties;
- three detector hypersurface files provide multiplicative corrections, binned also in atmospheric mass splitting, for five detector/calibration parameters;
- the exact release binning is 10 reconstructed-energy bins, 10 reconstructed-coszen bins, and 2 PID bins, hence 200 analysis bins.

The included example notebook demonstrates data loading, daemonflux evaluation, a two-flavor oscillation approximation, detector-hypersurface interpolation, atmospheric-muon normalization and a simplified optimization path.

## Critical completeness finding

The verified notebook explicitly states that its example is **not intended to fully reproduce the paper result**. It uses a two-flavor approximation and intentionally omits many systematic uncertainties, including flux, cross-section, atmospheric-muon-scale and normalization treatment in the complete collaboration sense.

Therefore:

- the notebook itself cannot be promoted to the frozen 0105a5b full standard-3nu likelihood implementation;
- successful execution of the notebook would not satisfy R2 or R3;
- the complete 18-nuisance model must be reconstructed only from the byte-locked schemas plus the collaboration publication and independently audited public dependencies;
- if any required nuisance response is not reproducibly determined by those authorities, the correct classification is `BLOCKED_0105A5B_RELEASE_SEMANTICS_INCOMPLETE`, not an invented or simplified replacement.

## Guards retained

Artifact inspection confirms:

- `event_csv_opened = false`;
- `event_rows_parsed = false`;
- `observed_residual_execution_allowed = false`;
- `bsm_interpretation_allowed = false`.

## Next authorized action

Continue R1 with a byte-first **machine-readable schema/completeness audit** of the nine CSV assets. Verify all 0105a4d SHA256 values before parsing; then inspect only schemas, bin coordinates, encoded systematic-response fields and structural counts needed to decide whether R2 can be implemented under the frozen 18-nuisance contract. Do not compute an observed-minus-null residual or fit BSM parameters.
