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
    
    
    
#for loop
#No condition. Only returns the values in the list
arr = [12,34,5,612,87,23,1,65,231]
for num in arr:
    print(num)