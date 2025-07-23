from library import Library
from student import Student

def main():
    library = Library()
    student = Student("Alice")

    # Add books to library
    library.add_book("Python Basics", "John Smith", "12345")
    library.add_book("OOP Concepts", "Jane Doe", "67890")
    library.add_book("Data Structures", "Alan Turing", "11122")

    while True:
        print("\n=== Library Menu ===")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            library.list_books()

        elif choice == '2':
            title = input("Enter the title of the book to borrow: ")
            book = library.find_book_by_title(title)
            if book:
                student.borrow(book)
            else:
                print("Book not found.")

        elif choice == '3':
            title = input("Enter the title of the book to return: ")
            book = library.find_book_by_title(title)
            if book:
                student.return_book(book)
            else:
                print("Book not found.")

        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
