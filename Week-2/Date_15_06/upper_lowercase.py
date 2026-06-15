value=str(input("enter a string:"))
count_upper=0
count_lower=0
for i in value:
    if i in value.lower():
        count_lower+=1
    else:
        count_upper+=1
        
print("lower:",count_lower)
print("upper:",count_upper)