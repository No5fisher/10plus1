# Financial Quality & 10-Year Return Engine

This module extends (does not replace) the 10-box investment map and the canonical 8-page report. Its purpose is to test whether accounting earnings are economically real, whether assets are recoverable, and whether per-share intrinsic value can compound at the investor's required rate.

## 1. Classify the business before selecting metrics

Do not classify by company age or label alone. Classify by economic state:

- **Growth / investment phase**: demand and product-market fit are still developing; current margins or ROIC may be depressed by deliberate investment; the key question is whether incremental investment earns attractive returns.
- **Scaling / transition phase**: revenue is growing and operating leverage is emerging; determine whether unit economics, retention, pricing and incremental margins improve as scale rises.
- **Mature / cash-generation phase**: economics are established; focus on durability of margins, asset quality, cash conversion, maintenance investment and capital allocation.
- **Cyclical / restructuring phase**: normalize mid-cycle earnings, working capital and capex; do not extrapolate peak or trough metrics.

A company can be mature in one segment and growth-stage in another. Use segment-level analysis where material.

## 2. Growth-company financial quality

Prioritize leading indicators and incremental economics rather than blindly applying mature-company thresholds.

### Commercial validation
Track revenue growth by organic / acquired / price / volume; customer count and concentration; retention, repeat purchase, usage, ARPU or same-store metrics where relevant; backlog only when conversion quality is evidenced. Distinguish TAM from serviceable demand and realized revenue.

### Margin and operating leverage
Track gross margin, contribution margin, GAAP operating margin, and incremental operating margin:
`Incremental operating margin = change in operating profit / change in revenue`.
A rising gross margin with rising sales-and-marketing or support costs may not create operating leverage. Do not rely on adjusted EBITDA alone.

### Incremental capital efficiency
`Incremental ROIC = change in NOPAT / change in invested capital`.
Use multi-year windows when annual changes are noisy. Adjust for acquisitions, asset sales, working-capital swings, capitalized development and lease liabilities. For R&D-intensive firms, show reported ROIC and a clearly labeled R&D-capitalized sensitivity if material; never silently capitalize costs.

### Cash runway and financing dependence
Show operating cash flow, reported FCF, capex, cash balance, net debt, maturities, cash burn and months of runway where relevant. Separate growth capex from maintenance capex when evidence permits. If the company needs repeated external funding before reaching self-funding economics, model dilution and refinancing risk explicitly.

### Per-share validation
Track revenue/share, FCF/share, diluted EPS and diluted shares. Growth in total revenue or EBITDA is not a substitute for growth in value per share.

## 3. Mature-company financial quality

Use at least 5 years and preferably 10 years when comparable data exists. Prioritize:

- Revenue / organic growth and segment mix
- Gross margin, GAAP operating margin and normalized net margin
- Operating cash flow / net income; FCF / net income; FCF margin
- ROIC, ROCE and ROE with capital-structure context
- Maintenance capex, total capex and reinvestment rate
- Net debt, interest coverage, lease liabilities, pension and contingent liabilities
- Receivables, inventory, payables, goodwill, intangibles and impairments
- Diluted shares, SBC, buybacks, dividends and per-share outcomes

A high ROE is not sufficient evidence of quality if leverage is high, equity is unusually small/negative, or buybacks have distorted book equity. Prefer ROIC/ROCE for operating businesses, but adapt for banks, insurers, utilities, REITs and distributors.

## 4. Earnings quality and cash conversion

Calculate and interpret, not merely list:

- `OCF / Net income`: compare across a cycle; explain working-capital timing, taxes, litigation, provisions and non-cash items.
- `FCF = OCF - cash capex`; disclose whether capitalized software is included. FCF is not automatically distributable if maintenance needs are understated.
- `FCF margin = FCF / revenue`.
- `FCF conversion = FCF / net income`.
- `Cash conversion cycle = DSO + DIO - DPO`; interpret against business model and supplier terms.
- `DSO = average trade receivables / revenue × days`; `DIO = average inventory / cost of sales × days`; `DPO = average trade payables / cost of sales × days`. Use average balances and align periods; if only point-in-time balances exist, label the estimate.
- For distributors, assess gross profit dollars and operating profit per unit of working capital, receivable aging, customer concentration, supplier terms and inventory turns. Thin margins make small changes in working-capital funding or gross profit economically important.

Do not interpret a single-year OCF spike as recurring cash earning power. Reconcile the source of change.

## 5. Asset quality and balance-sheet integrity

Review asset recoverability and funding:

- Cash: restricted cash, pledged deposits, trapped cash and liquid investment quality.
- Receivables: aging, overdue balances, allowance coverage, write-offs, customer concentration and growth relative to sales.
- Inventory: turnover, aging, write-downs, obsolescence, price risk and inventory growth relative to sales/cost of sales.
- Prepayments and other current assets: explain material growth and recoverability.
- Goodwill/intangibles: acquisition origin, impairment headroom, amortization and post-deal returns.
- PP&E / capitalized software / development assets: maintenance burden, useful-life assumptions and impairment risk.
- Liabilities: distinguish trade payables/accruals from interest-bearing debt; inspect maturity schedule, leases, pensions, litigation, guarantees and off-balance-sheet commitments.
- Working-capital liabilities are not automatically “free financing”: assess supplier dependence, payment terms, concentration and the risk of reversal.

