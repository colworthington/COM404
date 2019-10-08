# While Loop with counter for Beep to remove the cables holding the robot.
avoid = int(input("How many live cables must I avoid? "))
live = 0
count = 0
print("\n")
while live < avoid:
    count = count +1
    print("Avoiding...Done! " + str(count) + " live cables avoided.")
    live = live +1  
print()
print ("Completed")