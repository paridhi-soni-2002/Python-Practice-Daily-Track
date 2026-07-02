#Encapsulation= it is the process of wrapping data attributes amd methods functions into single unit class
#it also help protected data by controlling how it is accessed or modified.
#benefits= data security , data hiding,better control,validation possible
#Access mofdifiers: public(): anywhere we can access
#protected(_name): inside class and subclass
#private(__name): inside the same class

# class Employee:  # protected attribute code
#     def __init__(self):
#         self._salary=40000
#     def details(self):
#         print(self._salary)
# class Attendence(Employee):
#     def show(self):
#         print(self._salary)

# emp=Employee()
# emp.details()
# at=Attendence()
# at.show()

class Employee:  # private attribute code
    def __init__(self):
         self.__salary=60000
    def details(self):
         print(self.__salary)
class Attendence(Employee):
   def show(self):
      print(self.__salary)
      
emp=Employee()
emp.details()

#getter= a getter is a method used to read retrieve the value of a private attribute

class Student:

    def __init__(self, name,age):
        self.__name = name
        self.__age=age
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age


s = Student("Paridhi",23)

print(s.get_name())
print(s.get_age())

#setter= A setter is used to modify (set) the value of a private variable after checking whether the new value is valid.

class Student:

    def __init__(self, age):
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

s = Student(20)

s.set_age(25)

print(s.get_age())

#@property decorator:you can create method as an attribute the property attribute 
# The @property decorator allows a method to be accessed like an attribute.

class Student:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

s = Student("Paridhi")

print(s.name)

#@get_salary.setter -implemnetaion

class Employee:
    def __init__(self):
        self.__salary=50000
        self.__name="xyz"
        
@property
def get_salary(self):
    return self.__salary

@get_salary.setter
def set_salary(self,value):
    if value>0:
        self.__salary=value


    
