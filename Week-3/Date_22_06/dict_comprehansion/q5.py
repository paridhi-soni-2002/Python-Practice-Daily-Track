# 26.	Create a frequency dictionary of characters in a string using dictionary comprehension.
value="rabbit"
frequency={ch: value.count(ch) for ch in value 
           
        }
print(frequency)