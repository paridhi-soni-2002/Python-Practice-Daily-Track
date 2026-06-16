 #Create a list of 10 numbers and print all numbers greater than 50.

numb=[]
final=[]
print("enter 10 numbers:")
for i in range(10):
    num =int(input("enter number:"))
    numb.append(num)
print(numb)
for i in numb:
    if i>50:
        final.append(i) 
print(final)    

