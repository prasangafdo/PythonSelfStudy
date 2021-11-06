'''
Created on Nov 5, 2021

@author: Prasanga Fernando
'''
myList = [2,4,54,23,67,34,987,12]

print(myList[4:34])#This will include the first value and excludes the second value

print(myList[2:7])#We can either put values or indexes


newList = myList[1:5]
print(newList)

#Printing including the last value of the list
print(myList[2:8])

print(myList[4:])

print(myList[:5])

#Using negative indexes
print(myList[-6:-2]) #Printing starts from left side, so the left side's absolute value should be higher

print(myList[-1:])

print(myList[:-4])

print(myList , myList[:])#Both of these return the same value
