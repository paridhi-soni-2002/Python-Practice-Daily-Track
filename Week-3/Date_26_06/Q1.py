# 1. Division Calculator

# Write a program that takes two numbers from the user and performs division. Handle ZeroDivisionError.

try:
    num1=int(input("enter first number:"))
    num2=int(input("enter second number:"))
    
    print("Result:",num1/num2)
    
except ZeroDivisionError:
    print("cannot divide by zero.")
