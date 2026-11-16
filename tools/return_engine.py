#!/usr/bin/env python3
"""Fisher Company Analysis: deterministic financial-quality and 10-year return calculator.

Usage:
  python tools/return_engine.py examples/return_engine_input.json
  python tools/return_engine.py examples/return_engine_input.json --format markdown

All monetary values must use one consistent currency/unit per input file.
This is a transparent scenario calculator, not a data provider or forecast generator.
"""
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
from typing import Any


def num(value: Any, field: str, *, optional: bool = False) -> float | None:
    if value is None and optional:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} must be a number" + (" or null" if optional else ""))
    value = float(value)
    if not math.isfinite(value):
        raise ValueError(f"{field} must be finite")
    return value


def cagr(start: float, end: float, years: int) -> float | None:
    if start <= 0 or end <= 0 or years <= 0:
        return None
    return (end / start) ** (1 / years) - 1


def irr(cashflows: list[float]) -> float | None:
    if len(cashflows) < 2 or cashflows[0] >= 0:
        return None
    def npv(rate: float) -> float:
        return sum(cf / ((1 + rate) ** i) for i, cf in enumerate(cashflows))
    lo, hi = -0.9999, 10.0
    flo, fhi = npv(lo), npv(hi)
    if flo * fhi > 0:
        return None
    for _ in range(250):
        mid = (lo + hi) / 2
        fm = npv(mid)
        if abs(fm) < 1e-10:
            return mid
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def run_scenario(base: dict[str, Any], s: dict[str, Any]) -> dict[str, Any]:
    years = int(base.get("years", 10))
    if years < 1 or years > 30:
        raise ValueError("years must be between 1 and 30")
    price0 = num(base["entry_price"], "entry_price")
    eps0 = num(base["normalized_eps"], "normalized_eps")
    hurdle = num(base.get("hurdle_rate", 0.13), "hurdle_rate")
    if price0 <= 0 or eps0 <= 0:
        raise ValueError("entry_price and normalized_eps must be positive")
    if hurdle <= -1:
        raise ValueError("hurdle_rate must be greater than -100%")

    name = s["name"]
    revenue_cagr = num(s["revenue_cagr"], f"{name}.revenue_cagr")
    margin0 = num(s["starting_operating_margin"], f"{name}.starting_operating_margin")
    marginN = num(s["terminal_operating_margin"], f"{name}.terminal_operating_margin")
    share_cagr = num(s.get("diluted_share_count_cagr", 0), f"{name}.diluted_share_count_cagr")
    other_eps_cagr = num(s.get("other_eps_cagr", 0), f"{name}.other_eps_cagr")
    terminal_pe = num(s["terminal_pe"], f"{name}.terminal_pe")
    payout = num(s.get("payout_ratio", 0), f"{name}.payout_ratio")
    roic = num(s.get("incremental_roic"), f"{name}.incremental_roic", optional=True)
    reinvest = num(s.get("reinvestment_rate"), f"{name}.reinvestment_rate", optional=True)

    if margin0 <= 0 or marginN <= 0 or terminal_pe <= 0:
        raise ValueError(f"{name}: margins and terminal_pe must be positive")
    if not 0 <= payout <= 1:
        raise ValueError(f"{name}: payout_ratio must be in [0,1]")
    if share_cagr <= -1 or other_eps_cagr <= -1 or revenue_cagr <= -1:
        raise ValueError(f"{name}: growth rates must be greater than -100%")

    entry_pe = price0 / eps0
    eps_path, price_path, dividends = [], [], []
    shares_reinvested = 1.0
    cashflows = [-price0]
    for year in range(1, years + 1):
        progress = year / years
        margin_t = margin0 + (marginN - margin0) * progress
        eps_t = (eps0 * ((1 + revenue_cagr) ** year) * (margin_t / margin0)
                 * ((1 + other_eps_cagr) ** year) / ((1 + share_cagr) ** year))
        pe_t = entry_pe + (terminal_pe - entry_pe) * progress
        price_t = eps_t * pe_t
        dividend_t = eps_t * payout
        eps_path.append(eps_t); price_path.append(price_t); dividends.append(dividend_t)
        cashflows.append(dividend_t if year < years else dividend_t + price_t)
        if price_t > 0:
            shares_reinvested += (shares_reinvested * dividend_t) / price_t

    terminal_eps, terminal_price = eps_path[-1], price_path[-1]
    cash_dividend_irr = irr(cashflows)
    reinvested_wealth = shares_reinvested * terminal_price
    reinvested_irr = (reinvested_wealth / price0) ** (1 / years) - 1
    required_eps_cagr = ((price0 * ((1 + hurdle) ** years)) / (eps0 * terminal_pe)) ** (1 / years) - 1
    sustainable_growth = roic * reinvest if roic is not None and reinvest is not None else None
    return {
        "name": name, "entry_pe": entry_pe, "terminal_eps": terminal_eps,
        "terminal_price": terminal_price, "terminal_pe": terminal_pe,
        "eps_cagr": cagr(eps0, terminal_eps, years),
        "price_cagr_ex_dividends": (terminal_price / price0) ** (1 / years) - 1,
        "total_dividends_per_initial_share": sum(dividends),
        "cash_dividend_irr": cash_dividend_irr,
        "dividend_reinvested_ending_wealth": reinvested_wealth,
        "dividend_reinvested_irr": reinvested_irr,
        "required_eps_cagr_no_dividends": required_eps_cagr,
        "incremental_roic": roic, "reinvestment_rate": reinvest,
        "roic_implied_growth": sustainable_growth,
        "revenue_growth_less_roic_implied_growth": revenue_cagr - sustainable_growth if sustainable_growth is not None else None,
        "annual_path": [{"year": i + 1, "eps": eps_path[i], "price": price_path[i],
                         "dividend_per_share": dividends[i]} for i in range(years)],
        "interpretation": "ROIC × reinvestment rate is a rough sustainable operating-growth cross-check, not an identity for revenue CAGR or EPS CAGR. Investigate material divergence."
    }


