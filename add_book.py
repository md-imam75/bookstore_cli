from validate_input import (
    get_non_empty_string,
    get_positive_float,
    get_non_neg
)
def add_book(books):
  print("\n--- Add a New Book ---")
  isbn=get_non_empty_string("Enter Book ISBN: ")
  
  for book in books:
    if book["isbn"]==isbn:
      print("Error: A book with this ISBN already exists")
      return
  
  title=get_non_empty_string("Enter Book Title:")
  author=get_non_empty_string("Enter Author Name:")
  genre = get_non_empty_string("Enter Genre: ")
  price = get_positive_float("Enter Price: ")
  quantity = get_non_neg("Enter Quantity in Stock: ")    
  
  new_book={
    "isbn":isbn,
    "title":title,
    "author":author,
    "genre":genre,
    "price":price,
    "quantity":quantity
  }
  books.append(new_book)
  print("Book added successfully.")