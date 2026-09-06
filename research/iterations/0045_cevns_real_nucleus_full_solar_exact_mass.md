# Iteration 0045 — exact-mass real-nucleus full-solar CEvNS inverse optimization

Date: 2026-09-06
Gate: G2 detection / target inverse design
Prospective contract: `research/cevns_real_nucleus_exact_mass_prereg.md`

## Scientific question

For a frozen set of real nuclei, which target maximizes the **ideal Standard-Model solar CEvNS event rate per kg** at a specified nuclear-recoil threshold after folding the full frozen B16-GS98 solar source set and a Helm nuclear form factor?

This is an ideal interaction/detection ranking only. It is not an interaction enhancement claim, not a real detector ranking, and not an energy-harvesting claim.

## Frozen inputs

- candidate set: 23 nuclei in `data/cevns_target_candidates_exact_mass.csv`;
- exact atomic masses frozen from NIST provenance in `data/cevns_target_exact_mass_provenance.md`;
- actual integer `Z/N` for every target;
- B16-GS98 component fluxes from the existing frozen solar ledger;
- pinned pp, hep, B8, N13, O15, F17 spectra;
- both Be7 branches, including the locally frozen Bahcall-1994 thermally broadened dominant profile;
- pep line;
- thresholds: `1, 3, 5, 10, 20, 40 eV`;
- Helm form factor included;
- detector efficiency, chemistry, natural abundance, metastable nucleation, backgrounds, dead time and reset energy excluded by scope.

## Preserved infrastructure failure before the authoritative run

The first hosted exact-mass attempt was **not a scientific failure**. Dedicated unit tests passed, but the benchmark raised

`ValueError: invalid CEvNS integration input`

because pinned continuum spectra legitimately include the endpoint `E_nu=0`, while the integration routine incorrectly rejected zero energy. In addition, the workflow benchmark used `python ... | tee ...` without `pipefail`, so GitHub Actions could report a false green status after the Python process failed.

This was classified `INFRASTRUCTURE_FAIL`, with all prospective scientific acceptance criteria unchanged.

Minimal repair:

1. `E_nu=0` now returns exactly zero CEvNS cross section;
2. negative neutrino energy remains invalid;
3. regression tests explicitly cover both conditions;
4. the hosted workflow uses `set -o pipefail`, so a benchmark failure cannot be hidden by `tee`.

No physical tolerance was relaxed.

## Authoritative corrected run

- workflow head: `58bbb246e47abc5541b216e4db18a6011e968c41`;
- hosted run: `34052577623`;
- job: `101538698697`;
- raw dedicated tests: `23 passed`;
- benchmark status: `PASS_REAL_NUCLEUS_SOLAR_EXACT_MASS_OPTIMIZATION`;
- artifact: `9995006029`;
- artifact ZIP SHA256: `5ec6157a102ba9dc4fc2d97fc710d975020641393a0f48c184f39235ea58c897`.

## Prospectively scored winners

| recoil threshold | winner | ideal events/(kg day) | runner-up | runner-up events/(kg day) | dominant source | winner Helm/no-Helm rate ratio |
|---:|---|---:|---|---:|---|---:|
| 1 eV | Pb-208 | 5.633559994e-2 | W-184 | 5.163448674e-2 | Be7 ground | 0.9973883 |
| 3 eV | Pb-208 | 3.025222341e-2 | W-184 | 2.890291478e-2 | Be7 ground | 0.9953068 |
| 5 eV | Xe-132 | 1.728556077e-2 | I-127 | 1.675116223e-2 | Be7 ground | 0.9962749 |
| 10 eV | Se-82 | 8.212077955e-3 | Ge-74 | 7.871654050e-3 | Be7 ground | 0.9964607 |
| 20 eV | Pb-208 | 4.227008240e-3 | W-184 | 3.820668921e-3 | B8 | 0.9705958 |
| 40 eV | Pb-208 | 3.873772682e-3 | W-184 | 3.394947723e-3 | B8 | 0.9682467 |

The frozen Ar-40 boundary control at 40 eV gives a Be7-ground contribution `3.972432637e-8 events/(kg day)`, reproducing iteration 0042 (`3.973604373e-8`) to the expected tiny Helm/exact-fold difference.

## Main scientific finding — source-regime-dependent, re-entrant optimum

The full solar-spectrum optimum is **not** a monotonic sequence toward lighter nuclei as recoil threshold rises.

Observed winner sequence over the preregistered grid:

`Pb-208 -> Pb-208 -> Xe-132 -> Se-82 -> Pb-208 -> Pb-208`.

At 1–10 eV the high-flux Be7 branch controls the optimum and the threshold/coherence compromise moves the winner from very heavy Pb to Xe and then Se. Once the threshold suppresses the low-energy high-flux components strongly enough, the surviving rate becomes B8 dominated; its much larger neutrino energy restores the advantage of large weak charge, so Pb-208 becomes optimal again at 20–40 eV within the frozen candidate set.

This is a **re-entrant heavy-target optimum caused by a solar-source regime transition**, not a new weak interaction.

## Relation to iteration 0043

Iteration 0043 derived the monoenergetic/fixed-`Q_W/A` local design rule

`A_star = 2 E_nu^2 / (3 m_u T_thr)`, equivalently `T_max(A_star) ≈ 3 T_thr`.

Iteration 0045 does not invalidate that result. It establishes its scope: the rule is a useful local/monoenergetic envelope, but a full broadband source can switch which solar component dominates the objective. The global optimum must therefore be treated as a **piecewise source-dependent phase diagram** rather than a single `A_star(T_thr)` curve.

## Form-factor result

For the winning targets the Helm suppression is small at 1–10 eV (roughly `0.3–0.5%`) and grows to about `3%` for Pb-208 at 20–40 eV. Thus finite nuclear size is not the origin of the winner transitions, but it is large enough at the high-energy/B8 end that it must remain in quantitative optimization.

## Classification

**PASS_REAL_NUCLEUS_SOLAR_EXACT_MASS_OPTIMIZATION**

- real-nucleus exact-mass gate: PASS;
- full frozen solar source fold: PASS;
- Helm finite-size control: PASS;
- 0042 Ar-40/Be7 regression: PASS;
- interaction enhancement: NONE;
- neutrino-energy gain: NONE;
- real detector performance: OPEN.

## Scope guards

1. A pure-isotope winner is not automatically a practical material winner.
2. Natural abundance, chemistry and attainable target phase are excluded here.
3. Ideal CEvNS counts do not include a nucleation/trigger transfer function.
4. Signal amplification by a metastable medium remains stored-energy release, not neutrino-energy amplification.
5. The six-point threshold grid establishes non-monotonicity but does not locate crossover thresholds precisely.

## Exact next gate

Prospectively construct a **continuous/adaptive threshold phase diagram** using the same frozen physical inputs. Locate and refine the target-winner crossover thresholds and source-dominance transitions, test their stability under threshold refinement, and quantify winner margins. Only after this ideal physics map is frozen should it be passed through a real metastable detector transfer function.
