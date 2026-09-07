# NMIR 0072b prospective subgate — Wagner left-panel vector-axis calibration

Date frozen: 2026-09-07
Parent: 0072 / 0072a Wagner primary vector extraction.
Status at freeze: primary EPS and structural frame/tick geometry materialized; no EPS coordinate has yet been accepted as a physical contour point and no official logarithmic calibration fit has been recorded.

## Frozen inputs
- EPS: `WEP_figure6.eps`, SHA256 `4adafc21e896aa3e19490a586e9249fb9b7c947ad9cbe9efd3416d5e00466882`.
- Structural vector extraction: `data/wagner_axis_ticks_0072a.json`.
- Printed primary-source tick authority: `data/wagner_figure6_tick_authority_0072a.json`.
- Existing 0072a acceptance threshold is unchanged: maximum back-projection residual <= `2e-3` decades independently for x and y.

## Frozen left-panel geometry
Structural EPS extraction identifies the left panel frame as
`x=[1.681,6.681]`, `y=[0.844,4.844]`.

Bottom/top x-axis vector ticks form 16 equally spaced decade ticks at approximately
`[1.683, 2.016, 2.349, 2.682, 3.015, 3.348, 3.682, 4.015, 4.348, 4.681, 5.014, 5.347, 5.680, 6.014, 6.347, 6.680]`.
The primary figure prints labels every two decades, starting at the leftmost detected tick (`10^-2`) and ending at the second-to-last detected tick (`10^12`); the final right-edge decade tick is unlabeled. Therefore the frozen x-fit association is the even zero-based tick indices `[0,2,4,6,8,10,12,14]` mapped to log10(lambda/m) `[-2,0,2,4,6,8,10,12]`.

Left/right y-axis vector ticks form 7 decade ticks at approximately
`[1.026,1.632,2.238,2.844,3.450,4.056,4.661]`.
All seven are printed/labeled in the primary figure, so the frozen y-fit association is these ticks bottom-to-top mapped to log10(|alpha_tilde|) `[-11,-10,-9,-8,-7,-6,-5]`.

This association is frozen from primary printed labels plus EPS vector tick ordering before the official affine log-axis fit. No contour geometry is used to choose the association.

## Fit and validation
Fit independently by ordinary least squares:
`log10(lambda/m)=a_x*x_eps+b_x`,
`log10(|alpha_tilde|)=a_y*y_eps+b_y`.
Use every frozen major tick above. Do not drop an outlier or refit endpoints.

For each axis compute the maximum absolute residual in decades at the fitted major ticks. Classification:
- `PASS_WAGNER_AXIS_CALIBRATION` only if both maxima are <= `2e-3` decades;
- `SCIENTIFIC_FAIL_VECTOR_CALIBRATION` otherwise.

Also require top/bottom x ticks and left/right y ticks to agree coordinate-for-coordinate within `2e-6` EPS units. A mismatch is `SCIENTIFIC_FAIL_VECTOR_CALIBRATION` rather than grounds to choose one side post hoc.

## Next action
On PASS, freeze the affine transforms and proceed to named-curve chaining/identity under 0072a. On FAIL, preserve the failed vector route and move to the already-frozen PandaX/De-Romeri likelihood reproduction. No raster/manual contour digitization is permitted.
