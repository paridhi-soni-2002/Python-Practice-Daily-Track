# 14. Using try-except-else-finally

# Write a program that:

# Takes an integer input
# Divides 100 by the number
# Uses except for errors
# Uses else to print the result
# Uses finally to print "Execution Finished"

try:
    num=int(input("enter a  number:"))
    value=100/num
    
except ValueError:
    print("Enter a valid number")
    
except ZeroDivisionError:
    print("cannot divide by zero")
    
else:
    print("result is:",value)
    
finally:
    print("Execution happend")