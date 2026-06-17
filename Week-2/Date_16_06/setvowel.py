#• Count vowels using a set. 
text = input("enter a string:")
vowels={'a','e','i','o','u'}
count=0
for ch in text.lower():
    if ch in vowels:
        count+=1
print("the vowels in the string is :",count) 
