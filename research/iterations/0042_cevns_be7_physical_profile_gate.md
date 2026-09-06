# Iteration 0042 — physical solar Be7 profile × Ar-40 CEvNS threshold gate

Date: 2026-09-06
Gate: G2 / F3–F7
Status: **PASS_CEVNS_BE7_PROFILE_GATE / DETECTION PASS-SURVIVOR / 40-eV RATE STRONGLY ENDPOINT-SUPPRESSED / INTERACTION GAIN NONE / NEUTRINO-ENERGY GAIN NONE**

## Why this iteration exists
Iteration 0041 established that a 40-eV Ar-40 nuclear-recoil threshold corresponds to `E_nu,min = 0.8628609380456526 MeV`, essentially at the thermally broadened dominant solar Be7 line. A rounded monoenergetic 861.8-keV line therefore cannot decide the rate. This iteration prospectively folds the physical line profile with the differential SM CEvNS response.

## Prospective contract
Authority: `research/cevns_be7_profile_prereg.md`.
The scientific criteria, source normalization, thresholds and classification rules were frozen before the hosted result was inspected.

## Frozen source/data provenance
Local authority: `data/be7_bahcall1994_ground_profile.csv`.
Physical source: J. N. Bahcall, Phys. Rev. D 49, 3923 (1994).
Mirrored numerical source: `michelelucente/PEANUTS`, commit `59e3a2ae102d58f42cc1146eaca2cae68be879ce`, source path `Data/be7ground_shape.csv`, source blob `19d97e87e8b03678d2e4629598f7d7fd7794eae0`.
B16 GS98 total Be7 flux: `4.93e9 cm^-2 s^-1`; dominant branch fraction: `0.897`.
CEvNS is neutral current, so no electron-neutrino survival factor is applied.

## Response used
Low-q ideal CEvNS benchmark:

`d sigma/dT = G_F^2 Q_W^2 M/(4 pi) [1 - M T/(2 E_nu^2)]`

with

`T_max = 2 E_nu^2/(M+2E_nu)`

and the exact inverse threshold from iteration 0041.
This is a detector-physics benchmark, not a precision electroweak/nuclear-form-factor prediction.

## Reproducibility
- implementation: `src/nmir/cevns_be7_profile.py`
- tests: `tests/test_cevns_be7_profile.py`
- benchmark: `scripts/cevns_be7_profile_benchmark.py`
- workflow: `.github/workflows/cevns-be7-profile.yml`
- workflow head: `a0d50d8d8bcfb8fffa0c5c95362d4527d25a3d15`
- hosted run: `34050807911`
- job: `101533964874`
- artifact: `9994471349`
- artifact ZIP SHA256: `510b200aa3d6b723c025b61280edd547f6716c3e6b0cb1b17fc53db254be9cdb`
- raw dedicated tests: `7 passed in 0.03s`
- frozen profile trapezoid normalization: `1.0`

All prospective checks passed.

## Raw threshold results

| Ar-40 threshold | `E_nu,min` [MeV] | line-profile fraction above `E_min` | retained CEvNS cross-section fraction | ideal events/(kg day) |
|---:|---:|---:|---:|---:|
| 0 eV | 0 | 1 | 1 | `8.09891299e-3` |
| 10 eV | 0.431425469 | 1 | `5.62275894e-1` | `4.55382355e-3` |
| 20 eV | 0.610130678 | 1 | `2.49702727e-1` | `2.02232066e-3` |
| 30 eV | 0.747257172 | 1 | `6.22804991e-2` | `5.04404343e-4` |
| 35 eV | 0.807131292 | 1 | `1.55009869e-2` | `1.25541144e-4` |
| 38 eV | 0.841012318 | 1 | `2.45139227e-3` | `1.98536127e-5` |
| 39 eV | 0.852006661 | 1 | `6.04546150e-4` | `4.89616667e-6` |
| **40 eV** | **0.862860938** | **0.311040148** | **4.90634283e-6** | **3.97360437e-8** |

Profile-averaged zero-threshold CEvNS cross section for the dominant Be7 line:

`<sigma>_0 = 1.4066113108028225e-42 cm^2`.

At 40 eV:

`<sigma>_above = 6.901317324978097e-48 cm^2`.

## Main scientific result
The 40-eV threshold is a **kinematic survivor but an endpoint-starved rate**.

About `31.104%` of the thermally broadened line lies above the source energy needed to make a 40-eV recoil, but only `4.906e-6` of the total ideal CEvNS cross section survives after the recoil spectrum is integrated. This is because neutrinos just above `E_min` have vanishingly little recoil phase space above threshold.

Thus the statement “thermal broadening opens Be7 at 40 eV” is mathematically true but highly misleading if interpreted as a useful event rate.

At the frozen B16 GS98 normalization, the ideal pure-Ar-40 rate at 40 eV is only

`3.9736e-8 events/(kg day)`

or about `1.45e-5 events/(kg year)`, i.e. roughly one ideal event per `6.89e4 kg-years` before detector/nucleation inefficiencies.

By comparison:
- 20 eV retains ~`24.97%` of the dominant-line CEvNS cross section and gives ~`0.738 events/(kg year)`;
- 10 eV retains ~`56.23%` and gives ~`1.662 events/(kg year)`;
- the zero-threshold ideal dominant-line ceiling is ~`2.956 events/(kg year)`.

## Classification
✅ **DETECTION PASS-SURVIVOR:** the metastable/low-threshold concept remains physically viable as a detector interface.

❌ **40-eV PRACTICAL Be7 RATE:** strongly endpoint-suppressed in this ideal fold; a nominal 40-eV threshold should not be described as effectively opening the dominant Be7 CEvNS flux.

❌ **INTERACTION ENHANCEMENT:** none. Lowering detector threshold does not increase the weak CEvNS cross section itself.

❌ **NEUTRINO ENERGY GAIN:** none. Any avalanche/bubble amplification remains stored-medium energy under iteration 0040.

🟡 **REAL DETECTOR AUTHORITY:** OPEN. Nucleation efficiency, recoil-dependent acceptance, dark counts, threshold calibration/stability, backgrounds and reset/dead-time must be folded before an experimental sensitivity claim.

## Design implication
For an Ar metastable solar-neutrino interface, the physically interesting target is not merely “40 eV or below.” The source-profile fold identifies a much sharper engineering region: roughly **10–20 eV** begins retaining an order-unity fraction (tens of percent) of Be7 CEvNS, while ~40 eV is essentially an endpoint-only regime.

The pp endpoint from iteration 0041 is only ~9.48 eV on Ar; therefore a full pp-spectrum fold below 10 eV is the next natural threshold question, but endpoint opening alone must again not be mistaken for useful rate.

## Next high-value funnel step
Do not optimize Ar in isolation. Build an inverse target/threshold map at fixed target mass:

`target* = argmax_target ∫ dE Phi_solar(E) sigma_target(E; T_thr) / m_target`

for candidate nuclei over a threshold grid, using the full frozen pp + Be7 + pep + CNO + B8/hep source set. This asks which nuclear mass/weak-charge compromise is optimal for a metastable detector, rather than assuming Ar.

Keep detector efficiency and metastable reservoir gain as separate ledgers.

`NMIR_READINESS` recommendation after reconciliation: **72%** (audit estimate; +1% for a prospectively frozen physical source-profile F7 rate closure, not for documentation volume).
