# a=10
# b=20
 
# print(a+b)
# #tokenization: smallest unit of code
# x= NameError= operator
# 10 = number
# \n newline

# import tokenize

# with open("test.py","rb") as f:
#     tokens = tokenize.tokenize(f.readline)
#     for token in tokens:
#         print(token)

# import ast
# x=2+5
# code ="x=10"
# tree = ast.parse(code)
# print(ast.dump(tree))

# def task(a,b):
#     x=a
#     print(x)
    
# res = task(10,20)
# print(res)

# def task():
#     print("hello")
    
# #task

# print(task.__code__.co_consts) vaibale to find 


# import dis
# def task():
#     print("hello")
#     x=10
#     y=20
#     print(x)
    
# task()
# print(dis.dis(task))

#pvm = byte code to machine code
a=10
b=10
c=a+b
print(c)

# bytecode
# load fast a
# load fast b

# binary_op+
# store_fast c

#frame object: stores execution information for each function call
import inspect
def add():
    frame=inspect.currentframe()
    print(frame.f_locals)
    print(frame.f_globals)
    print(frame.f_lineno)
    x=10
    y=20
    return x+y

x=add()
print(x)


