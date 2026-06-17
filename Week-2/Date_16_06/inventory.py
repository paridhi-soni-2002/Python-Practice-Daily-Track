inventory={}
n = int(input("enter the  number of products:"))

for i in range(n):
    product=input("enter the product name:")
    quantity=input("enter the product quantity:")
    inventory[product]=quantity
    
print("\n Inventory")
for product,quantity in inventory.items():
    print(product ,":" ,quantity)