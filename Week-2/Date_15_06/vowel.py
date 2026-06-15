#Take a string and count how many vowels (a, e, i, o, u) are present.
value = str(input("enter a string:"))
count=0
for i in value.lower():
    if i in "aeiou":
     count+=1

print(count)