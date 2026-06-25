# 10.	Build a generator that filters out odd numbers from a list.
def odd_num(N):
    for i in range(1,N+1):
        if  i%2!=0:
            yield i
            
print(list(odd_num(10)))