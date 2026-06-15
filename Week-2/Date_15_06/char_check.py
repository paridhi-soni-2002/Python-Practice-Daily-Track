#Take a string and check whether it starts with a given character.

str=str(input("enter a string:"))
char="A"
for i in str:
    if i==char:
        print("character is present in the given string:")
        break
else:
     print("character is not present in the string:")

