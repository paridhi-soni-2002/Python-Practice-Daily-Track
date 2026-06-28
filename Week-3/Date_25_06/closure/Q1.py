# 1.	Write a closure that remembers a name provided to the outer function and prints a greeting when called.
def outer(name):
    def inner():
        return f"Hello,{name}"
    return inner   

greet=outer("paridhi")
print(greet())