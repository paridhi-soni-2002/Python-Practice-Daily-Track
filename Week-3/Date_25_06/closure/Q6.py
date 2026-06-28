# 6.	Implement a closure that uses the nonlocal keyword to modify an outer variable.
def outer():
    #message=("Python is a programming language")
    num=10
    def inner():
        nonlocal num
        num+=5
        print (num)
    return inner

obj=outer()
obj()
obj()