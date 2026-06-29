class Book:

  
    def __init__(self, book_id, title, author,
                 publisher, genre, price,
                 total_pages, available_copies):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.publisher = publisher
        self.genre = genre
        self.price = price
        self.total_pages = total_pages
        self.available_copies = available_copies

    def issue_book(self):

        if self.available_copies > 0:
            self.available_copies -= 1
            print("Book Issued Successfully.")
        else:
            print("Book is not available.")


    def return_book(self):

        self.available_copies += 1
        print("Book Returned Successfully.")

  
    def show_details(self):

        print("\n------ Book Details ------")
        print("Book ID          :", self.book_id)
        print("Title            :", self.title)
        print("Author           :", self.author)
        print("Publisher        :", self.publisher)
        print("Genre            :", self.genre)
        print("Price            :", self.price)
        print("Total Pages      :", self.total_pages)
        print("Available Copies :", self.available_copies)

  
    def update_price(self, new_price):

        self.price = new_price
        print("Price Updated Successfully.")

  
    def check_availability(self):

        if self.available_copies > 0:
            print("Book is Available.")
        else:
            print("Book is Not Available.")



book1 = Book(
    101,
    "Python Programming",
    "Guido Van Rossum",
    "ABC Publication",
    "Programming",
    550,
    450,
    5
)



book1.show_details()

book1.check_availability()

book1.issue_book()

book1.show_details()

book1.return_book()

book1.show_details()

book1.update_price(650)

book1.show_details()