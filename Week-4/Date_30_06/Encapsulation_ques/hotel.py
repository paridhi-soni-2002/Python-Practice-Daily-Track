class HotelRoom:

    def __init__(self):
        self.__room_status = "Available"

    def book_room(self):
        self.__room_status = "Booked"

    def checkout(self):
        self.__room_status = "Available"

    def get_status(self):
        return self.__room_status


obj = HotelRoom()

obj.book_room()

print(obj.get_status())

obj.checkout()

print(obj.get_status())