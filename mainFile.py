class LibraryBook:
    def __init__(self, title, author, publication_year, isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn
        self.checked_out = False

class Library:
    def __init__(self):
        self.books = []
        self.total_books = 0
        self.available_books = 0

    def add_book(self, title, author, publication_year, isbn):
        book = LibraryBook(title, author, publication_year, isbn)
        self.books.append(book)
        self.total_books += 1
        self.available_books += 1

    def remove_book(self, book):
        self.books.remove(book)
        self.total_books -= 1
        if not book.checked_out:
            self.available_books -= 1

    def search_books(self, search_term):
        results = []
        for book in self.books:
            if search_term in book.title or search_term in book.author:
                results.append(book)
        return results

    def check_out(self, book):
        if not book.checked_out:
            book.checked_out = True
            self.available_books -= 1

    def check_in(self, book):
        if book.checked_out:
            book.checked_out = False
            self.available_books += 1

    def list_books(self):
        print("Library Inventory:")
        for book in self.books:
            status = "Checked out" if book.checked_out else "Available"
            print(f"{book.title} by {book.author}, {book.publication_year}, ISBN: {book.isbn} ({status})")
        print(f"Total books: {self.total_books}, Available books: {self.available_books}")

# Demonstration of using the Library class

# Create a new library object
library = Library()

# Add three new books to the library
library.add_book("Python for Data Analysis", "Wes McKinney", 2012, "978-1449319793")
library.add_book("Fluent Python", "Luciano Ramalho", 2015, "978-1491946008")
library.add_book("Automate the Boring Stuff with Python", "Al Sweigart", 2015, "978-1593275990")

# Search for books with the search term "Python" and print the results
search_results = library.search_books("Python")
for book in search_results:
    print(f"{book.title} by {book.author}, {book.publication_year}, ISBN: {book.isbn}")

# Check out one of the books
library.check_out(search_results[0])

# List all of the books in the library
library.list_books()

# Check in the book that was checked out
library.check_in(search_results[0])

# List all of the books in the library again to verify that the book was checked in successfully
library.list_books()
