class ElectricityBill:

    def __init__(self):
        self.__units = 0
        self.__bill = 0

    def set_units(self, units):
        self.__units = units

    def calculate_bill(self):
        self.__bill = self.__units * 8

    def get_bill(self):
        return self.__bill


obj = ElectricityBill()

obj.set_units(100)
obj.calculate_bill()

print(obj.get_bill())