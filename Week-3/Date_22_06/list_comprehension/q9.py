# 9.	Create a list of common elements between two lists.
list1=[1,2,3,4,5]
list2=[2,4,5,6,7]

common=[x for x in list1 for y in list2 if x==y ]
print(common)