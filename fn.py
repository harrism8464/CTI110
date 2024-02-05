# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 10:04:36 2024

@author: harrism8464
"""

def getInputs():
    #ask user arrival rate and service rate
    arrival_rate=float(input("Enter average arrival rate:"))
    service_rate =float(input("Enter the service rate:"))
    return arrival_rate, service_rate

def calcWaitTime(arrival_rate, service_rate):
    #calculate average wait time
    waitTime= 1/(service_rate - arrival_rate)- 1/service_rate
    return waitTime

def displayResult(expWaitTime):
    
    #convert time from hours to minutes
    wait_time_minutes = expWaitTime *60
    print (f'Average Customer Wait Time: {wait_time_minutes:.2f} minutes')