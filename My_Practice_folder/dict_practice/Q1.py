# student={
#     "Name":"Paridhi","age":23,"Class":"MCA"}
# print(student.items())
# student["Rollno"]=11
# print(student.items())
# for k,v in student.items():
#     print(k,v)

# fruit="banana"# fequency count in the dictionary
# dict={}

# for ch in fruit:
#     if ch in dict:
#         dict[ch]+=1
#     else:
#         dict[ch]=1
        
# print(dict.items())
    

#counting word in a dictionary
# sentence="Python is fun Python is simple"

# word=sentence.split()
# dict={}
# for i in word:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
 
        
# for k,v in dict.items():
#     print(k,v)

#find duplicate words
# sentence="apple mango apple orange mango kiwi"
# word=sentence.split()
# dict={}
# for i in word:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
        
# for k,v in dict.items():
#     if v>1:
#      print(k,":are duplicate words")

#merge two dict

# d1={"a":10,"b":20,"c":30}
# d2={"l":40,"m":50,"n":60}
# d1.update(d2)
# print(d1)
     
#sort dict by values
d1={"c":1,"b":33,"a":13,"d":20}
sort_dict=dict(sorted(d1.items(),key=lambda x:x[0]))
print(sort_dict)