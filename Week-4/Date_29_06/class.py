#oops:object oriented programming: it is programming style
# where we represent real world things as object

#for example student object each object has data (Attributes),functions(methods)
#class=blue print used to creat object
#object=object is a real instance of class
#constructor: - it is name as class name and initialize the object and called automaticaly

#methods are always take the self keyword in the parenthesis
#self-self refers to current object class
# class Student:
#     name="abc"#instance attribute
   
#     def study(self):
#         print("hello")
#     def attend_class():
#         pass
    
# obj1= Student()
# obj1.study()

# class Student:
#     def __init__(self,name,age,department):
#         self.fullname=name
#         self.age=age
#         self.department=department
#         print("called")
#         print(self.fullname,self.age,self.department)
        
# obj1=Student("paridhi",18,"IT")
# obj2=Student("suhani",30,"BSC")

#class Attribute-class attribute are global inside the class it is described,shared copy
#instance Attribute-it belongs to each instance of the class,using self keyword accessed

# operation=deposite,withdraw,total_balance
class BankAccount:
   
   
    def __init__(self,name,balance,acc_no,Ifsc_code,branch):
        self.fullname=name
        self.acc_no=acc_no
        self.Ifsc_code=Ifsc_code
        self.branch=branch
        self.balance=1000
        
    def deposite(self,amount):
        self.balance+=amount
        print("after deposite",self.balance)
        
    def withdraw(self,amount):
        if amount>self.balance:
            print("not able to withdraw")
        else:
            self.balance-=amount
            print("after withdraw", self.balance)
    
    def total(self):
        
        print(self.balance)
        
obj1=BankAccount("paridhi",1000,12223121,103,"BOI")
obj1.deposite(3000)
obj1.withdraw(1000)
obj1.total()