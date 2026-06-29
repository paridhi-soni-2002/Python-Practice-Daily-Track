# 2. Student Management System
# Create a Student class.

class Student:
    def __init__(self,student_id,name,age,gender,class_name,section,roll_number,marks):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.gender=gender
        self.class_name=class_name
        self.section=section
        self.roll_number=roll_number
        self.marks=marks
        
    def study(self):
        print("the student study at :",self.class_name)
    def attend_class(self):
        print("the student the class:",self.name)
    def taken_exam(self):
        print("the student has taken the ",self.name)
    def show_result(self):
        if self.marks>35:
          print("the student passed the exam")
        else:
            print("the student is failed")
        
    def show_profile(self):
         print("\n------ Student Profile ------")
         print(self.student_id)
         print(self.name)
         print(self.age)
         print(self.gender)
         print(self.class_name)
         print(self.section)
         print(self.roll_number)
         print(self.marks)
obj=Student(101,"paridhi",23,"F","12th class","A",11,90)
obj.show_profile()