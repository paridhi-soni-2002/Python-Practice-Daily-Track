# Prime numbers (1–100) using list comprehension

prime=[num for num in range(2,101) 
        if all ( num%i!=0 for i in range(2,num))]
print(prime)