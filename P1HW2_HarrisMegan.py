#travel expenses
#9-27-23
#CTI-111 P1HW2-Travel Expense
#Megan Harris

print("This program calculates and displays travel expenses")


trip_budget=float(input("Enter your budget:"))

travel_dest=input("Enter your destination:")

travel_gas=float(input("Enter your gas amount:"))

travel_accom=float(input("Enter how much you will need for accomodation/hotel:"))

travel_food=float(input("Enter your amount for food:"))



print("---------------Travel Expenses-------------------")

print("Location:", (travel_dest))
print("Initial Budget:", (trip_budget))
print("Fuel:", (travel_gas))
print("Accomodation:", (travel_accom))
print("Food:", (travel_food))

print("Remaining Balance:",(trip_budget)-(travel_gas + travel_accom + travel_food))

