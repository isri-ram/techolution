# Techolution Library Management System
Library Management System - Python Project
This project implements a simple library management system using Python. It allows users to manage book borrowing and availability.

Features:

Book Management:

Add new books.

View a list of available books.

Search for books by title or ISBN.


User Management:

Register new users.

View user information.

Borrowing/Returning Books:

Borrow a book by searching or browsing.

Return a borrowed book.

Track book availability (available/borrowed).


Dependencies:
Python 3.x
csv module
Usage:
1. Clone the repository or download the project files.
2. Run the main script:
  `python main.py`

Project Structure:
The project is organized into several modules:

main.py: Entry point for the program, handles user interaction and calls functionalities from other modules.

book.py: Defines the Book class to represent book information (title, author, ISBN, availability).

user.py: Defines the User class to represent library users (name, ID, borrowed book).

usermanager.py: Handles user registration, information retrieval, and other user-related functionalities.

storage.py: Handles data operations using JSON files (stores book and user information).

checkout.py: Handles borrowing and returning book logic (depending on your implementation).
