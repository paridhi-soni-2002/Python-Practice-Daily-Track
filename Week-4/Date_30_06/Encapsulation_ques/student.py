# Student Marks
class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def get_name(self):
       return self.__name
    def get_marks(self):
        if 0<self.__marks<=100 :
         return self.__marks
        else:
           print("invalid marks")
    def show_details(self):
       print("name:",self.__name)
       print("marks:",self.__marks)
       
obj=Student("paridhi",90)
print(obj.get_name())
print(obj.show_details())
        