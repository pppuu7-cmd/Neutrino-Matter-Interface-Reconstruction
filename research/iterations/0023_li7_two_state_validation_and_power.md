# Iteration 0023 — 7Li two-state response validation and power authority

Date: 2026-09-06

## Objective
Close the Li7 full-response gate prospectively: add the independently authorized first excited-state strength, reproduce a matched published `8B` source-average response without tuning to that response, and only then compute the frozen B16+MSW neutrino-only W/kg ceiling.

## Starting authority
Iteration 0022 had only the directly crossed ground-state anchor:
- `7Be(gs,3/2-) -> 7Li(gs,3/2-)` EC;
- `Q_EC=861.815 keV`;
- `log ft=3.324`;
- GS98+MSW gs-only screen `7.49107965e-22 W/kg` pure `7Li`.

That result was explicitly non-authoritative because a complete response had not passed an external matched check.

## Independent excited-state input
For `7Li(nu_e,e-)7Be`, the first `7Be` excited state lies at `429 keV`, so its neutrino threshold is about `1.291 MeV`. The two-state model uses independent allowed strengths `B(F)_gs=1`, `B(GT)_gs=1.19`, `B(GT)_ex=1.06`, with `g_A/g_V=1.2723`. The ground normalization remains fixed by evaluated `log ft`; the excited branch is generated only from the measured allowed-strength ratio and shifted phase space. No published neutrino cross section is used as a fit parameter.

Implementation:
- `src/nmir/li7_full_response.py`;
- `tests/test_li7_full_response.py`;
- `scripts/li7_two_state_validation.py`;
- `.github/workflows/li7-two-state-validation.yml`.

## Prospective validation gate
The matched spectrum is the already frozen Bahcall-Lisi 1996 `8B` table used elsewhere in NMIR. Published source-average controls were frozen in the benchmark before hosted execution:
- ground `2.470e-42 cm^2`;
- excited `1.289e-42 cm^2`;
- total `3.759e-42 cm^2`.

Prospective acceptance limits were also frozen before execution:
- each component: `|residual| <= 12%`;
- total: `|residual| <= 10%`.

The benchmark always exits zero for a scientific mismatch so a red workflow is not confused with a scientific FAIL.

## Infrastructure failure and repair
Initial run `34037418081`, job `101497916296`, failed before any scientific calculation because `pytest` was not installed: `No module named pytest`. Classification: **INFRASTRUCTURE FAIL only**.

Minimal repair commit `5b9728b8f9d2159e291f2e35e4460d43846a1463` added the same pytest dependency setup already used by baseline CI. Nuclear inputs, formulas, published controls and acceptance limits were unchanged.

## Matched `8B` scientific result
Repaired run `34037499594`, job `101498137412`, head `5b9728b8f9d2159e291f2e35e4460d43846a1463` completed successfully. Raw log was inspected before classification.

Results:
- ground: `2.50624404599e-42 cm^2`, residual `+1.46737%`;
- excited: `1.30740264751e-42 cm^2`, residual `+1.42767%`;
- total: `3.81364669350e-42 cm^2`, residual `+1.45376%`.

All prospectively frozen gates PASS with large margin. Artifact `9990627394`, ZIP SHA256 `a3ecbf1d489c215576b9e7b99c3ae7017509070c77104aa4a7265576246e9eb6`.

Scientific classification: **PASS — two-state Li7 response externally validated on a matched source-average benchmark without neutrino-cross-section tuning.**

## Full B16+MSW fold
Only after that validation PASS was `src/nmir/li7_full_solar_fold.py` added and the same frozen B16 flux/spectrum/matter/MSW pipeline used. Scientific fold run `34037570254`, job `101498329856`, head `c826fc69429589744996132d03aa462eb148fa4c` completed SUCCESS; raw result log was inspected.

### GS98 + MSW
- total rate: `19.3488133336 SNU`;
- energy moment: `77.5070777600 SNU MeV`;
- mean captured incident energy: `4.0057793945 MeV`;
- pure `7Li` neutrino-only ceiling: **`1.06589117436e-21 W/kg`**;
- natural lithium ceiling (`7Li` fraction 0.9241): **`9.95777155992e-22 W/kg`**.

Main GS98 components:
- `8B`: `7.24139975 SNU`, `62.60900535 SNU MeV`;
- `7Be`: `4.07166111 SNU`, `3.51461158 SNU MeV`;
- pep: `4.80745287 SNU`, `6.93234704 SNU MeV`;
- `15O`: `2.52908133 SNU`, `3.44715278 SNU MeV`.

### AGSS09met + MSW
- total rate: `16.8416529756 SNU`;
- energy moment: `65.0336486081 SNU MeV`;
- pure `7Li`: `8.94354349192e-22 W/kg`;
- natural Li: `8.35523974408e-22 W/kg`.

Artifact `9990650435`, ZIP SHA256 `320331ff1d3c068d78a27ff09d61a0e07965ff6ef7f2884d940fc7f214fb41cd`.

## Scientific consequences
1. `7Li/GS98` becomes the new validated passive-target leader, replacing `82Se/GS98`.
2. Pure Li7 exceeds pure Se82 by about `3.63x`; natural Li still exceeds pure Se82 by about `3.39x`.
3. The gain comes primarily from low target mass plus the high-energy `8B` contribution: `8B` supplies ~81% of the Li energy moment even though it is not the majority of events.
4. The validated upper bound is still only `~1.07e-21 W/kg`, roughly `9.38e20` below `1 W/kg`. It therefore changes the numerical passive-target leader but not the qualitative SM-power conclusion.
5. This remains a four-target benchmark, not a global all-nuclei theorem. Broader target screening and a target-space upper bound remain necessary.

## Gate status
- ✅ Direct production↔absorption route for Li7: strengthened from gs-only screen to externally validated two-state response.
- ✅ G3 Li7 target gate: PASS and promoted to the validated power ledger.
- ❌ Global G3 target-space ceiling: still open.
- 🟡 G8 resonance-strength, G2 sum-rule response, G9 finite-source focusing and G10 fixed-column metamaterial gates remain open.

## Exact next gate
With Li7 now validated, prioritize a **target-space passive-SM upper-bound formulation** and parallel modern low-A/strong-allowed target screening. The bound must combine allowed-transition strength/sum rules, nuclei per kg, the solar spectral energy flux and weak phase space, and must not use peak resonance cross sections unless G8 integrated-strength/linewidth overlap is passed.

**NMIR_READINESS: 44%** — increased only because a previously non-authoritative candidate now passes an external response benchmark and a hosted full B16+MSW power fold, adding a fourth validated target and a new reproducible G3 leader.
