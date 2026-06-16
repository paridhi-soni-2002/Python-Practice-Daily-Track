# Create a tuple of subject names and a list of marks. Print:
# Maths : 90
# English : 85
# Science : 80
# using a loop.

subject_names=("Maths","English","Science")
marks=[90,85,80]
for i in range(len(subject_names)):
    print(subject_names[i],":",marks[i])


