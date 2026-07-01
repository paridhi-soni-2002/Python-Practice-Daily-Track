class Flight:

    def __init__(self, seats):
        self.__available_seats = seats

    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            print("Seat Booked")
        else:
            print("No Seats Available")

    def cancel_booking(self):
        self.__available_seats += 1

    def get_available_seats(self):
        return self.__available_seats


obj = Flight(5)

obj.book_seat()
obj.book_seat()

print(obj.get_available_seats())