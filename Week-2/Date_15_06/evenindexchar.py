# Take a string and create a new string containing only the even index characters.
# Example:
# Input: Python
# Output: Pto

string = str(input(" enter a string value:"))

# for i in range(0,len(string),2):
#     print(string[i])

print(string[::2])