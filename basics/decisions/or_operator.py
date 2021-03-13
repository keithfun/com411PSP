#ask the user for a input
print("What type of adventure should I have?")
adventure_type = input()
#first code block with an if and or statement
if ((adventure_type == "short") or (adventure_type == "scary")):
  print("Entering the dark forest")
elif ((adventure_type =="safe") or (adventure_type =="long")):
  print("Taking the safe route")
else:
  print("Not sure which route to take")
  