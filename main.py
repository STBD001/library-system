library = []
borrowed_books = []

def add_books():
    global library
    print("Add new book")
    quantity = int(input("Number of books to add: "))

    for _ in range(quantity):
        book_name = input("Book name: ")
        author = input("Author's name: ")

        found = False
        for book in library:
            if book['book_name'].lower() == book_name.lower():
                book['count'] += 1
                found = True
                break

        if not found:
            library.append({'book_name': book_name, 'author': author, 'count': 1, 'rent_count': 0})
            print(f"Book '{book_name}' by {author} added to the library.")
        else:
            print(f"Book '{book_name}' already exists in the library.")

def display_library():
    print("\nLibrary contains:")
    for index, book in enumerate(library, start=1):
        print(f"{index}. '{book['book_name']}' by {book['author']} - Available: {book['count']}")

def rent_book():
    global borrowed_books
    want_book = input("Write the book you want to rent: ").strip().lower()
    found = False
    for book in library:
        if book['book_name'].lower() == want_book:
            if book.get('count', 0) > 0:
                print(f"Book '{want_book}' is available for rent.")
                book['count'] -= 1
                book['rent_count'] += 1
                borrowed_books.append(book['book_name'].lower())
                print(f"Book '{want_book}' has been rented.")
            else:
                print(f"Book '{want_book}' is currently not available for rent.")
            found = True
            break

    if not found:
        print(f"Book '{want_book}' is not available in the library.")

def return_book():
    global borrowed_books
    return_book = input("Enter the title of the book you want to return: ").strip().lower()
    if return_book in borrowed_books:
        found = False
        for book in library:
            if book['book_name'].lower() == return_book:
                book['count'] += 1
                borrowed_books.remove(return_book)
                print(f"Book '{return_book}' has been returned.")
                found = True
                break
        if not found:
            print(f"Book '{return_book}' is not recognized.")
    else:
        print(f"Book '{return_book}' was not borrowed.")

def find_book():
    looking_book = input("Enter the title of the book you are looking for: ").strip().lower()
    found = False
    for book in library:
        if book['book_name'].lower() == looking_book:
            print(f"Book '{looking_book}' is available")
            found = True
            break
    if not found:
        print(f"Book '{looking_book}' is not available")

def best_book():
    if not library:
        print("\nNo books in the library to recommend.")
        return

    sorted_books = sorted(library, key=lambda x: x['rent_count'], reverse=True)
    print("\nRecommended books based on popularity:")
    for index, book in enumerate(sorted_books[:5], start=1):
        print(f"{index}. '{book['book_name']}' by {book['author']} - Rented {book['rent_count']} times")

def main():
    print("Library System")
    while True:
        print("\nChoose your option")
        print("1. Add Books")
        print("2. Display Library")
        print("3. Rent a Book")
        print("4. Return a Book")
        print("5. Find Book")
        print("6. Recommend Books")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_books()
        elif choice == '2':
            display_library()
        elif choice == '3':
            rent_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            find_book()
        elif choice == '6':
            best_book()
        elif choice == '7':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
