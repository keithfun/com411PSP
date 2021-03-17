#ask user for input
print("What level of brightness is required?")
lvl_req = int(input())

#summoning another variable that tracks user input
lvl_current = 0 

print("Adjusting brightness...")
print()
#applying the for loop for even number sequence

for lvl_current in range(2,lvl_req+1,2):
  print("Beep's birghtness level: ", end="")
  print("*"*lvl_current)
  print("Bop's brightness level: ", end="")
  print("*"*lvl_current)
  print()

print("Adjustments complete!")


