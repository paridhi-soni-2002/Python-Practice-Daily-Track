words = [
    'apple',
    'banana',
    'ant',
    'cat',
    'air'
]

result=list(filter(lambda x:x.startswith('a'),words))
print(result)