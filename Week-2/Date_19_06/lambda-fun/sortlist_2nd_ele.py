# 12.	Sort the list according to the second element.
# data = [(1,4),(2,1),(3,2),(4,5)]
# Expected Output
# [(2,1),(3,2),(1,4),(4,5)]

data = [(1,4),(2,1),(3,2),(4,5)]

sorting= sorted(data,key=lambda x:x[1])
print(sorting)