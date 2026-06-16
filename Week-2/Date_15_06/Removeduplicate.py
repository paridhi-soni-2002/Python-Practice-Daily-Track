# Create a list with duplicate values and remove duplicates without using set().
# Example:
# Input: [1,2,2,3,4,4,5]

# Output: [1,2,3,4,5]

number=[1,2,2,3,4,4,5]
visited=[]
for i in number:
    if i not in visited:
        visited.append(i)
print("after removing duplicate values:",visited)       
        
    
    

