# NMIR iteration 0061 — distant CCSN transparent-Sun lens utility

Date: 2026-09-07
Classification: **PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY**

## Funnel target
Close the remaining G9 question at F3–F7 for one real distant neutrino-source class. The question is not whether a transparent Sun can focus neutrinos — 0029–0030 already established the physical focal scale — but whether a finite-source, finite-receiver, alignment/duty-weighted distant-source gain can remain useful after no-free-lunch constraints.

## Prospective contract
Frozen before result-dependent calculation in commit `4396de3ae532b574f76e3a34d935b08e51746868`, file `research/prereg/0061_g9_ccsn_solar_lens_utility.md`.

Frozen PASS survivor criterion: receiver-integrated finite-source magnification >1 and alignment/duty-weighted expected gain >=2 relative to the same detector without requiring solar-lens alignment. Strong-negative classification was preregistered when a physical instantaneous magnification exists but the realistic/upper-bounded duty-weighted expected gain remains <2.

## Source authority and local freeze
The benchmark source is a Galactic core-collapse supernova at 10 kpc.

### Fluence/spectrum
Primary model: Nakazato et al., ApJS 205 (2013) 2 / Supernova Neutrino Database, exact database slot `20 Msun`, `Z=0.02`, shock revival `200 ms`, Shen EOS, time-integrated to 20 s, file `integ2002.data`.

The primary payload was not copied from chat. It was fetched by hosted GitHub Actions and then frozen byte-for-byte in the repository:
- materialization run/job: `34071104818 / 101588491017`
- artifact: `10000475043`
- artifact ZIP SHA256: `c3b1ed43e8452455c34a8d3bd1081ae4f4dfe661e6e8b88eda464fc928c94a30`
- primary payload SHA256: `3e422ceff392d2f70521b4bbda7ad8df4674a69ed1c55b693b88e46e27dfa03b`
- local file: `data/g9_ccsn_nakazato_integ2002.data`
- local freeze commit: `fe604e4b5e826588433c06107a6b2637c8f8075b`
- Git blob: `e8dfc9f616cdd62cf26224ac32e528c429dbb6fc`

The database convention is `nu_x` per heavy-lepton species, so the all-flavour total uses multiplicity four. Frozen totals are

`N_all = N_nue + N_anue + 4 N_nux = 1.0648982e58`,

`E_all = E_nue + E_anue + 4 E_nux = 1.9194865e53 erg`.

At 10 kpc the unlensed all-flavour fluence is

`Phi_all = 8.900146153964761e11 cm^-2`.

### Finite source, occurrence and direction controls
- fiducial neutrino-emission radius: `21 km`, from the independently frozen neutrinosphere-scale authority in `data/g9_ccsn_source_authority_0061.json`; a deliberately larger `100 km` sensitivity control is also run;
- Galactic CCSN occurrence rate: `1.63 / 100 yr = 0.0163 yr^-1`;
- smooth thin-disk direction control: massive-star exponential vertical scale height `76 pc`; the benchmark also retains an independent isotropic random-sky control and uses the *larger* alignment probability fail-closed.

The source radius is only a geometric finite-source control and is not used to renormalize the Nakazato luminosity/spectrum.

## Extended-Sun lens and receiver integration
The lens reuses the previously validated pinned Model-S projected transparent-Sun model:
- Model-S pinned commit `cfb2af4a17dc7fe0c367ebb1dbbc121483d2a38b`
- pinned Git blob `e3a0fad3ff877338aad926dbd0a9a43e6c0a897f`
- frozen representative focal ring `b/R_sun = 0.024`
- resulting observer distance `F(b)=24.073780819657056 AU`.

For a distant on-axis source the focal-plane mapping used is

`y(b) = b [1 - z/F(b)]`.

For a finite circular receiver, the code solves the two impact-parameter boundaries whose mapped radius equals the receiver radius and integrates the corresponding incident annulus area. This is a receiver-integrated finite quantity, not a point-caustic divergence.

For a uniform finite source with projected source radius `s`, the code uses the triangle-inequality bracket: rays mapped within `a-s` are accepted for every source point, while no accepted ray can originate outside `a+s`. At 10 kpc and `z=24.0738 AU`, a `21 km` emission radius projects to only

`0.0245097264 cm = 0.2451 mm`,

so the bracket is already tight for metre-class receivers.

