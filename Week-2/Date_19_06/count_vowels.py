# def count_vowels(n):
#     count=0
#     for i in n.lower():
#      if i in "aeiou":
#         count+=1
#     return count
    
    

# value=str(input("enter the string name:"))
# print(count_vowels(value))

#another approch
def count_vowel(text):
   vowels="aeiouAEIOU"
   count=0
   for i in text:
      if i in vowels:
         count+=1
   return count
   
text=str(input("enter the string name:"))
print(count_vowel(text))
