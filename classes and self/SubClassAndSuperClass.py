'''
Created on Dec 4, 2021

@author: Prasanga Fernando
'''
class Parent:
    number1 = 43
    number2 = 32
    
class Parent2:
    stringTest = "Hello, I'm a string in Parent2 class"
    
class Child (Parent, Parent2): #Multiple inheritance
    pass #We need to use pass to fix the indentation issue 

childObject = Child()
print(childObject.number1)
print(childObject.number2)
print(childObject.stringTest)