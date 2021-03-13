#retrieve data from the user by asking two questions
print("What did I hear ?")
noise = input()
print("What did I see ?")
view = input()
# generating an if and and statement for the user input
if ((noise == "grrr") and (view == "two red eyes")):
  print("There is a scary creature. I should get out of here!")
else:
  print("I am a little scared but I will continue")
  