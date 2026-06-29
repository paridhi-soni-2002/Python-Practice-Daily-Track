class Mobile:

    def __init__(self, brand, model, ram,
                 storage, battery, camera,
                 processor, price):

        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
        self.battery = battery
        self.camera = camera
        self.processor = processor
        self.price = price

    def call(self):
        print("Calling...")

    def send_message(self):
        print("Message Sent")

    def take_photo(self):
        print("Photo Captured")

    def charge(self):
        print("Charging Started")

    def show_specification(self):
        print("\nBrand:", self.brand)
        print("Model:", self.model)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Battery:", self.battery)
        print("Camera:", self.camera)
        print("Processor:", self.processor)
        print("Price:", self.price)


phone = Mobile(
    "Samsung",
    "S24",
    "8GB",
    "256GB",
    "5000mAh",
    "50MP",
    "Snapdragon",
    65000
)

phone.show_specification()
phone.call()
phone.send_message()
phone.take_photo()
phone.charge()