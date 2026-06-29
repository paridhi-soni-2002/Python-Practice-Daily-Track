class FoodOrder:

    def __init__(self, order_id, customer_name,
                 restaurant_name, food_item,
                 quantity, price,
                 delivery_address, payment_status):

        self.order_id = order_id
        self.customer_name = customer_name
        self.restaurant_name = restaurant_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price
        self.delivery_address = delivery_address
        self.payment_status = payment_status

    def place_order(self):
        print("Order Placed Successfully")

    def cancel_order(self):
        print("Order Cancelled")

    def track_order(self):
        print("Your order is on the way.")

    def make_payment(self):
        self.payment_status = "Paid"
        print("Payment Successful")

    def show_order(self):
        print("\nCustomer:", self.customer_name)
        print("Food:", self.food_item)
        print("Quantity:", self.quantity)
        print("Payment:", self.payment_status)


order = FoodOrder(
    201,
    "Paridhi",
    "Dominos",
    "Pizza",
    2,
    600,
    "Indore",
    "Pending"
)

order.show_order()
order.make_payment()
order.track_order()