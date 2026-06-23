# 4.	Create a list of vowels present in a string entered by the user

word="apple"
vowel=[x.lower() for x in word if x in "aeiou"]
print(vowel)