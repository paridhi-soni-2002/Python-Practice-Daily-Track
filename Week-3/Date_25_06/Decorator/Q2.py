# 2.	Write a decorator that accepts an argument n and executes the decorated function n times.
def repeat(n):
    def decorator(num):
        def wrapper():
           
           for i in range(n):
            num()
           
        return wrapper
    return decorator
    
@repeat(3)
def number():
    print("hello")
    
number()
    

    