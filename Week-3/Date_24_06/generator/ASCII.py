def ascii_values(s):
    for ch in s:
        yield ord(ch)

print(list(ascii_values("hi")))