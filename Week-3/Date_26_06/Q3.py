try:
    num=int(input("enter a number:"))
    print(100/num)
except ValueError:
    print("please enter only integers")
    
except ZeroDivisionError:
    print("Cannot divide by zero")