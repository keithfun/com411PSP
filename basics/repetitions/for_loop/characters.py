#asking user for input
print("What strange markings do you see")
markings = str(input())

print("Identifying..")

#applying the for loop
print()
for position in range (0, len(markings),1):
  print("index", position, ":", markings[position])
print("Done!")
