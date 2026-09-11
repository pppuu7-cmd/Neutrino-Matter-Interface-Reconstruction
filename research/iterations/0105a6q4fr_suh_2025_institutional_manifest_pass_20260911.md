# 0105a6q4fr — validated Suh 2025 institutional manifest transport repair

Date: 2026-09-11
Gate: `NMIR-V2-0105A6Q4FR`
Classification: `PASS_0105A6Q4FR_INSTITUTIONAL_MANIFEST_TRANSPORT_REPAIRED_NONDISCOVERY`
Scope: official-IU institutional metadata identity/transport only; NONDISCOVERY.

## Prospective chain

- parent q4ft record: `82df8544f41ef34e5557a389335a595b900d2635`
- q4fr preregistration: `f47dda9bd5fda788c4497d58e4a2f58f2e042cb3`
- implementation/workflow head: `f7d3171d98b68074a802c58ff8dc0ade961cde7f`

## Hosted validation

- run/job/artifact: `34545436341/103096914611/10178825152`
- dedicated guards: `5 passed`
- provider artifact ZIP SHA256: `700e03367aa2f7760c3bfe8272ed2efe29236790d6fcc78746c905e3de5eef89`
- independently downloaded ZIP SHA256: `700e03367aa2f7760c3bfe8272ed2efe29236790d6fcc78746c905e3de5eef89`
- independent inner `result.json` SHA256: `af1af99fec76f8e3a1c20056af7be3cf6e688314b7703e58eaf871c5c985681a`

Both prospectively frozen official Indiana University endpoints independently returned HTTP 200 and contained the frozen Benjamin Suh / 2025 / dissertation-title identity:

1. `https://ceem.indiana.edu/events/phd-plaques/suh-benjamin.html`
   - 23370 bytes
   - SHA256 `f1c245e9675c1a533bc9ad03ca928820499381d576c5f6fefee59c33b91d7488`
2. `https://ceem.indiana.edu/education/index.html`
   - 67845 bytes
   - SHA256 `3de3e09e5ebdb4006c0d8b969c3f73a25b041b31534476b6bf6987bbf5591fe6`

The hosted result explicitly records `page_links_followed=false`, `pdf_downloaded=false`, `pdf_content_inspected=false`, `pdftotext_executed=false`, `ocr_executed=false`, `likelihood_evaluated=false`, `pseudo_data_generated=false`, `observed_bsm_residual_inspected=false`, and `bsm_fit_executed=false`.

This PASS repairs institutional manifest provenance only. It is secondary institutional authority and does not replace collaboration/Tier-A authority. It permits only a separately prospectively preregistered dissertation locator/acquisition step.

`SYSTEMATIC_MONTE_CARLO_PREREGISTRATION_PERMISSION = 0%`
`SYSTEMATIC_MONTE_CARLO_EXECUTION_PERMISSION = 0%`
`OBSERVED_BSM_RESIDUAL_PERMISSION = 0%`
