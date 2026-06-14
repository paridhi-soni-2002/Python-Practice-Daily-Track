
original_pass=1234

while True:
   password = int(input("enter the  your password:"))
    
   if original_pass== password:
        print("correct password")       
        break
   else:
    print("wrong password: enter again")
   
# print(type(original_pass))
# print(type(password))