#Megan Harris
#11-29-23
#CTI-110-P5HW Math Quiz
#menu style math quiz






import random

import mfunction as MF

def main ():
    """ incorporates a math quiz option of 1, 2 or 3 """
    print ("Welcome to Math Quiz")

    menu_option =0   

    while menu_option != 3:

        MF.menu ()

        menu_option= int(input("Please choose of of the menu options:"))
        
        if menu_option ==1:
            addition()

        elif menu_option ==2:
            subtraction ()

        elif menu_option ==3:
            print ("Thanks for playing, Goodbye!")

        else:
            print ("Error!! Please choose 1, 2 or 3")

    
    

def addition():
    """ adds two random numbers"""
    
    integer_1 = random.randint (0, 50)
    integer_2 = random.randint (0, 50)
    i=1

    right = integer_1 + integer_2

    print( "What is", integer_1, "+", integer_2 ,"?", end="") 

    answer = int(input())

    while right != answer:

        i = i+1
        if right < answer:

            print ("Try again", answer)

            print ("Sorry guess is too high")

            print (f'What is {integer_1} + {integer_2} ?')

            answer = int(input())

        elif right > answer:

            print ("Try again", answer)

            print ("Sorry guess is too low")

            print (f'What is {integer_1} + {integer_2} ?')

            answer = int(input())

    
            
    print("Congratulations!! Your answer is correct!")
    print ("Number of guesses:", i)






def subtraction ():
    

    """subtracts two random numbers"""
     
    integer_1 = random.randint (0, 50)
    integer_2 = random.randint (0, 50)
    i=1

    right = integer_1 - integer_2

    print( "What is", integer_1, "-", integer_2 ,"?", end="") 

    answer = int(input())

    while right != answer:

        i = i+1
        if right < answer:

            print ("Try again", answer)

            print ("Sorry guess is too high")

            print (f'What is {integer_1} - {integer_2} ?')

            answer = int(input())

        elif right > answer:

            print ("Try again", answer)

            print ("Sorry guess is too low")

            print (f'What is {integer_1} - {integer_2} ?')

            answer = int(input())

    
            
    print("Congratulations!! Your answer is correct!")
    print ("Number of guesses:", i)

 
main ()


#program completion


    

    
