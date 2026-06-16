#Take a string and print the frequency of each character.
string = str(input("enter a string:"))
visited= ""
for ch in string:
    if ch not in visited:
        print(ch ,"=",string.count(ch))
        visited=visited+ch
