# 11.	Write a generator that yields factorial of numbers from 1 to N.
def factorial(num):
    fact=1
    for i in range(num,1,-1):
        fact=fact*i
        
    
    yield fact
        
print(list(factorial(4)))