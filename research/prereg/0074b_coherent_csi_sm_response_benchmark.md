# Iteration 0074b — COHERENT CsI first-observation SM response benchmark

Status: **PROSPECTIVE / frozen before independent CsI SM signal output**
Date frozen: 2026-09-07
Parent: 0074 COHERENT CsI+Ar B-L likelihood materialization
Prerequisite: 0074a `PASS_COHERENT_AR_SM_NORMALIZATION_BENCHMARK`.

## Scientific question
Can an independent Standard-Model CsI[Na] CEvNS source+nuclear-response+detector-response calculation reproduce the primary COHERENT first-observation predicted signal normalization closely enough to validate the CsI response chain before any `U(1)_{B-L}` likelihood/exclusion calculation?

This is a pre-BSM validation gate. It is not a fit to the observed excess and not a B-L scan.

## Frozen primary authorities and exact package
Use only the already hash-pinned official COHERENT first-observation release, Zenodo `10.5281/zenodo.1228631` v1.0, whose exact bytes are frozen in `data/coherent_primary_packages_0074_manifest.json`, together with the primary first-observation analysis `arXiv:1708.01294` for its published SM prediction and the parent Cadeddu convention where a common SM nuclear convention is required.

The release README explicitly states that these data correspond to `arXiv:1708.01294`, and that the YAML contains the energy-independent QF used for the 2017 analysis. No later CsI response/QF release may be substituted without a separate prospective amendment.

Frozen release scalars:
- detector mass `14.6 kg`;
- baseline `19.3 m`;
- neutrino yield `0.08 neutrinos/flavor/proton`;
- first-observation exposure corresponding to the published dataset (`N_POT=17.6e22` in the parent Cadeddu authority; release beam exposure `7.47594 GW hr` is retained as same-dataset metadata, not an independent fluence normalization to be multiplied again);
- constant nuclear-recoil quenching factor `QF=0.0878` with quoted uncertainty `0.0166`;
- light yield `13.348 PE/keVee`;
- release acceptance `f(x)=a/[1+exp(-k(x-x0))] H(x-5)` with `a=0.6655`, `k=0.4942`, `x0=10.8507`, and the release modified step `H=0` below 5 PE, `1/2` for 5<=x<6, `1` for x>=6;
- acceptance evaluated at 1-PE bin centers as specified by the release.

The release prompt-neutron PDF is a background input and must not be used to construct the SM CEvNS signal normalization.

## Frozen SM/source convention
Use the same DAR source normalization convention validated by 0074a: prompt monoenergetic `nu_mu` from pion decay plus delayed Michel `nu_e` and `anti-nu_mu`, isotropically diluted to 19.3 m.

Use the parent Cadeddu SM CEvNS convention with flavor-dependent radiatively corrected weak proton couplings and Helm nuclear form factors. Treat natural CsI as one Cs-133 plus one I-127 nucleus per CsI molecule; number of target molecules is determined from 14.6 kg and standard isotopic molar masses. Nuclear recoil spectra for Cs and I are computed separately before detector response.

The detector map is frozen as:
1. convert `T_nr -> E_ee = QF*T_nr`;
2. mean photoelectrons `mu_PE = 13.348 * E_ee/keVee`;
3. Poisson-smear integer PE response for a recoil with mean `mu_PE`;
4. apply the official acceptance at each 1-PE bin center;
5. sum all accepted PE bins represented by the first-observation prediction.

No deterministic `PE=mu_PE` substitution is allowed for the primary benchmark. Numerical PE truncation must leave omitted Poisson tail probability <=1e-8 per sampled recoil or use an analytically equivalent converged treatment.

## Frozen benchmark target
The primary COHERENT first-observation result reports a Standard-Model prediction of **`173 ± 48 CEvNS events`** for this CsI[Na] dataset, before comparison with the fitted excess `134 ± 22` events.

The fitted `134 ± 22` is explicitly forbidden as the benchmark target.

## Frozen acceptance criterion
`PASS_COHERENT_CSI_SM_RESPONSE_BENCHMARK` iff the independent accepted SM signal count `N_calc` satisfies:

`abs(N_calc - 173) <= 48 events`.

Also require, without post-result relaxation:
1. recoil/source numerical refinement changes total `N_calc` by <=0.5%;
2. Cs and I contributions and all three source-flavor contributions are finite and non-negative;
3. disabling acceptance must not reduce the predicted count;
4. replacing physical Helm form factors with `F=1` must not reduce the count;
5. exact recoil endpoints/support are unit-tested;
6. Poisson probabilities normalize to unity within numerical tolerance and PE-tail truncation meets the frozen `<=1e-8` condition;
7. setting QF or light yield upward with all else fixed must not decrease accepted signal in a local monotonicity test around the central release values.

The ±48 band is frozen from primary authority before independent CsI output and may not be enlarged after seeing the result.

## Failure classes
- `PASS_COHERENT_CSI_SM_RESPONSE_BENCHMARK`: all frozen criteria pass.
- `SCIENTIFIC_FAIL_COHERENT_CSI_SM_RESPONSE_BENCHMARK`: complete calculation misses `173±48` or an invariant/refinement check fails.
- `BLOCKED_COHERENT_CSI_SM_RESPONSE_INPUT`: a controlling same-analysis primary input required by the frozen mapping cannot be determined without an unregistered assumption.
- `INFRASTRUCTURE_FAIL`: transport/runtime/parser failure prevents scientific assessment.

## Next actions frozen prospectively
- On PASS: incorporate validated CsI response into parent 0074 and freeze the exact combined CsI+Ar SM/background likelihood-reproduction criterion before any B-L parameter scan. Overall 0074 is not automatically PASS from the normalization benchmark alone.
- On SCIENTIFIC_FAIL: retain the failure and audit conventions prospectively; do not tune QF, radii, flux or tolerance to 173.
- On BLOCKED: classify the CsI normalization route accordingly; do not substitute another COHERENT generation.

## Guards
No `134±22` fit target. No B-L coupling/mass calculation. No contour reading. No later-generation QF/response substitution. No prompt-neutron background added to the CEvNS signal. No post-result tolerance changes. No multiplying this validation result by any NMIR interaction/detector gain.
