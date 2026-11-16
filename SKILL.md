---
name: fisher-company-analysis
description: Use when a user wants to understand a listed company, build or update an investment thesis, compare current price with business quality and intrinsic value, or produce a structured equity-research report for an investment decision.
---

# Fisher Company Analysis

## Overview
Turn a listed-company question into an evidence-based investment decision. Start from the business, industry and competitive position; then test financial quality, management, valuation, risks and falsification conditions. Distinguish facts, estimates, inference and judgment.

For a full equity-research report, use `templates/report-template.md` as the canonical structure. If the runtime can generate DOCX/PDF, render that same specification into an investment-bank-style document.

## Core Principles
1. Stock = fractional ownership of a business; analyze the business before price.
2. Analyze from system to company: macro/technology -> industry -> company -> product/customer -> financials -> valuation.
3. Seek causal drivers, not indicator accumulation. Reduce the company to 3-5 variables that determine long-term value.
4. Think probabilistically. Every thesis needs a bear case and explicit kill criteria.
5. Separate business quality from valuation. A great company can be a poor investment at the wrong price.
6. Prefer per-share economics and cash generation over headline growth.
7. Never fill data gaps silently. Mark unavailable, estimated, inferred or stale information.
8. Treat SBC/dilution as an owner-economics issue. Read `references/SBC-RULES.md` whenever SBC may be material.
9. Classify lifecycle before choosing metrics: growth, scaling/transition, mature cash-generation, or cyclical/restructuring. Never force one scorecard onto all companies.
10. Apply `references/FINANCIAL-QUALITY-RETURN-ENGINE.md` to all full reports. It governs lifecycle-specific financial quality, asset quality, cash conversion, ROIC and the 10-year return hurdle.

## Evidence Standard
Use, in descending priority when available:
- regulatory filings and audited annual/quarterly reports
- company investor-relations materials and earnings calls
- government/regulator/industry primary data
- high-quality financial databases and reputable research
- credible news and expert commentary

For time-sensitive metrics, state the period/date. For controversial claims, triangulate independent sources when feasible. Clearly label:
- FACT: directly supported by a source
- ESTIMATE: analyst/model estimate
- INFERENCE: reasoned conclusion from facts
- JUDGMENT: investment interpretation

## Workflow

### 1. Define the company in one sentence
Explain what the company sells, to whom, and why customers pay.

### 2. Build the One-Page Investment Map
Complete all ten boxes before forming a recommendation:
1. Company definition - problem solved and customer value
2. Market growth - 5-10 year demand and structural drivers
3. Why this company can win - moat and competitive advantage
4. Economic engine - revenue, margins, FCF, ROIC and per-share economics
5. Management - execution, incentives and capital allocation
6. Key variables - only 3-5 variables that drive long-term value
7. Bear case - at least three ways the thesis can fail
8. Valuation - current expectations, historical/peer context and implied assumptions
9. Investment thesis - concise reason to own or avoid now
10. Kill criteria - observable facts that force thesis re-evaluation

### 3. Industry and System Analysis
Map upstream suppliers -> company -> customers/downstream. Add competitors, complements, substitutes, regulators and capital providers where material. Identify industry structure, profit pool, bargaining power, structural vs cyclical growth, regulatory/technology shifts and company position.

### 4. Competitive Advantage
Identify only evidence-backed advantages: technology/know-how, cost, network effects, switching costs, brand/trust, distribution, data/scale/ecosystem, regulation/license. State whether the moat is widening, stable or narrowing and the metric that proves it.

### 5. Financial Quality — Mandatory Lifecycle Split
Read `references/FINANCIAL-QUALITY-RETURN-ENGINE.md`. Classify lifecycle before selecting KPIs.

**Growth / scaling**: validate product/customer demand, organic growth, retention, unit economics, margin trajectory, incremental ROIC, runway, financing needs and diluted per-share economics. Do not reject a young business solely for low current ROE, but do not accept TAM as evidence of future profits.

**Mature**: use 5-10 years where possible to test earnings quality, asset quality, cash conversion, ROIC/ROCE, maintenance investment, leverage, capital allocation and per-share value creation.

**Cyclical / restructuring**: normalize across a cycle; do not extrapolate peak/trough margins or working capital.

Minimum financial outputs:
- Revenue growth and organic growth where available
- Gross and GAAP operating margin
- OCF / net income, reported FCF, FCF margin and FCF conversion
- Receivables, inventory, payables and cash conversion cycle where relevant
- ROIC / ROCE definition, ROE context and incremental ROIC for growth
- Net debt, liquidity, maturity and interest coverage
- Share count, SBC, buybacks, dividends and per-share FCF/EPS growth

Explain working-capital effects and distinguish maintenance from growth capex when evidence permits. Do not call a one-period cash-flow spike sustainable without reconciling its source.

