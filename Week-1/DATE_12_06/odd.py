#Print odd numbers only.
num=int(input("enter a number:"))
i=1
while i<=num:
    if i%2==0:
        i+=1
        continue
    else: 
     print(i)
    i+=1
   
   