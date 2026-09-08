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
Map upstream suppliers -> company -> customers/downstream. Add competitors, complements, substitutes, regulators and capital providers where material.

Identify:
- industry structure and profit pool
- bargaining power and control of scarce resources
- structural growth vs cyclical growth
- technology/regulatory changes that could alter the system
- company position: challenger, enhancer, platform, incumbent, niche or commodity player

### 4. Competitive Advantage
Identify only evidence-backed advantages:
- technology/know-how
- cost advantage
- network effects
- switching costs
- brand/trust
- distribution/channel
- data/scale/ecosystem
- regulation/license

Then answer: Is the moat widening, stable or narrowing? What metric proves it?

### 5. Financial Quality
Use at least 5 years when available; 10 years for mature companies when useful.

Minimum metrics:
- revenue growth and organic growth where available
- gross and operating margin
- free cash flow and FCF margin
- ROIC (or best available proxy) and ROE where relevant
- net debt / liquidity / interest coverage
- share count and dilution; stock-based compensation where material
- per-share FCF/EPS/value growth

Look for divergence: earnings vs cash flow, revenue vs receivables, buybacks vs dilution, growth vs capital intensity.

#### Mandatory SBC Gate
Before valuation, run the materiality test in `references/SBC-RULES.md`.

If SBC is material, the analysis MUST:
- show Reported FCF and Economic FCF
- quantify SBC / revenue and SBC / reported FCF
- examine diluted share-count change and gross/net dilution
- test whether buybacks create net share reduction or merely offset SBC issuance
- assess whether buybacks are funded by FCF, cash or debt
- use at least two valuation lenses: reported-FCF and SBC-adjusted owner economics
- include SBC as a quarterly monitoring variable

Default conservative cross-check: `Economic FCF = Reported FCF - SBC`.
Do not claim this is the only theoretically valid treatment; explain alternative company-specific treatment when used.

### 6. Management and Capital Allocation
Evaluate:
- strategic consistency and execution record
- candor about failures and guidance quality
- insider incentives and ownership
- reinvestment returns
- M&A discipline
- buyback/dividend/debt decisions
- whether management optimizes per-share value or empire size

For buybacks, never equate repurchase dollars with shareholder friendliness. Verify net diluted-share reduction, repurchase valuation and balance-sheet impact.

### 7. Key Variables and Monitoring
Reduce the thesis to 3-5 measurable variables. Each variable must have:
- why it matters
- current value/status
- direction needed for thesis to strengthen
- warning threshold
- update frequency

### 8. Valuation
Do not rely on a single method. Use methods appropriate to the company:
- historical multiples
- peer multiples adjusted for growth/quality
- FCF yield / owner earnings
- DCF or scenario DCF
- Reverse DCF: what growth/margin assumptions are embedded in today's price?
- sum-of-the-parts when segments require it

Always produce Bear / Base / Bull scenarios with explicit assumptions. Show expected return/range when enough data exists. If inputs are too uncertain, state that valuation confidence is low rather than inventing precision.

If SBC is material, Reported FCF must not be the only DCF/owner-earnings base. Prefer Economic FCF as the conservative base case and show how the conclusion changes under the reported-FCF lens.

### 9. Decision
Use one conclusion label:
- CORE LONG-TERM HOLD
- ACCUMULATE ON WEAKNESS
- WATCHLIST
- TACTICAL/CYCLICAL ONLY
- AVOID

Include:
- thesis in 3 bullets maximum
- what the market may be missing
- main variant perception
- valuation/risk balance
- suitable investor/time horizon

Do not present the label as personalized financial advice. Position sizing depends on the investor's objectives, diversification, tax situation and risk tolerance.

### 10. Falsification and Review
Provide:
- Bear case: minimum 3 credible failure paths
- Kill Criteria: 3-5 observable conditions
- next catalysts: 3-5 events/data releases
- quarterly monitoring checklist

A thesis without falsification criteria is incomplete.

## Final Report Format - Investment-Bank Style
Use `templates/report-template.md` as the canonical content template. Default to 8 concise pages. Page 1 must be an executive dashboard with investment snapshot, KPIs, valuation range, key variables, risks and confidence.

When the runtime supports document generation, render the template into PDF/DOCX while preserving its information hierarchy. Do not make the methodology depend on a particular document tool.

## Writing Standard
- Lead with conclusions, then evidence.
- Use short paragraphs, tables and charts; avoid narrative padding.
- Every table must answer a decision question.
- Distinguish reported data from analyst calculations.
- Use exact dates/periods for current metrics.
- Avoid false precision and promotional language.
- State uncertainty explicitly.
- For material SBC companies, never describe valuation as “cheap on FCF” without also showing the SBC-adjusted owner-economics view.

## Common Failure Modes
- Starting from PE instead of business quality -> analyze business first.
- Treating TAM as revenue opportunity -> test adoption, competition and economics.
- Calling technology a moat without customer evidence -> show retention, pricing, share or cost proof.
- Confusing company growth with per-share value -> inspect dilution and FCF per share.
- Treating SBC as free because it is non-cash -> run the mandatory SBC gate.
- Praising buybacks while share count does not fall -> classify them as dilution-offsetting.
- Using reported FCF alone for high-SBC software companies -> show Economic FCF cross-check.
- Listing 20 risks without prioritization -> identify 3-5 thesis-breaking risks.
- Forecasting one precise future -> use scenarios and probabilities.
- Producing a recommendation without kill criteria -> incomplete analysis.
- Using stale market data as current -> date every time-sensitive metric.

## Portable Execution Notes
This skill is platform-neutral. Use whatever browsing, file-reading, spreadsheet, coding, charting or document-generation capabilities the current AI platform provides. If a capability is unavailable, do not simulate it: state the limitation, continue with available evidence, and list the missing data needed to complete the analysis.
