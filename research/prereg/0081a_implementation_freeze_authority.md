# NMIR 0081a implementation freeze — subordinate to prereg ad37205e

Date frozen: 2026-09-08
Authority: this file only specifies implementation details for the already-frozen scientific contract `research/prereg/0081a_bl_bbn_vector_calibration_semantic_identity.md`, commit `ad37205e6a30188f4129fdca8e0d49a156ab6e36`. It does not alter that contract.

A later competing prereg `research/prereg/0081a_bl_bbn_axis_calibration.md` and its workflow are non-authoritative because they were created after `ad37205e`; their results must not be used to choose/tune the implementation below.

## Frozen exact assets
- source archive SHA256 `484f1fa28985897def86bff6c4399ce074ede6b0cd8ce565d169dc320be47a8c`
- Majorana `Presentation/CnstrntPlotMajoranaYp.pdf`, SHA256 `4326f3ac9ba29e515aa22afafef27d08c05d0e6be04db605c4706418c6cd8926`
- Dirac `Presentation/CnstrntPlotDiracYp.pdf`, SHA256 `14d9afe16f4c38f1d3c08f97ccf086a570739b18731b0b6ffee97fe4b9e63b15`

## Axis implementation
Use extractable native PDF text only. Require source-native axis-title evidence for mediator mass in MeV and coupling `g_X`. Parse logarithmic tick labels from the bottom and left page margins without importing any CMB affine coefficients. At least four distinct anchors per axis are required in each panel. Fit `log10(m_X/MeV)=a_x*x+b_x` and `log10(g_X)=a_y*y+b_y` independently. Ordinary and leave-one-out residual maxima remain <=0.015 decade per the parent prereg. Compare independently recovered Majorana/Dirac transforms on common major ticks; max difference <=0.015 decade.

## Threshold semantic-identity implementation
Inventory all native text spans and all `page.get_drawings()` stroke/fill styles before selecting anything.

For every text span whose normalized text is exactly `0.008`:
1. record its text RGB color and bbox;
2. group vector drawings by deterministic style key `(stroke RGB rounded to 6 decimals, fill RGB/null, dashes string, width rounded to 4 decimals)`;
3. primary identity route: if exactly one non-CMB-overlay style has stroke RGB equal to the 0.008 text RGB within `1/255 + 1e-6` per channel, that style is the candidate;
4. adjacency fallback, used only if the color route is not unique: compute minimum distance from each drawing's sampled native path to the 0.008 label bbox. Lines use their endpoints; cubic Beziers use fixed 32-step parameter sampling; rectangles/quads use their native vertices. A style qualifies only if its minimum bbox distance is <=2.5 PDF points. Exactly one non-CMB-overlay style must qualify across all 0.008 labels in that panel.

A CMB overlay style is excluded deterministically when it is both red-dominant (`R>=0.7`, `G<=0.45`, `B<=0.45`) and non-solid/dashed according to the native PDF dash string. This implements the parent prereg's explicit dashed-red exclusion and is not a generic exclusion of red solid BBN contours.

The same route (color-primary then adjacency-fallback with identical thresholds) must succeed independently for Majorana and Dirac. Record source drawing indices belonging to the selected style, but do not assemble an excluded polygon.

## PASS/BLOCKED/FAIL
Use exactly the parent prereg classifications. Parser/PDF-operator/dependency issues remain implementation failures. No threshold, tolerance, color definition or adjacency radius may be changed after inspecting the authoritative hosted result.

## Guards
No physical polygon construction; no excluded-side assignment; no CMB+BBN union; no Majorana/Dirac union; no response scan. The later non-authoritative 0081a workflow output is ignored for scientific classification and may only be archived as a namespace/concurrency artifact after this authoritative implementation is frozen.
