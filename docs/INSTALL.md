# Installation Guide

## 1. Agent Skills compatible runtimes

The most portable location is:

```bash
~/.agents/skills/fisher-company-analysis/
```

Install from GitHub:

```bash
git clone https://github.com/No5fisher/10plus1.git
mkdir -p ~/.agents/skills/fisher-company-analysis
cp -R 10plus1/* ~/.agents/skills/fisher-company-analysis/
```

Update later:

```bash
cd 10plus1
git pull
cp -R . ~/.agents/skills/fisher-company-analysis/
```

## 2. Claude Code

Claude Code can use:

```bash
~/.claude/skills/fisher-company-analysis/
```

Copy the same repository contents there.

## 3. ChatGPT / Gemini / DeepSeek / other hosted AI products

When native local skills are unavailable, use the repository as a portable prompt package:

- `SKILL.md` -> project instructions / system instructions
- `references/SBC-RULES.md` -> supporting knowledge
- `templates/report-template.md` -> canonical report structure
- DOCX/PDF templates -> visual/output reference when supported

The skill intentionally does not depend on vendor-specific tool names.

## 4. Version pinning

For reproducible research, install a tagged release instead of the moving `main` branch once releases/tags are created.

Recommended tag format:

```text
v1.1.0
v1.2.0
v2.0.0
```

## 5. Maintenance workflow

1. Open an Issue describing the research-method problem.
2. Create a branch such as `fix/sbc-dilution-rule`.
3. Update the relevant rule/template.
4. Test on at least one real public company.
5. Update `CHANGELOG.md` and `VERSION`.
6. Merge to `main`.
7. Create a GitHub Release and attach the distribution ZIP.
