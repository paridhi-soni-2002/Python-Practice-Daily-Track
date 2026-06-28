# 6.	Write a decorator that counts how many times a function has been called and stores the count as an attribute of the function.
def counter(func):
    def wrapper():
        wrapper.count+=1
        print("called",wrapper.count,"times")
        func()
    wrapper.count=0
    return wrapper

@counter
def greet():
    print("Hello")
    
greet()
greet()
greet()