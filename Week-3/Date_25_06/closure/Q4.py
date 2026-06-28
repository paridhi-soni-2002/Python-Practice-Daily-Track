#  4.	Create a closure representing a bank account with operations to deposit, withdraw, and check balance.
def outer():
    balance=1000
    def inner(ch,amt=0):
        nonlocal balance
        if ch=="deposit":
            balance+=amt
            print("account balance: ",balance)
        elif ch=="withdraw":
            if amt<=balance:
                balance-=amt
                print("balance total:",balance)
            else:
                print("Not sufficent balance")   
        elif ch=="check":
            print("your account balance is: ",balance)
    return inner
    


obj=outer()
obj("check")
obj("deposit",500)
obj("check")
obj("withdraw",300)
obj("check")
