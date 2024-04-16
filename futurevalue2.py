#!/usr/bin/env python3
# futurevalue2.py
#
def calculate_future_value(monthly_investment, yearly_interest, 
                           years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = float(input("Enter monthly investment: "))
        yearly_interest_rate = float(input("Enter yearly interest rate: "))
        years = int(input("Enter number of years: "))

        # get and display future value
        future_value = calculate_future_value(monthly_investment, 
                                              yearly_interest_rate, years)

        print("Future value: " + str(round(future_value, 2)))
        print()
        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()
    print("Bye!")
    
main()
