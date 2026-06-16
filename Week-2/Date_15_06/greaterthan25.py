number=[]
for i in range(6):
    num=int(input("enter the number:"))
    number.append(num)
print("current list:",number)  
new_number=[]

for i in number:
    if num>25:
        new_number.append(i)
        
print(new_number)