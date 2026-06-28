# 2.	Create a closure that acts as a counter and returns the next count value each time it is called.
def counter():
    count=0
    def inner():
        nonlocal count #uses the outer variables
        count+=1
        return count
    return inner

next_val=counter()
print(next_val())
print(next_val())
print(next_val())
print(next_val())
print(next_val())















# def counter(num):
    
#     def inner():
        
#         for i in range(1,num+1):
#             print(i) 
#         i+=1
#         print(i) 
#     return inner

# number=counter(10)
# print(number())
            