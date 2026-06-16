#Take a string from the user and count:
# Alphabets 
# Digits 
# Special Characters 
# Example:
# Input: Python123@
# Output:
# Alphabets = 6
# Digits = 3
# Special Characters = 1


text=input("enter a string:")
alphabet=0
digit=0
special=0

for ch in text:
    if ch.isalpha():
        alphabet+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1
        
print("alphabet:",alphabet)
print("digit:",digit)
print("special:",special)
