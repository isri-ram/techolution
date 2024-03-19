from library import Library
from usermanager import UserManager
from checkout import Checkout
import logging

# Configure logging with levels and format
logging.basicConfig(filename='library_logger.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def main():
    """
  Main function to start the library management application.
  """
    library = Library('books.csv')
    user_manager = UserManager('users.csv')
    checkout_manager = Checkout()

    while True:
        print("\nLibrary Management System")
        print("1. Books")
        print("2. Users")
        print("3. Borrow/Return Books")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manage_books(library)
        elif choice == '2':
            manage_users(user_manager)
        elif choice == '3':
            borrow_return_books(library, user_manager, checkout_manager)
        elif choice == '4':
            print("Exiting the application...")
            logging.info("Application exited successfully")
            break
        else:
            print("Invalid choice. Please try again.")


def manage_books(library):
    """
  Provides options for managing books in the library.
  """
    while True:
        print("\nBook Management")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Books")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            if library.search_books(isbn):
                print(f"Book with ISBN {isbn} already exists.")
            else:
                library.add_book(title, author, isbn)
            logging.info(f"Book added: Title: {title}, Author: {author}, ISBN: {isbn}")
        elif choice == '2':
            library.display_books()
            logging.info(f"Displayed all books")
        elif choice == '3':
            query = input("Enter search term (title, author, or ISBN): ")
            search_results = library.search_books(query)
            if search_results:
                print("Search Results:")
                for book in search_results:
                    print(f"Title: {book.get('title', 'Unknown')}, Author: {book.get('author', 'Unknown')}, "
                          f"ISBN: {book.get('isbn', 'Unknown')}, Availability: {book.get('available')}")
                    logging.info(
                        f"Searched for {query} and found {f"Title: {book.get('title', 'Unknown')}, Author: {book.get('author', 'Unknown')}, ISBN: {book.get('isbn', 'Unknown')}, Availability: {book.get('available')}"}")
            else:
                print("No books found matching your search criteria.")
                logging.info(f"Searched for {query} and found nothing similar")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


def manage_users(user_manager):
    """
  Provides options for managing users in the library.
  """
    while True:
        print("\nUser Management")
        print("1. Add User")
        print("2. Delete User")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter user name: ")
            user_id = input("Enter user ID: ")
            user_manager.add_user(name, user_id)
            logging.info(f"User added: Name: {name}, ID: {user_id}")
        elif choice == '2':
            user_id = input("Enter user ID to delete: ")
            if user_manager.delete_user(user_id):
                logging.info(f"User deleted: ID: {user_id}")
            else:
                print("User not found.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


def borrow_return_books(library, user_manager, checkout_manager):
    """
  Provides options for borrowing and returning books, including user lookup.
  """
    while True:
        print("\nBorrow/Return Books")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = input("Enter user ID: ")
            user = user_manager.find_user_by_id(user_id)
            if user:
                # Display available books for the user to borrow
                available_books = [book for book in library.books if book.get('available')]
                if available_books:
                    print("Available Books:")
                    for book in available_books:
                        print(
                            f"Title: {book.get('title', 'Unknown')}, Author: {book.get('author', 'Unknown')},"
                            f" ISBN: {book.get('isbn', 'Unknown')}, Availability: {book.get('available')}")

                    book_isbn = input("Enter ISBN of the book to borrow: ")
                    book_to_borrow = library.search_books(book_isbn)
                    if book_to_borrow and book_to_borrow[0].get('available'):
                        result = checkout_manager.borrow_book(user, book_to_borrow)
                        logging.info(f"Book borrowed: User ID: {user_id}, Book ISBN: {book_isbn}")
                        print(result)
                    else:
                        print("Book not found or unavailable.")
                else:
                    print("No books currently available for borrowing.")
            else:
                print("User not found.")
        elif choice == '2':
            user_id = input("Enter user ID: ")
            user = user_manager.find_user_by_id(user_id)
            if user:
                isbn = input("Enter the ISBN of the book to return: ")
                book_to_return = library.search_books(isbn)

                # Check if book exists and is borrowed by the user
                if book_to_return:
                    is_borrowed = False
                    for borrowed_isbn in user.get('borrowed_books', '').split(','):
                        if borrowed_isbn == book_to_return[0]['isbn']:
                            is_borrowed = True
                            break

                    if is_borrowed:
                        # Return book if borrowed by the user
                        result = checkout_manager.return_book(user, book_to_return)
                        logging.info(f"Book returned: User ID: {user_id}, Book ISBN: {isbn}")
                    else:
                        print(f"Book with ISBN {isbn} is not borrowed by this user.")
                else:
                    print(f"Book with ISBN {isbn} not found.")
            else:
                print("User not found.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
