#CTI-110
#P4HW2
#Megan Harris
#11-13-23

#ask user to input name
#get user pay rate
#get hours worked

employee_name = input("Please enter employee's name or 'Done' to terminate:")


print ("----------------------------------------------")

print("Employee name:" , employee_name)

#determining if loop continues

count =0
overtime =0
hours =0
gross =0

while employee_name != 'Done':
    
    pay_rate = float(input("What is " +employee_name +"'s pay rate:"))
    hours_worked = float (input("How many hours did " +employee_name +" work:"))

    count +=1

# calculate



    if hours_worked <=40:
        gross_pay = pay_rate * hours_worked
        regular_pay = hours_worked * pay_rate
        overtime_hours = 0
        overtime_pay = 0
        overtime = overtime + overtime_pay
        hours = hours + regular_pay
        

    else:
        overtime_hours = hours_worked -40

        overtime_pay = overtime_hours * (pay_rate * 1.5)

        regular_pay = 40 * pay_rate

        overtime = overtime + overtime_pay
        
        hours = hours + regular_pay

    gross_pay = overtime_pay + regular_pay

    gross = gross + gross_pay



    

    
        

    
    
# print results




    print(f'{"Hours Worked":<15}{"Pay Rate":<15} {"Overtime":<15} {"OverTime Pay":<15} {"RegHour Pay":<15} {"Gross Pay":<15}')

    print ("---------------------------------------------------------------------------------------------------------------------")


    print(f'{hours_worked:<15} {pay_rate:<15.2f} {overtime_hours:<15} {overtime_pay:<15.2f} ${regular_pay:<15.2f} ${gross_pay:<15.2f}')
    
    employee_name = input("Please enter employee's name or 'Done' to terminate:")




print ("Total number of employees entered:", count)
print (f'Total amount paid for overtime: ${overtime:.2f}')
print (f'Total amount paid for regular hours: ${hours:.2f}')
print (f'Total amount paid in gross:${gross:.2f}')
