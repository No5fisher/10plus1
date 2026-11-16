# #5 Fisher Company Analysis
# 5号渔夫

A platform-neutral AI skill for listed-company research, valuation and investment-thesis monitoring.

Current version: **v1.2.0**

## What it does

- one-page investment map and industry-system analysis
- evidence-backed moat and business-quality assessment
- lifecycle-specific financial analysis: growth, scaling, mature and cyclical
- earnings quality, asset quality, working-capital and cash-conversion analysis
- ROIC / ROCE / ROE definitions and capital-efficiency analysis
- mandatory SBC, dilution and buyback checks where material
- 10-year per-share value bridge and configurable return hurdle (default test: 13%)
- Bear / Base / Bull valuation, Reverse DCF and 3-5 monitoring variables
- Bear Case and observable Kill Criteria
- unchanged 8-page investment-bank-style report structure

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
│   └── FINANCIAL-QUALITY-RETURN-ENGINE.md
├── templates/
│   └── report-template.md
└── docs/
    ├── INSTALL.md
    └── MAINTENANCE.md
```

Canonical report structure: `templates/report-template.md`. Methodology extension: `references/FINANCIAL-QUALITY-RETURN-ENGINE.md`. SBC treatment: `references/SBC-RULES.md`.

## Install

```bash
git clone https://github.com/No5fisher/10plus1.git
cd 10plus1
bash install.sh
```

Default location: `~/.agents/skills/fisher-company-analysis/`.

## Example prompts

- `用 Fisher Company Analysis 分析 MCK，并生成中文 PDF 报告。`
- `用 Fisher Company Analysis 对伊利股份做十年回报情景分析。`
- `更新 Palantir 的投资逻辑，重点检验 AIP/Ontology、SBC 和每股 FCF。`

## Updating

```bash
cd 10plus1
git pull
bash install.sh
```

See `docs/INSTALL.md` and `docs/MAINTENANCE.md`.

## License

No explicit open-source license has been added. Public availability does not by itself grant a redistribution/modification license.
