a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
choice=input("Enter your choice:\n 1.Addition\n 2.Subtraction \n 3.Multiplication \n 4.Division\n")
if choice=='1':
    print(f"Addition is:{a+b}")
elif choice=='2':
    print(f"Subtraction is:{a-b}")
elif choice=='3':
    print(f"Multiplication is:{a*b}")
elif choice=='4':
    print(f"Division is:{a/b}")
else:
    print("wrong input")
    