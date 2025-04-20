def get_non_empty_string(s):
  while True:
    value=input(s).strip()
    if value:
      return value
    print("Error: This field cannot be empty.")
    
def get_positive_float(s):
  while True:
    try:
      value=float(input(s))
      if value>0:
        return value
      print("Error: Price must be a positive number.")   
    except ValueError:
      print("Error: Please Enter a valid number")

def get_non_neg(s):
  while True:
    try:
      value=int(input(s))
      if value>=0:
        return value
      print("Error: Quantity must be a non-negative integer.")
      
    except ValueError:
       print("Error: Please enter a valid whole number.")
        
               