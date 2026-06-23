# 1.	Find the frequency of each element in a list using dictionary comprehension.
list1=[1,1,2,3,4,4,5,5,6]
frequency={key:list1.count(key) for key in list1}
print(frequency)