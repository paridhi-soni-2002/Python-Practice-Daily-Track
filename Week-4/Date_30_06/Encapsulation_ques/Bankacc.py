# create BankAccount
class BankAccount:
    def __init__(self,acc_num,balance):
        self.__account_number=acc_num
        self.__balance=balance
    def deposit(self,amt):
        self.__balance+=amt
        print(self.__balance)
        
    def withdraw(self,amt):
        if amt>self.__balance:
            print("Insufficient balance")
        else:
            self.__balance-=amt
            print("after withdrawl:",self.__balance)        
    def get_balance(self):
        return self.__balance
    
obj=BankAccount(1243545545,50000)
print(obj.get_balance())