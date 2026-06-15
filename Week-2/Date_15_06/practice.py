# #Enumerate
# fruits=["Apple","Banana","Orange","Kiwi"]
# for index,fruit in enumerate(fruits):
#  print(index,fruit)
 
# students=["Ram","shyam","ganga","mohit"]
# for rollno,name in enumerate(students,start=101):
#  print(rollno,name)
 
# #without enumerate
# fruits=["Apple","Banana","Orange","Kiwi"]
# # for i in fruits:
# #  print(len(i))
# for index,name in enumerate(fruits,start=100):
#  print(index,name)
 
# #zip function  
# #convert zip object to list 
#  a=[1,2,3]    
#  b=['A','B','C']
#  result=list(zip(a,b))
 
# print(result)

# #zip file
# names = ["Ram", "Shyam", "Mohan"]
# marks = [85, 90, 78]

# for name, mark in zip(names, marks):
#     print(name, mark)
    

# students=["Ram","shyam","ganga","mohit"]
# marks=[85,90,60,20]

# for index,(name,marks) in enumerate(zip(students,marks),start=1):
#   status ="pass" if marks>30 else "fail"
#   print(index,name,marks,status)


# #id()-id function used to find the id of the variable
# a=12
# print(id(a))

# #fibnocci series
# num=int(input("enter a number:"))
# a=0
# b=1
# count=0
# # for i in range(num):
# #   print(a,end="")
# #   a,b=b,a+b
  
# #   print()

# while count<num:
#   print(a,end=" ")
#   c=a+b
#   a=b
#   b=c
#   count+=1


#reverse a number

num=1234
reverse=0
# while num>0:
#   digit=num%10
  
#   num=num//10
#   reverse=reverse*10+digit
  
# print(reverse)

for i in range(len(str(num))):
    digit=num%10
  
    num=num//10
    reverse=reverse*10+digit
  
print(reverse)


#string reverse
number="12345"
print(number[::-1])

