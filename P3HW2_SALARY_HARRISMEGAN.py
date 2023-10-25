#CTI-110
#P3HW2-Salary
#Megan Harris
#10-23-23

#ask user to input name
#get user pay rate
#get hours worked

employee_name = input("Please enter your name:")
pay_rate = float(input("Enter your pay rate:"))
hours_worked = float (input("Enter hours worked:"))


print ("----------------------------------------------")

print("Employee name:" , employee_name)

# calculate



if hours_worked <=40:
    gross_pay = pay_rate * hours_worked
    regular_pay = hours_worked * pay_rate
    overtime_hours = 0
    overtime_pay = 0
    

else:
    overtime_hours = hours_worked -40

    overtime_pay = overtime_hours * (pay_rate * 1.5)

    regular_pay = 40 * pay_rate

    gross_pay = overtime_pay + regular_pay
    

    
    
# print results


print(f'{"Hours Worked":<15}{"Pay Rate":<15} {"Overtime":<15} {"OverTime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')

print ("---------------------------------------------------------------------------------------------------------------------")


print(f'{hours_worked:<15} {pay_rate:<15.2f} {overtime_hours:<15} {overtime_pay:<15.2f} ${regular_pay:<15.2f} ${gross_pay:<15.2f}')
