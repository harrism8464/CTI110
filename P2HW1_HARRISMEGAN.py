#travel expenses
#10-4-23
#CTI-111 P2HW1-Travel Expense
#Megan Harris

# tell user about program

print("This program calculates and displays travel expenses")

# ask user to input budget, destination, gas, hotel and food amounts


trip_budget=float(input("Enter your budget:"))

travel_dest=input("Enter your destination:")

travel_gas=float(input("Enter your gas amount:"))

travel_accom=float(input("Enter how much you will need for accomodation/hotel:"))

travel_food=float(input("Enter your amount for food:"))

#input will now be displayed

#use correct formatting to display information

remaining_balance=trip_budget-(travel_gas+travel_accom+travel_food)

print("---------------Travel Expenses-------------------")

print(f'{"Location:":<25} {travel_dest}')
print(f'{"Initial Budget:":<25} ${trip_budget:.1f}')
print(f'{"Fuel:" :<25} ${travel_gas:.1f}')
print(f'{"Accomodation:" :<25} ${travel_accom:.1f}')
print(f'{"Food:" :<25} ${travel_food:.1f}')

print("-------------------------------------------------")

print(f'{"Remaining Balance:" :^25} ${remaining_balance:.1f}')
