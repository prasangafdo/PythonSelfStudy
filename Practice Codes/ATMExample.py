'''
Created on Dec 5, 2021

@author: Prasanga Fernando
'''

#Scenario -> Withdraw money from ATM when the account balance is 50k

class BackgroundWorker:
    accountBalance = 50000
    def withdrawMoney(self,requestedAmount):
        print("Current account balance is ", self.accountBalance)
        if(requestedAmount<= self.accountBalance):
                print("Transaction completed! \nCurrent account balance is ", self.accountBalance - requestedAmount)      
        else:
            print("Account balance is not sufficient")
            
#class Runner:

worker = BackgroundWorker()
#while worker.accountBalance !=0:
amount = int(input("Please enter the amount you want to withdraw"))
worker.withdrawMoney(amount)