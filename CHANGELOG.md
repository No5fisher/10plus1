# Changelog

All notable changes to Fisher Company Analysis are documented here.

## [1.3.0] - 2026-11-16

### Added
- Reproducible Python calculator for financial-quality ratios and 10-year return scenarios, with JSON and Markdown outputs.
- Bear/Base/Bull scenario paths including revenue growth, operating-margin transition, diluted-share growth, other EPS effects, payout ratio, terminal P/E and dividend reinvestment.
- Historical calculations for gross/operating/net margins, OCF/net income, FCF, FCF margin/conversion, SBC-adjusted FCF cross-check, DSO/DIO/DPO/CCC, ROIC and ROE.
- Data standardization contract, evidence ledger, period alignment rules, A-D confidence grading and quality-control flags.
- Automated unit tests and an illustrative JSON input example.
- Companion data/reproducibility appendix while retaining the canonical 8 numbered report pages.

### Changed
- Skill workflow now requires source-data traceability and calculator assumptions/output to be retained with each research package.
- Clarified that ROIC × reinvestment rate is a consistency check, not a guaranteed equation for revenue or EPS growth.
- Clarified that the calculator is deterministic, does not fetch data and must not be populated with invented assumptions.

## [1.2.0] - 2026-11-16

### Added
- Financial Quality & 10-Year Return Engine: lifecycle classification, growth vs mature scorecards, earnings/asset quality, working-capital and cash-conversion analysis, ROIC definitions and sector-specific overrides.
- Explicit 10-year per-share value bridge and 13% hurdle test, including dividends, dilution, buybacks, entry discount and terminal multiple.
- Mandatory reporting of cash-flow drivers and asset-quality checks; added distributor and consumer-staples analysis overrides.

### Changed
- Preserved the canonical 8-page report sequence while adding lifecycle, financial-quality and 10-year return panels.
- Replaced one-size-fits-all ROE/ROIC and cash-flow interpretation with business-model-specific definitions and caveats.

## [1.1.0] - 2026-08-28

### Added
- Bundled investment-bank-style report templates in Markdown, DOCX and PDF.
- Mandatory SBC materiality gate before valuation.
- Dual valuation view for material-SBC companies: Reported FCF and Economic FCF.
- Buyback quality checks covering dilution offset, repurchase valuation, funding source and leverage.
- Quarterly SBC monitoring requirements.

### Changed
- High-SBC software companies can no longer be described as "cheap on FCF" using reported FCF alone.
- Capital allocation review now distinguishes gross buybacks from actual net share-count reduction.

## [1.0.0] - 2026-08-28

### Added
- Initial Fisher Company Analysis skill.
- One-page investment map methodology.
- Industry, moat, financial quality, management, valuation, bear/base/bull and kill-criteria workflow.
