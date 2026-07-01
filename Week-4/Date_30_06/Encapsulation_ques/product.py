class Product:
    def __init__(self,name,price):
        self.__name=name
        self.__price = price

    def get_price(self):
        return self.__price
    def set_price(self,price):
        if price>0:
            self._price=price
        else:
            print("Invalid price")
            
obj=Product("laptop",30000)
obj.set_price(40000)
print(obj.get_price())