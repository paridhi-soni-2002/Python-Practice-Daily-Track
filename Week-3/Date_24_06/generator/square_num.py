num=[1,2,3,4,5]
def squarenum(num):
    for i in num:
        val=i*i
        yield val
        
print(list(squarenum(num)))