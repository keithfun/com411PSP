#ask user for input
print("How many rows should I have")
rows = int(input())
print("How many columns should I have")
columns = int(input())

print("Here I go:")

#nesting loops
for row in range(0,rows,1):
  for col in range(0,columns,1):
    print(":-)", end ="")
  print()
