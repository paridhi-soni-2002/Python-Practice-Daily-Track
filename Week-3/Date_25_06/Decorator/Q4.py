def log(func):
    def wrapper(*args,**kwargs):
        print("function name",func.__name__)
        print("Arguments",args)
        print("keyword arguments",kwargs)
        return func(*args,**kwargs)
    return wrapper

@log
def student(name,age):
    print(name,age)
    
student("Paridhi",23)