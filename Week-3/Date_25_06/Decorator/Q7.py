# 7.	Create a decorator that caches the result of a function so repeated calls with the same arguments do not recompute the value.
def cache(func):
    memory={}
    def wrapper(n):
        if n in memory:
            print("from cache")
            return memory[n]
        result=func(n)
        memory[n]=result
        return result
    return wrapper

@cache
def square(n):
    print("calculating....")
    return n*n

print(square(5))
print(square(5))