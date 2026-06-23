# 7.	Create a list of cubes of odd numbers from 1 to 30
odds=[x**3 for x in range(1,31) if x%2!=0 ]
print(odds)