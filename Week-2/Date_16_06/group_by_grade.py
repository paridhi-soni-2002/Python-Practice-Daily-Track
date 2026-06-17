student={
    "Ram":"A",
    "Mohit":"B",
    "vishesh":"A",
    "Neha":"C"
}

grades={}
for name, grade in student.items():
    if grade not in grades:
        grades[grade]=[]
        
    grades[grade].append(name)
print(grades)
        