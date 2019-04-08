import unittest
import portfolioHW

class portfolioTest(unittest.TestCase):

    def testCashBalance(self):

        portfolio = portfolioHW.Portfolio()
        portfolio.addCash(500)
        portfolio.withdrawCash(200)

        self.assertEqual(300, portfolio.cash)

    def testStockOperations(self):

        portfolio = portfolioHW.Portfolio()
        s = portfolioHW.Stock(20, "HFH")
        portfolio.buyStock(5, s)
        amount = portfolio.stocks["HFH"]
        self.assertEqual(amount, 5)

if __name__ == "__main__":
    unittest.main()
