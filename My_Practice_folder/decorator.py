def decorator(func):
    
    def wrapper():
        print("Welcome!")
        
        func()
        
        print("Have anice day!")
        
    return wrapper
    
@decorator
def greet():
    print("paridhi")
greet()
    