## Hosted scientific authority
Dedicated fail-closed workflow:
- run `34071432319`
- job `101589393517`
- scientific head `696aeeeff1ff08c8a50dfaf3f76c5b3a82e9a0a4`
- artifact `10000583684`
- artifact ZIP SHA256 `8ddb043e5ef0fdcccbd046c28a87ded8ad27077797144cf6fa51bba4f5557c76`
- result JSON SHA256 `94765d46a4e18b0f335f2658ffc9cd0db86526f055ebda8131f0ccfb6b1522cd`

Job metadata confirms dedicated regression tests, fail-closed benchmark and artifact upload all completed successfully. The machine-readable artifact was downloaded and inspected directly; scientific classification comes from its frozen benchmark result, not from green CI alone.

## Raw finite-source physical magnification
At `z = 24.073780819657056 AU`:

| receiver radius | one-ring finite-source mu lower | mu upper | upper/lower |
|---:|---:|---:|---:|
| 1 m | `3.676518664e9` | `3.678321621e9` | `1.000490398` |
| 10 m | `3.726019304e8` | `3.726206939e8` | `1.000050358` |
| 100 m | `6.987535545e7` | `6.987548249e7` | `1.000001818` |

Therefore a **real, finite, receiver-integrated instantaneous gravitational magnification exists** and is large. This is not counted as a useful survivor yet because alignment/duty remains part of the preregistered F6/F7 score.

## Fail-closed duty/utility ceiling
To avoid relying on any unresolved detailed caustic strength, the utility step deliberately grants an impossible best case: **every neutrino crossing the entire solar disk is perfectly redirected into the receiver**. Thus

`mu_aperture,max = (R_sun/a)^2`.

The source-centre alignment tolerance is also made optimistic by granting any overlap,

`theta_align <= (a+s)/z`.

For the fiducial `21 km` source the isotropic cap probability is larger than the smooth thin-disk control (`thin-disk/isotropic = 0.7336870743`), so the isotropic value is used as the fail-closed duty ceiling.

| receiver radius | p_align ceiling | impossible full-Sun mu ceiling | expected multiplier ceiling | aligned CCSN rate ceiling | mean interval ceiling |
|---:|---:|---:|---:|---:|---:|
| 1 m | `1.928472468e-26` | `4.84416e17` | `1.000000009341829` | `3.143410122e-28 yr^-1` | `3.181258446e27 yr` |
| 10 m | `1.927621976e-24` | `4.84416e15` | `1.000000009337709` | `3.142023821e-26 yr^-1` | `3.182662058e25 yr` |
| 100 m | `1.927536937e-22` | `4.84416e13` | `1.000000009337297` | `3.141885208e-24 yr^-1` | `3.182802470e23 yr` |

The near receiver-size cancellation is expected: for `s << a`, `p_align ~ a^2/(4z^2)` while the impossible aperture ceiling scales as `R_sun^2/a^2`, so their product approaches `R_sun^2/(4z^2)`.

The deliberately enlarged `100 km` source-radius sensitivity gives a 1-m receiver expected-multiplier ceiling only `1.0000000093590597`, still orders of magnitude below the preregistered `>=2` useful-survivor threshold.

## Scientific interpretation
G9 splits cleanly:
1. **physical focusing:** PASS — the extended transparent Sun produces a large finite receiver-integrated magnification for an exactly aligned distant CCSN;
2. **usefulness after alignment/duty:** STRONG NEGATIVE — even an impossible perfect full-solar-aperture collector, combined with an optimistic alignment overlap criterion and the larger of two sky-distribution controls, yields only `~1 + 9.4e-9` expected event/fluence multiplier.

Because the strong-negative utility result is obtained with an upper ceiling that is vastly more optimistic than the real lens, unresolved higher-fidelity caustic details cannot rescue the preregistered `>=2` occurrence-weighted utility criterion for this source class.

## Scope and guards
- This closes the **10-kpc Galactic CCSN distant-source benchmark**, not every conceivable persistent/known-direction neutrino source.
- It does not claim gravitational focusing is nonexistent; instantaneous focusing is explicitly demonstrated.
- It does not apply to solar-neutrino self-lensing, which remains geometrically inapplicable.
- It does not multiply lensing by metastable detector gain, resonances, structured matter or any other F9 candidate.
- It scores interaction/event fluence only; no neutrino-energy creation occurs.
- The smooth thin-disk model is a control, not a full Milky-Way population synthesis; the isotropic control is independently retained and is actually the looser ceiling here.

## F10 classification
**PASS_G9_PHYSICAL_BUT_STRONG_NEGATIVE_UTILITY** for the preregistered Galactic CCSN benchmark.
