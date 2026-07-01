class Mobile:
    def __init__(self,battery_per):
        self.__battery_percentage=battery_per
    def charge(self):
        if self.__battery_percentage<100:
            self.__battery_percentage+=10
    def use_phone(self):
       if self.__battery_percentage>0:
           self.__battery_percentage-=10
    def get_battery(self):
        return self.__battery_percentage

obj=Mobile(30)  
obj.charge()  
print(obj.get_battery())    