# 0105a4d — DeepCore B4RITM original-representation byte-lock result

Date: 2026-09-10
Gate: `NMIR-V2-0105A4D`
Classification: **`PASS_0105A4D_DEEPCORE_B4RITM_ORIGINAL_REPRESENTATION_BYTE_LOCK_NONDISCOVERY`**

This is an authority/provenance result only. It is not a BSM residual, significance, model preference, or discovery result.

## Frozen authority

- Dataset DOI: `10.7910/DVN/B4RITM`
- Release: `1.0`, `RELEASED`
- Forbidden substitution: `10.7910/DVN/QKL28Z`
- Preregistration commit: `f8265c78e6caed6615eb6a1f620e7a711b629c9c`
- Implementation commit: `0b8b086f8b3b7d2ab2b784b9f95a52a4618f957a`
- Tests commit: `be12270097e275deb684adb21bfbefd1da7fd064`
- Workflow registration commit: `589eb17bd348097f4f0cf293d46c99a8cdaeae4d`
- Trigger-only commit, no scientific-contract change: `7fa83c288181c20c9e9417fc231bee00767404b9`
- Parent raw metadata SHA256: `50b0e1ed9d939d1a2b2f4e497dd3841c9c73eb8ecaa4a589268d3ba75ad3d0db`
- Parent normalized inventory SHA256: `1cfc666849a7cf200ef4cdaf47b926e9ece44b63a92d4e29710c5a0cba441baa`

## Hosted execution

- Workflow run: `34428678301`
- Job: `102719279680` (`original-byte-lock`)
- Head SHA: `7fa83c288181c20c9e9417fc231bee00767404b9`
- Job conclusion: `success`
- Artifact: `10133622404`, `nmir-v2-0105a4d-deepcore-b4ritm-original-byte-lock`
- Artifact digest reported by GitHub: `sha256:ec78634fd8c07ec1f36d5ce5922008dbfb1457fdcf0204f4df924e3724223436`
- Inner canonical manifest SHA256: `e0c1d4d88234160b7ee443cea3d38979c84d4f9c3ac50dc12f815c60f7fdda1c`

The dedicated representation/fail-closed tests passed before the live fetch. The live byte-hash step, explicit PASS assertions, and artifact upload all completed successfully.

Independent artifact inspection after download confirmed that the manifest itself carries the exact PASS label and all frozen guards. The experimental payload bytes were not committed or uploaded by the workflow.

## Exact byte ledger

| file id | consumed representation | expected/original name | SHA256 of consumed bytes |
|---:|---|---|---|
| 11646859 | saved-original | `data.csv` | `68bdc3db7404d497a0c439fb2d95ab0b7ed9942ac4ed6dde236e761413360cfd` |
| 11674675 | direct | `example.ipynb` | `900acac6e74cced45e0b894017340b7aa0a64ccb615365b865cc7b4ae87be1a3` |
| 11646858 | saved-original | `hs_numu_cc.csv` | `115faa79d37e36da7a170f26003aa10fed8b4f74cc4f05c8bc80a14c4c66c80a` |
| 11646854 | saved-original | `hs_nu_nc_nue_cc.csv` | `b0dad7154fd0f1ca0b76c04f47bcdfd56de5689ac882238a1b5e9e4033e248be` |
| 11646853 | saved-original | `hs_nutau_cc.csv` | `811ee4547e60a8e1ebe9037f6b6c48a2c4720b20daa49298af888aa384479f11` |
| 11646851 | saved-original | `mc_mu.csv` | `b4efdd740b85bbfe5a8365d5f82284946620af3d355de795bb5bf9606958f28c` |
| 11646852 | saved-original | `mc_nue_cc.csv` | `a968f274726dc4b316c6eb9d93901dacda13dc92528d1081887fd473a958cf8b` |
| 11646856 | saved-original | `mc_numu_cc.csv` | `a3bc53223d8e6f9b9e43e36d277550976631315f5a00771dff2c588120410724` |
| 11646850 | saved-original | `mc_nu_nc.csv` | `aab94b5e0e285135471d5eb7b27db3f818f40c423ed95f27af6d3ba06becf355` |
| 11646855 | saved-original | `mc_nutau_cc.csv` | `7e8596016ae4a9fca8e2d805c132f3b89ac9a6eacfb1ea828a7347f6c0184f07` |
| 11674676 | direct | `readme.md` | `0f8e7bbc6059d18376843370e36e98a0cfa69fbc4bd767df694c6d65f861149f` |

For every one of the 11 rows, the consumed byte count matched the prospectively frozen original/direct byte count and the computed MD5 matched the Dataverse provider MD5. Exactly nine requests used `?format=original`; exactly two non-tabular files used the direct route.

## Gate audit

All are true in the validated manifest:

- exact B4RITM identity and release;
- exact 11-file representation metadata;
- exact `9 saved-original + 2 direct` split;
- no QKL28Z substitution;
- 11/11 provider MD5 matches;
- 11/11 byte-size matches;
- 11/11 independent SHA256 values present;
- request representation modes exact;
- scientific payload content was not parsed;
- observed BSM residual execution remained locked;
- BSM interpretation remained locked.

Baseline repository-integrity CI on the trigger head also completed successfully: run/job `34428678229/102719279393`, including full `python -m pytest -q` and `python -m nmir.baseline`. This is reproducibility evidence only and is not an additional scientific PASS.

## Scientific meaning

0105a4d closes the exact-byte authority problem for the selected DeepCore `B4RITM` Stage-A propagation dataset, including the distinction between Dataverse archival tabular representations and Saved Original CSV bytes. The previous 0105a4c checksum block remains valid historical evidence explaining why the Saved Original route was required; it is not rewritten as a PASS.

This result does **not** show any anomalous residual and does not support NSI, a light mediator, sterile neutrinos, or other BSM physics.

## Authorization boundary

`observed_residual_execution_allowed = false` remains mandatory.

This PASS authorizes only a separately prospectively preregistered DeepCore standard-3nu/null-reproduction gate. That gate must reproduce the collaboration-authority baseline/likelihood behavior with frozen event binning, standard oscillation treatment, nuisance/systematic response semantics, objective definition and acceptance thresholds before any model-agnostic or BSM residual is inspected.
