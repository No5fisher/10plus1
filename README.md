# Fisher Company Analysis

A platform-neutral AI skill for listed-company investment research, valuation and investment-thesis monitoring.

Current version: **v1.1.0**

## What it does

Fisher Company Analysis turns a company question into an evidence-based investment decision using a consistent research system:

- one-page investment map
- industry and competitive-system analysis
- moat and business-quality assessment
- 5-10 year financial-quality review
- management and capital-allocation analysis
- mandatory SBC/dilution checks where material
- Bear / Base / Bull valuation
- Reverse DCF / implied-expectations analysis
- 3-5 key monitoring variables
- Bear Case and Kill Criteria
- investment-bank-style PDF/DOCX report structure

## Repository structure

```text
fisher-company-analysis/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── references/
│   └── SBC-RULES.md
├── templates/
│   ├── report-template.md
│   ├── 投行风格公司投资研究报告模板.docx
│   └── 投行风格公司投资研究报告模板.pdf
├── docs/
│   └── INSTALL.md
└── dist/
    └── Fisher-Company-Analysis-v1.1.zip
```

## Install

### Cross-runtime Agent Skills

```bash
git clone https://github.com/No5fisher/10plus1.git
mkdir -p ~/.agents/skills/fisher-company-analysis
cp -R 10plus1/* ~/.agents/skills/fisher-company-analysis/
```

### Claude Code

```bash
mkdir -p ~/.claude/skills/fisher-company-analysis
cp -R 10plus1/* ~/.claude/skills/fisher-company-analysis/
```

### Other AI platforms

If the platform does not support Agent Skills directly:

1. Add `SKILL.md` as project/system instructions.
2. Add `references/SBC-RULES.md` as a reference file.
3. Add `templates/report-template.md` as the canonical output structure.
4. Provide the DOCX/PDF template when the platform can use visual document references.

See [docs/INSTALL.md](docs/INSTALL.md) for more details.

## Example prompts

- `用 Fisher Company Analysis 分析 Salesforce，并生成中文 PDF 报告。`
- `Use Fisher Company Analysis to update the investment thesis for Palantir.`
- `按 Fisher Company Analysis 对 Adobe 做 Bear/Base/Bull 估值并列出 Kill Criteria。`

## SBC rule

For material stock-based compensation, the skill requires both **Reported FCF** and a conservative **Economic FCF** cross-check, together with dilution, buyback and leverage analysis. See [references/SBC-RULES.md](references/SBC-RULES.md).

## Updating

For your own installations:

```bash
cd 10plus1
git pull
cp -R . ~/.agents/skills/fisher-company-analysis/
```

For public changes, use normal GitHub issues / branches / pull requests and update `CHANGELOG.md` plus `VERSION` for releases.

## License

No explicit open-source license has been added yet. Add a `LICENSE` file before inviting unrestricted redistribution or modification by third parties.
