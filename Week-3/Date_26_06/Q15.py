# 15. Student Marks Validation

# Accept marks from the user.

# Conditions:

# Marks cannot be negative.
# Marks cannot exceed 100.

# Raise an exception with an appropriate message if validation fails.

try:
    num=int(input("enter the marks:"))
    if num<0:
        print("Negative marks are not valid")
    if num>100:
        print("greater tha 100 not valid")
    
    
    print("valid marks")
except Exception as e:
    print(e)      