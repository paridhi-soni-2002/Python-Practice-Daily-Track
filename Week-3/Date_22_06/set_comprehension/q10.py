# 20.	Create a set of common elements from two lists.
list1=[10,20,30,40,50]
list2=[10,30,50,70,80]

common={n for n in list1 for j in list2 if n==j}
print(common)