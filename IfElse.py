'''
Created on Oct 28, 2021

@author: Prasanga Fernando
'''

print("This is a small program to use conditional statements in Python")

a = 100
b = 50

if(a>b):
    maxValue = a
else:
    maxValue = b
    
print(maxValue)

category = input("Enter category")


if category== "pet":
    animalName = input("Enter pet type")
    if animalName == "dog":
        print("You are a "+animalName+" person")
    elif animalName == "cat":
        print("You are a "+animalName+" person")
    else:
        print("You are missing a great time without a pet")
elif category== "car":
    print("You're a car person")
       
#Nested if statements