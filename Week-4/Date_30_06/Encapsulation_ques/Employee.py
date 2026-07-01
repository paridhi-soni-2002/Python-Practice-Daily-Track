class Employee:

    def __init__(self, employee_id, salary):
        self.__employee_id = employee_id
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):

        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")


obj = Employee(101, 30000)

obj.set_salary(50000)

print(obj.get_salary())