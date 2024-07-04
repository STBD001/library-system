library = []
count=0
def add_books():
    print("Add new book")
    quantity = int(input("Number of books to add: "))
    for _ in range(quantity):
        book_name = input("Book name: ")
        author = input("Author's name: ")
        library.append({'book_name': book_name, 'author': author})

def display_library():
    print("\nLibrary contains:")
    for index, book in enumerate(library, start=1):
        print(f"{index}. '{book['book_name']}' by {book['author']}")

def Rent_book():
    want_book = input("Write your book you want to rent: ")
    found = False
    for book in library:
        if book['book_name']==want_book:
            print(f"Book '{want_book}' is available for rent.")
            library.remove(book)
            print(f"Book '{want_book}' has been rented and removed from the library.")
            found = True
            break

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
            Rent_book()
        elif choice == '4':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()