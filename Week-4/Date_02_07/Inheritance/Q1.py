# 1.	Create a Vehicle class with a start() method. Create Car, Bike, and Truck classes that inherit from Vehicle and add their own methods.
class Vehicle:
    def start(self):
        print("its the vehicle class")
        
class Car(Vehicle):
    def drive(self):
        print("its the car class")
        
class Bike(Vehicle):
    def ride(self):
        print("its the bike class")
        
class Truck(Vehicle):
    def loading(self):
        print("its the truck class")
        
obj=Truck()
obj.start()
obj.loading()
    