# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#CalculateAverageWaitTime
#2-5-24
#CSC121 M2Lab-Functions Review
#Megan Harris


#the main function
import fn
    
def main ():
    choice =0
    while choice != 2:
        
    
    #choice variable controls the loop
    #user chooses choice from menu
        print("--------MENU-------------")
        print("1. Calculate Average Wait Time")
        print("2. Exit")
        print("--------------------------")
        
        #user inputs 1 or 2
        choice=int(input("Enter your choice 1 or 2: "))
        
        if choice ==1:      
           
                      
            #get input from user
            arrival_rate, service_rate = fn.getInputs()
            
            #calculate average wait time
            exp_wait_time = fn.calcWaitTime(arrival_rate, service_rate)
            
            #display results
            
            fn.displayResult(exp_wait_time)
        #program exits if user enters 2
        elif choice ==2:
            print("Exiting the program. Goodbye!")
        #invalid entry if user types anything other than 1 or 2   
        else:
            print ("Invalid choice. Please enter 1 or 2 only!")
    
if __name__ =="__main__":
    main()