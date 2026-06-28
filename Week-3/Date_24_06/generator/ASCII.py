def ascii_values(s):
    for ch in s:
        yield ord(ch)#ord is used to print the ascii value

print(list(ascii_values("hi")))