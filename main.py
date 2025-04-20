from book_data import load_books,save_books
from add_book import add_book
from view_books import view_books
from remove_books import remove_book

def main():
  books=load_books()
  
  while True:
    print("1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")
    
    choice= input("Choose an option: ").strip()
    
    if choice == '1':
      add_book(books)
    elif choice == '2':
      view_books(books)
    elif choice == '3':
      remove_book(books)
    elif choice == '4':
      save_books(books)
      print("Data saved. Goodbye!")
      break
    else:
      print("Invalid choice. Please enter 1, 2, 3, or 4.")
      
if __name__ == "__main__":
    main() 