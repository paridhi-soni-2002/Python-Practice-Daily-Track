emp1 = set(input("enter employee 1 skills:").split())
emp2= set(input("enter employee 2 skills:").split())

common=emp1 & emp2
print("common skills:",common)