Where possible compute net operating working capital and invested capital consistently. State the definition:
`Invested capital = interest-bearing debt + equity - excess cash` is one common convention, but for businesses with negative equity or large operating liabilities also calculate an operating approach:
`Operating invested capital = operating assets - non-interest-bearing operating liabilities`.
Do not compare ROIC values built on different definitions without reconciliation.

## 6. ROIC, ROE and reinvestment

Default formulas:
- `NOPAT = EBIT × (1 - normalized cash tax rate)`.
- `ROIC = NOPAT / average invested capital`.
- `ROCE = EBIT / average capital employed`; define capital employed.
- `ROE = net income attributable to common shareholders / average common equity`.
- `Sustainable growth ≈ ROIC × reinvestment rate`, only when incremental returns are reasonably close to the measured ROIC and leverage/payout policy are stable.
- `Required reinvestment rate = target growth / incremental ROIC`.

Show both reported and adjusted ROIC where acquisitions, excess cash, unusual working capital, leases or negative equity materially distort the result. Do not present a precise ROIC when invested capital cannot be reliably defined; give a range or proxy and explain the limitation.

## 7. 10-Year Return Engine

The required return is a hurdle, not a forecast. Default test case may be 13% annualized over 10 years, but make the hurdle editable.

### Core mathematics
- `Future value factor = (1 + hurdle)^10`; at 13%, this is 3.3946x.
- With unchanged valuation multiple and no dividends, per-share earnings / owner earnings / intrinsic value must grow about 3.3946x, or 13% CAGR.
- `Future price = future per-share earnings × terminal P/E`.
- `Total shareholder return = price appreciation + dividends`; model dividends explicitly, including payout, reinvestment and taxes where relevant.
- For reinvested dividends, calculate IRR from dated cash flows or use a clearly labeled simplified compounding approximation. Do not simply add dividend yield to EPS growth as an exact identity.
- For share repurchases, model net diluted-share change and repurchase price. Repurchases below intrinsic value can increase per-share value; above intrinsic value can destroy it.
- For SBC, apply the mandatory SBC rules and show owner economics separately.

### Required bridge
`Per-share intrinsic value growth = operating growth + margin change + capital-efficiency change + net capital-allocation effect - dilution effect`.
Avoid double-counting buybacks, dividends or changes in valuation multiple.

### Scenario table
Build Bear / Base / Bull cases over 10 years. For each show revenue CAGR, operating margin, incremental ROIC/reinvestment, net share-count CAGR, dividend yield/payout, terminal multiple and resulting per-share value/IRR. If inputs cannot be supported, mark the scenario as illustrative and confidence low.

### 13% hurdle diagnosis
State which of these is required:
1. per-share earnings / owner earnings CAGR if valuation is unchanged and dividends are excluded;
2. lower required operating growth if sustainable dividends contribute;
3. lower required growth if the purchase price is below estimated intrinsic value;
4. higher required growth if valuation compresses or dilution rises.

A low entry price can improve investor IRR without improving business quality. Never use a discount to excuse weak assets, poor cash conversion or sub-cost-of-capital reinvestment.

## 8. Lifecycle-specific scorecards

Suggested starting weights only; adjust by sector and explain any change.

**Growth / scaling businesses**
- Market and product validation 20%
- Revenue and margin quality 20%
- Incremental ROIC / capital efficiency 20%
- Cash runway / funding resilience 15%
- Asset quality 10%
- Management / capital allocation / dilution 15%

**Mature operating businesses**
- Earnings quality 20%
- Asset quality 20%
- ROIC / capital efficiency 20%
- FCF and cash conversion 20%
- Capital allocation 10%
- Financial resilience 10%

For cyclical, financial, regulated, asset-heavy or distributor models, replace generic measures with sector-specific ones. Weights are analytical aids, not universal truth.

## 9. Sector-specific overrides

- **Pharmaceutical / healthcare distributors**: revenue is high-volume/low-margin; prioritize gross profit dollars, operating profit, customer concentration, receivable collectability, inventory turns, supplier credit, working-capital volatility, litigation and contract renewals. Revenue growth alone is weak evidence of value creation.
- **Consumer staples / branded food**: prioritize volume vs price/mix, brand strength, channel inventory, gross margin, selling/marketing efficiency, distributor receivables, inventory freshness, raw-material exposure, capex and dividend sustainability. Separate recurring operating earnings from investment income and fair-value gains.
- **Software / platform**: include SBC, retention, customer concentration, R&D, capitalized software, deferred revenue and net dilution.
- **Banks / insurers**: do not apply industrial-company FCF or ROIC mechanically; use regulatory capital, underwriting/credit quality, reserve adequacy, solvency, book value and distributable earnings.
- **Utilities / REITs / infrastructure**: assess regulated returns, asset base, maintenance and growth capex, leverage, refinancing, occupancy/FFO and asset duration.

## 10. Required report outputs

Within the existing 8-page report, add:
- A lifecycle label and reason.
- A financial quality panel: earnings quality, asset quality, cash conversion, capital efficiency and per-share economics.
- A reconciliation of OCF and FCF drivers, including working capital.
- ROIC definition and limitations.
- A 10-year per-share value bridge and 13% hurdle test.
- Bear / Base / Bull ten-year IRR, with assumptions and confidence.
- Explicit warning when data is insufficient to support a precise estimate.

Facts, company guidance, analyst calculations, inferences and judgments must remain separately labeled.
