# 2. Integer Input Validation

# Take an integer input from the user. If the user enters anything other than an integer, display "Invalid Input".
try:
    num=int(input("enter an interger:"))
    print("you entered :",num)
    
except ValueError:
    print("Invalid Input")