def financial_quality(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    out = []
    for row in rows:
        year, days = row.get("period", "unknown"), float(row.get("days", 365))
        revenue = num(row.get("revenue"), f"{year}.revenue", optional=True)
        cogs = num(row.get("cogs"), f"{year}.cogs", optional=True)
        gp = num(row.get("gross_profit"), f"{year}.gross_profit", optional=True)
        ebit = num(row.get("ebit"), f"{year}.ebit", optional=True)
        ni = num(row.get("net_income"), f"{year}.net_income", optional=True)
        ocf = num(row.get("operating_cash_flow"), f"{year}.operating_cash_flow", optional=True)
        capex = num(row.get("cash_capex"), f"{year}.cash_capex", optional=True)
        sbc = num(row.get("sbc"), f"{year}.sbc", optional=True)
        fcf = ocf - capex if ocf is not None and capex is not None else None

        def balance(begin: str, end: str, ending: str):
            if row.get(begin) is not None and row.get(end) is not None:
                return (float(row[begin]) + float(row[end])) / 2, "average_begin_end"
            if row.get(end) is not None:
                return float(row[end]), "ending_balance_proxy"
            if row.get(ending) is not None:
                return float(row[ending]), "ending_balance_proxy"
            return None, None

        rec, rec_basis = balance("receivables_begin", "receivables_end", "receivables")
        inv, inv_basis = balance("inventory_begin", "inventory_end", "inventory")
        ap, ap_basis = balance("payables_begin", "payables_end", "payables")
        dso = rec / revenue * days if rec is not None and revenue and revenue > 0 else None
        dio = inv / cogs * days if inv is not None and cogs and cogs > 0 else None
        dpo = ap / cogs * days if ap is not None and cogs and cogs > 0 else None
        invested = num(row.get("average_invested_capital"), f"{year}.average_invested_capital", optional=True)
        tax = num(row.get("normalized_tax_rate"), f"{year}.normalized_tax_rate", optional=True)
        nopat = ebit * (1 - tax) if ebit is not None and tax is not None else None
        roic = nopat / invested if nopat is not None and invested is not None and invested > 0 else None
        equity_avg, equity_basis = balance("equity_begin", "equity_end", "equity")
        roe = ni / equity_avg if ni is not None and equity_avg is not None and equity_avg > 0 else None
        gross_margin = gp / revenue if gp is not None and revenue else ((revenue-cogs)/revenue if revenue and cogs is not None else None)
        op_margin = ebit / revenue if ebit is not None and revenue else None
        net_margin = ni / revenue if ni is not None and revenue else None
        ocf_ni = ocf / ni if ocf is not None and ni not in (None, 0) else None
        fcf_margin = fcf / revenue if fcf is not None and revenue else None
        fcf_conv = fcf / ni if fcf is not None and ni not in (None, 0) else None
        warnings = []
        if "ending_balance_proxy" in (rec_basis, inv_basis, ap_basis):
            warnings.append("Working-capital days use ending-balance proxies; average balances are preferred.")
        if equity_basis == "ending_balance_proxy":
            warnings.append("ROE uses ending equity as a proxy; average equity is preferred.")
        if equity_avg is not None and equity_avg <= 0:
            warnings.append("ROE suppressed because average common equity is non-positive; use operating returns and capital-structure analysis instead.")
        if roic is None:
            warnings.append("ROIC unavailable: provide EBIT, normalized_tax_rate and positive average_invested_capital.")
        if fcf is not None and sbc is None:
            warnings.append("SBC not supplied; Economic FCF cross-check unavailable.")
        if ni is not None and ni > 0 and ocf is not None and ocf < 0:
            warnings.append("Positive net income with negative operating cash flow: investigate earnings-to-cash divergence.")
        out.append({
            "period": year, "gross_margin": gross_margin, "operating_margin": op_margin,
            "net_margin": net_margin, "ocf_to_net_income": ocf_ni, "fcf": fcf,
            "fcf_margin": fcf_margin, "fcf_conversion": fcf_conv,
            "economic_fcf_minus_sbc": fcf - sbc if fcf is not None and sbc is not None else None,
            "sbc_to_revenue": sbc / revenue if sbc is not None and revenue else None,
            "dso_days": dso, "dio_days": dio, "dpo_days": dpo,
            "cash_conversion_cycle_days": dso + dio - dpo if dso is not None and dio is not None and dpo is not None else None,
            "working_capital_balance_basis": {"receivables": rec_basis, "inventory": inv_basis, "payables": ap_basis},
            "nopat": nopat, "average_invested_capital": invested, "roic": roic, "roe": roe,
            "roe_equity_basis": equity_basis, "warnings": warnings
        })
    return out


def calculate(data: dict[str, Any]) -> dict[str, Any]:
    scenarios = data.get("scenarios", [])
    if not scenarios:
        raise ValueError("At least one scenario is required")
    years, hurdle = int(data.get("years", 10)), float(data.get("hurdle_rate", 0.13))
    return {
        "company": data.get("company", "Unspecified"), "as_of": data.get("as_of", "not supplied"),
        "currency_unit": data.get("currency_unit", "not supplied"), "years": years, "hurdle_rate": hurdle,
        "hurdle_future_value_factor": (1 + hurdle) ** years,
        "scenarios": [run_scenario(data, s) for s in scenarios],
        "historical_financial_quality": financial_quality(data.get("historical_financials", [])),
        "limitations": [
            "Scenario outputs are only as reliable as user-supplied assumptions and source data.",
            "Revenue growth, operating-margin change, other EPS effects and diluted-share growth are modeled separately.",
            "ROIC × reinvestment rate is a consistency check, not a guaranteed growth equation.",
            "Dividends are modeled annually; actual ex-dates, taxes, withholding and reinvestment prices may differ.",
            "The script does not fetch filing/market data or estimate maintenance capex automatically."
        ]
    }


def fmt(v):
    if v is None: return "n/a"
    if isinstance(v, float) and abs(v) < 1 and v != 0: return f"{v:.2%}"
    if isinstance(v, float): return f"{v:,.3f}"
    return str(v)


def to_markdown(r):
    lines = [f"# {r['company']} — 10-Year Return Engine",
             f"- As of: {r['as_of']}", f"- Currency/unit: {r['currency_unit']}",
             f"- Horizon: {r['years']} years", f"- Hurdle: {r['hurdle_rate']:.2%}",
             f"- Required future-value factor: {r['hurdle_future_value_factor']:.4f}x", "",
             "| Scenario | EPS CAGR | Terminal EPS | Terminal price | Terminal P/E | Cash-dividend IRR | Reinvested-dividend IRR | Required EPS CAGR (no div.) |",
             "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for s in r["scenarios"]:
        lines.append("| " + " | ".join([s["name"], fmt(s["eps_cagr"]), fmt(s["terminal_eps"]),
            fmt(s["terminal_price"]), fmt(s["terminal_pe"]), fmt(s["cash_dividend_irr"]),
            fmt(s["dividend_reinvested_irr"]), fmt(s["required_eps_cagr_no_dividends"])]) + " |")
    if r["historical_financial_quality"]:
        lines += ["", "## Historical financial quality", "",
                  "| Period | Gross margin | Operating margin | OCF/NI | FCF margin | FCF conversion | ROIC | ROE | CCC days |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for x in r["historical_financial_quality"]:
            lines.append("| " + " | ".join([str(x["period"]), fmt(x["gross_margin"]), fmt(x["operating_margin"]),
                fmt(x["ocf_to_net_income"]), fmt(x["fcf_margin"]), fmt(x["fcf_conversion"]),
                fmt(x["roic"]), fmt(x["roe"]), fmt(x["cash_conversion_cycle_days"])]) + " |")
    lines += ["", "## Limitations"] + [f"- {x}" for x in r["limitations"]]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        result = calculate(data)
        output = to_markdown(result) if args.format == "markdown" else json.dumps(result, ensure_ascii=False, indent=2)
        if args.output: args.output.write_text(output, encoding="utf-8")
        else: print(output)
        return 0
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
