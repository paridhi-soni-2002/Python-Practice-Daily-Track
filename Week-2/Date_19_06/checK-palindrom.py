def palindrom(value):
     rev=value[::-1]
     if rev==value:
      return True
     else:
        return False
     
print(palindrom("madam"))
        