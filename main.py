library = []


def add_books():
    global library
    print("Add new book")
    quantity = int(input("Number of books to add: "))

    for _ in range(quantity):
        book_name = input("Book name: ")
        author = input("Author's name: ")

        found = False
        for book in library:
            if book['book_name'] == book_name:
                book['count'] = book.get('count', 0) + 1
                found = True
                break

        if not found:
            library.append({'book_name': book_name, 'author': author, 'count': 1})
            print(f"Book '{book_name}' by {author} added to the library.")
        else:
            print(f"Book '{book_name}' already exists in the library.")

def display_library():
    print("\nLibrary contains:")
    for index, book in enumerate(library, start=1):
        print(f"{index}. '{book['book_name']}' by {book['author']} - Avilable {book['count']}")

def rent_book():
    want_book = input("Write the book you want to rent: ")
    found = False
    for book in library:
        if book['book_name'] == want_book:
            if book.get('count', 0) > 0:
                print(f"Book '{want_book}' is available for rent.")
                book['count'] -= 1  # Zmniejszamy liczbę dostępnych kopii książki o 1
                print(f"Book '{want_book}' has been rented.")
            else:
                print(f"Book '{want_book}' is currently not available for rent.")
            found = True
            break

    if not found:
        print(f"Book '{want_book}' is not available in the library.")

        if not found:
            print(f"Book '{want_book}' is not available in the library.")

        if not found:
            print(f"Book '{want_book}' is not available in the library.")

def main():
    print("Library System")
    while True:
        print("\nChoose your option")
        print("1. Add Books")
        print("2. Display Library")
        print("3. Books rent")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_books()
        elif choice == '2':
            display_library()
        elif choice == '3':
            rent_book()
        elif choice == '4':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()