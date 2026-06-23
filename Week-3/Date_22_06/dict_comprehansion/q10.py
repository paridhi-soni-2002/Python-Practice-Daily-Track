# 32.	Create a dictionary of prime numbers from 1 to 100 and their squares.
new_dict={
    i:i*i for i in range(1,101) 
    if i>1 and all( i% n!=0 for n in range(2,i))}
print(new_dict)