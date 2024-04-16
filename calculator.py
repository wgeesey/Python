#!/usr/bin/env python3
# calculator program which demonstrates exceptions

def get_price():
    price = float(input("Enter price: "))
    return price
#end get_price

def get_quantity():
    quantity = int(input("Enter quantity: "))
    return quantity
#end get_quantity

def main():
    print("The Total Calculator program\n")

    # get the price and quantity
    price = get_price()
    quantity = get_quantity()
    
    # calculate the total
    total = price * quantity

    # display the results
    print()
    print("PRICE:    ", price)
    print("QUANTITY: ", quantity)
    print("TOTAL:    ", total)

if __name__ == "__main__":
    main()
