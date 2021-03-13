#asking user to input the search location
print("Where shoud I look")
location = input ()
if (location =="in the bedroom"):
  print("Where in the bedroom should I look?")
  bed_loc = input()
  if (bed_loc == "under the bed"):
    print("Found some shoes but no battery")
  else:
    print("Found some mess but no battery")
#second code block with nested decisions
elif (location == "in the bathroom"):
  print("Where in the bathroom should I look?")
  bath_loc = input()
  if (bath_loc == "in the bathtub"):
    print("Found a rubber duck but no battery")
  else:
    print("Found a wet surface but no battery")
#third code block with nested decisions
elif (location == "in the lab"):
  print("Where in the lab should I look?")
  lab_loc = input()
  if (lab_loc == "on the table"):
    print("Yes! I found my battery")
  else: 
    print("Found some tools but no battery")
# else code in the event of a false if
else:
  print("I do not know where that is but I will keep looking.")
