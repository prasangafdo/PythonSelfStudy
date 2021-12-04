'''
Created on Dec 4, 2021

@author: Prasanga Fernando
'''
class Person:
    def setName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def getName(self):#Passing self is a must. "self" is like "this" keyword in Java
        print(self.firstName," ",self.lastName)   
        
      
#Creating the class object outside the class    
personName = Person()
personName.setName("Kasun", "Sandaruwan") 
personName.getName()   