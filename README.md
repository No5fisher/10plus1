# #5 Fisher Company Analysis
# 5号渔夫

A platform-neutral AI skill for evidence-based listed-company research, valuation and investment-thesis monitoring.

Current version: **v1.3.0**

## What it does

- one-page investment map and industry-system analysis
- evidence-backed moat, lifecycle and business-quality assessment
- growth, scaling, mature and cyclical financial-analysis scorecards
- earnings quality, asset quality, working-capital and cash-conversion analysis
- ROIC / ROCE / ROE definitions, invested-capital reconciliation and capital efficiency
- mandatory SBC, dilution and buyback checks where material
- 10-year per-share value bridge with configurable return hurdle (default test: 13%)
- Bear / Base / Bull scenarios, dividends, terminal multiple and diluted-share effects
- reproducible Python calculator for historical financial-quality ratios and 10-year return scenarios
- standardized data schema, evidence ledger and A-D confidence grading
- unchanged 8-page investment-bank-style report, with a companion reproducibility appendix

## Repository structure

```text
10plus1/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── install.sh
├── references/
│   ├── SBC-RULES.md
│   ├── FINANCIAL-QUALITY-RETURN-ENGINE.md
│   └── DATA-STANDARDIZATION.md
├── tools/
│   └── return_engine.py
├── examples/
│   └── return_engine_input.json
├── tests/
│   └── test_return_engine.py
├── templates/
│   └── report-template.md
└── docs/
    ├── INSTALL.md
    └── MAINTENANCE.md
```

## Run the calculator

Requires Python 3.10+; no third-party packages.

```bash
python tools/return_engine.py examples/return_engine_input.json
python tools/return_engine.py examples/return_engine_input.json --format markdown
python -m unittest discover -s tests -v
```

The sample input is explicitly illustrative. Replace every value with sourced company data before using it for an investment decision. Monetary values must use one consistent currency and scale per input file.

The calculator does not fetch data or make forecasts. It calculates transparent scenario paths and selected historical ratios from user-supplied inputs. Review its limitations and the data contract before relying on outputs.

## Install the skill

```bash
git clone https://github.com/No5fisher/10plus1.git
cd 10plus1
bash install.sh
```

Default location: `~/.agents/skills/fisher-company-analysis/`.

## Update

```bash
cd 10plus1
git pull
bash install.sh
```

See `docs/INSTALL.md`, `docs/MAINTENANCE.md`, and `references/DATA-STANDARDIZATION.md`.

## License

No explicit open-source license has been added. Public availability does not by itself grant a redistribution/modification license.
