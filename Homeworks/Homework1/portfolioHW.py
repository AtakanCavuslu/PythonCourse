import random
from datetime import datetime

# Keep a list of stock objects for future price check
globalStocks = []

# Portfolio object storing a client's portfolio
class Portfolio():

    # Initialize with 0 balance
    cash = 0
    stocks = {}
    mutualFunds = {}
    transactions = []

    # Override the print methods
    def __str__(self):
        # Store the variables to return
        cash = self.cash
        stocks = self.stocks.keys()
        mutualFunds = self.mutualFunds.keys()
        # Create a list with rows to join together
        display = ["------------------------------------------------------------------------------------"]
        display.append("Here is the portfolio")
        display.append("------------------------------------------------------------------------------------")
        display.append("%-12s%-1s%-12i" % ("CASH:", "$",cash))
        for stock in stocks:
            display.append("%-12s%-6.2f%-12s" % ("STOCK:", self.stocks[stock], stock))
        for mutualFund in mutualFunds:
            display.append("%-12s%-6.2f%-12s" % ("M.FUND:", self.mutualFunds[mutualFund], mutualFund))
        display.append("------------------------------------------------------------------------------------")
        return "\n".join(display)

    # History method to list all the transactions
    # Reverse the list to order the list from the latest
    def history(self):
        self.transactions.reverse()
        display = ["------------------------------------------------------------------------------------"]
        display.append("Here is the transaction history")
        display.append("------------------------------------------------------------------------------------")
        display.append("%-29s%-8s%-11s%-8s%-8s%-5s" % ("DATE", "TYPE", "ORDER", "AMOUNT", "SYMBOL", "PRICE"))
        display.append("------------------------------------------------------------------------------------")
        for transaction in self.transactions:
            type = transaction.type
            order = transaction.order
            amount = transaction.amount
            date = transaction.date
            symbol = transaction.symbol
            price = transaction.price
            display.append("%-29s%-8s%-11s%-8s%-8s%-5s" % (date, type, order, amount, symbol, price))
        display.append("------------------------------------------------------------------------------------")
        output = "\n".join(display)
        print(output)

    # Define custom object methods - Operations
    def addCash(self, amount):
        self.cash = self.cash + amount
        # Add to transcations
        transaction = Transaction("CASH", "ADD", amount)
        self.transactions.append(transaction)

    def withdrawCash(self, amount):
        self.cash = self.cash - amount
        # Add to transcations
        transaction = Transaction("CASH", "WITHDRAW", amount)
        self.transactions.append(transaction)

    def buyStock(self, amount, stock):
        symbol = stock.symbol
        price = stock.price
        self.stocks[symbol] = amount
        # Deduct the price from the cash balance
        self.cash = self.cash - (amount * price)
        # Add to transcations
        transaction = Transaction("STOCK", "BUY", amount, symbol, price)
        self.transactions.append(transaction)

    def sellStock(self, symbol, amount):
        if symbol in self.stocks.keys():
            # Stock is present in the inventory
            if self.stocks[symbol] > amount:
                # Sell order is applicaple
                self.stocks[symbol] = self.stocks[symbol] - amount
                # Add the price to the cash balance
                for globalStock in globalStocks:
                    if globalStock.symbol == symbol:
                        # Sell price is uniformly drawn from [0.5X - 1.5X]
                        upperLimit = 1.5 * globalStock.price
                        lowerLimit = 0.5 * globalStock.price
                        sharePrice = random.uniform(lowerLimit, upperLimit)
                        totalPrice = sharePrice * amount
                        self.cash = self.cash + totalPrice
                        # Add to transcations
                        transaction = Transaction("STOCK", "SELL", amount, symbol, sharePrice)
                        self.transactions.append(transaction)
            else:
                # Not enough shares present to sell
                print("Error! Not enough stock shares owned")
        else:
            # Stock shares iare not present
            print("Error! No shares of specified stock owned")

    def buyMutualFund(self, amount, mutualFund):
        symbol = mutualFund.symbol
        price = mutualFund.price
        self.mutualFunds[symbol] = amount
        # Deduct the price from the cash balance
        # Price of each share is $1
        self.cash = self.cash - amount
        # Add to transcations
        transaction = Transaction("M.FUND", "BUY", amount, symbol, price)
        self.transactions.append(transaction)

    def sellMutualFund(self, symbol, amount):
        if symbol in self.mutualFunds.keys():
            # Stock is present in the inventory
            if self.mutualFunds[symbol] > amount:
                # Sell order is applicaple
                self.mutualFunds[symbol] = self.mutualFunds[symbol] - amount
                # Add the price to the cash balance
                # Selling price is uniformly drawn from [0.9 - 1.2]
                sharePrice = random.uniform(0.9, 1.2)
                totalPrice = sharePrice * amount
                self.cash = self.cash + totalPrice
                # Add to transcations
                transaction = Transaction("M.FUND", "SELL", amount, symbol, sharePrice)
                self.transactions.append(transaction)
            else:
                # Not enough shares present to sell
                print("Error! Not enough mutual funds shares owned")
        else:
            # Mutual fund shares are not present
            print("Error! No shares of specified mutual fund owned")

# Create stock and mutual fund objects
# No need to use inheritance since objects only use initializer method
# - no custom methods
class Stock():
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol
        # Save the share to the global list
        globalStocks.append(self)

class MutualFund():
    def __init__(self, symbol):
        self.price = 1
        self.symbol = symbol

# Transaction object to store transactions
class Transaction():
    def __init__(self, type, order, amount, symbol = None, price = None, date = datetime.now()):
        self.type = type
        self.order = order
        self.amount = amount
        self.date = date
        self.symbol = symbol
        self.price = price

########### EXAMPLE #############
portfolio = Portfolio()
portfolio.addCash(300.50)
s = Stock(20, "HFH")
portfolio.buyStock(5, s)
mf1 = MutualFund("BRT")
mf2 = MutualFund("GHT")
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2)
print(portfolio)
portfolio.sellMutualFund("BRT", 3)
portfolio.sellStock("HFH", 1)
portfolio.withdrawCash(50)
portfolio.history()
