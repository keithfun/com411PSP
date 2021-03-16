#display ascii character in congruence with while loop 
#Print a question in order to get an input from the user
print("How many bars should be charged ?")
user_input = int(input())
#Need to create a variable to track the number of bars charged  and set this to 0
bars_input = 0
#Implementing while repetitions
while (user_input>bars_input):
  bars_input = bars_input + 1
  print("Charging:", end="")
  print("█"* bars_input)
print("The battery is fully charged.")