from functools import reduce
words = [
    'Python',
    'is',
    'awesome'
]
result = reduce(lambda x,y: x +" "+y,words)
print(result)