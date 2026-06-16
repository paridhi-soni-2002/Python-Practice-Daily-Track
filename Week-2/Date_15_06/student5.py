# Take 5 student names in a list and search for a specific student name.
# If found print:
# Student Found
# otherwise:
# Student Not Found

student=["Suhani","Rahul","Rohit","Naman","Sakshi"]
name=str(input("enter a student name want to find\n"))

for i in student:
    if i==name:
        print("Student name is found:",name)
        break
    else:
        print("student name is not found:",name)
