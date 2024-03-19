import csv
from storage import Storage


class Checkout:
    """
    Manages book borrowing and returning operations using CSV storage.
    (Consider extending this class for future cart functionalities)
    """

    def __init__(self):
        self.book_storage = Storage("books.csv")  # Use CSV storage
        self.user_storage = Storage("users.csv")

    def borrow_book(self, user, book):
        """
        Performs book borrowing logic, delegating to user and book methods.
        Updates book availability in CSV if successful.
        """

        if book[0]['available']:
            try:
                # Update book availability in CSV
                data = self.book_storage.load_data()
                user_data = self.user_storage.load_data()

                for row in data:
                    if row['isbn'] == book[0]['isbn']:
                        row['available'] = False
                        break

                for user_row in user_data:
                    if user_row['user_id'] == user['user_id']:
                        borrowed_books = user_row.get('borrowed_books', '')
                        user_row['borrowed_books'] = borrowed_books + ',' + book[0]['isbn'] if borrowed_books else \
                            book[0]['isbn']
                        break

                with open(self.book_storage.filename, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=['title', 'author', 'isbn', 'available'])
                    writer.writeheader()
                    writer.writerows(data)  # Write all books at once

                with open(self.user_storage.filename, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=['name', 'user_id', 'borrowed_books'])
                    writer.writeheader()
                    writer.writerows(user_data)

                return "Book borrowed successfully!"
            except FileNotFoundError:
                print(f"Error: File '{self.book_storage.filename}' or '{self.user_storage.filename}' not found.")
        else:
            return "Book borrowing failed. Book might be unavailable."

    def return_book(self, user, book):
        """
        Performs book returning logic, delegating to user and book methods.
        Updates book availability and user borrowed books in CSV if successful.
        """
        print(book)
        try:
            # Update book availability and user borrowed books in CSV
            book_data = self.book_storage.load_data()
            user_data = self.user_storage.load_data()

            # Update book availability
            for row in book_data:
                if row['isbn'] == book[0]['isbn']:
                    row['available'] = True
                    break

            # Update user borrowed books (assuming 'user_id' matches in user.csv)
            for user_row in user_data:
                if user_row['user_id'] == user['user_id']:
                    borrowed_books = user_row.get('borrowed_books', '').split(',')  # Split ISBNs into a list
                    borrowed_books.remove(book[0]['isbn'])  # Remove the returned book's ISBN
                    user_row['borrowed_books'] = ','.join(
                        borrowed_books) if borrowed_books else ''  # Join back with commas
                    print("Book returned successfully!")
                    break

            # Write updated data back to CSV files
            with open(self.book_storage.filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['title', 'author', 'isbn', 'available'])
                writer.writeheader()
                writer.writerows(book_data)

            with open(self.user_storage.filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=['name', 'user_id', 'borrowed_books'])
                writer.writeheader()
                writer.writerows(user_data)

        except FileNotFoundError:
            print(f"Error: File not found.")
        except ValueError:  # Handle potential ValueError if ISBN not found in borrowed_books
            print("Book not found in user's borrowed list.")
