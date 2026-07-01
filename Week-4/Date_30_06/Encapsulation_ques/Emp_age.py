class EmployeeAge:
    def __init__(self,age):
        self.__age=age
        
    @property
    def age(self):
            return self.__age
    
    @age.setter
    def age(self,value):
        if 18<=value<=60:
              self.__age=value
        else:
             print("invalid")
                         
obj=EmployeeAge(23)
print(obj.age)
obj.age=22
print(obj.age)