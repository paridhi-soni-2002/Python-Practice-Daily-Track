number= list(map(int,input("enter number:").split()))
 
seen=set()
duplicate = set()
for num in number:
    if num in seen:
        duplicate.add(num)
    else:
        seen.add(num)
        
print("Duplicate numbers:",duplicate)