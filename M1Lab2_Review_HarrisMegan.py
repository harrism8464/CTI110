# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Program to determine the total cost for a set of purchases
#Megan Harris
#1-23-24
#CSC121 M1Lab2-Review




#use variables to count within the program
userChoice ="y"
count=0
total_cost=0
quantity=0

#while user enters yes, the following while loop will occur

while userChoice == 'y':
   
    quantity += 1

    #item will count
    print('Item', quantity)

    #user enters count of item and cost

       
    count = int(input("Enter count of item:"))
    unit_cost = float(input("Enter unit cost:"))
   
    #formula for one item and the amount purchased
    item_cost = count * unit_cost
    total_cost += item_cost

    #ask the user if they want to input more items
    userChoice=input("Add more items? (y/n):")


   
#hard code tax rate to 7.5%
   
tax_rate = 0.075

#formula for tax amount on total cost
tax_amount = total_cost * tax_rate

#formual for total cost and added tax
total_cost_with_tax= total_cost + tax_amount

#display results

print(f"\nPre-tax cost: ${total_cost:.2f}")
print(f"Tax (7.5%): ${tax_amount:.2f}")
print(f"Total cost including tax: ${total_cost_with_tax:.2f}")



