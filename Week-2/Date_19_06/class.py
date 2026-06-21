#functions in python- it is reuasble block of code 
#def - keyword is used for the functions

# def add():
#     a=10
#     b=20
#     sum=a+b
#     print(sum)
    
# add()

# #taking arguments setting parameters

# def sum(a,b):
#     return a+b

# print(sum(20,30))

#multiplication
# def multiply(a,b):
#     return a*b

# print(multiply(20,30))

# #square of a number


# #1 positional arguments- argument must be passed in the exact order by the fucntion definition

# # keyword arguments-passing used the name of the parameter explicity not order 

# # arbitrary argument= when we do not know how many data is passed into fucntions(tuple)(*args)

# #default argument= passing before the functions call pre assigned values

# # arbitrary keyword argument= key and value pairs are called keyword args *kargs 
#             recieves arguemnts as a dictionary used when passing a variable in key and value pairs

# def multi(a,b=40):
#     #c =a*a
#     d=b*b
#     return d
# result=multi(20)
# print(result)

# def multi(a,b):
#     #c =a*a
#     d=a*a
#     return d
# result=multi(b=20,a=30)
# print(result)

# #keyword argument
# def multi(a,b,m=50):
#     c=a*a
#     d=b*b
#     print(f"{c} {d} {m}")
#     result = multi(b=20,a=30)
#     print(result)
    
# #arbitary

# def multi(a,b,m=50):
#     c=a*a
#     d=b*b
#     print(f"{c} {d} {m}")
    
def add(*args):
    result=sum(args)
    
    print(result)
    
add(20,30,40,50)


def add(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}{value}")
        
add(name= "demo",args= "22")


def add(**kwargs):
    res=0
    for key,value in kwargs.items():
        res+=(value)
    print(res)
    
add(a=20,b=22,c=40)
#print(result)

#print every character in the string in the capital letters
def capital(a):
    cap=a.upper()
    print(cap)

capital("paridhi")   


#lambda functions
#nameless functions- lambda arguments:
res= lambda a,b:a+b
print(res(3,4))


multiply = lambda a,b:a*b
print(multiply(4,4))
#lambda function with ternary operator
res= lambda a:"even" if a%2==0 else "odd"
print(res(20))

#map: functions applies a function to every element of an iterable
#filter: select elements based on a conditon(function,iterable)
#reducer: collective data se single value is return hogi
#lambda function: lambda argument

# map function
# syntax: map(function,iterable)
#filter fucntion,iterable filtering
#
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * x, numbers))

print(result)

var1=["1","2","3","4"]

res= map(lambda x:int(x),var1)
print(res)

list1=[1,2,3,4,5,6,7,8]
res=filter(lambda x:x%2==0,list1)
print(list(res))

age=[22,56,66,78,90]
res= filter(lambda x:x>=18,age)
print(list(res))


#to use reducer
from functools import reduce

res= reduce(lambda x,y:x+y,list1)
print(res)

#reducer functions (aggregation)
age=[22,56,78,23,56,12,34,14,100]

res=reduce(lambda x,y: x if x>y else y, age)
print(res)

students=[("name",80),("aman",70),("ajay",80)]

res= filter(lambda x:x[1]>70,students)
print(list(res))