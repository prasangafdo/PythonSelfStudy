'''
Created on Oct 31, 2021

@author: Prasanga Fernando
'''
names=["Supun", "Kasun", "Gihan"]
print(names)

#In Python we can have index backwards also. It starts from -1
print(names[-2])#This will print second value from last

names.append("New name") #This will add a new value
print(names[-1])

#Adding another list to another list. Also the list can contain multiple data types

ages = [21,43,10,19] 
print(ages)

names.extend(ages)

print(names)

names.remove(43)

print(names)

print(names, ages) #Printing multiple lists

print(len(names))

print(max(ages)) #To use this, list should only contain integer values