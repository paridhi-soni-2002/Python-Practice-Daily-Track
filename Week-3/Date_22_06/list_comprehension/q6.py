# 6.	Flatten the following nested list:

nested = [[1, 2], [3, 4], [5, 6]]

result=[i for j in nested  for i in j ]
print(result)