# Practical target regret from validated iteration 0045

Last updated: 2026-09-06
Status: post-validation derived design note, not a preregistered scientific gate; no readiness credit by itself.

## Definition

For a practical target `i` at recoil threshold `T`, define ideal target regret relative to the best nucleus in the frozen iteration-0045 set as

`regret_i(T) = 1 - R_i(T)/R_best(T)`.

This is a physics-only CEvNS rate regret. It excludes detector efficiency, chemistry, abundance, background, reset/live time and cost.

## Argon-40 — important metastable-target proxy

Using the validated 0045 artifact:

| threshold | best target / rate [events/(kg day)] | Ar40 rate [events/(kg day)] | Ar40 / optimum | regret | Ar40 dominant solar source |
|---:|---|---:|---:|---:|---|
| 10 eV | Se82 / `8.212077955e-3` | `6.486648607e-3` | `0.78989` | **21.01%** | Be7 ground |
| 20 eV | Pb208 / `4.227008240e-3` | `3.617516800e-3` | `0.85581` | **14.42%** | Be7 ground |
| 40 eV | Pb208 / `3.873772682e-3` | `1.161110164e-3` | `0.29974` | **70.03%** | B8 |

Interpretation:

- At **10–20 eV**, pure Ar40 is surprisingly close to the ideal target optimum at fixed kg, despite not being the mathematical winner.
- At **20 eV**, Ar40 loses only ~14% of the ideal total rate and still receives its largest contribution from the high-flux Be7 branch, whereas the global Pb208 optimum has already switched to B8 dominance.
- By **40 eV**, Ar40 suffers strong endpoint/source loss and its regret rises to ~70%; the detector has entered the high-energy-source regime where very heavy nuclei win.

Therefore the engineering value of a metastable Ar detector is highly nonlinear in threshold. Reducing an Ar nuclear-recoil acceptance scale from O(100 eV) toward **10–20 eV** is not merely a modest rate improvement; it moves the detector into a qualitatively different solar-source regime while bringing it close to the global target optimum.

## Germanium-74 — practical cryogenic proxy

At 10 eV:

- global winner Se82: `8.212077955e-3 events/(kg day)`;
- Ge74: `7.871654050e-3 events/(kg day)`;
- ratio Ge74/optimum = `0.95855`;
- regret = **4.15%**.

This is important because Ge is a mature cryogenic detector material. The ideal nuclear-species advantage of Se82 over Ge74 at 10 eV is only a few percent; detector scalability/background/response can easily dominate that difference.

## Design implication

The practical optimization should not be

`choose mathematical best nucleus`.

It should be

`maximize accepted solar-CEvNS information or significance over target + achievable transfer function + scalable mass + background`.

A material can be scientifically preferable while having nonzero ideal-rate regret if its detector response is substantially better.

## Scope guard

This note is derived from the six validated 0045 thresholds. The active preregistered 0046 phase-diagram gate will determine the exact threshold intervals/crossovers. Do not interpolate these regret values into a continuous curve until 0046 is validated.
