# 13. Bank Withdrawal System

# Given a balance of 10000, ask the user for a withdrawal amount.

# Raise a custom exception if the withdrawal amount exceeds the balance
class InsufficientBalanceError(Exception):
    pass
balance=10000
try:
    amount=int(input("Enter withdraw amount:"))
    if amount>balance:
        raise InsufficientBalanceError("Insufficient Balance!")
    balance-=amount
    
    print("withdrawal Successful")
    print("Remaining balance:",balance)
    
except InsufficientBalanceError as e:
    print(e)