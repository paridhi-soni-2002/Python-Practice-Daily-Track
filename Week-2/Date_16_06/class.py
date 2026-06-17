# #list comprehansion short way to create a list
# #list = [expression for num in iterable]
# list=[]
# for i in range(6):
#     list.append(i)
# print(list)
# #list comprehansion
# new_list=[i**3 for i in range(1,6)]
# print(new_list)

# new_one=[i for i in range(1,20) if i%2==0]
# print(new_one)
# #ternary operator
# number=["even" if x%2==0 else "odd" for x in range(5)]
# print(number)

# num1 =[10,20,30,40,50]
# num2=[x+5 for x in num1]
# print(num2)

# fruits=["apple","banana","orange","kiwi"]
# new_list=[len(num) for num in fruits]
# print(new_list)
# new_list=[num for num in fruits]


#set 
# num={10,20,30,40,50}
# print(num)
# num.add(70)
# print(num)
# num.remove(50)
# print(num)
# num.discard(30)
# print(num)
# # ans=num.pop()
# # print(num)
# num.update(34)
# print(num)

# #set operations
# a={2,3,4,5}
# b={3,5,6,7}
# print(a & b)#intersection
# print(a|b) #union
# print(a-b) #differnce
# print(a^b) #symmetric difference 


#dictionary :(key,values)

# dict ={id:1,"name":"monika","age":22}
# print(dict)

# print(dict.keys())
# print(dict.values())
# print(dict.items())


# for key,value in dict.items():
#     print(key,value)
    
# for key in dict.keys():
#     print(key)
    
# student={"maths":98,"hindi":67,"python":95,"english":88}
# sum=0
# for key,value in student.items():
#     sum=sum+student[key]

# print(sum/len(student))

# for value in student.values():
#     sum+=value
    
# print(sum)


# total=sum(student.values()
#nested dicitionary
students ={
1:{"maths":98,"hindi":67,"python":95,"english":88},
2:{"maths":98,"hindi":67,"python":95,"english":88},
3:{"maths":98,"hindi":67,"python":95,"english":88},
4:{"maths":98,"hindi":67,"python":95,"english":88}
}

for key,subject in students.items():
    # print(key,value)
    # print(students[key]["maths"])#dictionary for nested dict
    for sub,mark in subject.items():
     print(students[key][sub],end =" ")
    print(key)    
    
dict={1:20,2:30,3:40}
print(dict.items())
print(dict[2])
print(dict.keys())
dict={1:{20,30},2:{40,50}}
x=dict[2]
print(x)


dict={1:{"m":20,"n":30},2:{"k":40,"l":50}}
x=dict[2]
print(x["l"])
print(dict[1]["m"])


#frozen set 
#unorderd,unique values, immutable

# num = frozenset([40,50,60,70])
# print(type(num))

#dicitonary uses hash functions for the occurring
dict = {2:{34.567,877}}

print(dict)
