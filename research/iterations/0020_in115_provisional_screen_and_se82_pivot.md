# Iteration 0020 — In-115 provisional screen and Se-82 pivot

Date: 2026-09-06

## Question
Does the historically attractive low-threshold 115In solar-neutrino target beat the validated 71Ga neutrino-only power ceiling when reconstructed on the same frozen B16+MSW solar authority?

## Prospective scope
This iteration is a **screening** test, not a precision 115In response authority.  The provisional nuclear model contains only the historically emphasized dominant transition

`115In(9/2+) + nu_e -> 115Sn*(612.8 keV, 7/2+) + e-`

with threshold `0.114 MeV` and `B(GT)=0.17`, using an allowed-GT charged-current formula and a point-Coulomb Fermi/Sommerfeld factor.  Finite-size/screening/radiative/recoil/forbidden corrections and additional excited-state strength are not promoted into authority.

The solar side is unchanged from the validated Ga/Cl pipeline: frozen B16 GS98/AGSS09met fluxes and spectra plus the same production-averaged daytime three-flavour MSW convention.

## Reproducibility
- response code: `src/nmir/in115_response.py`
- matched solar fold: `src/nmir/in115_solar_screen.py`
- benchmark: `scripts/in115_solar_screen_benchmark.py`
- workflow: `.github/workflows/in115-solar-screen.yml`
- workflow run: `34032630382`
- job: `101484903209`
- head SHA: `2991b26b71e2937479176727a676afa899f0a065`
- artifact: `9989115502` (`in115-solar-screen`)
- artifact digest: `sha256:d173c1788833a4bcbe3c1b1194818ac1f044835f014e7afe8fd0e9a206be40d0`
- same-head baseline CI: run `34032630392`, SUCCESS.

The raw artifact JSON was downloaded and inspected before classification.

## Raw screening results

| quantity | GS98 no oscillation | GS98 MSW | AGSS09met no oscillation | AGSS09met MSW |
|---|---:|---:|---:|---:|
| total capture [SNU] | 371.7141269 | 199.8856483 | 363.9000945 | 195.9132852 |
| neutrino-energy moment [SNU MeV] | 196.9461013 | 99.06490688 | 183.7533413 | 93.16975198 |
| capture-weighted E_nu [MeV] | 0.5298322 | 0.4956079 | 0.5049555 | 0.4755684 |
| pure-115In neutrino-only ceiling [W/kg] | 1.65376576e-22 | **8.31852723e-23** | 1.54298552e-22 | **7.82350827e-23** |

For the GS98 MSW result the rate is dominated by pp (`148.6356 SNU`) and Be7 (`42.6226 SNU`), while the total capture-weighted neutrino energy remains only `~0.496 MeV`.

## Gate classification

### 1. Historical full-response normalization: FAIL for the provisional model
The no-oscillation GS98 screening prediction is `371.7 SNU`, only about one half of the historical full 115In expectation of order `~750 SNU`.  Therefore the one-state `B(GT)=0.17` model is incomplete as a full 115In solar-capture response and **must not** enter the authoritative G3 cross-target ledger.

Plausible missing/inadequate ingredients include additional GT strength, heavy-nucleus Coulomb/finite-size response details, and the known limitations of inferring weak GT strengths solely from charge-exchange data.  These are hypotheses to test, not post-hoc corrections to force agreement.

### 2. Energy-harvesting screening: no advantage over authoritative Ga-71
Even if the provisional one-state response were used only as a screen, its GS98 MSW pure-isotope neutrino-only ceiling is `8.3185e-23 W/kg`, below the validated 71Ga/GS98 value `1.03091848e-22 W/kg`.

This is a useful NMIR lesson: a low capture threshold and high pp event count do **not** imply a larger neutrino-carried power.  Low-energy pp captures increase event count while contributing relatively little energy per capture.

## New target discovered during audit: 82Se
A 2016 high-resolution `82Se(3He,t)82Br` measurement (Frekers et al., Phys. Rev. C 94, 014614) extracted the GT-minus distribution and identified strong isolated low-lying transitions at 75, 1484 and 2087 keV plus fragmented strength above ~2.1 MeV.  The authors evaluated the **nonoscillation** solar-neutrino capture rate as `668 ± 12(stat) ± 60(sys) SNU`.

The accepted-manuscript tables further report that about 97% of the total capture proceeds through the 75-keV 1+ state and that pp neutrinos contribute about `459 SNU`.  Because this response is modern, directly measured, and published together with an explicit solar-capture integral, 82Se is promoted ahead of 115In for the next matched B16+MSW cross-target reconstruction.

## Status
- ✅ hosted In-115 provisional response/fold is reproducible;
- ✅ raw artifact inspected;
- ❌ provisional one-state In-115 model fails the historical full-response normalization gate and is **not** G3 authority;
- ✅ low-threshold/high-event-count ≠ high neutrino-only W/kg demonstrated quantitatively;
- 🟡 82Se promoted as next quantitative cross-target candidate;
- 🟡 precision 115In reconstruction remains possible later with a fuller primary response.

**NMIR_READINESS: 38%** — unchanged.  This iteration closes a useful negative screening branch but does not add a new authoritative target to the G3 power ledger.

## Exact next gate
Reconstruct 82Se on the already frozen B16+MSW authority using the measured GT distribution / published capture tables, first reproducing the paper's `668 ± ... SNU` no-oscillation control, then compute the oscillated component fold, neutrino-energy moment, pure/natural-isotope W/kg ceiling and compare directly with 71Ga and 37Cl.
