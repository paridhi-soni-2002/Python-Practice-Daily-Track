books = []



def add_book():

    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "available": True
    }

    books.append(book)

    print("Book Added Successfully")



def view_books():

    if len(books) == 0:
        print("No Books Available")
        return

    print("\nBook List")

    for book in books:

        print("--------------------")
        print("ID       :", book["book_id"])
        print("Title    :", book["title"])
        print("Author   :", book["author"])
        print("Available:", book["available"])



def search_book():

    title = input("Enter Book Title: ")

    found = False

    for book in books:

        if book["title"].lower() == title.lower():

            print("Book Found")
            print(book)

            found = True
            break

    if found == False:
        print("Book Not Found")



def issue_book():

    book_id = int(input("Enter Book ID: "))

    for book in books:

        if book["book_id"] == book_id:

            if book["available"] == True:

                book["available"] = False

                print("Book Issued Successfully")

            else:

                print("Book Already Issued")

            return

    print("Book Not Found")



def return_book():

    book_id = int(input("Enter Book ID: "))

    for book in books:

        if book["book_id"] == book_id:

            if book["available"] == False:

                book["available"] = True

                print("Book Returned Successfully")

            else:

                print("Book Already Available")

            return

    print("Book Not Found")



def delete_book():

    book_id = int(input("Enter Book ID: "))

    for book in books:

        if book["book_id"] == book_id:

            books.remove(book)

            print("Book Deleted Successfully")

            return

    print("Book Not Found")


# Main Menu
while True:

    print("\n== LIBRARY MANAGEMENT ==")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        issue_book()

    elif choice == "5":
        return_book()

    elif choice == "6":
        delete_book()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")