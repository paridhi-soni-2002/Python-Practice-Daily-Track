# Remove duplicates from a list using set. 
number=[10,20,30,40,40,50,60,60,70]
unique_num = list(set(number))

print(unique_num)

#using list comprehension
number=[10,20,30,40,40,50,60,60,70]

unique=[]
[unique.append(num)  for num in number if num  not in unique]

print(unique)

#another approch

set= set()
a = int (input(("enter the values:")))
for i in range(1,6):
    set.add(i)
print(set)
