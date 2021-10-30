'''
Created on Oct 29, 2021

@author: Prasanga Fernando
'''

#We can use any of these ways to initiate strings in Python
x = 'This is a string in single quotes'
y = "This is a string in double quotes"
z = """This is a string in tripple quotes"""

print(x)
print(y)
print(z)

escapeSequence = 'In python, escape sequence is \'backslash\''
escapeSequence2 = "In python, escape sequence is \"backslash\""
printBackslash = "Print this backslash \\ \nThis is a new line"

print(escapeSequence)
print(escapeSequence2)
print(printBackslash)

#Printing the same result multiple times
sampleString = "Hi "

print(sampleString * 10)

#Type casting int -> String

number1 = 40

print(sampleString + str(number1))
