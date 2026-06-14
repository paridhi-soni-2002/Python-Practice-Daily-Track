list =[10,20,30,40,50,60,70]
num=int(input("enter a number:"))
for i in list:
   if num==i:
      print(f"{num} is found in the list")
      break
else:
      print("wrong input")    