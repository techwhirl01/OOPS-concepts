from user import User

class Student(User):
    def __init__(self, name):
        super().__init__(name)
        self.borrowed_books = []

    def borrow(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")
