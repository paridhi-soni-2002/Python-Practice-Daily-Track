class LibraryBook:

    def __init__(self, book_name, copies):

        self.__book_name = book_name
        self.__available_copies = copies

    def issue_book(self):

        if self.__available_copies > 0:
            self.__available_copies -= 1
            print("Book Issued")
        else:
            print("Book Not Available")

    def return_book(self):

        self.__available_copies += 1
        print("Book Returned")

    def get_available_copies(self):

        return self.__available_copies


obj = LibraryBook("Python", 5)

obj.issue_book()

obj.return_book()

print(obj.get_available_copies())