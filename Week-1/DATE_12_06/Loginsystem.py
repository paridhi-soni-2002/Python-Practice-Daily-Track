Username = "Admin"
Password = 1234
user_new = input("enter the user name:")

if user_new==Username:
    for i in range(4):
        pass_new=int(input("enter the password:"))
        if pass_new==Password:
            print("Login Successfull..!")
            break
        i+=1
        if i==3:
            print("Account Locked")
            break
else:
        print("Ivalid Username")