#Trying to incorporate if elif and else in a program
print("Towards which direction should I paint (up, down, left or right)")
y = str(input())
if (y == "up"):
  print("I am painting in the upward direction")
elif (y == "down"):
  print("I am painting in the downward direction")
elif (y == "left"):
  print ("I am painting in the left direction")
elif (y == "right"):
  print("I am painting in the right direction")
else:
  print("I am confused")
print("Thank you for your help")
