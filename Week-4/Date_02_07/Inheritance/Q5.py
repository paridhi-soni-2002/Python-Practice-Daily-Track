# 5.	Create a BankAccount parent class and derive SavingsAccount and CurrentAccount. Add account-specific features while reusing common methods
class BankAccount:
    def __init__(self,accno,balance):
        self.ANo=accno
        self.Balance=balance
    def check_balance(self):
            print("balance:",self.Balance)
    def AccNo(self):
         print("account number:",self.ANo)
        
class SavingAccount(BankAccount):
    def interest(self):
         print("saving account earn interest")
         
    
class CurrentAccount(BankAccount):
    def overdraft(self):
         print("current account has overdraft")
         

obj=SavingAccount(12345666,50000)
obj.interest()
obj.check_balance()
obj.AccNo()

obj=CurrentAccount(12345776,40000)
obj.overdraft()
obj.check_balance()
obj.AccNo()