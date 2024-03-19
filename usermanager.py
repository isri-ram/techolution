import csv
from user import User
from storage import Storage


class UserManager:
    """
    Manages user functionalities in the library system using CSV storage.
    """

    def __init__(self, storage_filename):
        self.storage = Storage(storage_filename)
        self.users = self.storage.load_data()  # Load users from CSV directly

    def add_user(self, name, user_id):
        """
      Adds a new user to the system and storage.
      """
        new_user = User(name, user_id)
        new_user_dict = new_user.to_dict()
        new_user_dict['borrowed_books'] = new_user.get_borrowed_book_isbns()
        self.users.append(new_user_dict)
        self.save_changes()

    def delete_user(self, user_id):
        """
        Deletes a user from the system and CSV storage.
        """
        for user in self.users:
            if user.get('user_id') == user_id:
                self.users.remove(user)
                self.save_changes()
                return True
        return False

    def find_user_by_id(self, user_id):
        """
        Finds a user by their ID.
        """
        for user in self.users:
            if user.get('user_id') == user_id:
                return user
        return None

    def save_changes(self):
        """
        Saves user data to CSV storage.

        - Ensures 'borrowed_books' is included in fieldnames and data.
        """
        with open(self.storage.filename, 'w', newline='') as csvfile:
            fieldnames = ['name', 'user_id', 'borrowed_books']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user in self.users:
                user['borrowed_books'] = ','.join(user['borrowed_books'])  # Join ISBNs with commas
            writer.writerows(self.users)
