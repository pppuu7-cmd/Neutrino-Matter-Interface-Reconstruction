# Iteration 0074a — COHERENT Ar Analysis-A SM normalization benchmark

Date: 2026-09-07
Classification: **PASS_COHERENT_AR_SM_NORMALIZATION_BENCHMARK**
Parent: 0074 COHERENT B-L likelihood materialization.
Frozen prereg: `research/prereg/0074a_coherent_argon_sm_benchmark.md`, commit `09ca12d9d82b96ee38502d639196adbb162dad65`.

## Prospective contract
Before any independent SM normalization was inspected, the official COHERENT Ar Analysis-A YAML froze the target `128 ± 17` CEvNS events, explicitly the initial prediction before the 3D likelihood fit. PASS required `abs(N_calc-128) <= 17`, numerical refinement <=0.5%, finite/non-negative flavor pieces, rate non-decrease when disabling efficiency or setting Helm `F=1`, and endpoint/unit tests. The separately fitted `159 ± 43` was forbidden as target. Release `cevnspdf.txt` was forbidden as the calculated answer.

Frozen official inputs: Zenodo `10.5281/zenodo.3903810` v1.0, exact package manifest `data/coherent_primary_packages_0074_manifest.json`; POT `13.8e22`, baseline `27.5 m`, fiducial mass `24.4 kg`, yield `0.09` neutrinos/flavor/proton; official Analysis-A efficiency SHA256 `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`; pion/muon DAR spectra; Ar40 `Z=18,N=22`; radiatively corrected Cadeddu couplings `gV^p(nu_e)=0.0401`, `gV^p(nu_mu)=0.0318`, `gV^n=-0.5094`; Helm proton/neutron rms radii `3.448/3.55 fm`.

## Independent implementation
Implementation commit `0b2361c8e421e09d35448029507159404f18eb5d` added:
- `src/nmir/coherent_argon_sm_0074a.py`;
- `tests/test_coherent_argon_sm_0074a.py`;
- `scripts/benchmark_coherent_argon_sm_0074a.py`;
- fail-closed hosted workflow `.github/workflows/coherent-0074a-argon-sm.yml`.

The calculation integrates the CEvNS recoil spectrum independently using exact recoil support, separate proton/neutron Helm responses, flavor-dependent weak proton couplings, monoenergetic prompt nu_mu and analytically integrated Michel nu_e/anti-nu_mu spectra, and the hash-pinned release efficiency. It does not use the release `cevnspdf.txt` normalization.

## Infrastructure-only first attempt
Initial hosted run/job `34135721502/101786088632` is retained as **INFRASTRUCTURE_FAIL**. Dedicated tests passed `6/6`, but shell redirection attempted to open `artifacts/coherent_0074_materialization.log` before the directory existed, so package materialization and the scientific benchmark never ran. Workflow-only fix commit `1dd4043956285e8da6290be2d44d75a28872574c` added `mkdir -p artifacts`; no scientific input, formula, criterion or tolerance changed.

## Authoritative hosted result
Run/job: `34135884676/101786622645`.
Artifact: `10023995784`, `coherent-0074a-argon-sm-result`, size 4619 bytes.
Artifact ZIP SHA256: `b96835cb2533839b303c2acc36150e296797de487d826591adff5194efd8c55f` (Actions upload digest and independent downloaded ZIP agree).
Raw job log inspected directly; workflow status alone was not used as scientific evidence.

Fine integration (`n_t=8000`) gives:
- prompt `nu_mu`: `30.4161042922515` events;
- delayed `nu_e`: `42.276166423657926` events;
- delayed `anti-nu_mu`: `61.52213166652559` events;
- **total `N_calc = 134.21440238243503` events**.

Coarse (`n_t=2000`) total is `134.21443218589957`; refinement fraction `2.2205861676146713e-7`, far below the frozen 0.5% ceiling.

All frozen scientific checks pass:
- `abs(134.21440238243503 - 128) = 6.21440238243503 <= 17`;
- all flavor contributions finite and non-negative;
- no-efficiency total `258.65709512626637 >= N_calc`;
- unit-form-factor total `180.3718386900809 >= N_calc`;
- endpoint/support/cross-section-normalization tests passed (`6 passed` hosted).

Guards recorded in the raw result: `release_cevnspdf_used_as_answer=false`, `bestfit_159_used_as_target=false`, `b_minus_l_scan_performed=false`.

## Scientific conclusion
The independent Ar source+target+detector-response chain reproduces the primary pre-fit CEvNS normalization under the preregistered tolerance. Therefore 0074a is **PASS_COHERENT_AR_SM_NORMALIZATION_BENCHMARK**. This validates the Ar SM normalization chain only; it is not an overall 0074 likelihood PASS and not a B-L constraint/enhancement result.

## Next funnel action
Parent 0074 remains OPEN. Before any B-L scan, prospectively define and validate the remaining CsI/combined-likelihood response requirement using the already hash-pinned first-observation package. Prefer a non-circular primary SM/response benchmark; if no independent numerical benchmark exists, freeze a likelihood/data-model reproduction criterion before result inspection. No B-L mass/coupling calculation is authorized until overall 0074 likelihood materialization passes.

`NMIR_READINESS` increases from 89% to **90%** because a reproducible scientific detector/SM-normalization gate closed under a frozen external benchmark.
