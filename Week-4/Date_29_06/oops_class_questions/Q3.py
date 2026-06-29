
# 3. Employee Management System

class Employee:
    def __init__(self,emp_id,name,department,designation,salary,email,joining_date,experience):
        self.emp_id=emp_id
        self.name=name
        self.department=department
        self.designation=designation
        self.salary=salary
        self.email=email
        self.joining_date=joining_date
        self.experience=experience
        
    def login(self):
        print(f"{self.name} is login ")
        
    def apply_leave(self):
        print("apply for leave",self.name,self.emp_id)
    
    def calculate_salary(self):
         print(f"{self.salary} calculated salary ")
   
    def show_detail(self):
        print("\n------ Employee Details ------")
        print("Employee ID   :", self.employee_id)
        print("Name          :", self.name)
        print("Department    :", self.department)
        print("Designation   :", self.designation)
        print("Salary        :", self.salary)
        print("Email         :", self.email)
        print("Joining Date  :", self.joining_date)
        print("Experience    :", self.experience, "Years")
        
obj=Employee(101,"paridhi","IT","python developer","50000","paridhi@123","12-06-2026","4years")
obj.login()
obj.apply_leave()