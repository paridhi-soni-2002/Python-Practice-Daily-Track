# 3.	Implement a closure that maintains a running total and updates it whenever a new number is passed.
def outer():
    total=0
    def inner(num):
     nonlocal total
     total+=num
     return total
      
    return inner

obj=outer()
print(obj(10))
print(obj(20))
print(obj(30))
