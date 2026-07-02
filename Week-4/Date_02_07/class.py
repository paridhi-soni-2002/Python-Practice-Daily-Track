#polymorphism= one interface many form the same method or operation bheaves differently depending on the object that used it
#compile time polymorphism and run time polymorphism
#compile time polymorphism- method overloading not to suported but can achieve by *args  support in python 
# : same name with differnet parameter in the same class
#runtime polymorphism - support(method overiding ):same name with same parameter achieve in inheritance
#built in polymorphism- 
#why direct values passed in sum functions doesnot operate..?
class Dog:
    def sound(self):
        print("bark")
        
class Cat:
    def sound(self):
        print("meow")
        
class Cow:
    def sound(self):
        print("Moo")
        
obj1=Dog()
obj1.sound()

#duck typing- 


#Abstraction = hinding thr internal implementation and
#showing only the necessary features to the user
from abc import ABC,abstractmethod

#ABC : Abstract base class
#abstractmethod: method that must be implemented by child classes
#abstract class- it is a blue print for other classes we cant creat its object directly 
#but child classes can inherit and implement its methods
#ABC- Abstract base class
# steps:
#provided by python to create abstract classes it defines common
#rules that all child classes must follow
#abstract method- it is a decorator that declare a method which every child class
# must have implement a subclass cannot be create 
class demo(ABC):
    @abstractmethod
    def say(self):
      print("hello")  
    
obj=demo()
obj.say


    