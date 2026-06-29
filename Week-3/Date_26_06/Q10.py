# 10. NameError Handling

# Try to print a variable that has not been defined and handle the exception gracefully.


try:
    # name="paridhi"
    print(name)
except NameError:
    print("Variable is not defined.")