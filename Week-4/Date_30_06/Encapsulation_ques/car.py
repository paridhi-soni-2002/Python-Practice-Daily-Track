class Car:
    def __init__(self):
        self.__speed=0
    def accelerate(self):
        self.__speed +=20
            
    def brake(self):
        if self.__speed>=20:
            self.__speed-=20
    def get_speed(self):
        return self.__speed
    
obj=Car()
obj.accelerate()
obj.accelerate()
obj.brake()
print(obj.get_speed())

            