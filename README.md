# #5 Fisher Company Analysis
# 5号渔夫 e.gonghui@gmail.com 

A platform-neutral AI skill for listed-company research, valuation and investment-thesis monitoring.

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
- investment-bank-style report structure, with a page-1 executive dashboard

## Repository structure

```text
10plus1/
├── SKILL.md
├── README.md
├── VERSION
├── CHANGELOG.md
├── install.sh
├── references/
│   └── SBC-RULES.md
├── templates/
│   └── report-template.md
└── docs/
    ├── INSTALL.md
    └── MAINTENANCE.md
```

The canonical report template is Markdown so the skill remains portable across ChatGPT, Claude, Gemini, DeepSeek, Codex and other AI runtimes. A runtime with DOCX/PDF generation can render the same specification into an investment-bank-style document.

## Install

### One-command install on macOS / Linux

```bash
git clone https://github.com/No5fisher/10plus1.git
cd 10plus1
bash install.sh
```

Default cross-runtime location:

```text
~/.agents/skills/fisher-company-analysis/
```

### Claude Code

```bash
bash install.sh --claude
```

### Hosted AI products

If the platform does not support local Agent Skills directly:

1. Add `SKILL.md` as project/system instructions.
2. Add `references/SBC-RULES.md` as a reference file.
3. Add `templates/report-template.md` as the canonical output structure.

See [docs/INSTALL.md](docs/INSTALL.md) for details.

## Download without Git

GitHub automatically provides a source ZIP for the current `main` branch:

```text
https://github.com/No5fisher/10plus1/archive/refs/heads/main.zip
```

This avoids maintaining a stale duplicate ZIP inside the repository.

## Example prompts

- `用 Fisher Company Analysis 分析 Salesforce，并生成中文 PDF 报告。`
- `Use Fisher Company Analysis to update the investment thesis for Palantir.`
- `按 Fisher Company Analysis 对 Adobe 做 Bear/Base/Bull 估值并列出 Kill Criteria。`

## SBC rule

For material stock-based compensation, the skill requires both **Reported FCF** and a conservative **Economic FCF** cross-check, together with dilution, buyback and leverage analysis. See [references/SBC-RULES.md](references/SBC-RULES.md).

## Updating

For an installed copy:

```bash
cd 10plus1
git pull
bash install.sh
```

For methodology changes, use normal GitHub issues / branches / pull requests. Update `CHANGELOG.md` and `VERSION` whenever behavior changes. See [docs/MAINTENANCE.md](docs/MAINTENANCE.md).

## License

No explicit open-source license has been added yet. The repository is public and downloadable, but a formal redistribution/modification license should be selected before inviting third-party forks or redistribution.
