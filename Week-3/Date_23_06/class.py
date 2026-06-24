# #iterators - are the objects that produce value one at a time
# # protcol- Iter() return iterator object
# #and next() it return next value
# #iterables- collective datatypes list tuple range dict

# list1=[1,2,3,4,5,6,7,8,9,10]
# # it=iter(list1)#__iter__()
# # print(it)
# # print(next(it))#__next__()
# # print(next(it))
# # list1=(1,2,3,4,5,6,7,8,9,10)
# # it=iter(list1)
# # print(it)
# # print(next(it))

# # it=iter(list1)
# # while True:
# #     try:
# #         item = next(it)
# #         print(item)
# #         expect StopIteration:
# #         break


# # decoupled traversal state: data object stores only the data store current value and move to next
# # memory efficieny
# # uniform interface
# #custom iterator: init(start,stop),iter(),next()

# #counting iterator
# class Counter:
#     def __init__(self,start,end):
#         self.start=start
#         self.end=end
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         # if self.current > self.end:
#         #     raise StopIteration
#         value = self.current
#         self.current+=1
        
#         return value
         
# c=Counter(1,5)

# for i in c:
#     print(i)
    
#infinite iterator


#genrator-that genrate one by one value

def counter(max_value):
    count=1
    while count<= max_value:
        yield count
        count +=1
x=counter(5)
for num in x:
    print(num)