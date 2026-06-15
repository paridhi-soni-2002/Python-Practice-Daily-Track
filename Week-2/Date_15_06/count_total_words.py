#Take a sentence and count the total number of words.
sentence=str(input("enter a sentence in the input block:"))
count=0
for i in sentence:
    if i==" ":
        continue
    else:
        count+=1
        
print("words are:",count)
