def view_books(books):
    print("\n--- Book Inventory ---")

    if not books:
        print("No books found in the store.")
        return
      
    for i,book in enumerate(books,1):
      print(f"\nBook #{i}")
      print(f" Title     : {book['title']}")
      print(f"  Author   : {book['author']}")
      print(f"  ISBN     : {book['isbn']}")
      print(f"  Genre    : {book['genre']}")
      print(f"  Price    : ${book['price']:.2f}")
      print(f"  Quantity : {book['quantity']}")
      
        