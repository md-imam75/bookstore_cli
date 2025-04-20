def remove_book(books):
  print("\n--- Remove a Book ---")
  isbn_to_remove = input("Enter the ISBN of the book to remove: ").strip()
  
  for book in books:
    if(book["isbn"]==isbn_to_remove):
      books.remove(book)
      print("Book removed successfully.")
      return
    
  print("No book found with that ISBN")  