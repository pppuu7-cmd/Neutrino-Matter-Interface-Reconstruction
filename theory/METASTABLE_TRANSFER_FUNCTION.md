# Metastable detector transfer-function formalism

Status: theory/convention note; not a scientific PASS by itself.
Last updated: 2026-09-06.

## 1. Purpose

The ideal CEvNS target optimization returns a differential nuclear-recoil production rate. A metastable medium is useful only after this recoil distribution is passed through an experimentally meaningful trigger/nucleation transfer function.

Never identify a thermodynamic threshold with a step-function detector threshold unless calibration supports that approximation.

## 2. Ideal recoil source

For solar component `s`, target nucleus `i`, recoil energy `T` and detector mass `M_det`,

`dR_i,s/dT = N_i integral dE_nu Phi_s(E_nu) d sigma_i(E_nu,T)/dT`,

where exact isotope masses, actual Z/N and the chosen nuclear form factor are part of `d sigma/dT`.

At fixed target kg, `N_i` is the number of target nuclei per kg.

## 3. Metastable response state

Let `x` denote the thermodynamic/material state, for example

`x = (temperature, pressure, composition, impurity state, field state, time since expansion, position, ...)`.

The calibrated nuclear-recoil response is

`epsilon_NR(T,x) = P(trigger | nuclear recoil T, state x)`,

with `0 <= epsilon_NR <= 1`.

A Seitz or analogous thermodynamic threshold `Q_th(x)` is a state descriptor, not automatically the actual `50%` or `90%` trigger energy.

If the operating state fluctuates with normalized distribution `p(x)`, the effective acceptance is

`epsilon_bar_NR(T) = integral dx p(x) epsilon_NR(T,x)`.

This automatically includes threshold/state dispersion when `p(x)` is measured or prospectively specified.

## 4. Accepted neutrino signal rate

The accepted rate per kg is

`R_acc/kg = f_live sum_i w_i sum_s integral dT [dR_i,s/(kg dT)] epsilon_bar_NR(T)`.

For a pure-isotope ideal target, `w_i=1`. For a compound or mixture, `w_i` must be derived from actual stoichiometric/mass fractions before rates are combined.

The accepted source fraction is

`A_s = R_acc,s / R_ideal,s`.

This is a detector quantity, not a change of the weak cross section.

## 5. False-trigger / background ledger

Keep distinct at minimum:

`R_false = R_spontaneous + R_wall + R_ER + R_neutron + R_cosmogenic + R_instrumental + ...`.

Every term must carry geometry/site/state provenance. A calibration-site neutron background must not be transferred to another site without a transport model.

For bubble-like detectors, electronic-recoil blindness must be represented by a measured/calibrated probability `epsilon_ER(E,x)` or a validated upper bound. It must not be assumed from the NR thermodynamic threshold alone.

## 6. Dead time / reset

Let `tau_reset` be the mean non-live reset/recompression time per trigger and `R_trig` the total signal + background trigger rate while live. A simple non-paralyzable approximation gives

`f_live ~= 1 / (1 + R_trig tau_reset)`.

Use the actual experiment's timing model when available. For extremely rare neutrino signals, backgrounds or spontaneous triggers can dominate dead-time loss even when the signal rate itself is negligible.

## 7. Signal significance / exposure

For a frozen exposure `E = M_det * t_live`, report at least:

- expected accepted signal `S`;
- expected background `B`;
- signal/background ratio `S/B`;
- a prospectively chosen discovery/exclusion statistic rather than optimizing the statistic after seeing the result.

For a simple counting positive control, the Asimov discovery approximation may be used when its conditions are stated:

`Z_A = sqrt(2[(S+B) ln(1+S/B) - S])`.

Systematic uncertainties require an explicit nuisance model; they are not hidden inside an effective background count.

## 8. Energy accounting

A metastable event can release stored free energy. Keep the source ledger explicit:

`E_out,total = E_nu,dep + DeltaF_store + E_external_assist`.

Only

`E_nu,dep <= E_nu`

is neutrino-supplied energy. `DeltaF_store` and reset/preparation work belong to the detector.

For cyclic operation, report at minimum

- `P_nu,dep`;
- `P_store,release`;
- `P_reset`;
- `P_prep/pump`;
- net external energy balance if an engineering claim is made.

A large macroscopic bubble/avalanche therefore may be an excellent **readout amplifier** while providing zero neutrino-energy amplification.

## 9. Inverse detector requirement

Given an ideal recoil spectrum, NMIR can ask the inverse question:

`epsilon_req(T) = argmin technology_distance[epsilon]`

subject to a prospectively frozen physics target such as

- `R_acc >= R_min`,
- `S/B >= q`,
- `Z >= Z_min` at fixed exposure,
- false-trigger and stability constraints.

This converts “we need a lower threshold” into a quantitative required turn-on curve, stability band and false-trigger ceiling.

## 10. Current evidence anchors

See `research/metastable_detector_evidence_ledger.md`.

Current primary-source anchors include:

- measured Xe scintillating bubble-chamber response at sub-keV thermodynamic thresholds, PRD 111, 032002 (2025), DOI `10.1103/PhysRevD.111.032002`;
- SBC-LAr10 100-eV-target calibration plan, JINST 21 P03020 (2026), DOI `10.1088/1748-0221/21/03/P03020`.

The future detector gate must use measured/primary response information where available and label unmeasured sub-100-eV response as an extrapolation or required technology target, never as established performance.
