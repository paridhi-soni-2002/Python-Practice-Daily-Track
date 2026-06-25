def Evennum(num):
    for i in range(2,num+1,2):
        yield i

for val in Evennum(10):
        print(val)    