# list comprehansion
val=[1,2,3,4,5]
val1=[x*x for x in val]
print(val1)

#set comprehansion

num1={1,2,3,4,5}

num2={i*i for i in num1}
print(num2)

#dictionary comprehansion

num=[1,1,2,3,4,5,5]
dict={}

for i in num:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
        
print(dict)
        

val=["mango","apple","orange","kiwi"]
# dict={}
# for i in val:
#     dict[i]=len(i)
    
# print(dict)

value={i:len(i) for i in val}
print(value)


text={"mango":80,"apple":90,"orange":65,"kiwi":59}
# answ={k:v for k,v in text if v>60}
# print(answ)

dict1={k:v+10 if len(k)>5 else v-10 for k,v in text.items() if v>=90}
print(dict1)

#it takes less time 
import time
start =time.time()
list1=[i*i for i in range(1000000)]
print(time.time()-start)


#create employee bonus dict

dict3={
    "paridhi":65000,
    "avantika":55000,
    "gurman":50000,
    "pranjali":70000,   
}

#salary>=55000:10%
#salary<55000:5%
Bonus={ k:v*10//100+v if v>55000 else v*5//100+v for k,v in dict3.items() }

print(Bonus)

# 55k+ then 10% incre else 5%
# emp = {
#     "paridhi"= {"salary":50000,"bonus":1,"total": 54423},
#     "gurman"= {"salary": 60000,"bonus":2,"total":34},
#     "avantika"= {"salary":56000,"bonus":2, "total":54},
#     "arya"= {"salary":32000, "bonus":2,"total":54},
#     "hjdfg"= {"salary":43000, "bonus":1,"total":43}
# }

#salary, bonus,total : in one nested dictionary comprehansion
evaluate = {k:{"salary":v,
               "bonus":(v*10//100) if v>=55000 else(v*5//100),
               "total":(v*10//100)+v if v>=55000 else(v*5//100)+v}
                for k,v in dict3.items()}
print(evaluate)
