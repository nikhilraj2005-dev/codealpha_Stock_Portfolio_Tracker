# Stock prices dictionary

stock_prices = {
    "APPLE": 180,
    "TESLA": 250,
    "GOOGLE": 150,
    "MICROSOFT": 420,
    "AMAZON": 200
}

print("Welcome to Stock Portfolio Tracker!")
print("\nAvailable Stocks:")

for stock, price in stock_prices.items():
    print(stock, ":", price)
    
# Taking user inputgoogl

portfolio = {}

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available!")
        continue

    quantity = int(input("Enter quantity: "))

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\nYour Portfolio:")
print(portfolio)

# Calculate total investment

total_investment = 0

print("\nStock Investment Details:")
print("------------------------")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]

    investment = price * quantity

    total_investment += investment

    print(stock, "| Price:", price,
          "| Quantity:", quantity,
          "| Investment:", investment)

print("------------------------")
print("Total Investment Value:", total_investment)


import csv

with open("portfolio.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Stock Name", "Stock Price", "Quantity", "Investment"])

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        investment = price * quantity

        writer.writerow([stock, price, quantity, investment])

    writer.writerow(["", "", "Total Investment", total_investment])

print("\nPortfolio saved successfully in portfolio.csv!")