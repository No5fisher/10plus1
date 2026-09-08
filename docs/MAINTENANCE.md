# Maintenance & Release Guide

Fisher Company Analysis is intended to improve through real-company testing rather than prompt accumulation.

## Change workflow

1. Open an Issue describing the research failure, ambiguity or missing rule.
2. Reproduce the problem on at least one listed company.
3. Change the minimum necessary rule, reference or report-template section.
4. Re-run the company test and compare the output before/after.
5. Update `CHANGELOG.md` and increment `VERSION` when behavior changes.
6. Merge to `main` only after the revised rule produces a better, auditable result.

## Versioning

Use semantic versioning:

- PATCH: wording, examples, small fixes that do not materially change research behavior.
- MINOR: new analysis rule, valuation lens, report section or monitoring requirement.
- MAJOR: incompatible methodology or report-structure change.

Examples: `1.1.1`, `1.2.0`, `2.0.0`.

## Recommended tests before release

At minimum, test three different company archetypes when a major methodology rule changes:

- high-growth / high-SBC software or internet company
- mature high-quality compounder
- cyclical, capital-intensive or balance-sheet-sensitive company

Check that the skill does not mechanically force the same metrics or valuation model on every business.

## Release checklist

- `SKILL.md` is internally consistent.
- All referenced files exist.
- Current-data rules require explicit dates/periods.
- SBC materiality gate still works for software/platform companies.
- Bear / Base / Bull assumptions are explicit.
- Kill Criteria are observable, not vague risks.
- Report template still starts with the executive dashboard.
- `VERSION` and `CHANGELOG.md` match.
- Installation instructions have been tested from a clean folder.

## Distribution

The GitHub repository is the source of truth. Users can clone `main` or download GitHub's automatically generated source ZIP. When tags/releases are added, users who need reproducibility should pin a version rather than follow `main`.
