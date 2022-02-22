'''
Created on Oct 19, 2021

@author: Prasanga Fernando
'''
print("Hello World")


# Passing multiple values to the same variable via function

def nameAddress(name, *address):
    print(name)
    print(address)


nameAddress("Supun", "Kasun", "Dulaj", "Kapila", "Sanith")
