#CTI-110
#P2HW2-List
#Megan Harris
#10-4-23

#ask user to enter grades for modules 1-6

module_one = float(input("Please enter grades for module one:"))
module_two = float(input("Please enter grades for module two:"))
module_three = float(input("Please enter grades for module three:"))
module_four = float(input("Please enter grades for module four:"))
module_five = float(input("Please enter grades for module five:"))
module_six = float(input("Please enter grades for module six:"))

#create list for grades entered

module_grades = [module_one, module_two, module_three, module_four, module_five, module_six]

print ("-----------------Results-------------------")

#find lowest grade

print(f'{"Lowest grade:" :<25}  {min(module_grades)}')

#find highest grade
print(f'{"Highest grade:" :<25} {max(module_grades)}')

#find sum of grades
print(f'{"Sum of grades:" :<25} {sum(module_grades)}')

#find average of grades
print(f'{"Average of grades:" :<25} {sum(module_grades)/len(module_grades):.2f}')

print ("-----------------------------------------------------------")
