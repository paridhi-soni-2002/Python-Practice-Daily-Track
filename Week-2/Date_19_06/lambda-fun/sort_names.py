# 13.	Sort names by their length.
# names = ["John","Alexander","Bob","David"]

name = ["John","Alexander","Bob","David"]
result= sorted(name,key=lambda x:len(x))

print(result)