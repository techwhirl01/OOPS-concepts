from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))

    def list_books(self):
        print("\n📚 Library Books:")
        for book in self.books:
            print(book)

    def find_book_by_title(self, title):
        return next((book for book in self.books if book.title.lower() == title.lower()), None)
