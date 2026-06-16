# Take a string and print it in reverse order without using slicing ([::-1]).
# Example:
# Input: Python
# Output: nohtyP

string=input("enter the string:")
reverse=""
for i in range(len(string)-1,-1,-1):
    reverse+=string[i]
print(reverse)