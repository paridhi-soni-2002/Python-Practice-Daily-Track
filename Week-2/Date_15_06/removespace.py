#Take a string and remove all spaces from it.
# Example:
# Input: Python Programming Language
# Output: PythonProgrammingLanguage

string=str(input("enter a string in input:"))
var="  hello there  "
result=string.replace(" ","")
ans=var.replace(" ","")
print(result)
print(ans)