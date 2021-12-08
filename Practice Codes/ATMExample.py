'''
Created on Dec 5, 2021

@author: Prasanga Fernando
'''

#Scenario -> Withdraw money from ATM when the account balance is 50k

class BackgroundWorker:
    
  accountBalance = 50000
  def withdrawMoney(self):
      
       while self.accountBalance !=0: 
        requestedAmount = int(input("\nEnter amount to withdraw or enter 0 to exit"))
      #  print("Current account balance is ", self.accountBalance)
        if requestedAmount!=0:
            if(requestedAmount<= self.accountBalance):
                if requestedAmount%100 !=0:
                    print("Please enter as a multiplier of 100")  
                else:
                    print("Transaction completed! \nCurrent account balance is ", self.accountBalance - requestedAmount)     
                    self.accountBalance = self.accountBalance - requestedAmount 
            else:
                print("Account balance is not sufficient")              
        elif requestedAmount==0:
            print("Thank you for banking with us")
            quit()       

worker = BackgroundWorker()
print("Your current balance is", worker.accountBalance)
worker.withdrawMoney()
