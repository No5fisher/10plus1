# Maintenance & Release Guide

Fisher Company Analysis improves through real-company tests, reproducible calculations and explicit failure analysis rather than prompt accumulation.

## Change workflow

1. Record the research failure or ambiguity and the company archetype where it appeared.
2. Preserve source filings, normalized input data and prior output.
3. Reproduce the issue with the calculator/tests where possible.
4. Change the minimum necessary methodology, code, reference or report-template rule.
5. Run `python -m unittest discover -s tests -v`.
6. Re-run the affected company and at least one contrasting business archetype.
7. Compare before/after results; explain whether the change improves decision usefulness or merely changes the answer.
8. Update CHANGELOG.md and VERSION.

## Versioning

- PATCH: wording, examples or bug fix without intended methodology change.
- MINOR: new analytical rule, calculator capability or reporting requirement.
- MAJOR: incompatible methodology, input schema or report-structure change.

## Required validation archetypes

Before a material methodology release, test:
- high-growth / high-SBC software or internet company
- mature high-quality compounder
- cyclical, capital-intensive or balance-sheet-sensitive company
- where relevant, financial company or distributor with unusual working capital

Do not force identical metrics or valuation models across archetypes.

## Calculator validation

- Run unit tests and preserve test output.
- Verify 13% over 10 years equals a 3.3946x future-value factor.
- Check flat earnings/unchanged multiple/zero dividend gives zero return.
- Check dilution reduces EPS, margin expansion increases EPS, and dividends affect total return.
- Check negative/zero equity or invested capital does not produce misleading ratios.
- Reconcile calculator outputs with an independent spreadsheet or hand calculation for material investment decisions.
- Never treat the illustrative example as company data.

## Release checklist

- SKILL.md references files that exist.
- Input schema and calculator behavior agree.
- Source periods, units and reported/adjusted status are explicit.
- Missing data is not silently treated as zero.
- SBC gate still works.
- Bear/Base/Bull assumptions and Kill Criteria are explicit.
- Eight numbered report pages remain in the original order.
- Data appendix permits reproduction.
- VERSION and CHANGELOG match.

## Distribution

GitHub is the source of truth. Clone or download the source ZIP. For reproducibility, pin a release/tag or commit rather than following main.
