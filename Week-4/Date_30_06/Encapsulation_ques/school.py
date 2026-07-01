class School:

    def __init__(self):
        self.__student_strength = 0

    def add_student(self):
        self.__student_strength += 1

    def remove_student(self):
        if self.__student_strength > 0:
            self.__student_strength -= 1

    def get_strength(self):
        return self.__student_strength


obj = School()

obj.add_student()
obj.add_student()

print(obj.get_strength())