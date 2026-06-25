
def sentence(value):
    words=value.split()
    for i in words:
        yield i
        
value="Python is a programming language"
print(list (sentence(value)))