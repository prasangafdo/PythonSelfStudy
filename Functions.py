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

#default parameters
def studentDetails(name="Supun", marks=70):
    print(name, "scored", marks)
    
studentDetails() #This will print the default value
studentDetails("Kamal", 20) #This will override the default values
studentDetails("Janith") #This will override only the name
studentDetails(marks=60) #This will override only the marks (If we are calling the second parameter, we have to specify that within the brackets. Otherwise it will override the first parameter