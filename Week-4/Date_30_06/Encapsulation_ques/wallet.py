class Wallet:

    def __init__(self):
        self.__balance = 0

    def add_money(self, amount):
        self.__balance += amount

    def spend_money(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance


obj = Wallet()

obj.add_money(1000)

obj.spend_money(300)

print(obj.check_balance())