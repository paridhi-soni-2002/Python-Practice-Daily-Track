contact={}

for i in range(5):
    name = input("enter a name:")
    phone=input("enter the phone number:")
    
    contact[name]=phone
print("\n Contact Book")

for name,phone in contact.items():
    print(name,":",phone)