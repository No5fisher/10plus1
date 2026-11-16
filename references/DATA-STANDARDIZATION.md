# Data Standardization & Research Controls

## 1. Source hierarchy and evidence ledger
Use sources in this order: audited annual reports/regulatory filings; interim or quarterly filings; official earnings releases, presentations and transcripts; regulators/exchanges/government datasets; reputable financial databases; secondary media.

Every material input records: metric, value, currency/unit, period start/end, filing/publication date, source URL/document/page, reported vs adjusted status, analyst note. Record retrieval date separately from financial period.

## 2. Period alignment
- Never mix FY, calendar year, TTM/LTM, YTD and quarterly values without labeling.
- TTM = latest YTD + prior FY - prior-year comparable YTD; reconcile fiscal year ends.
- For balance-sheet ratios, use average beginning/ending balances where possible.
- For YTD cash flow and income statement comparisons, use same-length prior-year periods.
- Use diluted weighted-average shares for EPS; period-end diluted shares for ownership dilution.
- Separate continuing/discontinued operations, acquisitions, divestitures and accounting-policy changes when material.
- Currency translation must state conversion date and FX rate.

## 3. Standardized input schema
Each annual/interim row may include: period, days, revenue, cogs, gross_profit, ebit, net_income, operating_cash_flow, cash_capex, sbc, receivables_begin/end, inventory_begin/end, payables_begin/end, equity_begin/end, average_invested_capital, normalized_tax_rate.

Use one currency and scale consistently in a file. Missing data remains absent/null; do not enter zero unless zero is the reported fact.

## 4. Ratio definitions and caveats
- Gross margin = gross profit / revenue; fallback = (revenue - COGS) / revenue.
- Operating margin = GAAP EBIT / revenue. Keep adjusted EBIT separate.
- FCF = OCF - cash capex. State whether capitalized software, leases or acquisitions are included.
- Economic FCF cross-check = reported FCF - SBC when material; conservative cross-check, not universal accounting identity.
- OCF/net income and FCF/net income are n/a if net income is zero or negative.
- DSO = average trade receivables / revenue × period days.
- DIO = average inventory / COGS × period days.
- DPO = average trade payables / COGS × period days.
- CCC = DSO + DIO - DPO. Use trade balances; do not mix tax, payroll, contract or financing balances.
- ROIC = NOPAT / average invested capital. State invested-capital definition.
- ROE = net income attributable to common shareholders / average common equity. Suppress or qualify when average equity is zero/negative/distorted.
- Incremental ROIC = change in NOPAT / change in invested capital; use multi-year periods when annual changes are noisy.

## 5. Invested capital definitions
Choose and disclose a primary approach:
- Financing approach: interest-bearing debt + common equity - excess cash.
- Operating approach: operating assets - non-interest-bearing operating liabilities.

Reconcile material differences. Avoid double-counting leases/pensions. State whether goodwill is included; show tangible invested capital as a separate sensitivity for acquisitive businesses. Negative equity is not a license to report meaningless ROE or ROIC.

## 6. Quality-control flags
Investigate: receivables growing materially faster than revenue; inventory growing faster than COGS/sales; payables days sharply increasing and driving OCF; net income rising while OCF persistently lags; FCF positive only through deferred capex or working-capital release; goodwill rising without post-deal returns; buybacks failing to reduce diluted shares; repurchases exceeding FCF while leverage rises; material other income/fair-value gains/tax benefits; short-term debt rising while cash is restricted or illiquid; restatements, auditor changes, related-party transactions or covenant risks.

These are investigation triggers, not automatic proof of misconduct or poor quality.

## 7. Data confidence
- A: audited/filing value, clearly defined and comparable.
- B: company-reported but adjusted/unaudited or needs limited reconciliation.
- C: analyst-derived estimate with disclosed formula and source inputs.
- D: proxy, incomplete or materially non-comparable.

Do not give overall High confidence if a key valuation driver or balance-sheet risk is C/D. State what evidence would raise confidence.

## 8. Reproducibility
Save source-data table, assumptions, model version, report date and calculator output with each research package. A second analyst must reproduce key ratios and scenarios without guessing.
