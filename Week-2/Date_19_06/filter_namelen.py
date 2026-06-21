names = [
    'Ram',
    'Shyam',
    'John',
    'Bob',
    'Alexander'
]

result=list(filter(lambda x:len(x)>4,names))
print(result)