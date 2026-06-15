# #strings
# str3=""" i am paridhi soni
#           i am studying python"""
          
# print(str3)

# greet= "hello"
# print(greet[0])
# new_str="m"+greet[1:]
# print(new_str)

# for i  in range(len(new_str)-1):
#     print(new_str[i])
    
# #negative indexing

# print(greet[::-1])

# #slicing in a string

# str="hello world"
# print(str[2:8])

# #concatnation
# first="demo"
# last= "test"
# str=first+last
# print(str)
# print("demo"*5)

# #it is case sensitive

# str3="demo"
# # str3=str3+"demo2"
# print(str3)

# #python creatred new string instead of modifying the old one

# print("n" in str3)

# #string methods
# print(str3.capitalize())

# print(str3.strip)

# #replace method
# st="i like c"
# print(st.replace("c", "python"))

# text="python java c++ c"
# print(text.split(","))

# #list to string

# list=["apple","banana","orange"]
# print(",".join(list))



#conconent in string
# arr= "apple"
# count=0
# for ch in arr.lower():
#     if ch  not in "aeiou":
#         count+=1
        
# print(count)

#list detailed methods

list=[12,23,45,67]
list.append(90)
list.insert(0,16)
list.extend([30,50])
# list.remove(16)
# list.pop(1)
# list.clear()

list.index(67)
list.sort()

print(list)
#tuples methods

#tuple does not allow sort function

tuple=(1,2,3,4,5)
tuple.index(4)
print(tuple)


#packing in the tuple
tuple=("demo",24,80)
#unpacking the tuple
name,age,weight = tuple
print(name)
print(age)
print(weight)


#constant value ke liye tuple and variable and changing value ke liye list use kerte hai