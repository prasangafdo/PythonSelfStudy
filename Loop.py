'''
Created on Nov 14, 2021

@author: Prasanga Fernando
'''

#while loop

a = 0
while a<5:
    print(a) 
    a+=1 #This is same as a++ in Java
   
   
total = 0
inputVal = 1
print("Enter some numbers one by one to add and press enter for each")

print("Press 0 to exit")


while inputVal !=0:
    print("Current sum : ",total) #We can't use + for concat like we use in Java. Instead we have to use comma (,)
    inputVal = float(input("Please enter a number: "))   
    total = total+inputVal