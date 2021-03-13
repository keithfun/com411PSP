#ask user to enter the book cover type
print("What type of cover does the book have?")
book_type = input()
#select if the book has a hard or soft cover
if (book_type == "soft"):
  print("Is the book  perfect-bound?")
  bound_type = input()
#adding a nesting decision therefore another if that will be run only if the main decision is true
  if (bound_type == "yes"):
    print("Soft cover, perfect bound books are very popular")
  else:
    print("Soft cover with coils or stiches are great for short books")
# adding an outcome for false if statement
else:
  print("Books with hard covers can be more expensive!")

