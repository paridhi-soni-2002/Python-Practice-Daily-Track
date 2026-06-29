class BankAccount:

    def __init__(self, account_number, account_holder, bank_name,
                 branch, balance, account_type,
                 IFSC, mobile_number):

        self.account_number = account_number
        self.account_holder = account_holder
        self.bank_name = bank_name
        self.branch = branch
        self.balance = balance
        self.account_type = account_type
        self.IFSC = IFSC
        self.mobile_number = mobile_number

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited Successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def transfer_money(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Money Transferred Successfully")
        else:
            print("Insufficient Balance")

    def print_statement(self):
        print("\n-----Account Details-----")
        print("Account Holder :", self.account_holder)
        print("Account Number :", self.account_number)
        print("Bank Name      :", self.bank_name)
        print("Balance        :", self.balance)


obj = BankAccount(
    123456,
    "Paridhi",
    "SBI",
    "Indore",
    10000,
    "Saving",
    "SBIN000123",
    "9876543210"
)

obj.print_statement()
obj.deposit(5000)
obj.withdraw(2000)
obj.transfer_money(1000)
obj.check_balance()