#inheritance- one class inherit or reuse the properties and methods of another class
#Inheritance allows a class (child class) to inherit properties and 
# behaviors (attributes and methods) from another class (parent 
# class)

# Benefits of using inheritance is 
# Code reusability
# Organized structure
# Easy to maintain and exten
#parent class/base class/
#child class/sub class/derive class

#types of inheritance-
#1. single inheritance, 2. multilevel inheritance
#1. single inhertiance= one parent one child
#2. multilevel inheritance=one grandparent have parent class and the parent class to child class 
#3. multiple inheritance=Multiple Inheritance means there will be 2 parent classes and 
# only 1 child class and the child class will inherit all the 
# attributes and methods of both parents. 
#Hierarchical inheritance-
#hybrid inhertance-

#imp concept- MRO Method Resolution order
class Employee: #parent class
    def __init__(self,name):
        self.name=name
        
class child(Employee):#childclass
    def display(self):
        print(self.name)
        
obj=child("paridhi")
obj.display()

#super method-super function
#MRO- method resolution order
#python searches for a method or attribute when it is calles on an object 
#1. python checks the child class first
#2. 
