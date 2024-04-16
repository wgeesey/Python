#!/usr/bin/env python3
# Module 7
# customer_list.py
# uses the Customer class

from customer import Customer

# create and print two customers
cust1 = Customer("John Smith", "1 Oak St.")
cust2 = Customer("Sally Brown", "3 Elm St.")
print(cust1.name + ", " + cust1.strAddr + ", " + str(cust1.creationDate))
print(cust2.name + ", " + cust2.strAddr + ", " + str(cust2.creationDate))
