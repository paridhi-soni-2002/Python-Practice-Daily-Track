# 1.	Write a decorator that prints "Before Function" before execution and "After Function" after execution of a function.
def decorator(func):
    def wrapper():
        print("before function")
        func()
        print("after function")
    return wrapper


@decorator
def greet():
    print("Hello,Paridhi")
    
greet()