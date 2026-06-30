#   sort dict by values
marks = {
    "A":90,
    "B":70,
    "C":95,
    "D":80
}

result=dict(sorted(marks.items(),key=lambda x:x[1],reverse=True))

print(result)

highest=max(marks,key=marks.get)
print(highest)


#sort list of tuplpe by second element
students = [
    ("Ram",85),
    ("Shyam",95),
    ("Mohan",75),
    ("Riya",90)
]

result=sorted(students,key=lambda x:x[1])
print(result)