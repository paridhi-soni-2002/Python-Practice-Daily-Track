class ATM:
    def __init__(self,acc_no,card_no,pin,balance,acc_holder,bank_name,branch,ATM_location):
        self.acc_no=acc_no
        self.card_no=card_no
        self.pin=pin
        self.balance=balance
        self.acc_holder=acc_holder
        self.bank_name=bank_name
        self.branch=branch
        self.ATM_location=ATM_location
        
    def withdraw_cash(self,amt):
        if amt>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amt
            print("after withdraw:",self.balance)
        
       
    def deposite_cash(self,amt):
        self.balance+=amt
        print("the total balance after deposit:",self.balance)
    
    def check_balance(self):
        print("balance is:",self.balance)
        
    def change_pin(self,new_pin):
        self.pin=new_pin
        print("the pin has updated")
        
        
    def mini_statement(self):
        print("\nAccount Holder:", self.account_holder)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)
    
atm = ATM(
    123456,
    987654321,
    1234,
    20000,
    "Paridhi",
    "SBI",
    "Indore",
    "Vijay Nagar"
)

atm.mini_statement()
atm.deposit_cash(5000)
atm.withdraw_cash(3000)
atm.change_pin(4321)
atm.check_balance()