# set1=set("input enter a number:")
# set1 = set(map(int,input("enter number:")))
# set1 = set(map(float,input("enter number:")))
# print(set1)

#Memory management
#python virtrual machine
#python gil 

# import sys
# def task():

#     k=3 #3 
#     print(k)
# task()

# a=10
# b=10
# c=a
# a=12
# print(b) #refernce counting it excute on runtime
# print(id(a))
# print(id(b))
# print(id(c))

# print(sys.getrefcount(a))

# import gc
# gc.collect()

# list=[]
# list2=[]

# list.append(list2)
# list2.append(list)

# import time
# start = time.time()
# def task():
#     for i in range(5):
#         print(i)
#         time.sleep(1)
# task()
# print(time.time()- start)


import sys
a=[10,20,30,40]
b=(10,20,3040,50)
print(sys.getsizeof(a))
print(sys.getsizeof(b))

list=[x for x in a]
print(sys.getsizeof(list))
#Arena: 256 kb(pool)
#pool: 8byte,16 byte,32 bytes
#512<28

