import csv


class Storage:
    """
  Handles data persistence using JSON files.
  """

    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        """
      Loads data from a CSV file.
      """
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                return list(reader)
        except FileNotFoundError:
            return {}

    def save_book(self, data):
        """
      Saves book data to a CSV file.
      """
        with open(self.filename, 'w', newline='') as csvfile:
            fieldnames = ['title', 'author', 'isbn', 'available']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data.get('books', []))

    def save_user(self, data):
        """
      Saves user data to a CSV file.
      """
        with open(self.filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'user_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data.get('users', []))
