  #• Find missing numbers from a set. 

number={1,3,5,8,9,10}
all_num=set(range(1,11))
missing=all_num - number
print("missing_numbers:",missing)