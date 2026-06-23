text = input("Enter string: ")

vowels = "aeiouAEIOU"

freq = {v: text.count(v) for v in vowels if v in text}

print(freq)