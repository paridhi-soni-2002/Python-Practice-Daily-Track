def primenum(n):
    for i in range(2,n+1):
        is_prime=True
        for j in range(2,i):
         if i%j==0:
            is_prime=False
            break
         
        if is_prime:
          yield i
            
            
for num in primenum(10):
    print(num)
    
#2nd approach
def prime(num):
   for i in range(2,num+1):
     if all (i%j!=0  for j in range(2,i)):
        yield i
    
for num in prime(10):
    print(num)           