# Iteration 0074a — COHERENT Ar Analysis-A SM normalization benchmark

Status: PROSPECTIVE / frozen before inspecting any independently calculated SM CEvNS normalization.
Date frozen: 2026-09-07.
Parent gate: 0074 `PARTIAL_PASS_COHERENT_INPUTS`.

## Scientific question
Can an independent Standard-Model CEvNS source+target+detector-response calculation reproduce the official COHERENT liquid-Ar Analysis-A predicted CEvNS normalization closely enough to validate the numerical chain before any `U(1)_{B-L}` likelihood or exclusion calculation is permitted?

This is a pre-BSM validation gate. It is not a fit to the published best-fit signal and is not a B-L scan.

## Frozen primary inputs and provenance
Use only the official COHERENT Ar Analysis-A release, Zenodo DOI `10.5281/zenodo.3903810`, resolved record `3903810`, version `1.0`, whose exact file manifest is frozen in `data/coherent_primary_packages_0074_manifest.json`.

Controlling release files include:
- `LArParametersAnlA.yaml`, SHA256 `a206a77220436d0173c4783ae8fddeab97adf5e144f3d65005eff0870257693e`;
- `CENNS10AnlAEfficiency.txt`, SHA256 `21ce25451c1ed552752ff4a22496deab3ff5dba178bf360813eaff1d25be89e2`;
- `cevnspdf.txt`, SHA256 `3b1d5b25749e8d8e1cfdf5c32e48f026ce4aafec0a80632b3a63273e6e0e1f37` as a release-level cross-check only, not as a substitute for the independent SM calculation.

Frozen scalar inputs from the official YAML are:
- beam exposure `13.8e22 POT`;
- baseline `27.5 m`;
- fiducial mass `24.4 kg`;
- neutrino yield `0.09 ± 0.009` per flavor per proton;
- LAr quenching `QF(T_keVnr) = 0.246 + 0.00078 T_keVnr` with quoted release uncertainties.

The neutrino source is pion/muon decay at rest: prompt monoenergetic `nu_mu` from `pi+ -> mu+ nu_mu`, plus delayed Michel `nu_e` and `anti-nu_mu` spectra from `mu+` decay, normalized to the frozen per-flavor yield and isotropic dilution at 27.5 m.

## Frozen SM physics convention
Use the tree/radiatively-corrected CEvNS differential form consistent with the parent 0074/Cadeddu convention,

`d sigma/dT = (G_F^2 M / pi) Q_V^2 (1 - M T/(2 E_nu^2)) F^2(q^2)`

with the normalization convention implemented explicitly and unit-tested so that no factor-of-four ambiguity is hidden. For Ar, use `Z=18`, `N=22`, radiatively corrected weak couplings frozen by 0074 (`gV^p(nu_e)=0.0401`, `gV^p(nu_mu)=0.0318`, `gV^n=-0.5094`) and the published Helm form-factor convention/radii. Flavor dependence of the proton weak coupling must be respected. Kinematic support uses exact `T_max=2E_nu^2/(M+2E_nu)`.

Convert recoil energy through the frozen LAr QF and apply the official Analysis-A acceptance/efficiency from the hash-pinned efficiency file. Integrate over all accepted recoil energies represented by that release-level prediction. No fit to observed data is allowed in this benchmark.

## Frozen benchmark target
The primary Analysis-A YAML, inspected before any NMIR reproduction output, states:

`cevnsPredictionNormalization = 128` events with `uncertainty = 17` events,

explicitly described as the **initial predicted number of CEvNS before the 3D likelihood fit**.

The separately published best-fit `159 ± 43` events is *not* the target because using a fitted signal normalization would mix detector-model validation with statistical fitting.

## Frozen acceptance criterion
`PASS_COHERENT_AR_SM_NORMALIZATION_BENCHMARK` iff the independently calculated accepted SM CEvNS count `N_calc` satisfies

`abs(N_calc - 128) <= 17` events.

Also require:
1. numerical integration refinement changes `N_calc` by <= 0.5%;
2. all source-flavor contributions are finite and non-negative;
3. disabling efficiency must not reduce the rate;
4. replacing the physical Helm form factor by `F=1` must not reduce the rate;
5. unit tests reproduce exact endpoint/support behavior and basic cross-section scaling.

The ±17 acceptance band is frozen from primary authority before calculation and must not be enlarged after seeing the result.

## Failure classification
- `PASS_COHERENT_AR_SM_NORMALIZATION_BENCHMARK`: all criteria above pass.
- `SCIENTIFIC_FAIL_COHERENT_AR_SM_NORMALIZATION_BENCHMARK`: calculation runs with complete frozen inputs but misses the 128±17 primary target or an invariant/refinement check fails.
- `BLOCKED_COHERENT_AR_SM_BENCHMARK_INPUT`: a controlling numerical convention/input required to map the independent CEvNS spectrum into the release acceptance cannot be determined from primary material without an unregistered assumption.
- `INFRASTRUCTURE_FAIL`: transport/runtime/parser failure prevents the calculation from reaching scientific assessment.

## Next actions, frozen prospectively
- On PASS: incorporate the validated Ar response chain into 0074, then determine whether an equally controlling CsI input/response benchmark is required for the combined Cadeddu likelihood; only after overall 0074 likelihood materialization passes may a separate B-L contour calculation be preregistered.
- On SCIENTIFIC_FAIL: retain the failure; audit normalization/convention differences prospectively. Do not tune constants to 128 and do not run B-L.
- On BLOCKED: classify 0074 accordingly unless a genuinely primary missing input can be materialized under a new prospective amendment.

## Guards
No use of the release `cevnspdf.txt` integral as the calculated answer. It may only be inspected after `N_calc` exists as a diagnostic cross-check. No fitting to `159`. No post-result tolerance changes. No B-L coupling or mass is evaluated in this gate.
