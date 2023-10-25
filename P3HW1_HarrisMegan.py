# Debugging
# HarrisMegan
#10-20-23
#CTI-110


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float (input("Enter grade for Module 1: "))
mod_2 = float (input("Enter grade for Module 2: "))
mod_3 = float (input("Enter grade for Module 3: "))
mod_4 = float (input("Enter grade for Module 4: "))
mod_5 = float (input("Enter grade for Module 5: "))
mod_6 = float (input("Enter grade for Module 6: "))

# create list for grades entered

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]


print ("-----------------Results-------------------")


#determine lowest, highest, sum and average for grades

print(f'{"Lowest grade:" :<25}  {min(grades)}')

#find highest grade
print(f'{"Highest grade:" :<25} {max(grades)}')

#find sum of grades
print(f'{"Sum of grades:" :<25} {sum(grades)}')

#find average of grades
print(f'{"Average of grades:" :<25} {sum(grades)/len(grades):.2f}')

print ("-----------------------------------------------------------")

# determine letter grade for average

avg=(sum(grades)/len(grades))


if avg >= 90:
    print('Your grade is: A')

elif avg >= 80:

    print ('Your grade is: B')
           
        
elif avg >= 70:
    print ('Your grade is: C')

elif avg >= 60:
    print ('Your grade is: D')

else:
    avg >= 50
    print ('Your grade is:F')

  






