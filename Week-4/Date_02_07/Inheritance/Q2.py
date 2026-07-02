# 2.	Create a multilevel inheritance example using Person → Employee → Manager. Add different methods at each level and demonstrate method access.
class Person:
    def demo(self):
        print("this is the person class")
        
class Employee(Person):
    def demo1(self):
        print("this is the employee class")
        
class Manager(Employee):
    def demo2(self):
        print("this is the manager class")
        
obj=Manager()
obj.demo1()
obj.demo2()
obj.demo()
