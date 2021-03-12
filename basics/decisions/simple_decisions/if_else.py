#Adding an else option for the if statement. That should trigger another command.
print("Please enter the activity to be performed.")
x = str(input())
if (x == "calculate"):
  print("Performing calculations...")
else:
  print("Performing activity...")
print("Activity completed")
