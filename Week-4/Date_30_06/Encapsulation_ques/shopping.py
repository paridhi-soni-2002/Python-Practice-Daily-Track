class ShoppingCart:

    def __init__(self):
        self.__total_amount = 0

    def add_item(self, price):
        self.__total_amount += price

    def remove_item(self, price):
        if price <= self.__total_amount:
            self.__total_amount -= price

    def get_total(self):
        return self.__total_amount


obj = ShoppingCart()

obj.add_item(500)
obj.add_item(300)
obj.remove_item(200)

print(obj.get_total())