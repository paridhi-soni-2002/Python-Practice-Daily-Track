# Using map(), filter(), and reduce() together:
# nums = [1,2,3,4,5,6,7,8,9,10]
# Steps:
# 1.	Filter even numbers.
# 2.	Square them.
# 3.	Find their sum.
# Expected Output
# 220
from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10]

even=list(filter(lambda x:x%2==0,nums))


square=list(map(lambda x: x*x ,even))


sum=reduce(lambda x,y:x+y,square)


print(sum)