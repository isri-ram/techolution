class Book:
    """
  Represents a book in the library system.
  """

    def __init__(self, title, author, isbn, available=True):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = available

    def __str__(self):
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}"

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_isbn(self):
        return self._isbn

    def is_available(self):
        return self._available

    def set_availability(self, available):
        self._available = available

    def to_dict(self):
        return {
            "title": self.get_title(),
            "author": self.get_author(),
            "isbn": self.get_isbn(),
            "available": self.is_available()
        }
