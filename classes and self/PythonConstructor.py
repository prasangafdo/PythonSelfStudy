'''
Created on Dec 4, 2021

@author: Prasanga Fernando
'''
class PythonConstructor:
    def __init__(self): #We use __init__ to create a constructor. We can also pass parameters if we like
        print("Hello I'm the constructor")
    def __del__(self):   # This is no longer useful due to automatic garbage collection
         print("Test destructor")
         
    def testFunction(self):
        print("Hello I'm a test function")
         
objectName = PythonConstructor()   
objectName.testFunction()      