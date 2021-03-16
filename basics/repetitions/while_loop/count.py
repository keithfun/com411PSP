#asking user to input 
print("How many live cables must I avoid ?")
live_cables = int(input())
#adding a variable to track the number of live cables and set it to 0.
track_cables = 0
#using while loop to count iterate the message and increment the variable to track the number of live cables avoided
while (live_cables>track_cables):
    track_cables = track_cables +1
    print("Avoiding...", end="")
    print("...Done!{} live cable(s) avoided".format(track_cables))
print("All live cables have been avoided ")


