#Trying to implement a while loop to ask the question again depending on the user input
print("How many numbers should I sum up?")
numbers_quantity = int(input())
numbers_tracker = 0
total = 0
while numbers_quantity> numbers_tracker:
  numbers_tracker=numbers_tracker + 1
  print("Please enter the number {} out of {} ".format(numbers_tracker,numbers_quantity))
  numbers_entered = int(input())
  total = total + numbers_entered
  

print("The answer is",total)
