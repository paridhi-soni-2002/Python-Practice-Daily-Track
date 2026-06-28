while True:
    try:
        num=int(input("enter an integer:"))
        print("you entered:",num)
        break
    except ValueError:
        print("Invalid input .Try again")
        