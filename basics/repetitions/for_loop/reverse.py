#asking for user input
print("What phrase do you see")
phrase_typed = str(input())

print("Reversing...")
print()
for phrase_reversed in range (len(phrase_typed) -1, -1, -1,):
  print(phrase_typed[phrase_reversed], end="")



