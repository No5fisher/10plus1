import unittest
from tools.return_engine import calculate, irr, financial_quality


class ReturnEngineTests(unittest.TestCase):
    def base(self):
        return {"company":"TestCo","years":10,"hurdle_rate":0.13,"entry_price":100,"normalized_eps":5,
                "scenarios":[{"name":"Flat","revenue_cagr":0,"starting_operating_margin":0.1,
                              "terminal_operating_margin":0.1,"terminal_pe":20,"payout_ratio":0,
                              "diluted_share_count_cagr":0}]}

    def test_hurdle_factor(self):
        self.assertAlmostEqual(calculate(self.base())["hurdle_future_value_factor"],3.394567,places=5)

    def test_flat_business_flat_multiple(self):
        x=calculate(self.base())["scenarios"][0]
        self.assertAlmostEqual(x["terminal_price"],100,places=8)
        self.assertAlmostEqual(x["dividend_reinvested_irr"],0,places=8)

    def test_dividend_reinvestment(self):
        d=self.base(); d["scenarios"][0]["payout_ratio"]=0.5
        x=calculate(d)["scenarios"][0]
        self.assertGreater(x["dividend_reinvested_irr"],0)
        self.assertGreater(x["cash_dividend_irr"],0)

    def test_dilution_reduces_eps(self):
        d=self.base(); d["scenarios"][0]["diluted_share_count_cagr"]=0.02
        self.assertLess(calculate(d)["scenarios"][0]["terminal_eps"],5)

    def test_margin_expansion_lifts_eps(self):
        d=self.base(); d["scenarios"][0]["terminal_operating_margin"]=0.12
        self.assertGreater(calculate(d)["scenarios"][0]["terminal_eps"],5)

    def test_financial_quality_ratios(self):
        rows=[{"period":"FY","days":365,"revenue":1000,"cogs":600,"ebit":120,"net_income":90,
               "operating_cash_flow":110,"cash_capex":30,"sbc":5,"receivables_begin":80,
               "receivables_end":100,"inventory_begin":100,"inventory_end":120,"payables_begin":70,
               "payables_end":90,"average_invested_capital":600,"normalized_tax_rate":0.25,
               "equity_begin":500,"equity_end":600}]
        x=financial_quality(rows)[0]
        self.assertAlmostEqual(x["fcf"],80)
        self.assertAlmostEqual(x["gross_margin"],0.4)
        self.assertAlmostEqual(x["roic"],0.15)
        self.assertAlmostEqual(x["roe"],90/550)
        self.assertIsNotNone(x["cash_conversion_cycle_days"])

    def test_invalid_price(self):
        d=self.base(); d["entry_price"]=0
        with self.assertRaises(ValueError): calculate(d)

    def test_irr(self):
        self.assertAlmostEqual(irr([-100,110]),0.1,places=7)


if __name__ == "__main__":
    unittest.main()
