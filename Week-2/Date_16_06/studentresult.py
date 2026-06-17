student = {}

student["name"] = input("Enter student name: ")

marks = []

for i in range(5):
    mark = int(input(f"Enter mark {i+1}: "))
    marks.append(mark)

student["marks"] = marks

student["total"] = sum(marks)
student["average"] = student["total"] / len(marks)
student["highest"] = max(marks)
student["lowest"] = min(marks)

if student["average"] >= 35:
    student["result"] = "PASS"
else:
    student["result"] = "FAIL"

print("\nStudent Report")

print("Name      :", student["name"])
print("Marks     :", student["marks"])
print("Total     :", student["total"])
print("Average   :", round(student["average"], 2))
print("Highest   :", student["highest"])
print("Lowest    :", student["lowest"])
print("Result    :", student["result"])