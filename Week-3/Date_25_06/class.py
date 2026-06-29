#closure- it is a fuction object that remember values from its enclosing scope 
#even after the outer function has finished execution

# def outer():
#     a="hello"
#     return a
# x=outer()
# print(x)

# #LEGB
# # local,global,enclosing scopes,builtin scope

# a=15#global scope
# def outer():
#     print("outer functions")
#     y=5#enclosing scope
    
#     def inner():
       
#         nonlocal y
#         y=y+1
#         z=10#local scope
#     print("inner functions") 
#     return (f"{a} {y} {z}")
    
#     return inner

# x=outer()
# print(x())

#nonlocal kerword--

#decorator: a decorator is a function tha modifies or extend 
#the behavior of another function without changing the original code

# def decorator(func):
#     def wrapper():
#         print("before functions")
#         func()
#         print("after functions")
#         return wrapper
    

# @decorator     
# def message():
#  print("welcome")
# message()
# wrapper_obj =decorator(message) 
# wrapper_obj()

#time coud be find out using decorator
# import time
 
# def login_required(abc):
#    def wrapper(*args,**kwrgs):
#     start=time.time()
#     abc(*args,**kwargs)    
#     end=time.time()
#     print("Execution Time:",end-start)
#     return wrapper
   
# @login_required
# def dashboard(user):
#    print("welcome",user)
#    dashboard("abc")
   
# print(dashboard.__name__)
#@wraps - function in decorator


# def function_sum(a,b):
  
# def wrapper
# def rectangle(x,y):
#    Area=x*y
#    def triangle(a,b):
#      Area=1/2(a*b)   
   

   