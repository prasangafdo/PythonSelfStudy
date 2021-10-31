'''
Created on Oct 24, 2021

@author: Prasanga Fernando
'''
print("This is a simple calculator created by Prasanga Fernando using Python \nOnly performs addition and deletion...")

x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
operation = input("Enter '1' for addition or '2' for subtraction")

if operation == "1":
    print("Answer is :"+str(x+y))
elif operation == "2":
    print("Answer is :"+str(x-y))
else:
    print("Incorrect input")
input("Press enter to exit") #If we don't use this, it will terminate the application immediately
