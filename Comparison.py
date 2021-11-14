'''
Created on Nov 7, 2021

@author: Prasanga Fernando
'''

'''
Comparison operators
<
<=
>
>=
==
!=

Logical operators
and
or
'''

print(1<3)

print(3<=3)

print(5>3)

print(3>=2)

print(5!=3)

print(3<=3) and (5!=4)

print(3<=3) or (32<2)

#in
testString = "abcdefg"

print('a' in testString)

print('ab' in testString)

print('ac' in testString)

a=[1,2,3]

b=[1,2,3]

print(a is b)#This will return false. Because these are not logically equal

c=d=[1,2,3]

print(c is d)#This will return true