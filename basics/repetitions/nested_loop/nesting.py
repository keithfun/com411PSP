#ask user for inputs
print("Please enter a sequence of characters consisting of dashes and two markers")
sequence = input()

print("Please enter the character representing the markers")
character =input()


#rep markers
char1 = -1
char2 = -1


#loop function
for position in range(0,len(sequence),1):
  letter = sequence[position]

  if (letter == character):
    if(char1 == -1):
      char1 = position
    else:
      char2 = position
    
print("The distance between the markers is {}".format (char2 - char1 -1))
