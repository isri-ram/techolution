class User:
    """
  Represents a user of the library system.
  """

    def __init__(self, name, user_id):
        # Encapsulate class attributes
        self._name = name
        self._user_id = user_id
        self._borrowed_books = []

    def get_name(self):
        return self._name

    def get_user_id(self):
        return self._user_id

    def get_borrowed_book_isbns(self):
        return [book.get_isbn() for book in self._borrowed_books]

    def to_dict(self):
        return {
            "name": self.get_name(),
            "user_id": self.get_user_id(),
            "borrowed_books": self.get_borrowed_book_isbns()
        }

    def borrow_book(self, book):
        """
    Attempts to borrow a book, updates availability if successful.
    """
        if book.is_available():
            self._borrowed_books.append(book)
            book.set_availability(False)
            return True
        else:
            return False

    def return_book(self, book):
        """
    Attempts to return a book, updates availability if successful.
    """
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            book.set_availability(True)
            return True
        else:
            return False
