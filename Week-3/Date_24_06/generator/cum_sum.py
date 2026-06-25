def cumulativesum(num):
    total=0
    for i in num:
        total+=i
        yield total
        
val=[1,2,3,4,5]  
print(list(cumulativesum(val)))