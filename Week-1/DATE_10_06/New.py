# print("hello,world")
# a=5
# print(type(a))

# a=[10,202,30,40,50,60,70]
# print(a)
# a.append(90)

# set ={10,20,30,40,50}
# print(set)

# dict={
#     id: 11, "name":"paridhi","age":23}
# print(dict)

# a=10
# b=11
# c=30
# if a>b and a>c:
#     print(" a is greater")
# elif b>a and b>c:
#     print("b is greater")
# else:
#     print("c is greater")


#Insurance eligibility: Age 18-60,M, Non-smoker, BMI between 18-30
#Insurance eligibility: Age 16-50,F, Non-smoker, BMI between 18-30


Age = int(input("enter your age:"))
Gender = input("enter your gender: Male = M and Female = F:")
Habit = str(input("enter your  if you are \nsmoker =yes \n non-somker= no:"))
BMI =input("enter your BMI:")

if 18<=Age<=60 :
    if Gender=='M' :
        if Habit =="no" and 18<=BMI<=30:
         print("Insurance Eligibility:")
    


                  

