#generator

def counter():
    yield 1 #stop (pause)
    yield 2
    yield 3
    
iterator = counter()#create object
print(next(iterator))
print(next(iterator))

#generators: are special was to produce value one by one
#instead of creating everything at once
#lazy iterator : it doesnot do work needed

#start execution
#one value return,pauses itself
#remember its postion

# def counter():
#     for i in range(1,5):
#        yield[i]
#        yield=counter(i) 
#      for i in iterator:
#         print(i)
    
# iterator = counter()#create object
# print(next(iterator))
# print(next(iterator))

def counter(max_value):
    count=1
    while count<=max_value:
        yield count
        count+=1
        
x=counter(5)
print(next(x))

def counter(max_value):
    for num in range(1,max_value+1):
        if num%2==0:
            yield num
            
x=counter(20)
for i in x:
    print(i)
    
#genrator expression

x=(x*x for x in range(1,6))

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))


#return- used in normal fucntions terminates completely
#return single value or an entire collection at once
#memory usage: high(for large collections)
#yield: used in generator pauses the fuction and saves state
       #once at time in sequence
       #minimal(once one item exists in memeory aa time)
       
#advance methods
#send()- send data into running generator
#throw()-exception to occur at the location where the generator is currently paused
#close()-ternimate the generators immedialtely

#send method use
def sender():
    while True:
        value=yield
        print("recieved value:", value)
        
g=sender()
next(g)
g.send(21)


#throw method
def demo():
    try:
     yield 1
    except ValueError:
        yield "valueError handled"

g=demo()
print(next(g))
print(g.throw(ValueError))

#close()=method use

def sender():
    while True:
        yield 1
        yield 2
        
g=sender()
print(next(g))
g.close()
print(next(g))

#global, local inclosing scope
x=10
def demo_outer():
    x="hello" #enclosing scope
    def demo_inner():
        m=10 #local scope
        print(f"{m} {x}")
        
    return demo_inner
k=demo_outer()
print(k)

#closure- it is a fuction object that remember values from its enclosing scope 
#even after the outer function has finished execution