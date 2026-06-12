
# Q12. ATM Machine Simulation
# Menu:
# Check Balance
# Withdraw Money
# Deposit Money
# Exit

balance = 5000

print("== ATM MENU ==")
print("1. Check Balance")
print("2. Withdraw Money")
print("3. Deposit Money")
print("4. Exit")

choice = int(input("Enter your choice (1-4): "))

# Check Balance
if choice == 1:
    print("Current Balance: ₹", balance)

# Withdraw Money
elif choice == 2:
    amount = float(input("Enter amount to withdraw: ₹"))
    
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful!")
        print("Remaining Balance: ₹", balance)
    else:
        print("Insufficient Balance!")

# Deposit Money
elif choice == 3:
    amount = float(input("Enter amount to deposit: ₹"))
    balance = balance + amount
    print("Deposit Successful!")
    print("Updated Balance: ₹", balance)

# Exit
elif choice == 4:
    print("Thank you for using ATM!")

# Invalid Choice
else:
    print("Invalid Choice! Please select between 1 and 4.")