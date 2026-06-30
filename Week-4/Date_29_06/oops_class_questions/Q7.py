# Amazon Product
class Product:
    def __init__(self,
                 product_id,product_name,category,brand,price,stock,rating,warranty):
        self.product_id=product_id
        self.product_name=product_name
        self.category = category
        self.brand = brand
        self.price = price
        self.stock = stock
        self.rating = rating
        self.warranty = warranty
        
    def buy(self):
        if self.stock>0:
            self.stock-=1
            print("buy:",self.product_name)
        else:
            print("not available")
            


    def add_to_cart(self):
        print("added to cart")
        

    def update_stock(self,qty):
        self.stock+=qty
        print("stock updated")
          
    def show_details(self):
        print("\n the product name:",self.product_name)
        print("the brand is:",self.brand)
        print("the price:",self.price)
        print("the stock is :",self.stock)
           
    def apply_discount(self,per):
        self.price-=self.price*per/100
        print("discount applied")
        
obj = Product(
    101,
    "Laptop",
    "Electronics",
    "Dell",
    60000,
    5,
    4.5,
    "2 Years"
)

obj.show_details()
obj.add_to_cart()