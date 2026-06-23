
# 10.Create a list of tuples containing:[(number, square)]for numbers from 1 to 10.
number=[ (res,res*res) for res in range(1,11)]
print(tuple(number))