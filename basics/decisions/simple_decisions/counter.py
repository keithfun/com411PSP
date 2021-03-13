#Code meant to discriminate between even and odd numbers as well as count them
print("Please enter the first whole number")
x = int(input())
print("Please enter the second whole number")
y = int(input())
print("Please enter the third whole number")
z = int(input())
even_numbers = 0
odd_numbers = 0
if (x%2==0):
  even_numbers = even_numbers +1
else:
  odd_numbers = odd_numbers +1
if (y%2==0):
  even_numbers = even_numbers +1
else:
  odd_numbers = odd_numbers + 1
if (z%2==0):
  even_numbers = even_numbers + 1
else:
  odd_numbers = odd_numbers + 1
print("There are {} even and {} odd numbers".format(even_numbers, odd_numbers))
