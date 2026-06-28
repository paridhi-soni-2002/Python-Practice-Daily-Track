# 8.	Write a decorator that validates all arguments passed to a function are positive integers and raises an exception otherwise.
def validate(func):
    def wrapper(*args):
        for value in args:

            if value <= 0:
                raise ValueError("Only Positive Integers Allowed")

        return func(*args)

    return wrapper


@validate
def add(a, b):
    print(a + b)


add(10, 20)