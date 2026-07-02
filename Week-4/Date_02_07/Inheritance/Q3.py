# 3.	Implement multiple inheritance using Father and Mother classes. Create a Child class that inherits from both and accesses methods from each parent.

class Father:
    def func(self):
        print("Inside the father class")
        
class Mother:
    def func1(self):
        print("Inside the mother class")
        
class Child(Father,Mother):
    def func2(self):
        print("Inside the child class")
        
obj=Child()
obj.func()
obj.func1()
obj.func2()