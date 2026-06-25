def Number(n):
    for i in range(1,n+1):
        yield i
        
# print(list(Number(5)))
for val in Number(5):
    print(val)