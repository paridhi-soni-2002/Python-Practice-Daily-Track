def reverse(value):
    for i in value[::-1]:
        print(i)
        
reverse("hello")

#another
def rev_string(test):
    reverse=" "
    for i in test:
        reverse=i+reverse
    return reverse

print(rev_string("apple"))