def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True

result=list(filter(lambda x: is_prime(x),range(1,51)))

print(result)