# 8.	Write a closure that stores a secret message and provides access to it only through an inner function.
def secret():
    message="It's a secret message"
    def inner():
        print(message)
    return inner

obj=secret()
obj()