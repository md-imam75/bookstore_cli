import json
import os

File_name="books.json"
def load_books():
  if os.path.exists(File_name):
    with open(File_name,'r') as file:
      try:
        return json.load(file)
      except json.JSONDecodeError:
        print("Error: book.json is not a valid JSON file.Starting with empty data")
        return []
  else:
    return []
  
def save_books(books):
  with open(File_name,'w')as file:
    json.dump(books,file,indent=4) 
        