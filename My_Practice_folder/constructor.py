# class Student:

#     def __init__(self):
#         print("Default Constructor")

# s = Student()

#parameterized constructor
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# s=Student("paridhi",23)
# print(s.name)
# print(s.age)

class Employee:
    def __init__(self,name):
        self.name=name
        print("Employee constructor")
        
class Manager(Employee):
    def __init__(self,department,name):
        self.department=department
        super().__init__(name)
        print("manager constructor")
        
m=Manager("paridhi","HR")
print(m.name)
print(m.department)

    