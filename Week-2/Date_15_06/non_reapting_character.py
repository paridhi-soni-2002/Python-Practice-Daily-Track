# Take a string and find the first non-repeated character.
# Example:
# Input: swiss
# Output:
# w
str=str(input("enter a string:"))
for i in str:
    if str.count(i)==1:
      print("First non-repeated character:",i)
    break
    
