# # Q4.Check whether a number is zero, positive, or negative
# a=int(input("enter a number:"))
# if a>0:
#     print(f"{a} is positive")
# elif a==0:
#      print(f"{a} is zero")
# else:
#     print(f"{a} is negative")


# # check whether a number is a multiple of 7
# number=int(input("enter the number:"))
# if number%7==0:
#     print(f"{number} is a multiple of 7")
# else:
#     print(f"{number} is not a multiple of 7")

# # Q7. Check employee bonus eligibility:
# # Salary > 50000 → Bonus Eligible
# # Otherwise Not Eligible

# salary=float(input("enter your salary:"))
# if salary>50000:
#     print("the employee is eligible for bonus")
# else:
#     print("the employee is not eligible")

# # Q8. Check login eligibility:
# Username = admin
# Password = 1234

# username = input("enter the username:")

# if username == "admin":
#     print("username is correct")
#     password = int(input("enter the password:"))
#     if password == 1234:
#         print("Password is correct \n Login sucessful")
#     else:
#         print("Incorrect password")
# else:
#     print("Invalid username")

# # Q9.Check scholarship eligibility:
# # Marks ≥ 80 AND Attendance ≥ 75

# Marks=int(input("enter your marks:"))
# Attendance=float(input("enter the attendance:"))
# if Marks>=80 :
#     if Attendance>= 75:
#          print("they are eligible for the scholarship:")
#     else:
#         print("Your Attendance should be more than 75% to be eligible for the scholarship")    
# else:
#     print("your marks should be more than 80 to be eligible for the scholarship")

# # Q10.Check admission eligibility:
# # Marks ≥ 60 OR Sports Certificate = Yes

# Marks=float(input("enter the marks:"))

# if Marks>=60 :
#     print("eligible for admission:")
# else:
#     Sports_certificate=input("if you are having certificate:  yes or no:")
#     if  Sports_certificate=='yes':
#      print("eligible for admission:")
#     else:
#      print("not eligible:")    
 
# # Q11. Check ATM withdrawal eligibility:
# # Balance ≥ Amount

# Balance=90000
# Amount=float(input("enter the amount you want to withdraw:"))
# if Amount>Balance:
#     print("Insufficient Balance:")
# else:
#     print(f"able to withdraw \n after withdraw the balance is{Balance-Amount}")



