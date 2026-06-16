subjects = ("Maths", "English", "Science", "Hindi", "SS")
marks = [90, 85, 78, 88, 92]

print("Subject-wise Marks")

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("\nTotal Marks :", total)
print("Average     :", round(average, 2))
print("Highest     :", highest)
print("Lowest      :", lowest)

if average >= 35:
    print("Result      : PASS")
else:
    print("Result      : FAIL")