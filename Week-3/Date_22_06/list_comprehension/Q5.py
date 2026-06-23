# 5.	Create a list of numbers from 1 to 50 that are divisible by both 2 and 5.
number=[num for num in range(1,51) if num%2==0 and num%5==0]
print(number)