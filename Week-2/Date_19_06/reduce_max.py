from functools import reduce
nums = [10,45,23,67,12]

result=reduce(lambda x,y:
              x if x>y else y ,nums)

print(result)