password = "python123"

attempt = 3

while attempt > 0:

    user = input("Enter password: ")

    if user == password:

        print("Login Successful")

        break

    else:

        attempt -= 1

        print("Wrong Password")

if attempt == 0:

    print("Account Locked")