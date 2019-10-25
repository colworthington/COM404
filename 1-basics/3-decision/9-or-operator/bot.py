# pick an adventure
# Retrieve adventure from user
adventure = (input("What type of adventure? "))
print()
# adventure responses
if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest!")
elif ((adventure == "safe") or (adventure == "long")):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
print()