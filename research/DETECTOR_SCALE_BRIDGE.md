# Detector scale bridge from ideal solar CEvNS to demonstrated low-threshold hardware

Last updated: 2026-09-06
Status: derived bridge/evidence note; not a scientific gate PASS and no NMIR readiness credit by itself.

## Purpose

Translate the exact-mass full-solar CEvNS rates from iteration 0045 into simple exposure scales for experimentally demonstrated or targeted low-threshold detector masses. This prevents threshold-only reasoning from hiding the equally important active-mass bottleneck.

## Frozen iteration-0045 Si-28 rate at 10 eV

For pure Si-28 at a `10 eV` nuclear-recoil threshold, the iteration-0045 full B16-GS98 solar fold with exact isotope mass, actual Z/N and Helm response gives

`R_ideal(Si28, 10 eV) = 0.0043476963498860904 events/(kg day)`

or

`1.5879960917958946 events/(kg year)`.

This is an **ideal interaction count** before detector efficiency/background acceptance.

## CRESST 10-eV positive control translated to solar CEvNS scale

CRESST-III demonstrated a `10.0 ± 0.2 eV_nr` threshold in a `0.35 g` Si cryogenic calorimeter (PRD 107, 122003; DOI `10.1103/PhysRevD.107.122003`).

Applying only the iteration-0045 ideal Si-28 rate to that mass:

`R_ideal(0.35 g Si, 10 eV) = 5.557986321e-4 events/year`.

Equivalent ideal exposure scales:

- one solar-CEvNS interaction per approximately **1799 detector-years** for one 0.35-g module;
- `0.01 kg` Si: `0.01588 events/year`, about **63 years/event**;
- `0.1 kg` Si: `0.1588 events/year`, about **6.30 years/event**;
- `1 kg` Si: `1.588 events/year`;
- `10 kg` Si: `15.88 events/year`.

These are optimistic interaction counts; an accepted event rate must be smaller after the detector transfer function and backgrounds are applied.

## Compare with the ideal target optimum at 10 eV

Iteration 0045 gives, at the same 10-eV threshold,

`R_ideal(Se82, 10 eV) = 0.008212077955017596 events/(kg day)`

or approximately

`2.99946 events/(kg year)`.

Thus the optimal pure-isotope target among the frozen candidate set gains only a factor ~1.89 over Si at 10 eV. The main difference between the CRESST positive control and a solar-neutrino detector is therefore not a hidden many-orders-of-magnitude target advantage; it is principally **deployable low-threshold mass + backgrounds + accepted efficiency**.

## Low-threshold theoretical upper corner from iteration 0045

At 1 eV, the frozen ideal winner Pb-208 gives

`R_ideal(Pb208, 1 eV) = 0.056335599939718796 events/(kg day)`

or approximately

`20.5766 events/(kg year)`.

This demonstrates why the 1-eV region is scientifically attractive, but it is **not** evidence that a kg-scale Pb-like detector with a calibrated 1-eV nuclear-recoil transfer function exists.

## Immediate detector-design implication

The practical inverse problem must be formulated in exposure space, not threshold space alone:

`N_acc = M t f_live sum_s integral dE_nu Phi_s integral dT (d sigma/dT) epsilon_NR(T)`.

For a fixed target and threshold, the first design quantity is the effective exposure

`E_eff = M t f_live <epsilon_NR>`.

Low threshold without scalable target mass can leave the expected solar signal effectively zero; large mass with a high threshold selects only the high-energy B8 source regime, as experimentally illustrated by XENONnT.

## Scope guard

- This note does not model CRESST's actual solar-neutrino acceptance or background spectrum.
- It uses pure Si-28 instead of natural-isotopic silicon; the difference must be handled in a later detector-specific gate if CRESST-like hardware is explicitly modeled.
- It is not a claim that a 1-kg or 10-kg 10-eV Si device currently exists.
- Signal/readout amplification in a metastable detector remains stored-medium energy, not neutrino-energy gain.
