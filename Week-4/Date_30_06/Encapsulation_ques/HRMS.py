class Employee:

    def __init__(self, salary, department):

        self.__salary = salary
        self.__department = department

    def set_department(self, department):

        valid = ["HR", "IT", "Sales", "Finance"]

        if department in valid:
            self.__department = department
        else:
            print("Invalid Department")

    def get_department(self):
        return self.__department


obj = Employee(40000, "IT")

obj.set_department("HR")

print(obj.get_department())