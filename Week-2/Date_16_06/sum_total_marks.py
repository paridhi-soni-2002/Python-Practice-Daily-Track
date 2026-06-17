marks={}

for i in range(5):
    subject = input("enter the subject name:")
    mark = int(input("enter the marks:"))
    marks[subject]=mark
    
total = sum(marks.values())
print("total marks =",total)

#average marks
#• Calculate average marks.
average=total/len(marks) 

print("averge is :",average)

#• Find topper subject.

topper_subject= max(marks,key=marks.get)

print("topper subjects:",topper_subject)
print("marks:",marks[topper_subject])
