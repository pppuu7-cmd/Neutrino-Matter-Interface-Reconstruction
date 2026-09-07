# Iteration 0074 — COHERENT CsI+Ar B-L primary likelihood materialization (in progress)

Date: 2026-09-07
Status: **PARTIAL_PASS_COHERENT_INPUTS / PRIMARY_BYTES_HASH_PINNED / benchmark preregistered**
Frozen parent prereg: `research/prereg/0074_coherent_b_minus_l_likelihood_materialization.md`, commit `1e9ffedebf56a5c07e14676a3aed03bfebd4ae23`.

## Primary B-L likelihood authority
Cadeddu et al., JHEP 01 (2021) 116 / arXiv:2008.05022 provides the explicit B-L CEvNS convention and CsI/Ar fit structure. The published convention uses lepton charge `Q'_ell=1` and quark charge `Q'_f=-Q'_ell/3`; the amplitude contains the SM weak charge minus the B-L propagator term proportional to `g_Z'^2 [Z F_Z+N F_N]/(q^2+M_Z'^2)`. No universal-vector contour is relabelled as B-L.

Frozen Cadeddu source/exposure values remain Ar `r=(9±0.9)e-2`, `N_POT=13.7e22`, baseline `27.5 m`, target mass `24 kg`; CsI `r=0.08`, `N_POT=17.6e22`, baseline `19.3 m`, active mass `14.6 kg`. Radiatively corrected weak couplings are `gV^p(nu_e)=0.0401`, `gV^p(nu_mu)=0.0318`, `gV^n=-0.5094`, with Helm form factors and published radii.

CsI fit uses bins `i=4..15` with nuisance widths `0.112`, `0.25`, `0.051`. Ar Analysis A uses `0–120 keVee` in 12 bins, with CEvNS/PBRN/LBRN nuisance widths `13.4%/32%/100%` plus `1.7%` uncorrelated BRN energy-shape uncertainty.

## Accepted primary package materialization subgate
A fail-closed hosted materializer was added in commit `85bf59471b9b18ac7da823f9b242dfc2a67f8450`; workflow commit `bfe83c5b54507fb3677cf86e8ab994cd3dc0dfd9`. It queries only official Zenodo records `3903810` (Ar Analysis A) and `1228631` (CsI first observation), downloads every exposed file, verifies exact sizes and Zenodo MD5 checksums when supplied, computes SHA256 per file, and performs no likelihood/B-L calculation.

Hosted authority: run/job `34130108479/101767911241`. The raw job log was inspected after terminal success. All exposed files passed verification: 24 Ar files + 13 CsI files; 38 artifact members including the manifest. Artifact `10021726721`, size `867839` bytes, ZIP SHA256 `10f96287ec55907b851e2f9b9d6ee1f6046665cd8492e9a36107ef791e2f3220`. The artifact API reports the same digest, and an independently downloaded ZIP reproduced the identical SHA256.

Exact per-file hashes are frozen in `data/coherent_primary_packages_0074_manifest.json`, commit `52e281e8dd858ea53240b4d527f2f5ca00030d83`. Key examples:
- Ar `LArParametersAnlA.yaml`: `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`;
- Ar `CENNS10AnlAEfficiency.txt`: `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`;
- Ar `cevnspdf.txt`: `3b1d5b25749e8d8e1cfdf5c32e48f026ce4aafec0a80632b3a63273e6e0e1f37`;
- Ar `datanobkgsub.txt`: `dabf3d80f13959f4b94b77c9b56f7347a645105801e8cc177424e7ffcf7c7f66`;
- CsI `data_coincidence_beamOn.txt`: `e6cfa6d22345721a0af8abb9db938c0e5d9785c698c98d9305964aeebf31aa50`;
- CsI `qfData_chicago.txt`: `31046d48092e619eb84f06acdf09ea8e86c642da6aa368c10fe338480b90a04f`;
- CsI `coherent_parameters.yaml`: `daa4f3feaeb5499cb1d876f8ea39f3cfd571f998a6ab92e9cdf552afc78b67e8`.

Therefore the byte/provenance part of 0074 is **PASS_INPUT_BYTES_HASH_PINNED**. This is not yet `PASS_COHERENT_B_MINUS_L_LIKELIHOOD_MATERIALIZED`.

## Prospective SM benchmark frozen before computation
Inspection of the primary Ar YAML, before any independent NMIR SM-rate output, identified a non-circular benchmark: `cevnsPredictionNormalization = 128 ± 17` events, explicitly the initial predicted CEvNS count before the 3D likelihood fit. The separate best-fit `159 ± 43` is deliberately not used as the target.

The benchmark calculation and acceptance criterion are now frozen in `research/prereg/0074a_coherent_argon_sm_benchmark.md`, commit `09ca12d9d82b96ee38502d639196adbb162dad65`. Scientific PASS requires `|N_calc - 128| <= 17` events, integration-refinement change `<=0.5%`, and preregistered monotonic/support/unit checks. The ±17 band may not be enlarged after result inspection. No independent `N_calc` has yet been generated.

The machine-readable 0074 ledger was updated in commit `ec36e4df1b76da34ece911fc8ff0bbe3bdd0f826`.

## Scientific guards
No B-L parameter scan has been performed. No contour points were read from a plot. No Asimov/diagonal substitute was introduced. No cross-generation response/template was mixed. The release `cevnspdf.txt` is forbidden as the calculated benchmark answer; it may only become a diagnostic after an independent rate exists.

## Current classification
**PARTIAL_PASS_COHERENT_INPUTS / PRIMARY_BYTES_HASH_PINNED / 0074a_BENCHMARK_PROSPECTIVE**.

Final 0074 PASS still requires the prospectively frozen SM/background benchmark to pass and any remaining combined-CsI likelihood validation requirement to be frozen and satisfied before a B-L contour calculation can be preregistered.

`NMIR_READINESS` remains 89%.
