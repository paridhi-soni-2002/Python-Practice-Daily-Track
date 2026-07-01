class MovieTicket:

    def __init__(self, seat_number, price):

        self.__seat_number = seat_number
        self.__price = price

    def book_ticket(self):
        print("Ticket Booked")

    def cancel_ticket(self):
        print("Ticket Cancelled")

    def get_ticket_details(self):

        print("Seat :", self.__seat_number)
        print("Price:", self.__price)


obj = MovieTicket("A12", 300)

obj.book_ticket()

obj.get_ticket_details()