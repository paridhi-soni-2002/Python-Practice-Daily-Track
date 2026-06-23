# 33.	Flatten a nested list and store only unique values using set comprehension.
nested = [[1, 2], [2, 3], [3, 4]]

result = {num for sublist in nested for num in sublist}

print(result)

value={n for sub in nested for n in sub}
print(value)