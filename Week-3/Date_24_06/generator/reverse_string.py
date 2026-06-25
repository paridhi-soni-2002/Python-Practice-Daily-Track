name=["paridhi"]
def reverse(name):
    for word in name:
        yield word[::-1]
        
for i in reverse(name):
    print(list(i))
        
