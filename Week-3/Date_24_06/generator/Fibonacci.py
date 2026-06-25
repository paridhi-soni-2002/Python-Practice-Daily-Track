def Fibonacci(num):
    first=0
    sec=1
    for i in range(num+1):
        yield first
        first,sec=sec,first+sec
       
        
        
for n in Fibonacci(5):
    print(n)