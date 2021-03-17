#ask user for input
print("How far are we from the cave")
distance_cave = int(input())
#using a second variable so it tracks the input variable aka makes the for loop legitimate
distance_remaining = 0
#implementing the for loop to countdown
for distance_remaining in range(distance_cave,0,-1):
  print(distance_remaining, ("steps remaining"))
print("\nWe have reached the cave")
