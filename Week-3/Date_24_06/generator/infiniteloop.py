def infinte(num):
    # num=1    
    while True:
     yield num
     num+=1
     

print(list(infinte(100)))