# 5.	Write a closure that generates functions for calculating powers, such as square, cube, and fourth power.
def outer(n):
   
    def inner(num):  
      print(num**n)
    return inner

square=outer(2)
cube=outer(3)
fourth=outer(4)

print(square(3))
      
   