# Installation Guide

## 1. Agent Skills compatible runtimes

The most portable location is:

```bash
~/.agents/skills/fisher-company-analysis/
```

Install from GitHub:

```bash
git clone https://github.com/No5fisher/10plus1.git
cd 10plus1
bash install.sh
```

Update later:

```bash
cd 10plus1
git pull
bash install.sh
```

## 2. Claude Code

Install to Claude Code's skill directory:

```bash
git clone https://github.com/No5fisher/10plus1.git
cd 10plus1
bash install.sh --claude
```

Target:

```text
~/.claude/skills/fisher-company-analysis/
```

## 3. ChatGPT / Gemini / DeepSeek / other hosted AI products

When native local skills are unavailable, use the repository as a portable prompt package:

- `SKILL.md` -> project instructions / system instructions
- `references/SBC-RULES.md` -> supporting knowledge
- `templates/report-template.md` -> canonical report/output specification

A platform with document-generation capability can render the Markdown template into PDF/DOCX. The methodology intentionally does not depend on vendor-specific tool names.

## 4. Download without Git

GitHub automatically packages the current `main` branch as a ZIP:

```text
https://github.com/No5fisher/10plus1/archive/refs/heads/main.zip
```

After extracting, add `SKILL.md`, `references/SBC-RULES.md`, and `templates/report-template.md` to the target AI project when local skill installation is not supported.

## 5. Version pinning

For reproducible research, use a tagged version once tags/releases are published instead of following the moving `main` branch.

Recommended tag format:

```text
v1.1.0
v1.2.0
v2.0.0
```

## 6. Maintenance workflow

See `docs/MAINTENANCE.md`. In brief:

1. Open an Issue describing the research-method problem.
2. Reproduce it on a real listed company.
3. Update the minimum necessary rule/template.
4. Re-test the methodology.
5. Update `CHANGELOG.md` and `VERSION` when behavior changes.
6. Merge to `main`.
