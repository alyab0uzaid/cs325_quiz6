from abc import ABC, abstractmethod

# Interface for guest users
class GuestLibrary(ABC):
    @abstractmethod
    def search_books(self, query):
        print("Guest searching for books with query:", query)

# Interface for librarian users
class LibrarianLibrary(ABC):
    @abstractmethod
    def add_book(self, book_title):
        print("Librarian adding book:", book_title)

    @abstractmethod
    def remove_book(self, book_title):
        print("Librarian removing book:", book_title)

    @abstractmethod
    def generate_reports(self):
        print("Librarian generating reports...")

# Concrete class implementing GuestLibrary interface
class LibrarySearch(GuestLibrary):
    def search_books(self, query):
        # Search logic
        print("Searching for books with query:", query)

# Concrete class implementing LibrarianLibrary interface
class LibraryManagement(LibrarianLibrary):
    def add_book(self, book_title):
        # Add book logic
        print("Adding book:", book_title)

    def remove_book(self, book_title):
        # Remove book logic
        print("Removing book:", book_title)

    def generate_reports(self):
        # Generate reports logic
        print("Generating reports...")

class LibraryUser:
    def borrow_book(self, book):
        # Borrow book logic
        print("Borrowing book...")

    def return_book(self, book):
        # Return book logic
        print("Returning book...")

def main():
    # Dummy values
    search_service = LibrarySearch()
    management_service = LibraryManagement()
    user_service = LibraryUser()

    # Usage examples
    search_service.search_books("Python")
    management_service.add_book("Introduction to Python")
    user_service.borrow_book("Introduction to Python")

if __name__ == "__main__":
    main()
