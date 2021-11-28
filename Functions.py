'''
Created on Nov 27, 2021

@author: Prasanga Fernando
'''
def printName(name):
    print(name)
    
def welcomeNote():
    print("Hello.. welcome to test run")
    
welcomeNote()
printName("Prasanga")
printName("Supun")
printName("Kaveesh")

#Function with return values
def addTwoNumbers(x,y):
    return (x+y)

sum = addTwoNumbers(10,21)
print(sum)