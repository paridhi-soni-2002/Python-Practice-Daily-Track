# 7.	Create a closure that returns a multiplier function capable of multiplying any input by a fixed number.
def outer(num1):
    def inner(num2):
        print(num1*num2)
    return inner

obj=outer(10)
obj(5)