import csv
from book import Book
from storage import Storage


class Library:
    """
  Represents the library system with book management functionalities using CSV storage.
  """

    def __init__(self, storage_filename):
        self.storage = Storage(storage_filename)
        self.books = self.storage.load_data()  # Load books from CSV directly

    def add_book(self, title, author, isbn):
        """
        Adds a new book to the library and CSV storage.
        """
        new_book = Book(title, author, isbn)
        new_book_dict = new_book.to_dict()
        self.books.append(new_book_dict)
        self.save_changes()

    def display_books(self):
        """
        Displays all books.
        """
        books_to_display = self.books.copy()

        for book in books_to_display:
            availability_status = "Available" if book["available"] == "True" else "Borrowed"
            print(
                f"Title: {book.get('title', 'Unknown')}, Author: {book.get('author', 'Unknown')},"
                f" ISBN: {book.get('isbn', 'Unknown')}, Availability: {availability_status}")

    def search_books(self, query):
        """
        Searches for books based on title, author, or ISBN.
        """
        search_results = [book for book in self.books if (
                query.lower() in book["title"].lower() or
                query.lower() in book["author"].lower() or
                query.lower() in book["isbn"].lower()
        )]
        return search_results

    def save_changes(self):
        """
        Saves book data to CSV storage.
        """
        with open(self.storage.filename, 'w', newline='') as csvfile:
            fieldnames = ['title', 'author', 'isbn', 'available']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.books)
