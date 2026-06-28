# 10.	Create a closure that returns two functions: one to increment a value and another to decrement it while sharing the same state.
def counter():
    value=0
    def increment():
        nonlocal value
        value+=1
        return value
    def decrement():
        nonlocal value
        value-=1
        return decrement
    return increment,decrement

obj1,obj2=counter()
print(obj1())
print(obj1())
print(obj2())
print(obj1())