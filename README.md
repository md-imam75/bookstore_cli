# Book Store Management System (CLI)

A simple Command Line Interface (CLI) Book Store Management System developed in Python using only standard libraries.

##  Features

-  Add new books with details (ISBN, title, author, genre, price, quantity)
-  Prevent duplicate books by ISBN
-  View all stored books in a user-friendly format
-  Remove books by ISBN
-  Save/load data to/from a `.json` file
-  Input validation and helpful error handling
-  Fully modular code with separate files for each feature
-  No external libraries or frameworks

##  File Structure

bookstore_cli/ 
├── main.py # Runs the menu and handles user flow 
├── add_book.py # Handles adding a book 
├── view_books.py # Displays all books 
├── remove_books.py # Deletes a book by ISBN 
├── validate_input.py # Input validation functions 
├── book_data.py # Loads and saves book data from/to JSON 
├── books.json # Data file (auto-created if missing) 
└── README.md # You're reading it!


##  How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/md-imam75/bookstore_cli.git
   cd bookstore_cli

    2. Run the program:
    python main.py

3. Follow the on-screen menu to add/view/remove books.
