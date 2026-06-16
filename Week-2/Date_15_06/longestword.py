value=str(input("enter a sentence:"))
word=value.split()
largest=""
for i in word:
    if len(i)>len(largest):
        largest=i
        
print("the largest word in a sentence is :",largest)
    
   
   
        
        