#### Mandatory SBC Gate
Before valuation, run the materiality test in `references/SBC-RULES.md`.

If SBC is material, show Reported FCF and Economic FCF; quantify SBC/revenue and SBC/reported FCF; examine gross/net dilution and buybacks; assess funding source; use at least two valuation lenses. Default conservative cross-check: `Economic FCF = Reported FCF - SBC`. Explain company-specific alternatives and retain the simple cross-check.

### 6. Management and Capital Allocation
Evaluate strategic consistency, execution, candor, guidance, incentives, reinvestment returns, M&A discipline, buybacks, dividends and debt. Verify net diluted-share reduction and repurchase valuation. Classify buybacks as value-accretive, dilution-offsetting or value-destructive/risky.

### 7. Key Variables and Monitoring
Reduce the thesis to 3-5 measurable variables. For each include why it matters, current value/status, direction needed, warning threshold and update frequency.

### 8. Valuation — Include 10-Year Return Engine
Use methods appropriate to the company: historical/peer multiples, FCF yield/owner earnings, DCF, Reverse DCF and sum-of-the-parts when relevant. Always produce Bear / Base / Bull with explicit assumptions.

Run a 10-year per-share value bridge. At a 13% hurdle, the required 10-year value factor is 3.3946x. With unchanged valuation and no dividends, per-share intrinsic value must compound at 13%; with dividends, entry discount, dilution or multiple change, model each explicitly. Do not add dividend yield to EPS growth as an exact identity. Show assumptions and confidence; do not manufacture precision.

If SBC is material, use both reported-FCF and Economic-FCF valuation views, preferring the conservative owner-economics base unless a well-supported alternative is explained.

### 9. Decision
Use one conclusion label:
- CORE LONG-TERM HOLD
- ACCUMULATE ON WEAKNESS
- WATCHLIST
- TACTICAL/CYCLICAL ONLY
- AVOID

Include thesis (max 3 bullets), variant perception, valuation/risk balance and suitable investor/time horizon. This is not personalized financial advice.

### 10. Falsification and Review
Provide at least 3 credible bear paths, 3-5 observable Kill Criteria, 3-5 catalysts and a quarterly monitoring checklist.

## Final Report Format — Investment-Bank Style
Use `templates/report-template.md` as canonical content structure. Default to 8 concise pages. Page 1 remains an executive dashboard with investment snapshot, KPIs, valuation range, key variables, risks and confidence. Keep the 8-page order unchanged.

## Writing Standard
Lead with conclusions, then evidence. Use short paragraphs, decision-useful tables and charts. Date every time-sensitive metric. Separate FACT / ESTIMATE / INFERENCE / JUDGMENT. Avoid false precision. Never call a high-SBC company cheap on reported FCF alone.

## Common Failure Modes
- Starting from PE instead of business quality.
- Treating TAM as revenue opportunity.
- Calling technology a moat without customer evidence.
- Confusing company growth with per-share value.
- Treating SBC as free because it is non-cash.
- Praising buybacks while diluted shares do not fall.
- Using reported FCF alone for high-SBC companies.
- Treating working-capital release or supplier-payment timing as recurring cash earnings.
- Using ROE when negative/small equity or leverage makes it meaningless.
- Applying industrial-company FCF/ROIC formulas mechanically to banks, insurers or REITs.
- Forecasting a single precise future or issuing a rating without Kill Criteria.



## Data Standardization and Reproducible Calculation
For any full report, apply `references/DATA-STANDARDIZATION.md` before calculating ratios. Maintain an evidence ledger for every material input: source, period, unit, reported/adjusted status and confidence grade. Do not mix FY, YTD, TTM or quarterly values without reconciliation.

Use `tools/return_engine.py` when a reproducible scenario calculation is needed. The calculator accepts standardized JSON inputs, produces machine-readable JSON or Markdown, and calculates historical quality ratios plus Bear/Base/Bull ten-year paths. Example input: `examples/return_engine_input.json`. Run:

```bash
python tools/return_engine.py examples/return_engine_input.json --format markdown
python -m unittest discover -s tests -v
```

The calculator is deterministic and does not fetch data. It must never be populated with invented values. Its EPS bridge is a transparent scenario model: revenue CAGR × operating-margin change × other EPS effects ÷ diluted-share growth. It does not independently forecast the income statement. ROIC × reinvestment rate is a cross-check, not a guaranteed growth identity. For material SBC, follow `references/SBC-RULES.md`; use Economic FCF cross-checks and do not mistake the calculator's simple FCF-minus-SBC figure for a universal owner-earnings definition.

For every company, store the standardized source-data file, scenario assumptions, calculator output and final report together. A report must distinguish source facts from model assumptions and show confidence grades for key inputs.

## Portable Execution Notes
This skill is platform-neutral. Use available browsing, file-reading, spreadsheet, coding and document-generation tools. If unavailable, state the limitation and list missing data; do not simulate it.
