#!/usr/bin/env python3

# stock_investment.py
# Im A. Programmer
# 6/3/2020
# Python program for WeBroker stock purchase

# Constants
COMMISSION_RATE = 0.02
INVESTMENT_AMOUNT = 5000

# Prompt user for input
company_name = input("Please enter the company name for the purchase: ")
stock_symbol = input("Please enter the trading symbol for {}: ".format(company_name))
cost_per_share = float(input("Please enter the cost per share for {} stock: ".format(stock_symbol)))

# Calculate maximum shares, subtotal, commission, and total cost

max_shares = int(INVESTMENT_AMOUNT / cost_per_share)
subtotal = round(max_shares * cost_per_share, 2)
commission = round(subtotal * COMMISSION_RATE, 2)
total_cost = round(subtotal + commission, 2)

# Display output
print("\nStock Purchase for {} ({}):".format(company_name, stock_symbol))
print("Shares: {}".format(max_shares))
print("Cost of Shares: ${}".format(subtotal))
print("Commission: ${}".format(commission))
print("Total cost: ${}".format(total_cost))

# constants
# # COMMISSION = 0.02     # 2%
# # INVEST_AMT = 5000.0

# prompt for company information
# # comp_name = input("Please enter the company name for the purchase: ")
# # comp_sym = input("Please enter the trading symbol for " + comp_name + ": ")
# # cost_per_share = float(input("Please enter the cost per share for " + comp_sym + ": "))

# calculations
# # max_shares = int(INVEST_AMT / cost_per_share)  # must be integer
# # cost_of_shares = max_shares * cost_per_share
# # commission_cost = COMMISSION * cost_of_shares
# # total_cost = cost_of_shares + commission_cost

# display, round all currency to 2 places
# # print("Stock Purchase for " + comp_name + " (" + comp_sym + ")")
# # print("Shares: " + str(max_shares))
# # print("Cost of Shares: $" + str(round(cost_of_shares,2)))
# # print("Commission: $" + str(round(commission_cost,2)))
# # print("Total cost: $" + str(round(total_cost,2)))