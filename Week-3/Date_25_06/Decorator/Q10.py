# 10.	Apply multiple decorators to a function and determine the order in which they execute.
def first(func):

    def wrapper():

        print("First Before")

        func()

        print("First After")

    return wrapper


def second(func):

    def wrapper():

        print("Second Before")

        func()

        print("Second After")

    return wrapper


@first
@second
def greet():
    print("Hello")


greet()