#ask user for input
print("What phrase do you see")
phrase = str(input())
print("\n Reversing...")
#integrating for loop 
reversed = ""
for letters in phrase:
  reversed = letters + reversed
print("The phrase is",reversed)
